#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1'
ANCHOR = '/* END SUPER_ADMIN_LOGIN_REFERENCE_MATCH_V2 */'

CSS = r'''
    /* SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1 */
    /* Presentation-only login gate refinement. Keep existing auth, recovery,
       IDs, handlers, routes and permissions unchanged. */

    /* The authenticated shell must never win an !important display rule while
       the login gate is active. This fixes Usage/Search/Security leaking under
       the unauthenticated login screen at responsive breakpoints. */
    #appShell.hidden{display:none!important;}
    body:has(#loginView:not(.hidden)) #appShell,
    body:has(#loginView:not(.hidden)) #impersonationBanner{display:none!important;}

    #loginView.tamiyouzLogin{
      position:fixed!important;
      inset:0!important;
      min-height:100dvh!important;
      overflow:auto!important;
      overscroll-behavior:contain;
      background:#f6f4ee!important;
    }
    #loginView .tamiyouzLoginShell{
      min-height:100dvh!important;
      grid-template-columns:minmax(360px,42vw) minmax(0,1fr)!important;
      align-items:stretch!important;
    }
    #loginView .tamiyouzLoginBrandPanel{
      min-height:100dvh!important;
      padding:clamp(42px,5vw,76px) clamp(34px,5vw,72px) 34px!important;
    }
    #loginView .tamiyouzBrandContent{
      margin:auto 0!important;
      max-width:430px!important;
    }
    #loginView .tamiyouzBrandTitle{
      font-size:clamp(44px,4.5vw,64px)!important;
    }
    #loginView .tamiyouzBrandContent h1{
      max-width:410px!important;
      font-size:clamp(27px,2.35vw,34px)!important;
    }
    #loginView .tamiyouzLoginMain{
      position:relative!important;
      justify-content:center!important;
      align-items:center!important;
      min-height:100dvh!important;
      padding:64px clamp(28px,6vw,88px) 34px!important;
      background:
        radial-gradient(circle at 88% 8%,rgba(196,154,88,.08),transparent 28%),
        linear-gradient(145deg,#ffffff 0%,#f8f6f0 100%)!important;
    }
    #loginView .tamiyouzLoginUtility{
      position:absolute!important;
      top:24px!important;
      right:30px!important;
      width:auto!important;
      z-index:3!important;
    }
    #loginView .tamiyouzLoginUtility span:first-child{
      background:rgba(255,255,255,.86)!important;
      border-color:#dde3eb!important;
    }
    #loginView .tamiyouzLoginCard{
      width:min(520px,100%)!important;
      max-width:520px!important;
      margin:0 auto!important;
      padding:32px 34px 28px!important;
      border:1px solid #dfe4eb!important;
      border-radius:18px!important;
      background:rgba(255,255,255,.98)!important;
      box-shadow:0 22px 56px rgba(21,39,64,.10)!important;
    }
    #loginView .tamiyouzFormIntro{
      padding-bottom:18px!important;
    }
    #loginView .tamiyouzFormKicker::after{
      content:' · OWNER ONLY';
      color:#8c96a3;
      letter-spacing:.10em;
    }
    #loginView .tamiyouzFormIntro h2{
      font-size:27px!important;
    }
    #loginView .tamiyouzLoginForm{
      gap:16px!important;
    }
    #loginView .tamiyouzInputWrap input{
      height:50px!important;
    }
    #loginView .tamiyouzSignIn{
      height:50px!important;
      min-height:50px!important;
    }
    #loginView .tamiyouzLoginMsg{
      min-height:0!important;
      margin:10px 0 0!important;
    }
    #loginView .tamiyouzLoginMsg:empty{
      display:none!important;
    }
    #loginView .tamiyouzLoginMsg:not(:empty){
      position:relative!important;
      display:flex!important;
      width:100%!important;
      margin-top:10px!important;
    }
    #loginView .tamiyouzSecurityNote{
      margin:18px 0 0!important;
      padding-top:14px!important;
      font-size:10.5px!important;
    }
    #loginView .tamiyouzSecurityNoteIcon{
      width:28px!important;
      height:28px!important;
    }
    #loginView .tamiyouzLoginFooter{
      width:min(520px,100%)!important;
      margin:18px auto 0!important;
      padding-top:0!important;
    }
    #loginView .tamiyouzLoginCard button:focus-visible,
    #loginView .tamiyouzLoginCard input:focus-visible,
    #loginView .tamiyouzLoginCard a:focus-visible{
      outline:3px solid rgba(196,154,88,.28)!important;
      outline-offset:2px!important;
    }

    /* Laptop/tablet: branding becomes a compact security header so the
       authentication form remains visible in the initial viewport. */
    @media(max-width:1100px){
      #loginView .tamiyouzLoginShell{
        grid-template-columns:1fr!important;
        grid-template-rows:210px minmax(0,1fr)!important;
      }
      #loginView .tamiyouzLoginBrandPanel{
        min-height:0!important;
        height:210px!important;
        padding:22px 32px 18px!important;
      }
      #loginView .tamiyouzLoginBrand{
        gap:8px!important;
      }
      #loginView .tamiyouzLoginLogo{
        width:42px!important;
      }
      #loginView .tamiyouzBrandContent{
        margin:14px 0 0!important;
        max-width:760px!important;
      }
      #loginView .tamiyouzBrandTitle{
        font-size:38px!important;
      }
      #loginView .tamiyouzBrandRule{
        width:52px!important;
        margin:9px 0 10px!important;
      }
      #loginView .tamiyouzBrandContent h1{
        display:inline!important;
        margin:0 12px 0 0!important;
        font-size:20px!important;
      }
      #loginView .tamiyouzBrandContent p{
        display:inline!important;
        margin:0!important;
        font-size:11px!important;
        line-height:1.45!important;
      }
      #loginView .tamiyouzSecurityBadge{
        margin-top:12px!important;
        padding:6px 10px!important;
        font-size:8.5px!important;
      }
      #loginView .tamiyouzBrandMeta{
        display:none!important;
      }
      #loginView .tamiyouzLoginMain{
        min-height:0!important;
        padding:54px 22px 24px!important;
      }
      #loginView .tamiyouzLoginUtility{
        top:14px!important;
        right:20px!important;
      }
      #loginView .tamiyouzLoginCard{
        margin:0 auto!important;
        padding:26px 30px 24px!important;
      }
      #loginView .tamiyouzLoginFooter{
        margin-top:12px!important;
      }
    }

    @media(max-width:700px){
      #loginView .tamiyouzLoginShell{
        grid-template-rows:168px minmax(0,1fr)!important;
      }
      #loginView .tamiyouzLoginBrandPanel{
        height:168px!important;
        padding:15px 20px 14px!important;
      }
      #loginView .tamiyouzLoginLogo{width:34px!important;}
      #loginView .tamiyouzLoginBrandName{font-size:9px!important;}
      #loginView .tamiyouzBrandContent{margin-top:10px!important;}
      #loginView .tamiyouzBrandTitle{font-size:32px!important;}
      #loginView .tamiyouzBrandRule{margin:7px 0 8px!important;}
      #loginView .tamiyouzBrandContent h1{font-size:17px!important;}
      #loginView .tamiyouzBrandContent p{display:none!important;}
      #loginView .tamiyouzSecurityBadge{margin-top:8px!important;padding:5px 8px!important;}
      #loginView .tamiyouzLoginMain{padding:48px 12px 18px!important;}
      #loginView .tamiyouzLoginUtility{top:10px!important;right:12px!important;gap:10px!important;}
      #loginView .tamiyouzLoginCard{padding:23px 20px 20px!important;border-radius:15px!important;}
      #loginView .tamiyouzFormIntro{padding-bottom:14px!important;}
      #loginView .tamiyouzFormIntro h2{font-size:23px!important;}
      #loginView .tamiyouzLoginForm{gap:13px!important;}
      #loginView .tamiyouzInputWrap input{height:48px!important;}
      #loginView .tamiyouzSignIn{height:48px!important;min-height:48px!important;}
      #loginView .tamiyouzSecurityNote{margin-top:12px!important;padding-top:11px!important;}
      #loginView .tamiyouzLoginFooter{margin-top:10px!important;font-size:7.5px!important;}
    }

    @media(max-width:440px){
      #loginView .tamiyouzLoginShell{grid-template-rows:138px minmax(0,1fr)!important;}
      #loginView .tamiyouzLoginBrandPanel{height:138px!important;padding:12px 16px!important;}
      #loginView .tamiyouzLoginBrand{gap:6px!important;}
      #loginView .tamiyouzLoginLogo{width:30px!important;}
      #loginView .tamiyouzBrandContent{margin-top:7px!important;}
      #loginView .tamiyouzBrandTitle{font-size:29px!important;}
      #loginView .tamiyouzBrandRule{width:42px!important;margin:5px 0 6px!important;}
      #loginView .tamiyouzBrandContent h1{font-size:15px!important;}
      #loginView .tamiyouzSecurityBadge{display:none!important;}
      #loginView .tamiyouzLoginMain{padding:43px 9px 14px!important;}
      #loginView .tamiyouzLoginUtility{font-size:9px!important;}
      #loginView .tamiyouzLoginUtility span:first-child{padding:5px 8px!important;}
      #loginView .tamiyouzLoginCard{width:100%!important;padding:20px 17px 18px!important;}
      #loginView .tamiyouzFormIntro h2{font-size:21px!important;}
      #loginView .tamiyouzFormIntro p{font-size:10.5px!important;}
      #loginView .tamiyouzSecurityNote{display:none!important;}
      #loginView .tamiyouzLoginFooter{display:none!important;}
    }

    /* Real dark mode for the login surface, not only the shell behind it. */
    html[data-theme="dark"] #loginView.tamiyouzLogin,
    html[data-sa-theme="dark"] #loginView.tamiyouzLogin{
      background:#08111d!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzLoginMain,
    html[data-sa-theme="dark"] #loginView .tamiyouzLoginMain{
      background:
        radial-gradient(circle at 88% 8%,rgba(196,154,88,.08),transparent 28%),
        linear-gradient(145deg,#0b1421 0%,#101b2b 100%)!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzLoginCard,
    html[data-sa-theme="dark"] #loginView .tamiyouzLoginCard{
      background:#111d2d!important;
      border-color:#2a3a50!important;
      box-shadow:0 24px 64px rgba(0,0,0,.34)!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzFormIntro,
    html[data-sa-theme="dark"] #loginView .tamiyouzFormIntro{
      border-bottom-color:#2a3a50!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzFormIntro h2,
    html[data-theme="dark"] #loginView .tamiyouzField label,
    html[data-sa-theme="dark"] #loginView .tamiyouzFormIntro h2,
    html[data-sa-theme="dark"] #loginView .tamiyouzField label{
      color:#eef4fb!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzFormIntro p,
    html[data-theme="dark"] #loginView .tamiyouzFieldHint,
    html[data-sa-theme="dark"] #loginView .tamiyouzFormIntro p,
    html[data-sa-theme="dark"] #loginView .tamiyouzFieldHint{
      color:#9eacc0!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzInputWrap input,
    html[data-sa-theme="dark"] #loginView .tamiyouzInputWrap input{
      background:#142238!important;
      border-color:#2d4059!important;
      color:#f3f7fc!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzInputWrap input::placeholder,
    html[data-sa-theme="dark"] #loginView .tamiyouzInputWrap input::placeholder{
      color:#788aa2!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzInputIcon,
    html[data-sa-theme="dark"] #loginView .tamiyouzInputIcon{
      background:#1d2d43!important;
      color:#d1ad66!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzPasswordToggle,
    html[data-sa-theme="dark"] #loginView .tamiyouzPasswordToggle{
      background:#18283d!important;
      border-color:#33475f!important;
      color:#d6b36d!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzLoginUtility,
    html[data-sa-theme="dark"] #loginView .tamiyouzLoginUtility{
      color:#9cabc0!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzLoginUtility span:first-child,
    html[data-sa-theme="dark"] #loginView .tamiyouzLoginUtility span:first-child{
      background:#111d2d!important;
      border-color:#2b3b51!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzSecurityNote,
    html[data-sa-theme="dark"] #loginView .tamiyouzSecurityNote{
      border-top-color:#2a3a50!important;
      color:#95a5ba!important;
    }
    /* END SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1 */
'''


def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        print('Premium login gate already applied; no changes made.')
        return

    if ANCHOR not in text:
        raise SystemExit('Super Admin Login V2 anchor not found; refusing to patch an unknown baseline.')
    if text.count(ANCHOR) != 1:
        raise SystemExit('Unexpected login anchor count; refusing ambiguous patch application.')

    required = [
        'id="loginView"',
        'id="appShell"',
        'id="loginFormPanel"',
        'id="loginEmail"',
        'id="loginPassword"',
        'id="loginToggleBtn"',
        'id="forgotPasswordLink"',
        'id="loginBtn"',
        'id="loginMsg"',
        'tamiyouzLoginBrandPanel',
        'tamiyouzLoginMain',
        'tamiyouzLoginCard',
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise SystemExit('Login baseline mismatch; missing: ' + ', '.join(missing))

    text = text.replace(ANCHOR, ANCHOR + '\n\n' + CSS, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Premium Login Control Gate V1.')


if __name__ == '__main__':
    main()
