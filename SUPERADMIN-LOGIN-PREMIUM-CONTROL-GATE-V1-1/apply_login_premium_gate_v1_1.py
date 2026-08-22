#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1_1'
ANCHOR = '/* END SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1 */'

CSS = r'''
    /* SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1_1 */
    /* Corrective visual-only pass after real responsive QA:
       - fit the full sign-in task above the fold at 1024x768,
       - remove the perceived double-surface on tablet/mobile,
       - make dark mode one coherent security surface. */

    #loginView .tamiyouzLoginMain.sa-page-frame{
      width:100%!important;
      max-width:none!important;
      margin:0!important;
      border:0!important;
      border-radius:0!important;
      box-shadow:none!important;
    }
    #loginView .tamiyouzLoginCard{
      width:min(500px,calc(100% - 24px))!important;
      max-width:500px!important;
      margin:0 auto!important;
      overflow:hidden!important;
    }
    #loginView #loginFormPanel{
      width:100%!important;
      min-width:0!important;
      margin:0!important;
      padding:0!important;
      border:0!important;
      border-radius:0!important;
      background:transparent!important;
      box-shadow:none!important;
    }

    /* Laptop/tablet height corrective: keep the entire authentication task,
       including the primary CTA, in the initial 768px viewport. */
    @media(max-width:1100px){
      #loginView .tamiyouzLoginShell{
        grid-template-rows:150px minmax(0,1fr)!important;
      }
      #loginView .tamiyouzLoginBrandPanel{
        height:150px!important;
        min-height:0!important;
        padding:16px 28px 12px!important;
      }
      #loginView .tamiyouzLoginBrand{gap:6px!important;}
      #loginView .tamiyouzLoginLogo{width:34px!important;}
      #loginView .tamiyouzLoginBrandName{font-size:9px!important;}
      #loginView .tamiyouzBrandContent{
        margin:8px 0 0!important;
      }
      #loginView .tamiyouzBrandTitle{
        font-size:31px!important;
        line-height:1!important;
      }
      #loginView .tamiyouzBrandRule{
        width:46px!important;
        margin:6px 0 7px!important;
      }
      #loginView .tamiyouzBrandContent h1{
        display:inline!important;
        margin:0 10px 0 0!important;
        font-size:17px!important;
        line-height:1.2!important;
      }
      #loginView .tamiyouzBrandContent p{
        display:none!important;
      }
      #loginView .tamiyouzSecurityBadge{
        margin-top:7px!important;
        padding:5px 8px!important;
        font-size:8px!important;
      }
      #loginView .tamiyouzLoginMain.sa-page-frame{
        min-height:calc(100dvh - 150px)!important;
        padding:40px 18px 16px!important;
        justify-content:flex-start!important;
      }
      #loginView .tamiyouzLoginUtility{
        top:9px!important;
        right:18px!important;
        gap:10px!important;
        font-size:9px!important;
      }
      #loginView .tamiyouzLoginCard{
        width:min(480px,calc(100% - 16px))!important;
        padding:20px 24px 18px!important;
        border-radius:15px!important;
      }
      #loginView .tamiyouzFormIntro{
        gap:4px!important;
        padding-bottom:11px!important;
      }
      #loginView .tamiyouzFormIntro h2{
        font-size:22px!important;
      }
      #loginView .tamiyouzFormIntro p{
        font-size:10.5px!important;
      }
      #loginView .tamiyouzLoginForm{
        gap:10px!important;
      }
      #loginView .tamiyouzField{
        gap:5px!important;
      }
      #loginView .tamiyouzField label{
        font-size:10px!important;
      }
      #loginView .tamiyouzInputWrap input{
        height:44px!important;
      }
      #loginView .tamiyouzRecoveryRow{
        min-height:26px!important;
      }
      #loginView .tamiyouzRecoveryLink{
        padding:2px 0!important;
        font-size:9.5px!important;
      }
      #loginView .tamiyouzSignIn{
        height:46px!important;
        min-height:46px!important;
      }
      #loginView .tamiyouzSecurityNote{
        margin-top:10px!important;
        padding-top:9px!important;
        font-size:9.5px!important;
      }
      #loginView .tamiyouzSecurityNoteIcon{
        width:24px!important;
        height:24px!important;
      }
      #loginView .tamiyouzLoginFooter{
        margin-top:8px!important;
        font-size:8px!important;
      }
    }

    @media(max-width:700px){
      #loginView .tamiyouzLoginShell{
        grid-template-rows:118px minmax(0,1fr)!important;
      }
      #loginView .tamiyouzLoginBrandPanel{
        height:118px!important;
        padding:10px 16px 9px!important;
      }
      #loginView .tamiyouzLoginLogo{width:28px!important;}
      #loginView .tamiyouzBrandContent{margin-top:5px!important;}
      #loginView .tamiyouzBrandTitle{font-size:27px!important;}
      #loginView .tamiyouzBrandRule{margin:4px 0 5px!important;}
      #loginView .tamiyouzBrandContent h1{font-size:14px!important;}
      #loginView .tamiyouzSecurityBadge{display:none!important;}
      #loginView .tamiyouzLoginMain.sa-page-frame{
        min-height:calc(100dvh - 118px)!important;
        padding:38px 8px 12px!important;
      }
      #loginView .tamiyouzLoginUtility{
        top:8px!important;
        right:10px!important;
      }
      #loginView .tamiyouzLoginCard{
        width:min(430px,calc(100% - 8px))!important;
        padding:18px 18px 16px!important;
        border-radius:14px!important;
      }
      #loginView .tamiyouzFormIntro h2{font-size:20px!important;}
      #loginView .tamiyouzFormIntro p{font-size:10px!important;}
      #loginView .tamiyouzInputWrap input{height:44px!important;}
      #loginView .tamiyouzSignIn{height:44px!important;min-height:44px!important;}
      #loginView .tamiyouzSecurityNote{display:none!important;}
      #loginView .tamiyouzLoginFooter{display:none!important;}
    }

    @media(max-width:440px){
      #loginView .tamiyouzLoginShell{
        grid-template-rows:104px minmax(0,1fr)!important;
      }
      #loginView .tamiyouzLoginBrandPanel{
        height:104px!important;
        padding:8px 14px!important;
      }
      #loginView .tamiyouzBrandTitle{font-size:25px!important;}
      #loginView .tamiyouzBrandContent h1{font-size:13px!important;}
      #loginView .tamiyouzLoginMain.sa-page-frame{
        min-height:calc(100dvh - 104px)!important;
        padding:36px 6px 10px!important;
      }
      #loginView .tamiyouzLoginCard{
        width:calc(100% - 12px)!important;
        max-width:none!important;
        padding:17px 16px 15px!important;
      }
      #loginView .tamiyouzFormKicker{font-size:8.5px!important;}
      #loginView .tamiyouzFormIntro h2{font-size:19px!important;}
      #loginView .tamiyouzLoginForm{gap:9px!important;}
      #loginView .tamiyouzInputWrap input{height:43px!important;}
      #loginView .tamiyouzSignIn{height:43px!important;min-height:43px!important;}
    }

    /* Coherent dark mode: the actual form/card surface must also be dark. */
    html[data-theme="dark"] #loginView .tamiyouzLoginCard,
    html[data-sa-theme="dark"] #loginView .tamiyouzLoginCard{
      background:#111d2d!important;
      border-color:#2a3a50!important;
      color:#eef4fb!important;
      box-shadow:0 22px 56px rgba(0,0,0,.32)!important;
    }
    html[data-theme="dark"] #loginView #loginFormPanel,
    html[data-sa-theme="dark"] #loginView #loginFormPanel{
      background:transparent!important;
      border:0!important;
      color:#eef4fb!important;
      box-shadow:none!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzFormKicker,
    html[data-sa-theme="dark"] #loginView .tamiyouzFormKicker{
      color:#d7b46c!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzRecoveryLink,
    html[data-sa-theme="dark"] #loginView .tamiyouzRecoveryLink{
      color:#d7b46c!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzLoginMsg:not(:empty),
    html[data-sa-theme="dark"] #loginView .tamiyouzLoginMsg:not(:empty){
      background:#17263a!important;
      border-color:#33475f!important;
    }
    /* END SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1_1 */
'''


def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        print('Premium login corrective V1.1 already applied; no changes made.')
        return

    if ANCHOR not in text:
        raise SystemExit('Premium login V1 anchor not found; apply V1 first.')
    if text.count(ANCHOR) != 1:
        raise SystemExit('Unexpected premium login V1 anchor count; refusing ambiguous patch application.')

    required = [
        'id="loginView"',
        'id="appShell"',
        'id="loginFormPanel"',
        'id="loginBtn"',
        'tamiyouzLoginMain',
        'tamiyouzLoginCard',
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise SystemExit('Login baseline mismatch; missing: ' + ', '.join(missing))

    text = text.replace(ANCHOR, ANCHOR + '\n\n' + CSS, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Login Premium Control Gate V1.1 corrective patch.')


if __name__ == '__main__':
    main()
