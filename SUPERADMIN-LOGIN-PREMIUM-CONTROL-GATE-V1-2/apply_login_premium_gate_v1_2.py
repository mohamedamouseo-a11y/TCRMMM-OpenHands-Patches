#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1_2'
ANCHOR = '/* END SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1_1 */'

CSS = r'''
    /* SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1_2 */
    /* Final presentation-only micro-corrective pass after screenshot review:
       1) remove clipped brand copy in the <=1100px compact header,
       2) keep Forgot password visually integrated in dark mode. */

    @media(max-width:1100px){
      #loginView .tamiyouzBrandContent h1,
      #loginView .tamiyouzBrandContent p,
      #loginView .tamiyouzSecurityBadge{
        display:none!important;
      }
      #loginView .tamiyouzLoginBrandPanel{
        display:flex!important;
        justify-content:flex-start!important;
      }
      #loginView .tamiyouzBrandContent{
        margin:7px 0 0!important;
      }
      #loginView .tamiyouzBrandTitle{
        margin:0!important;
        line-height:1!important;
      }
      #loginView .tamiyouzBrandRule{
        margin:7px 0 0!important;
      }
    }

    #loginView .tamiyouzRecoveryLink{
      border:0!important;
      background:transparent!important;
      box-shadow:none!important;
      border-radius:6px!important;
      min-height:auto!important;
    }
    #loginView .tamiyouzRecoveryLink:hover{
      background:rgba(184,139,62,.08)!important;
      box-shadow:none!important;
      transform:none!important;
    }

    html[data-theme="dark"] #loginView .tamiyouzRecoveryLink,
    html[data-sa-theme="dark"] #loginView .tamiyouzRecoveryLink{
      border:0!important;
      background:transparent!important;
      color:#d7b46c!important;
      box-shadow:none!important;
    }
    html[data-theme="dark"] #loginView .tamiyouzRecoveryLink:hover,
    html[data-sa-theme="dark"] #loginView .tamiyouzRecoveryLink:hover{
      background:rgba(215,180,108,.10)!important;
      color:#f0cc83!important;
    }
    /* END SUPER_ADMIN_LOGIN_PREMIUM_CONTROL_GATE_V1_2 */
'''


def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        print('Premium login corrective V1.2 already applied; no changes made.')
        return

    if ANCHOR not in text:
        raise SystemExit('Premium login V1.1 anchor not found; apply V1.1 first.')
    if text.count(ANCHOR) != 1:
        raise SystemExit('Unexpected premium login V1.1 anchor count; refusing ambiguous patch application.')

    required = [
        'id="loginView"',
        'tamiyouzBrandContent',
        'tamiyouzBrandTitle',
        'tamiyouzRecoveryLink',
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise SystemExit('Login baseline mismatch; missing: ' + ', '.join(missing))

    text = text.replace(ANCHOR, ANCHOR + '\n\n' + CSS, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Login Premium Control Gate V1.2 corrective patch.')


if __name__ == '__main__':
    main()
