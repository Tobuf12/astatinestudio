"""
Supabase client — shared between bot & web
"""
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://nuyqipvtqfzitihuzewg.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY", "sb_secret_GvgpG6AW91hdUbZ5V4kVow_1nrJW60B")  # service_role key

_client: Client | None = None

def get_sb() -> Client:
    global _client
    if _client is None:
        _client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return _client

# ── User helpers ──────────────────────────────────────────

def db_get_user(uid: str) -> dict | None:
    r = get_sb().table("users").select("*").eq("id", uid).execute()
    return r.data[0] if r.data else None

def db_get_or_create_discord(discord_id, username, email, avatar) -> dict:
    sb = get_sb()
    r = sb.table("users").select("*").eq("discord_id", discord_id).execute()
    if r.data:
        sb.table("users").update({
            "username": username, "email": email, "avatar": avatar
        }).eq("discord_id", discord_id).execute()
        u = r.data[0]
        u.update({"username": username, "email": email, "avatar": avatar})
        return u
    else:
        owner_ids = [x.strip() for x in os.getenv("LICENSE_OWNER_IDS", "").split(",") if x.strip()]
        is_admin = str(discord_id) in owner_ids
        ins = sb.table("users").insert({
            "discord_id": discord_id, "username": username,
            "email": email, "avatar": avatar, "is_admin": is_admin
        }).execute()
        return ins.data[0]

def db_get_or_create_google(google_id, username, email, avatar) -> dict:
    sb = get_sb()
    r = sb.table("users").select("*").eq("google_id", google_id).execute()
    if r.data:
        sb.table("users").update({
            "username": username, "email": email, "avatar": avatar
        }).eq("google_id", google_id).execute()
        u = r.data[0]
        u.update({"username": username, "email": email, "avatar": avatar})
        return u
    else:
        ins = sb.table("users").insert({
            "google_id": google_id, "username": username,
            "email": email, "avatar": avatar, "is_admin": False
        }).execute()
        return ins.data[0]

def db_all_users() -> list[dict]:
    r = get_sb().table("users").select("*").order("created_at", desc=True).execute()
    return r.data

def db_set_admin(uid: str, is_admin: bool):
    get_sb().table("users").update({"is_admin": is_admin}).eq("id", uid).execute()

# ── License helpers ───────────────────────────────────────

def lic_load_all() -> dict:
    """Returns {key: entry_dict, ...} matching the old licenses.json format"""
    r = get_sb().table("licenses").select("*").execute()
    result = {}
    for row in r.data:
        k = row.pop("key")
        result[k] = row
    return result

def lic_get(key: str) -> dict | None:
    r = get_sb().table("licenses").select("*").eq("key", key).execute()
    return r.data[0] if r.data else None

def lic_save(key: str, entry: dict):
    """Upsert a single license entry"""
    get_sb().table("licenses").upsert({"key": key, **entry}).execute()

def lic_delete(key: str):
    get_sb().table("licenses").delete().eq("key", key).execute()

def lic_get_by_user(discord_id: str) -> list[dict]:
    r = get_sb().table("licenses").select("*").eq("user_id", discord_id).execute()
    return r.data

def lic_update(key: str, updates: dict):
    get_sb().table("licenses").update(updates).eq("key", key).execute()
