"""
All HTML templates — identical lunar theme from original bot.py
Loaded via Jinja2 DictLoader
"""

T: dict[str, str] = {}

# ─── Copy ALL your _T templates here exactly as they are ───
# Just copy the entire _T dictionary contents from your bot.py

T['base.html'] = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{% block title %}Astatine Studio{% endblock %}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
  <style>
    :root{
      --bg:#04050f;--surface:#070a1a;--card:#0b0e22;
      --border:rgba(148,172,220,.1);--accent:#7eb3d6;--silver:#b8ceea;
      --glow:rgba(126,179,214,.18);--text:#c4d4ec;--dim:#4a5878;
      --success:#5cb88a;--warn:#c4a45a;--danger:#b06060;--info:#5a9fd4;
    }
    *,*::before,*::after{box-sizing:border-box}
    html,body{height:100%}
    body{font-family:"Inter",sans-serif;background:var(--bg);color:var(--text);
         min-height:100vh;display:flex;flex-direction:column;position:relative;overflow-x:hidden}
    body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
      background-image:
        radial-gradient(1px 1px at 10% 20%,rgba(200,220,255,.18) 0%,transparent 100%),
        radial-gradient(1px 1px at 85% 12%,rgba(200,220,255,.14) 0%,transparent 100%),
        radial-gradient(1px 1px at 45% 68%,rgba(200,220,255,.12) 0%,transparent 100%),
        radial-gradient(1px 1px at 72% 38%,rgba(200,220,255,.16) 0%,transparent 100%),
        radial-gradient(1px 1px at 28% 82%,rgba(200,220,255,.10) 0%,transparent 100%),
        radial-gradient(1px 1px at 92% 58%,rgba(200,220,255,.14) 0%,transparent 100%),
        radial-gradient(1px 1px at 53% 8%, rgba(200,220,255,.18) 0%,transparent 100%),
        radial-gradient(1px 1px at 8%  48%,rgba(200,220,255,.12) 0%,transparent 100%),
        radial-gradient(1px 1px at 78% 78%,rgba(200,220,255,.10) 0%,transparent 100%),
        radial-gradient(1px 1px at 22% 42%,rgba(200,220,255,.16) 0%,transparent 100%),
        radial-gradient(1px 1px at 63% 88%,rgba(200,220,255,.12) 0%,transparent 100%),
        radial-gradient(1px 1px at 38% 28%,rgba(200,220,255,.14) 0%,transparent 100%),
        radial-gradient(1px 1px at 96% 32%,rgba(200,220,255,.10) 0%,transparent 100%),
        radial-gradient(1px 1px at 4%  72%,rgba(200,220,255,.16) 0%,transparent 100%),
        radial-gradient(1px 1px at 60% 52%,rgba(200,220,255,.12) 0%,transparent 100%),
        radial-gradient(1px 1px at 17% 60%,rgba(200,220,255,.14) 0%,transparent 100%),
        radial-gradient(1px 1px at 50% 95%,rgba(200,220,255,.10) 0%,transparent 100%),
        radial-gradient(1px 1px at 33% 5%, rgba(200,220,255,.18) 0%,transparent 100%);}
    body::after{content:"";position:fixed;top:-150px;left:50%;transform:translateX(-50%);
      width:700px;height:350px;pointer-events:none;z-index:0;
      background:radial-gradient(ellipse,rgba(126,179,214,.07) 0%,transparent 70%);}
    main{flex:1;position:relative;z-index:1}
    code,.mono{font-family:"JetBrains Mono",monospace}
    .navbar{background:rgba(4,5,15,.9)!important;backdrop-filter:blur(16px);
            border-bottom:1px solid var(--border);position:relative;z-index:100}
    .navbar-brand{font-weight:700;font-size:1.1rem;letter-spacing:-.02em}
    .brand-moon{color:var(--accent)}
    .nav-link{color:var(--dim)!important;transition:color .15s}
    .nav-link:hover,.nav-link.active{color:var(--text)!important}
    .nav-badge{font-size:.6rem;font-weight:700;padding:.15em .45em;border-radius:.25rem;
               background:linear-gradient(135deg,var(--accent),var(--silver));
               color:#04050f;vertical-align:middle;margin-left:4px}
    .m-card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.5rem;
            transition:border-color .2s}
    .m-card:hover{border-color:rgba(126,179,214,.22)}
    .stat-card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.25rem 1.5rem}
    .stat-icon{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;
               justify-content:center;font-size:1.1rem}
    .stat-value{font-size:1.85rem;font-weight:700;line-height:1}
    .stat-label{font-size:.72rem;color:var(--dim);text-transform:uppercase;letter-spacing:.06em}
    .pill{display:inline-flex;align-items:center;gap:5px;padding:.22em .6em;border-radius:20px;
          font-size:.71rem;font-weight:600;letter-spacing:.03em}
    .pill-active {background:rgba(92,184,138,.15);color:var(--success)}
    .pill-expired{background:rgba(196,164,90,.15); color:var(--warn)}
    .pill-revoked{background:rgba(176,96,96,.15);  color:var(--danger)}
    .btn-moon{background:linear-gradient(135deg,var(--accent),var(--silver));color:#04050f;
              border:none;font-weight:700;letter-spacing:.01em;
              transition:opacity .15s,box-shadow .15s}
    .btn-moon:hover{color:#04050f;opacity:.9;box-shadow:0 0 24px var(--glow)}
    .btn-discord{background:#5865F2;color:#fff;border:none;font-weight:600;transition:background .15s}
    .btn-discord:hover{background:#4752c4;color:#fff}
    .btn-google{background:#fff;color:#333;border:1px solid #ddd;font-weight:600;transition:background .15s}
    .btn-google:hover{background:#f4f4f4}
    .form-control,.form-select{background:#04050f!important;border:1px solid var(--border)!important;
                                color:var(--text)!important;border-radius:8px}
    .form-control:focus,.form-select:focus{border-color:var(--accent)!important;
                                            box-shadow:0 0 0 3px var(--glow)!important}
    .form-label{font-size:.83rem;font-weight:500;color:var(--dim);margin-bottom:.3rem}
    .m-table{width:100%;border-collapse:separate;border-spacing:0 5px}
    .m-table thead th{font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.07em;
                      color:var(--dim);padding:.5rem .75rem;border-bottom:1px solid var(--border)}
    .m-table tbody tr{background:var(--card);transition:background .15s}
    .m-table tbody tr:hover{background:#0f1328}
    .m-table tbody td{padding:.7rem .75rem;vertical-align:middle;border-top:1px solid var(--border)}
    .m-table tbody td:first-child{border-radius:10px 0 0 10px}
    .m-table tbody td:last-child{border-radius:0 10px 10px 0}
    .key-display{font-family:"JetBrains Mono",monospace;font-size:.74rem;color:var(--dim);
                 background:rgba(0,0,0,.3);padding:.2em .55em;border-radius:5px;letter-spacing:.04em}
    .avatar{width:36px;height:36px;border-radius:50%;object-fit:cover;border:2px solid var(--border)}
    .avatar-lg{width:68px;height:68px;border-radius:50%;object-fit:cover;border:3px solid var(--accent)}
    .m-alert{border-radius:10px;font-size:.88rem;border:none;
             display:flex;align-items:center;gap:.6rem;
             background:var(--card);border:1px solid var(--border)}
    .m-alert.alert-success{border-color:rgba(92,184,138,.3)}
    .m-alert.alert-danger{border-color:rgba(176,96,96,.3)}
    .m-alert.alert-warning{border-color:rgba(196,164,90,.3)}
    .m-alert.alert-info{border-color:rgba(90,159,212,.3)}
    .m-tabs .nav-link{color:var(--dim)!important;border-bottom:2px solid transparent;
                      border-radius:0;padding:.6rem 1rem;font-weight:500;font-size:.88rem;
                      transition:color .15s,border-color .15s}
    .m-tabs .nav-link.active{color:var(--silver)!important;border-bottom-color:var(--accent);background:none}
    .m-tabs{border-bottom:1px solid var(--border)}
    .section-title{font-size:1.05rem;font-weight:700;margin-bottom:1.25rem}
    .text-muted{color:var(--dim)!important}
    .text-accent{color:var(--accent)}
    .text-silver{color:var(--silver)}
    .copy-btn{background:none;border:none;color:var(--dim);cursor:pointer;padding:.15rem .3rem;
              border-radius:4px;font-size:.8rem;transition:color .15s,background .15s}
    .copy-btn:hover{color:var(--text);background:rgba(255,255,255,.06)}
    .btn-act{padding:.22rem .5rem;font-size:.73rem;border-radius:6px;border:1px solid var(--border);
             background:none;cursor:pointer;font-weight:600;transition:background .15s,color .15s}
    .btn-act-ok{color:var(--success);border-color:rgba(92,184,138,.3)}
    .btn-act-ok:hover{background:rgba(92,184,138,.12)}
    .btn-act-warn{color:var(--warn);border-color:rgba(196,164,90,.3)}
    .btn-act-warn:hover{background:rgba(196,164,90,.12)}
    .btn-act-del{color:var(--danger);border-color:rgba(176,96,96,.3)}
    .btn-act-del:hover{background:rgba(176,96,96,.12)}
    .moon-divider{height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);
                  opacity:.25;margin:2rem 0}
    footer{border-top:1px solid var(--border);padding:1.2rem 0;font-size:.8rem;
           color:var(--dim);position:relative;z-index:1}
    ::-webkit-scrollbar{width:6px;height:6px}
    ::-webkit-scrollbar-track{background:var(--bg)}
    ::-webkit-scrollbar-thumb{background:#1a1f38;border-radius:3px}
    @keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
    .fade-in{animation:fadeIn .35s ease both}
    @keyframes moonrise{from{opacity:0;transform:translateY(20px) scale(.95)}to{opacity:1;transform:none}}
    .moonrise{animation:moonrise .5s ease both}
  </style>
  {% block extra_head %}{% endblock %}
</head>
<body>
<nav class="navbar navbar-expand-lg sticky-top">
  <div class="container">
    <a class="navbar-brand d-flex align-items-center gap-2" href="/">
      <i class="fa-solid fa-moon brand-moon" style="font-size:1.05rem;"></i>
      <span><span class="text-silver">Astatine</span> Studio</span>
    </a>
    <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navC">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navC">
      <ul class="navbar-nav ms-auto align-items-lg-center gap-1">
        <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
        {% if current_user %}
          <li class="nav-item"><a class="nav-link" href="/dashboard">Dashboard</a></li>
          {% if current_user.is_admin %}
          <li class="nav-item">
            <a class="nav-link" href="/admin">Admin<span class="nav-badge">ADMIN</span></a>
          </li>
          {% endif %}
          <li class="nav-item ms-lg-2 d-flex align-items-center gap-2">
            {% if current_user.avatar %}<img src="{{ current_user.avatar }}" class="avatar" alt="av"/>{% endif %}
            <span style="font-size:.82rem;color:var(--dim);">{{ current_user.username }}</span>
            <a class="btn btn-sm btn-outline-secondary ms-1" href="/logout">
              <i class="fa-solid fa-right-from-bracket"></i>
            </a>
          </li>
        {% else %}
          <li class="nav-item ms-lg-2">
            <a class="btn btn-moon btn-sm px-3" href="/login">
              <i class="fa-solid fa-moon me-1"></i> Sign In
            </a>
          </li>
        {% endif %}
      </ul>
    </div>
  </div>
</nav>
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
  <div class="container mt-3" style="position:relative;z-index:2;">
    {% for cat, msg in messages %}
      {% set icons = {"success":"circle-check","danger":"circle-xmark","warning":"triangle-exclamation","info":"circle-info"} %}
      <div class="alert m-alert alert-{{ cat }} alert-dismissible fade show" role="alert">
        <i class="fa-solid fa-{{ icons.get(cat,'circle-info') }}"></i> {{ msg }}
        <button type="button" class="btn-close btn-close-white ms-auto" data-bs-dismiss="alert"></button>
      </div>
    {% endfor %}
  </div>
  {% endif %}
{% endwith %}
<main>{% block content %}{% endblock %}</main>
<footer>
  <div class="container d-flex justify-content-between flex-wrap gap-2">
    <span><i class="fa-solid fa-moon text-accent me-1"></i> &copy; 2025 <strong>Astatine Studio</strong></span>
    <span>
      <a href="/api/v1/verify" class="text-muted text-decoration-none me-3">API</a>
      <a href="/login" class="text-muted text-decoration-none">Login</a>
    </span>
  </div>
</footer>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
{% block extra_scripts %}{% endblock %}
</body>
</html>'''

T['index.html'] = """{% extends "base.html" %}
{% block title %}Astatine Studio – License Portal{% endblock %}
{% block extra_head %}
<style>
  .hero{min-height:78vh;display:flex;align-items:center;padding:4rem 0;position:relative;overflow:hidden}
  .hero-glow{position:absolute;top:-80px;left:50%;transform:translateX(-50%);
    width:900px;height:500px;pointer-events:none;
    background:radial-gradient(ellipse,rgba(126,179,214,.12) 0%,transparent 65%)}
  .hero-badge{display:inline-flex;align-items:center;gap:.5rem;
    background:rgba(126,179,214,.1);border:1px solid rgba(126,179,214,.25);
    color:var(--accent);border-radius:20px;padding:.3em 1em;
    font-size:.78rem;font-weight:600;letter-spacing:.05em;margin-bottom:1.5rem}
  .hero-title{font-size:clamp(2rem,5vw,3.4rem);font-weight:800;line-height:1.08;
    letter-spacing:-.03em;margin-bottom:1.25rem}
  .hero-title .hl{background:linear-gradient(135deg,var(--accent),var(--silver));
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
  .hero-sub{font-size:1.05rem;color:var(--dim);max-width:500px;line-height:1.65}
  .hero-ctas{margin-top:2rem;display:flex;gap:.75rem;flex-wrap:wrap}
  .code-block{background:#04050f;border:1px solid var(--border);border-radius:14px;
    padding:1.5rem;font-family:"JetBrains Mono",monospace;font-size:.8rem;
    color:#9ccbba;overflow-x:auto;position:relative}
  .code-block .cmt{color:#2e3d55}
  .code-block .key{color:#8ab8d8}
  .code-block .val{color:#c4b87a}
  .code-block .moon-deco{position:absolute;top:1rem;right:1.25rem;font-size:1.4rem;opacity:.15}
  .feat-grid{display:grid;gap:1.2rem;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
  .feat-card{background:var(--card);border:1px solid var(--border);border-radius:12px;
    padding:1.4rem;transition:border-color .2s,transform .2s}
  .feat-card:hover{border-color:rgba(126,179,214,.3);transform:translateY(-2px)}
  .feat-icon{width:42px;height:42px;border-radius:10px;
    background:rgba(126,179,214,.1);color:var(--accent);
    display:flex;align-items:center;justify-content:center;font-size:1.15rem;margin-bottom:.9rem}
  .feat-title{font-weight:700;font-size:.93rem;margin-bottom:.3rem;color:var(--silver)}
  .feat-desc{font-size:.82rem;color:var(--dim);line-height:1.55}
</style>
{% endblock %}
{% block content %}
<section class="hero">
  <div class="hero-glow"></div>
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6 fade-in">
        <div class="hero-badge"><i class="fa-solid fa-moon"></i> LICENSE PORTAL</div>
        <h1 class="hero-title">Manage your<br/><span class="hl">Astatine</span> licenses</h1>
        <p class="hero-sub">Sign in with Discord or Google to view your plugin licenses, check expiry times, and verify keys from your Minecraft server in real time.</p>
        <div class="hero-ctas">
          {% if current_user %}
            <a href="/dashboard" class="btn btn-moon px-4 py-2"><i class="fa-solid fa-gauge me-2"></i>My Dashboard</a>
            {% if current_user.is_admin %}
            <a href="/admin" class="btn btn-outline-secondary px-4 py-2"><i class="fa-solid fa-sliders me-2"></i>Admin Panel</a>
            {% endif %}
          {% else %}
            <a href="/login" class="btn btn-moon px-4 py-2"><i class="fa-solid fa-moon me-2"></i>Sign In</a>
            <a href="#features" class="btn btn-outline-secondary px-4 py-2">Learn More</a>
          {% endif %}
        </div>
      </div>
      <div class="col-lg-6 fade-in" style="animation-delay:.12s">
        <div class="code-block">
          <span class="moon-deco">🌙</span>
          <span class="cmt"># GET /api/v1/verify?key=AG-FFFFFFFF-A3C8-1D4E</span><br/>{<br/>
          &nbsp;&nbsp;<span class="key">"valid"</span>:  <span class="val">true</span>,<br/>
          &nbsp;&nbsp;<span class="key">"plugin"</span>: <span class="val">"AstatineGuard"</span>,<br/>
          &nbsp;&nbsp;<span class="key">"user"</span>:   <span class="val">"YourUsername"</span>,<br/>
          &nbsp;&nbsp;<span class="key">"expiry"</span>: <span class="val">"29d 18h remaining"</span><br/>}
        </div>
      </div>
    </div>
  </div>
</section>
<section id="features" class="py-5">
  <div class="container">
    <h2 class="text-center fw-bold mb-2" style="color:var(--silver)">Everything you need</h2>
    <div class="moon-divider mb-5"></div>
    <div class="feat-grid">
      <div class="feat-card"><div class="feat-icon"><i class="fa-brands fa-discord"></i></div>
        <div class="feat-title">Discord Login</div>
        <div class="feat-desc">One-click sign in with your Discord account — no passwords needed.</div></div>
      <div class="feat-card"><div class="feat-icon"><i class="fa-brands fa-google"></i></div>
        <div class="feat-title">Google Login</div>
        <div class="feat-desc">Prefer Gmail? Sign in with your Google account just as easily.</div></div>
      <div class="feat-card"><div class="feat-icon"><i class="fa-solid fa-key"></i></div>
        <div class="feat-title">License Dashboard</div>
        <div class="feat-desc">See all your keys, statuses, and time remaining in one lunar view.</div></div>
      <div class="feat-card"><div class="feat-icon"><i class="fa-solid fa-plug"></i></div>
        <div class="feat-title">Plugin API</div>
        <div class="feat-desc">Your Minecraft server verifies keys in real-time via a secure REST endpoint.</div></div>
      <div class="feat-card"><div class="feat-icon"><i class="fa-solid fa-sliders"></i></div>
        <div class="feat-title">Admin Panel</div>
        <div class="feat-desc">Generate, revoke, and assign license keys from a sleek web UI.</div></div>
      <div class="feat-card"><div class="feat-icon"><i class="fa-solid fa-lock"></i></div>
        <div class="feat-title">HMAC Signed Keys</div>
        <div class="feat-desc">Every key is cryptographically signed — tampering is instantly detectable.</div></div>
    </div>
  </div>
</section>
{% endblock %}"""

T['login.html'] = """{% extends "base.html" %}
{% block title %}Sign In – Astatine Studio{% endblock %}
{% block extra_head %}
<style>
  .login-wrap{min-height:82vh;display:flex;align-items:center;justify-content:center;padding:2rem;position:relative}
  .login-wrap::before{content:"";position:absolute;inset:0;
    background:radial-gradient(ellipse 55% 55% at 50% 0%,rgba(126,179,214,.1),transparent);
    pointer-events:none}
  .login-card{width:100%;max-width:410px;background:var(--card);
    border:1px solid var(--border);border-radius:22px;padding:2.5rem 2rem;
    position:relative;z-index:1;overflow:hidden}
  .login-card::before{content:"🌕";position:absolute;right:-10px;top:-10px;
    font-size:7rem;opacity:.04;line-height:1;pointer-events:none}
  .login-icon{width:58px;height:58px;border-radius:16px;
    background:rgba(126,179,214,.12);color:var(--accent);
    display:flex;align-items:center;justify-content:center;
    font-size:1.7rem;margin:0 auto 1.5rem}
  .login-title{font-size:1.35rem;font-weight:700;text-align:center;margin-bottom:.3rem;color:var(--silver)}
  .login-sub{font-size:.85rem;color:var(--dim);text-align:center;margin-bottom:2rem}
  .oauth-btn{display:flex;align-items:center;justify-content:center;gap:.65rem;
    width:100%;padding:.72rem 1rem;border-radius:11px;font-weight:600;font-size:.91rem;
    text-decoration:none;transition:transform .15s,box-shadow .15s;border:none;cursor:pointer}
  .oauth-btn:hover{transform:translateY(-1px)}
  .oauth-discord{background:#5865F2;color:#fff}
  .oauth-discord:hover{background:#4752c4;color:#fff;box-shadow:0 4px 20px rgba(88,101,242,.35)}
  .oauth-google{background:#fff;color:#333;border:1px solid #e0e0e0}
  .oauth-google:hover{background:#f7f7f7;box-shadow:0 4px 20px rgba(0,0,0,.15)}
  .divider-or{display:flex;align-items:center;gap:.75rem;font-size:.76rem;color:var(--dim);margin:1.2rem 0}
  .divider-or::before,.divider-or::after{content:"";flex:1;height:1px;background:var(--border)}
  .login-foot{font-size:.77rem;color:var(--dim);text-align:center;margin-top:1.4rem}
  .login-foot a{color:var(--accent);text-decoration:none}
  .login-foot a:hover{text-decoration:underline}
  .phase-row{display:flex;justify-content:center;gap:.5rem;margin-bottom:1.5rem;font-size:1.4rem;opacity:.3}
</style>
{% endblock %}
{% block content %}
<div class="login-wrap">
  <div class="login-card moonrise">
    <div class="phase-row">🌑 🌒 🌓 🌔 🌕</div>
    <div class="login-icon"><i class="fa-solid fa-moon"></i></div>
    <h1 class="login-title">Welcome back</h1>
    <p class="login-sub">Sign in to manage your Astatine Studio licenses</p>
    <a href="/login/discord" class="oauth-btn oauth-discord mb-3">
      <i class="fa-brands fa-discord" style="font-size:1.2rem;"></i> Continue with Discord
    </a>
    <div class="divider-or">or</div>
    <a href="/login/google" class="oauth-btn oauth-google">
      <svg viewBox="0 0 48 48" width="20" height="20">
        <path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/>
        <path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/>
        <path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/>
        <path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/>
      </svg>
      Continue with Google
    </a>
    <div class="login-foot">
      By signing in you agree to our <a href="#">Terms</a> &amp; <a href="#">Privacy Policy</a>.<br/><br/>
      <i class="fa-solid fa-moon text-accent me-1"></i> Your data is never shared with third parties.
    </div>
  </div>
</div>
{% endblock %}"""

T['dashboard.html'] = """{% extends "base.html" %}
{% block title %}Dashboard – Astatine Studio{% endblock %}
{% block extra_head %}
<style>
  .page-hdr{padding:2.5rem 0 1.5rem;border-bottom:1px solid var(--border);margin-bottom:2rem}
  .user-name{font-size:1.3rem;font-weight:700;color:var(--silver)}
  .user-sub{font-size:.82rem;color:var(--dim);margin-top:.1rem}
  .u-badge{display:inline-flex;align-items:center;gap:.35rem;
    background:rgba(88,101,242,.12);border:1px solid rgba(88,101,242,.25);
    color:#8b9cf8;border-radius:6px;padding:.18em .55em;font-size:.7rem;font-weight:600}
  .u-badge.google{background:rgba(234,67,53,.08);border-color:rgba(234,67,53,.2);color:#f08080}
  .u-badge.admin{background:rgba(126,179,214,.12);border-color:rgba(126,179,214,.3);color:var(--accent)}
  .key-card{background:var(--card);border:1px solid var(--border);border-radius:14px;
    padding:1.4rem;display:flex;flex-direction:column;gap:.85rem;
    transition:border-color .2s,transform .2s;position:relative;overflow:hidden}
  .key-card::before{content:"";position:absolute;top:0;left:0;height:3px;width:100%;border-radius:14px 14px 0 0}
  .key-card.active::before{background:var(--success)}
  .key-card.expired::before{background:var(--warn)}
  .key-card.revoked::before{background:var(--danger)}
  .key-card:hover{transform:translateY(-2px);border-color:rgba(126,179,214,.2)}
  .key-card-hdr{display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem;flex-wrap:wrap}
  .plugin-icon{width:36px;height:36px;border-radius:9px;
    background:rgba(126,179,214,.1);color:var(--accent);
    display:flex;align-items:center;justify-content:center;font-size:.95rem;flex-shrink:0}
  .plugin-name{font-weight:700;font-size:.97rem;color:var(--silver)}
  .kf{display:flex;flex-direction:column;gap:.18rem}
  .kf-label{font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);font-weight:600}
  .kf-value{font-size:.86rem}
  .empty-state{text-align:center;padding:4rem 2rem;color:var(--dim)}
  .empty-icon{font-size:3rem;opacity:.15;margin-bottom:1rem}
  .crescent{position:absolute;right:.5rem;bottom:.5rem;font-size:4rem;opacity:.04;line-height:1;pointer-events:none}
</style>
{% endblock %}
{% block content %}
<div class="container">
  <div class="page-hdr fade-in">
    <div class="d-flex align-items-center gap-3 flex-wrap">
      {% if current_user.avatar %}
        <img src="{{ current_user.avatar }}" class="avatar-lg" alt="av"/>
      {% else %}
        <div class="avatar-lg d-flex align-items-center justify-content-center bg-secondary text-white fs-3">
          <i class="fa-solid fa-user"></i>
        </div>
      {% endif %}
      <div>
        <div class="user-name">{{ current_user.username }}</div>
        <div class="user-sub">{% if current_user.email %}{{ current_user.email }}{% endif %}</div>
        <div class="mt-2 d-flex gap-2 flex-wrap">
          {% if current_user.discord_id %}
            <span class="u-badge"><i class="fa-brands fa-discord"></i> Discord</span>
          {% endif %}
          {% if current_user.google_id %}
            <span class="u-badge google"><i class="fa-brands fa-google"></i> Google</span>
          {% endif %}
          {% if current_user.is_admin %}
            <span class="u-badge admin"><i class="fa-solid fa-moon"></i> Admin</span>
          {% endif %}
        </div>
      </div>
    </div>
  </div>
  <div class="fade-in" style="animation-delay:.06s">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2 class="section-title mb-0">
        <i class="fa-solid fa-key text-accent me-2"></i>Your License Keys
        <span class="ms-2 text-muted" style="font-size:.88rem;font-weight:400;">({{ keys|length }})</span>
      </h2>
    </div>
    {% if keys %}
    <div class="row g-3">
      {% for k in keys %}
      <div class="col-md-6 col-xl-4">
        <div class="key-card {{ k.status }}">
          <span class="crescent">🌙</span>
          <div class="key-card-hdr">
            <div class="d-flex align-items-center gap-2">
              <div class="plugin-icon"><i class="fa-solid fa-cube"></i></div>
              <div>
                <div class="plugin-name">{{ k.plugin }}</div>
                <span class="pill pill-{{ k.status }}">
                  {% if k.status == "active" %}<i class="fa-solid fa-circle" style="font-size:.4rem;"></i> Active
                  {% elif k.status == "expired" %}<i class="fa-solid fa-clock"></i> Expired
                  {% else %}<i class="fa-solid fa-ban"></i> Revoked{% endif %}
                </span>
              </div>
            </div>
          </div>
          <div class="kf">
            <div class="kf-label">License Key</div>
            <div class="d-flex align-items-center gap-2">
              <span class="key-display flex-grow-1">{{ k.key }}</span>
              <button class="copy-btn" onclick="cpKey('{{ k.key }}',this)" title="Copy">
                <i class="fa-regular fa-copy"></i>
              </button>
            </div>
          </div>
          <div class="d-flex gap-4 flex-wrap">
            <div class="kf">
              <div class="kf-label">Expiry</div>
              <div class="kf-value">
                {% if k.expiry == "Permanent" %}<i class="fa-solid fa-infinity" style="color:var(--success);"></i> Permanent
                {% elif k.expiry == "Expired" %}<span style="color:var(--danger);">Expired</span>
                {% else %}<i class="fa-regular fa-clock" style="color:var(--warn);"></i> {{ k.expiry }}{% endif %}
              </div>
            </div>
            <div class="kf">
              <div class="kf-label">Issued</div>
              <div class="kf-value text-muted">{{ k.created_at }}</div>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
    {% else %}
    <div class="m-card empty-state">
      <div class="empty-icon">🌑</div>
      <h4 class="fw-semibold mb-2" style="color:var(--silver);">No licenses found</h4>
      <p class="text-muted mb-2">No license keys are linked to your Discord account yet.</p>
      <p class="text-muted" style="font-size:.84rem;">Make sure your Discord ID matches your purchase, or contact support.</p>
      {% if not current_user.discord_id %}
      <div class="m-alert alert-warning mt-3 p-3">
        <i class="fa-solid fa-triangle-exclamation" style="color:var(--warn);"></i>
        You logged in via Google. Keys are linked by Discord ID — also sign in with Discord to see them.
      </div>
      {% endif %}
    </div>
    {% endif %}
  </div>
  <div class="m-card mt-4 fade-in" style="animation-delay:.1s;">
    <div class="d-flex align-items-start gap-3">
      <i class="fa-solid fa-circle-info text-accent mt-1" style="font-size:1.1rem;"></i>
      <div>
        <div class="fw-semibold mb-1" style="color:var(--silver);">Need help with your license?</div>
        <div class="text-muted" style="font-size:.86rem;">
          Open a support ticket in the Astatine Studio Discord server. Expired keys can be renewed
          and will automatically reactivate. Revoked keys require contacting support.
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
{% block extra_scripts %}
<script>
function cpKey(k,btn){navigator.clipboard.writeText(k).then(()=>{
  const i=btn.querySelector("i");i.className="fa-solid fa-check";
  btn.style.color="var(--success)";
  setTimeout(()=>{i.className="fa-regular fa-copy";btn.style.color="";},1800);
});}
</script>
{% endblock %}"""

T['admin.html'] = """{% extends "base.html" %}
{% block title %}Admin Panel – Astatine Studio{% endblock %}
{% block extra_head %}
<style>
  .page-hdr{padding:2.5rem 0 1.5rem;border-bottom:1px solid var(--border);margin-bottom:2rem}
  .stats-row{display:grid;gap:1rem;grid-template-columns:repeat(5,1fr)}
  @media(max-width:900px){.stats-row{grid-template-columns:repeat(3,1fr)}}
  @media(max-width:600px){.stats-row{grid-template-columns:repeat(2,1fr)}}
  .gen-card{background:var(--card);border:1px solid rgba(126,179,214,.25);border-radius:14px;padding:1.5rem}
  .tb-toolbar{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.75rem;margin-bottom:1rem}
  .usr-avatar{width:30px;height:30px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:.5rem}
  #fInp{max-width:240px}
  #fPlugin,#fStatus{max-width:160px}
  .pill-tag{display:inline-flex;align-items:center;gap:.3rem;padding:.2em .55em;border-radius:6px;
    font-size:.7rem;font-weight:600;background:rgba(126,179,214,.1);color:var(--accent)}
</style>
{% endblock %}
{% block content %}
<div class="container">
  <div class="page-hdr fade-in">
    <div class="d-flex align-items-center gap-3">
      <div style="width:48px;height:48px;border-radius:13px;background:rgba(126,179,214,.1);
                  color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:1.5rem;">
        <i class="fa-solid fa-moon"></i>
      </div>
      <div>
        <h1 class="mb-0 fw-bold" style="font-size:1.35rem;color:var(--silver);">Admin Panel</h1>
        <div class="text-muted" style="font-size:.83rem;">Manage all license keys and registered users</div>
      </div>
    </div>
  </div>
  <div class="stats-row mb-4 fade-in">
    {% set scfg = [
      ("total",  "fa-key",          "--info",    "Total Keys"),
      ("active", "fa-circle-check", "--success", "Active"),
      ("expired","fa-clock",        "--warn",    "Expired"),
      ("revoked","fa-ban",          "--danger",  "Revoked"),
      ("users",  "fa-users",        "--accent",  "Users"),
    ] %}
    {% for key2,icon,color,label in scfg %}
    <div class="stat-card">
      <div class="d-flex align-items-center gap-3">
        <div class="stat-icon" style="background:rgba(126,179,214,.1);color:var({{ color }});">
          <i class="fa-solid fa-{{ icon }}"></i>
        </div>
        <div>
          <div class="stat-value" style="color:var(--silver);">{{ stats[key2] }}</div>
          <div class="stat-label">{{ label }}</div>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
  <ul class="nav m-tabs" id="aTabs">
    <li class="nav-item"><a class="nav-link active" href="#" onclick="showTab(event,'keys')"><i class="fa-solid fa-key me-1"></i>Keys</a></li>
    <li class="nav-item"><a class="nav-link" href="#" onclick="showTab(event,'gen')"><i class="fa-solid fa-plus me-1"></i>Generate</a></li>
    <li class="nav-item"><a class="nav-link" href="#" onclick="showTab(event,'users')"><i class="fa-solid fa-users me-1"></i>Users</a></li>
  </ul>
  <div id="tab-keys" class="tab-pane fade-in">
    <div class="tb-toolbar mt-3">
      <div class="d-flex gap-2 flex-wrap">
        <input type="text" id="fInp" class="form-control form-control-sm" placeholder="🔍  Search…" oninput="filterTbl()"/>
        <select id="fPlugin" class="form-select form-select-sm" onchange="filterTbl()">
          <option value="">All plugins</option>
          {% for p in plugins %}<option value="{{ p }}">{{ p }}</option>{% endfor %}
        </select>
        <select id="fStatus" class="form-select form-select-sm" onchange="filterTbl()">
          <option value="">All statuses</option>
          <option value="active">Active</option>
          <option value="expired">Expired</option>
          <option value="revoked">Revoked</option>
        </select>
      </div>
      <span class="text-muted" style="font-size:.8rem;" id="rCount">{{ keys|length }} keys</span>
    </div>
    <div style="overflow-x:auto;">
      <table class="m-table" id="kTbl">
        <thead><tr><th>Key</th><th>Plugin</th><th>Status</th><th>Expiry</th><th>Assigned To</th><th>Created</th><th>Actions</th></tr></thead>
        <tbody>
          {% for k in keys %}
          <tr data-plugin="{{ k.plugin }}" data-status="{{ k.status }}"
              data-search="{{ k.key }}|{{ k.plugin }}|{{ k.user_name }}|{{ k.status }}">
            <td><span class="key-display">{{ k.key }}</span>
              <button class="copy-btn ms-1" onclick="cpKey('{{ k.key }}',this)"><i class="fa-regular fa-copy"></i></button></td>
            <td><span class="pill-tag">{{ k.plugin }}</span></td>
            <td><span class="pill pill-{{ k.status }}">
              {% if k.status == "active" %}<i class="fa-solid fa-circle" style="font-size:.4rem;"></i> Active
              {% elif k.status == "expired" %}<i class="fa-solid fa-clock"></i> Expired
              {% else %}<i class="fa-solid fa-ban"></i> Revoked{% endif %}</span></td>
            <td style="font-size:.83rem;">
              {% if k.expiry == "Permanent" %}<i class="fa-solid fa-infinity" style="color:var(--success);"></i> Permanent
              {% elif k.expiry == "Expired" %}<span style="color:var(--danger);">Expired</span>
              {% else %}{{ k.expiry }}{% endif %}</td>
            <td style="font-size:.83rem;">{{ k.user_name }}
              {% if k.user_id %}<div class="text-muted mono" style="font-size:.7rem;">{{ k.user_id }}</div>{% endif %}</td>
            <td class="text-muted" style="font-size:.77rem;white-space:nowrap;">{{ k.created_at }}<br/><span style="font-size:.7rem;">by {{ k.created_by }}</span></td>
            <td><div class="d-flex gap-1 flex-wrap">
              {% if k.status != "active" %}
              <form method="POST" action="/admin/activate" style="display:inline">
                <input type="hidden" name="key" value="{{ k.key }}"/>
                <button type="submit" class="btn-act btn-act-ok"><i class="fa-solid fa-play"></i> Activate</button></form>
              {% endif %}
              {% if k.status == "active" %}
              <form method="POST" action="/admin/revoke" style="display:inline">
                <input type="hidden" name="key" value="{{ k.key }}"/>
                <button type="submit" class="btn-act btn-act-warn"><i class="fa-solid fa-ban"></i> Revoke</button></form>
              {% endif %}
              <form method="POST" action="/admin/delete" onsubmit="return confirm('Permanently delete this key?')" style="display:inline">
                <input type="hidden" name="key" value="{{ k.key }}"/>
                <button type="submit" class="btn-act btn-act-del"><i class="fa-solid fa-trash"></i></button></form>
            </div></td>
          </tr>
          {% else %}
          <tr><td colspan="7" class="text-center text-muted py-4">No license keys yet.</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
  <div id="tab-gen" class="tab-pane fade-in" style="display:none;">
    <div class="gen-card mt-3">
      <h3 class="fw-bold mb-4" style="font-size:1rem;color:var(--silver);">
        <i class="fa-solid fa-moon text-accent me-2"></i>Generate New License Key</h3>
      <form method="POST" action="/admin/generate">
        <div class="row g-3">
          <div class="col-md-4">
            <label class="form-label">Plugin</label>
            <select name="plugin" class="form-select" required>
              {% for p in plugins %}<option value="{{ p }}">{{ p }}</option>{% endfor %}</select></div>
          <div class="col-md-4">
            <label class="form-label">Duration</label>
            <select name="duration" class="form-select">
              <option value="permanent">♾ Permanent</option><option value="7d">7 days</option>
              <option value="30d">30 days</option><option value="90d">90 days</option>
              <option value="6mo">6 months</option><option value="1y">1 year</option></select></div>
          <div class="col-md-4">
            <label class="form-label">Custom Duration <span class="text-muted">(overrides above)</span></label>
            <input type="text" name="duration_custom" class="form-control" placeholder="e.g. 45d, 3mo, 2y"/></div>
          <div class="col-md-6">
            <label class="form-label">Assign to Discord ID <span class="text-muted">(optional)</span></label>
            <input type="text" name="assign_discord" class="form-control" placeholder="e.g. 123456789012345678"/></div>
          <div class="col-md-6">
            <label class="form-label">Display Name <span class="text-muted">(optional)</span></label>
            <input type="text" name="assign_name" class="form-control" placeholder="Username or label"/></div>
          <div class="col-12 pt-1">
            <button type="submit" class="btn btn-moon px-4"><i class="fa-solid fa-key me-2"></i>Generate Key</button></div>
        </div>
      </form>
    </div>
    <div class="m-card mt-4">
      <h6 class="fw-bold mb-2" style="color:var(--silver);"><i class="fa-solid fa-plug text-accent me-2"></i>Plugin Verification Endpoint</h6>
      <p class="text-muted mb-2" style="font-size:.84rem;">Point this URL in your plugin <code>config.yml</code>:</p>
      <div class="key-display" style="padding:.65rem 1rem;word-break:break-all;font-size:.78rem;">
        {{ request.host_url }}api/v1/verify?key={LICENSE_KEY}</div>
      <p class="text-muted mt-2 mb-0" style="font-size:.78rem;">
        Returns <code>{"valid":true,"plugin":"...","expiry":"..."}</code> on success.</p>
    </div>
  </div>
  <div id="tab-users" class="tab-pane fade-in" style="display:none;">
    <div style="overflow-x:auto;" class="mt-3">
      <table class="m-table">
        <thead><tr><th>User</th><th>Email</th><th>Providers</th><th>Discord ID</th><th>Joined</th><th>Role</th><th>Action</th></tr></thead>
        <tbody>
          {% for u in users %}
          <tr>
            <td><div class="d-flex align-items-center gap-2">
              {% if u.avatar %}<img src="{{ u.avatar }}" class="usr-avatar" alt="av"/>{% endif %}
              <span class="fw-semibold" style="font-size:.88rem;color:var(--silver);">{{ u.username }}</span></div></td>
            <td class="text-muted" style="font-size:.83rem;">{{ u.email or "—" }}</td>
            <td>{% if u.discord_id %}<span class="pill-tag me-1"><i class="fa-brands fa-discord"></i></span>{% endif %}
              {% if u.google_id %}<span class="pill-tag" style="background:rgba(234,67,53,.08);color:#f08080;"><i class="fa-brands fa-google"></i></span>{% endif %}</td>
            <td class="mono text-muted" style="font-size:.77rem;">{{ u.discord_id or "—" }}</td>
            <td class="text-muted" style="font-size:.77rem;">{{ u.created_at[:10] if u.created_at else "—" }}</td>
            <td>{% if u.is_admin %}<span class="pill-tag"><i class="fa-solid fa-moon"></i> Admin</span>
              {% else %}<span class="text-muted" style="font-size:.83rem;">User</span>{% endif %}</td>
            <td>{% if u.id != current_user.id %}
              <form method="POST" action="/admin/set-admin" style="display:inline">
                <input type="hidden" name="uid" value="{{ u.id }}"/>
                <input type="hidden" name="is_admin" value="{{ '0' if u.is_admin else '1' }}"/>
                <button type="submit" class="btn-act {{ 'btn-act-warn' if u.is_admin else 'btn-act-ok' }}">
                  {% if u.is_admin %}<i class="fa-solid fa-user-minus"></i> Remove{% else %}<i class="fa-solid fa-moon"></i> Make Admin{% endif %}
                </button></form>
              {% else %}<span class="text-muted" style="font-size:.77rem;">You</span>{% endif %}</td>
          </tr>
          {% else %}
          <tr><td colspan="7" class="text-center text-muted py-4">No users registered yet.</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
</div>
{% endblock %}
{% block extra_scripts %}
<script>
function showTab(e,name){
  e.preventDefault();
  document.querySelectorAll(".tab-pane").forEach(el=>el.style.display="none");
  document.querySelectorAll(".m-tabs .nav-link").forEach(el=>el.classList.remove("active"));
  document.getElementById("tab-"+name).style.display="";
  e.target.classList.add("active");
  history.replaceState(null,"","#"+name);
}
window.addEventListener("DOMContentLoaded",()=>{
  const h=location.hash.replace("#","");
  if(["keys","gen","users"].includes(h)){
    const lk=document.querySelector(`.m-tabs .nav-link[onclick*="'${h}'"]`);
    if(lk)lk.click();
  }
});
function filterTbl(){
  const q=document.getElementById("fInp").value.toLowerCase();
  const pl=document.getElementById("fPlugin").value.toLowerCase();
  const st=document.getElementById("fStatus").value.toLowerCase();
  const rows=document.querySelectorAll("#kTbl tbody tr[data-search]");
  let c=0;
  rows.forEach(r=>{
    const m=(!q||r.dataset.search.toLowerCase().includes(q))
          &&(!pl||r.dataset.plugin.toLowerCase()===pl)
          &&(!st||r.dataset.status.toLowerCase()===st);
    r.style.display=m?"":"none"; if(m)c++;
  });
  document.getElementById("rCount").textContent=c+" keys";
}
function cpKey(k,btn){navigator.clipboard.writeText(k).then(()=>{
  const i=btn.querySelector("i");i.className="fa-solid fa-check";
  btn.style.color="var(--success)";
  setTimeout(()=>{i.className="fa-regular fa-copy";btn.style.color="";},1800);
});}
document.addEventListener("DOMContentLoaded",()=>{
  const c=document.querySelector("input[name=duration_custom]");
  const s=document.querySelector("select[name=duration]");
  if(c&&s)c.addEventListener("input",()=>{
    if(c.value.trim()){s.name="_dur";c.name="duration";}
    else{s.name="duration";c.name="duration_custom";}
  });
});
</script>
{% endblock %}"""

T['error.html'] = """{% extends "base.html" %}
{% block title %}{{ code }} – Astatine Studio{% endblock %}
{% block content %}
<div style="min-height:72vh;display:flex;align-items:center;justify-content:center;flex-direction:column;text-align:center;gap:1rem;">
  <div style="font-size:6rem;opacity:.08;line-height:1;">🌑</div>
  <div style="font-size:4rem;font-weight:800;color:var(--silver);line-height:1;margin-top:-3rem;">{{ code }}</div>
  <div class="fw-semibold" style="color:var(--dim);font-size:1rem;">{{ message }}</div>
  <a href="/" class="btn btn-moon px-4 mt-2"><i class="fa-solid fa-moon me-2"></i>Go Home</a>
</div>
{% endblock %}"""