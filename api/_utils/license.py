"""
License key generation / verification / formatting
(Same crypto logic as bot.py — shared)
"""
import os, hmac, hashlib, secrets, datetime

LICENSE_SECRET = os.getenv("LICENSE_SECRET", "astatine-guard-secret-change-me")

PLUGIN_PREFIXES = {
    "AstatineGuard": "AG",
    "AstatineLifeSteal": "AL",
    "AstatineHome": "AH",
}

def generate_key(plugin: str, expires_at: datetime.datetime | None = None) -> str:
    prefix = PLUGIN_PREFIXES.get(plugin, "XX")
    ts = int(expires_at.timestamp()) if expires_at else 0xFFFFFFFF
    eh = format(ts & 0xFFFFFFFF, "08X")
    rh = secrets.token_hex(4).upper()
    payload = f"{prefix}-{eh}-{rh}"
    sig = hmac.new(LICENSE_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()[:8].upper()
    return f"{payload}-{sig}"

def verify_key(key: str) -> bool:
    parts = key.strip().upper().split("-")
    if len(parts) != 4:
        return False
    payload = "-".join(parts[:3])
    sig = hmac.new(LICENSE_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()[:8].upper()
    return hmac.compare_digest(sig, parts[3])

def key_expiry(key: str) -> datetime.datetime | None:
    parts = key.strip().upper().split("-")
    if len(parts) != 4:
        return None
    try:
        ts = int(parts[1], 16)
        return None if ts == 0xFFFFFFFF else datetime.datetime.utcfromtimestamp(ts)
    except Exception:
        return None

def key_is_expired(key: str) -> bool:
    exp = key_expiry(key)
    return False if exp is None else datetime.datetime.utcnow() > exp

def fmt_expiry(key: str) -> str:
    exp = key_expiry(key)
    if exp is None:
        return "Permanent"
    diff = exp - datetime.datetime.utcnow()
    if diff.total_seconds() <= 0:
        return "Expired"
    d, h, m = diff.days, diff.seconds // 3600, (diff.seconds % 3600) // 60
    if d > 0:
        return f"{d}d {h}h remaining"
    if h > 0:
        return f"{h}h {m}m remaining"
    return f"{m}m remaining"

def parse_duration(s: str) -> datetime.datetime | None:
    s = s.strip().lower()
    if s in ("permanent", "perm", "lifetime", "none", "0", ""):
        return None
    units = {"mo": 2592000, "y": 31536000, "w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}
    for unit in sorted(units, key=len, reverse=True):
        if s.endswith(unit):
            try:
                return datetime.datetime.utcnow() + datetime.timedelta(seconds=int(s[:-len(unit)]) * units[unit])
            except ValueError:
                pass
    return None

def enrich(key: str, entry: dict) -> dict:
    expired = key_is_expired(key)
    active = entry.get("active", False) and not expired
    return {
        "key": key, "plugin": entry.get("plugin", "Unknown"),
        "status": "active" if active else ("expired" if expired else "revoked"),
        "expiry": fmt_expiry(key), "user_name": entry.get("user_name", "Unassigned"),
        "user_id": entry.get("user_id"), "created_at": entry.get("created_at", "Unknown"),
        "created_by": entry.get("created_by", "Unknown"),
    }
