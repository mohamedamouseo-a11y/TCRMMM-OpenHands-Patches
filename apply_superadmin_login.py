#!/usr/bin/env python3
from pathlib import Path
import shutil, sys

ROOT = Path('/var/www/TCRMMT')
INDEX = ROOT / 'server/_core/index.ts'
TARGET_LOGO = ROOT / 'client/public/tamiyouz-superadmin-logo.png'
SOURCE_LOGO = ROOT / 'client/public/logo.png'
MARKER = 'TAMIYOUZ_SUPER_ADMIN_LOGIN_LIGHT_V1'

if not INDEX.exists():
    raise SystemExit('FIRST_ERROR=missing_server_core_index')

text = INDEX.read_text(encoding='utf-8')
if MARKER in text:
    print('APPLY=ALREADY_APPLIED')
    raise SystemExit(0)

old = '''<section id="loginView" class="loginScreen">
  <div class="card loginCard">
    <div class="loginBrand"><div class="logoMark">T</div><div><strong>TCRM Multi</strong><span>Super Admin Console</span></div></div>
    <h2>تسجيل الدخول</h2>
    <p class="muted">دخول آمن للـ Super Admin فقط.</p>
    <div class="stack mt-md">
      <div class="field"><label>Email</label><input id="loginEmail" placeholder="admin@company.com" autocomplete="username" /></div>
      <div class="field"><label>Password</label><input id="loginPassword" type="password" placeholder="••••••••••" autocomplete="current-password" /></div>
      <button class="btn primary block" id="loginBtn">دخول</button>
    </div>
    <p id="loginMsg" class="msg" role="status"></p>
  </div>
</section>'''

new = '''<section id="loginView" class="loginScreen tamiyouzLogin" data-ui="TAMIYOUZ_SUPER_ADMIN_LOGIN_LIGHT_V1">
  <div class="tamiyouzLoginShell">
    <div class="tamiyouzLoginBrand" aria-label="Tamiyouz">
      <img class="tamiyouzLoginLogo" src="/tamiyouz-superadmin-logo.png" alt="Tamiyouz" />
      <span class="tamiyouzLoginBrandName">TAMIYOUZ</span>
    </div>

    <div class="tamiyouzLoginHeading">
      <span class="tamiyouzLoginEyebrow">SUPER ADMIN</span>
      <h1>Super Admin Portal</h1>
      <p>Secure platform administration</p>
      <div class="tamiyouzSecurityBadge"><span aria-hidden="true">◆</span> Protected Administrative Access</div>
    </div>

    <div class="card loginCard tamiyouzLoginCard">
      <form class="tamiyouzLoginForm" onsubmit="return false" aria-label="Super Admin sign in">
        <div class="field tamiyouzField">
          <label for="loginEmail">Email address</label>
          <div class="tamiyouzInputWrap">
            <span class="tamiyouzInputIcon" aria-hidden="true">✉</span>
            <input id="loginEmail" type="email" placeholder="admin@tamiyouz.com" autocomplete="username" inputmode="email" />
          </div>
        </div>
        <div class="field tamiyouzField">
          <label for="loginPassword">Password</label>
          <div class="tamiyouzInputWrap">
            <span class="tamiyouzInputIcon" aria-hidden="true">●</span>
            <input id="loginPassword" type="password" placeholder="Enter your password" autocomplete="current-password" />
          </div>
        </div>
        <button class="btn primary block tamiyouzSignIn" id="loginBtn" type="button">Sign In <span aria-hidden="true">→</span></button>
      </form>
      <p id="loginMsg" class="msg tamiyouzLoginMsg" role="status" aria-live="polite"></p>
    </div>

    <div class="tamiyouzLoginFooter">
      <span>Tamiyouz Platform Administration</span>
      <span class="tamiyouzFooterDot" aria-hidden="true"></span>
      <span>Secure access</span>
    </div>
  </div>
</section>'''

if old not in text:
    raise SystemExit('FIRST_ERROR=expected_login_markup_not_found')

css = r'''

    /* TAMIYOUZ_SUPER_ADMIN_LOGIN_LIGHT_V1 */
    #loginView.tamiyouzLogin{
      position:fixed;inset:0;z-index:100;overflow:auto;display:grid;place-items:center;
      min-height:100vh;padding:38px 20px;
      background:
        radial-gradient(circle at 12% 10%,rgba(196,154,73,.10),transparent 28%),
        radial-gradient(circle at 88% 88%,rgba(190,148,62,.08),transparent 30%),
        linear-gradient(180deg,#fbfaf7 0%,#f7f5ef 100%)!important;
      color:#162135;
    }
    #loginView.tamiyouzLogin::before,#loginView.tamiyouzLogin::after{
      content:"";position:fixed;pointer-events:none;border:1px solid rgba(191,151,74,.14);border-radius:50%;
      width:58vw;height:58vw;min-width:520px;min-height:520px;transform:rotate(-12deg);z-index:0;
    }
    #loginView.tamiyouzLogin::before{left:-35vw;bottom:-36vw}
    #loginView.tamiyouzLogin::after{right:-37vw;top:-38vw}
    #loginView .tamiyouzLoginShell{position:relative;z-index:1;width:min(100%,520px);display:flex;flex-direction:column;align-items:center}
    #loginView .tamiyouzLoginBrand{display:flex;flex-direction:column;align-items:center;gap:7px;margin-bottom:20px}
    #loginView .tamiyouzLoginLogo{display:block;width:72px!important;height:72px!important;object-fit:contain;filter:drop-shadow(0 8px 18px rgba(151,111,34,.12))}
    #loginView .tamiyouzLoginBrandName{font-size:10px;letter-spacing:.34em;font-weight:800;color:#a77c2e;margin-left:.34em}
    #loginView .tamiyouzLoginHeading{text-align:center;margin-bottom:25px}
    #loginView .tamiyouzLoginEyebrow{display:inline-block;margin-bottom:8px;font-size:10px;letter-spacing:.24em;font-weight:900;color:#aa7c2d}
    #loginView .tamiyouzLoginHeading h1{margin:0!important;font-size:clamp(28px,3vw,38px)!important;line-height:1.2!important;letter-spacing:-.035em!important;color:#142033!important;font-weight:850!important}
    #loginView .tamiyouzLoginHeading p{margin:8px 0 13px!important;color:#7a818d!important;font-size:13px!important}
    #loginView .tamiyouzSecurityBadge{display:inline-flex;align-items:center;gap:7px;padding:6px 10px;border-radius:999px;border:1px solid rgba(183,140,61,.22);background:rgba(255,255,255,.64);color:#9c742d;font-size:9px;font-weight:800;letter-spacing:.03em;box-shadow:0 5px 18px rgba(35,44,59,.035)}
    #loginView .tamiyouzLoginCard{width:100%!important;padding:26px 28px 24px!important;border-radius:18px!important;border:1px solid #e6dfd3!important;background:rgba(255,255,255,.94)!important;box-shadow:0 22px 55px rgba(24,35,52,.09),inset 0 1px 0 rgba(255,255,255,.9)!important}
    #loginView .tamiyouzLoginCard:hover{border-color:#e0d5c3!important;box-shadow:0 22px 55px rgba(24,35,52,.09),inset 0 1px 0 rgba(255,255,255,.9)!important;transform:none!important}
    #loginView .tamiyouzLoginForm{display:grid;gap:17px}
    #loginView .tamiyouzField{display:grid;gap:7px}
    #loginView .tamiyouzField label{font-size:10px!important;text-transform:uppercase;letter-spacing:.09em;font-weight:850!important;color:#4d5665!important}
    #loginView .tamiyouzInputWrap{position:relative}
    #loginView .tamiyouzInputIcon{position:absolute;left:14px;top:50%;transform:translateY(-50%);z-index:2;width:18px;text-align:center;color:#b08a48;font-size:12px;opacity:.88}
    #loginView .tamiyouzInputWrap input{width:100%!important;height:46px!important;padding:0 14px 0 42px!important;border-radius:9px!important;border:1px solid #dfd9ce!important;background:#fff!important;color:#1c2636!important;font-size:13px!important;box-shadow:0 1px 0 rgba(255,255,255,.8),inset 0 1px 2px rgba(35,44,59,.015)!important;transition:border-color .16s ease,box-shadow .16s ease!important}
    #loginView .tamiyouzInputWrap input::placeholder{color:#a3a8b0}
    #loginView .tamiyouzInputWrap input:focus{outline:none!important;border-color:#bd9448!important;box-shadow:0 0 0 3px rgba(189,148,72,.12)!important}
    #loginView .tamiyouzSignIn{height:46px!important;margin-top:2px!important;border-radius:9px!important;border:1px solid #17243a!important;background:linear-gradient(180deg,#263b5d 0%,#1c2e4b 100%)!important;color:#fff!important;font-size:11px!important;letter-spacing:.04em!important;font-weight:850!important;box-shadow:0 9px 22px rgba(26,45,75,.15)!important;display:flex!important;align-items:center!important;justify-content:center!important;gap:9px!important;transition:transform .16s ease,box-shadow .16s ease!important}
    #loginView .tamiyouzSignIn:hover{transform:translateY(-1px)!important;box-shadow:0 12px 28px rgba(26,45,75,.20)!important}
    #loginView .tamiyouzSignIn:active{transform:translateY(0)!important}
    #loginView .tamiyouzLoginMsg{min-height:18px;margin:12px 0 0!important;text-align:center!important;font-size:11px!important;color:#8c3c47!important}
    #loginView .tamiyouzLoginFooter{display:flex;align-items:center;justify-content:center;gap:9px;margin-top:19px;color:#9a9da3;font-size:8px;text-transform:uppercase;letter-spacing:.13em;font-weight:750;text-align:center}
    #loginView .tamiyouzFooterDot{width:3px;height:3px;border-radius:50%;background:#bd9448}
    @media(max-width:600px){
      #loginView.tamiyouzLogin{padding:24px 15px}
      #loginView .tamiyouzLoginLogo{width:62px!important;height:62px!important}
      #loginView .tamiyouzLoginHeading{margin-bottom:20px}
      #loginView .tamiyouzLoginHeading h1{font-size:27px!important}
      #loginView .tamiyouzLoginCard{padding:22px 18px 20px!important;border-radius:16px!important}
      #loginView .tamiyouzLoginFooter{flex-wrap:wrap;line-height:1.6}
    }
    @media(prefers-reduced-motion:reduce){#loginView *{scroll-behavior:auto!important;transition:none!important}}
    /* END TAMIYOUZ_SUPER_ADMIN_LOGIN_LIGHT_V1 */
'''

style_anchor = '</style>\n</head>\n<body>'
if style_anchor not in text:
    raise SystemExit('FIRST_ERROR=superadmin_style_anchor_not_found')

text = text.replace(old, new, 1)
text = text.replace(style_anchor, css + '\n</style>\n</head>\n<body>', 1)
INDEX.write_text(text, encoding='utf-8')

if not TARGET_LOGO.exists():
    if SOURCE_LOGO.exists():
        TARGET_LOGO.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SOURCE_LOGO, TARGET_LOGO)
        print('LOGO_SOURCE=client/public/logo.png')
    else:
        raise SystemExit('FIRST_ERROR=logo_source_missing: place the approved Tamiyouz PNG at client/public/tamiyouz-superadmin-logo.png before running')

print('APPLY=PASS')
print('FILES_CHANGED=server/_core/index.ts,client/public/tamiyouz-superadmin-logo.png')
