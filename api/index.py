"""
Astatine Studio — Vercel Serverless Flask App
All routes in one file, using Supabase for shared database
"""
import os, secrets, datetime, urllib.parse
from functools import wraps

import requests as http_requests
from flask import (Flask, abort, flash, jsonify, redirect,
                   render_template, request, session)
from jinja2 import DictLoader
from dotenv import load_dotenv

load_dotenv()

# Import our utilities
from _utils.db import (
    db_get_user, db_get_or_create_discord, db_get_or_create_google,
    db_all_users, db_set_admin, lic_load_all, lic_get, lic_save,
    lic_delete, lic_get_by_user, lic_update,
)
from _utils.license import (
    generate_key, verify_key, key_is_expired, fmt_expiry,
    parse_duration, enrich, PLUGIN_PREFIXES,
)
from _utils.templates import T

# ═══════════════════════════════════════════════════════════
#  FLASK APP
# ═══════════════════════════════════════════════════════════

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", secrets.token_hex(32))
app.jinja_loader = DictLoader(T)

# OAuth config
DISCORD_CLIENT_ID     = os.getenv("DISCORD_CLIENT_ID", "1189179702410223696")
DISCORD_CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET", "LGORcPOkrMFoToov7q6-bYFXlbK_G6eB")
DISCORD_REDIRECT_URI  = os.getenv("DISCORD_REDIRECT_URI", "")

GOOGLE_CLIENT_ID     = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "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")
GOOGLE_REDIRECT_URI  = os.getenv("GOOGLE_REDIRECT_URI", "")

# ── Auth decorators ───────────────────────────────────────

def login_required(f):
    @wraps(f)
    def dec(*a, **kw):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect("/login")
        return f(*a, **kw)
    return dec

def admin_required(f):
    @wraps(f)
    def dec(*a, **kw):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect("/login")
        u = db_get_user(session["user_id"])
        if not u or not u.get("is_admin"):
            abort(403)
        return f(*a, **kw)
    return dec

@app.context_processor
def _ctx():
    u = db_get_user(session["user_id"]) if "user_id" in session else None
    return {"current_user": u, "now": datetime.datetime.utcnow()}

# ── Public routes ─────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login_page():
    if "user_id" in session:
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect("/")

# ── Discord OAuth2 ────────────────────────────────────────

@app.route("/login/discord")
def login_discord():
    state = secrets.token_hex(16)
    session["oauth_state"] = state
    p = {
        "client_id": DISCORD_CLIENT_ID,
        "redirect_uri": DISCORD_REDIRECT_URI,
        "response_type": "code",
        "scope": "identify email",
        "state": state,
        "prompt": "none",
    }
    return redirect("https://discord.com/api/oauth2/authorize?" + urllib.parse.urlencode(p))

@app.route("/login/discord/callback")
def login_discord_callback():
    if request.args.get("error"):
        flash("Discord login was cancelled.", "warning")
        return redirect("/login")
    if request.args.get("state") != session.pop("oauth_state", None):
        flash("Invalid OAuth state – try again.", "danger")
        return redirect("/login")
    tr = http_requests.post("https://discord.com/api/oauth2/token",
        data={
            "client_id": DISCORD_CLIENT_ID,
            "client_secret": DISCORD_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": request.args.get("code"),
            "redirect_uri": DISCORD_REDIRECT_URI,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=10)
    if not tr.ok:
        flash("Failed to exchange Discord token.", "danger")
        return redirect("/login")
    ur = http_requests.get("https://discord.com/api/users/@me",
        headers={"Authorization": f"Bearer {tr.json()['access_token']}"}, timeout=10)
    if not ur.ok:
        flash("Failed to fetch Discord profile.", "danger")
        return redirect("/login")
    d = ur.json()
    did = d["id"]
    name = d.get("global_name") or d.get("username", "Unknown")
    ah = d.get("avatar")
    avatar = (f"https://cdn.discordapp.com/avatars/{did}/{ah}.png?size=128"
              if ah else f"https://cdn.discordapp.com/embed/avatars/{int(did) % 5}.png")
    u = db_get_or_create_discord(did, name, d.get("email", ""), avatar)
    session["user_id"] = u["id"]
    flash(f"Welcome back, {name}! 🌙", "success")
    return redirect("/dashboard")

# ── Google OAuth2 ─────────────────────────────────────────

@app.route("/login/google")
def login_google():
    state = secrets.token_hex(16)
    session["oauth_state"] = state
    p = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "state": state,
        "access_type": "online",
        "prompt": "select_account",
    }
    return redirect("https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(p))

@app.route("/login/google/callback")
def login_google_callback():
    if request.args.get("error"):
        flash("Google login was cancelled.", "warning")
        return redirect("/login")
    if request.args.get("state") != session.pop("oauth_state", None):
        flash("Invalid OAuth state – try again.", "danger")
        return redirect("/login")
    tr = http_requests.post("https://oauth2.googleapis.com/token",
        data={
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": request.args.get("code"),
            "redirect_uri": GOOGLE_REDIRECT_URI,
        }, timeout=10)
    if not tr.ok:
        flash("Failed to exchange Google token.", "danger")
        return redirect("/login")
    ur = http_requests.get("https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {tr.json()['access_token']}"}, timeout=10)
    if not ur.ok:
        flash("Failed to fetch Google profile.", "danger")
        return redirect("/login")
    g = ur.json()
    u = db_get_or_create_google(g["sub"], g.get("name", "Unknown"), g.get("email", ""), g.get("picture", ""))
    session["user_id"] = u["id"]
    flash(f"Welcome back, {g.get('name', 'there')}! 🌙", "success")
    return redirect("/dashboard")

# ── Dashboard ─────────────────────────────────────────────

@app.route("/dashboard")
@login_required
def dashboard():
    u = db_get_user(session["user_id"])
    disc = str(u.get("discord_id") or "")
    if disc:
        rows = lic_get_by_user(disc)
        keys = [enrich(r["key"], r) for r in rows]
    else:
        keys = []
    return render_template("dashboard.html", keys=keys)

# ── Admin ─────────────────────────────────────────────────

@app.route("/admin")
@admin_required
def admin():
    data = lic_load_all()
    users = db_all_users()
    keys = [enrich(k, v) for k, v in data.items()]
    stats = {
        "total": len(keys),
        "active": sum(1 for k in keys if k["status"] == "active"),
        "expired": sum(1 for k in keys if k["status"] == "expired"),
        "revoked": sum(1 for k in keys if k["status"] == "revoked"),
        "users": len(users),
    }
    return render_template("admin.html", keys=keys, users=users, stats=stats,
                           plugins=list(PLUGIN_PREFIXES))

@app.route("/admin/generate", methods=["POST"])
@admin_required
def admin_generate():
    plugin = request.form.get("plugin", "").strip()
    dur_custom = request.form.get("duration_custom", "").strip()
    dur = dur_custom if dur_custom else request.form.get("duration", "permanent").strip()
    ad = request.form.get("assign_discord", "").strip()
    an = request.form.get("assign_name", "").strip()
    if plugin not in PLUGIN_PREFIXES:
        flash("Invalid plugin.", "danger")
        return redirect("/admin")
    exp = parse_duration(dur)
    key = generate_key(plugin, exp)
    me = db_get_user(session["user_id"])
    entry = {
        "plugin": plugin, "active": True,
        "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "created_by": me.get("username", "Web Admin"),
    }
    if ad:
        entry["user_id"] = ad
        entry["user_name"] = an or ad
    lic_save(key, entry)
    flash(f"✅ Key generated: {key}", "success")
    return redirect("/admin#keys")

@app.route("/admin/revoke", methods=["POST"])
@admin_required
def admin_revoke():
    key = request.form.get("key", "").strip().upper()
    entry = lic_get(key)
    if not entry:
        flash("Key not found.", "danger")
    else:
        lic_update(key, {"active": False})
        flash(f"Key {key} revoked.", "warning")
    return redirect("/admin#keys")

@app.route("/admin/activate", methods=["POST"])
@admin_required
def admin_activate():
    key = request.form.get("key", "").strip().upper()
    entry = lic_get(key)
    if not entry:
        flash("Key not found.", "danger")
    else:
        lic_update(key, {"active": True})
        flash(f"Key {key} activated.", "success")
    return redirect("/admin#keys")

@app.route("/admin/delete", methods=["POST"])
@admin_required
def admin_delete():
    key = request.form.get("key", "").strip().upper()
    lic_delete(key)
    flash(f"Key {key} deleted.", "warning")
    return redirect("/admin#keys")

@app.route("/admin/set-admin", methods=["POST"])
@admin_required
def admin_set_admin():
    uid = request.form.get("uid", "").strip()
    if uid:
        db_set_admin(uid, request.form.get("is_admin") == "1")
        flash("User admin status updated.", "success")
    return redirect("/admin#users")

# ── Plugin API (public — called by Minecraft servers) ─────

@app.route("/api/v1/verify")
def api_verify():
    key = request.args.get("key", "").strip().upper()
    if not key:
        return jsonify({"valid": False, "error": "No key provided"}), 400
    if not verify_key(key):
        return jsonify({"valid": False, "error": "Invalid signature"})
    if key_is_expired(key):
        return jsonify({"valid": False, "error": "Key expired"})
    entry = lic_get(key)
    if not entry:
        return jsonify({"valid": False, "error": "Key not registered"})
    if not entry.get("active", False):
        return jsonify({"valid": False, "error": "Key revoked"})
    return jsonify({
        "valid": True,
        "plugin": entry.get("plugin"),
        "user": entry.get("user_name", "Unknown"),
        "expiry": fmt_expiry(key),
    })

# ── Error handlers ────────────────────────────────────────

@app.errorhandler(403)
def e403(e):
    return render_template("error.html", code=403,
                           message="You don't have permission to view this page."), 403

@app.errorhandler(404)
def e404(e):
    return render_template("error.html", code=404,
                           message="The page you're looking for doesn't exist."), 404