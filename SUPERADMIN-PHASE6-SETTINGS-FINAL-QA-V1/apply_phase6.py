#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_PHASE6_SETTINGS_FINAL_QA_V1'
ANCHOR = '/* END SUPER_ADMIN_PHASE5_1_TENANT_DRAWER_OVERFLOW_FIX_V1 */'

CSS = r'''
    /* SUPER_ADMIN_PHASE6_SETTINGS_FINAL_QA_V1 */
    /* Final presentation-only pass for the System Settings drawer.
       Keep all existing IDs, handlers, owner-only gates and source-code actions intact. */
    #settingsDrawer.drawerShell{
      width:min(620px,calc(100vw - 32px));
    }
    #settingsDrawer .drawerInner{
      padding:18px;
    }
    #settingsDrawer .drawerHead{
      margin-bottom:12px;
      padding:15px 16px;
      border-radius:18px;
    }
    #settingsDrawer .drawerHead h2{
      font-size:19px;
      line-height:1.25;
    }
    #settingsDrawer .drawerHead p{
      max-width:46ch;
      line-height:1.55;
    }
    #settingsDrawer .stack{
      gap:12px;
    }
    #settingsDrawer .panel{
      padding:14px!important;
      border-radius:16px!important;
      box-shadow:none!important;
      min-width:0;
    }
    #settingsDrawer .panelHead{
      margin-bottom:10px;
      gap:10px;
      align-items:flex-start;
    }
    #settingsDrawer .panelHead h3{
      font-size:14px;
      line-height:1.35;
    }
    #settingsDrawer .panelHead p{
      margin-top:3px;
      line-height:1.5;
    }
    #settingsDrawer .row{
      gap:8px;
      flex-wrap:wrap;
    }
    #settingsDrawer #setDarkBtn,
    #settingsDrawer #setLightBtn{
      flex:1 1 150px;
      justify-content:center;
      min-height:40px;
    }
    #settingsDrawer #accountBox,
    #settingsDrawer #sourceCodeBox{
      gap:8px;
      min-width:0;
    }
    #settingsDrawer #accountBox .quickItem,
    #settingsDrawer #sourceCodeBox .quickItem,
    #settingsDrawer #accountBox .infoBox,
    #settingsDrawer #sourceCodeBox .infoBox{
      padding:10px 12px;
      border-radius:12px;
      min-width:0;
      overflow-wrap:anywhere;
    }
    #settingsDrawer #developerHubPanel .badge{
      white-space:nowrap;
    }
    #settingsDrawer #downloadSourceCodeBtn,
    #settingsDrawer #refreshSourceCodeBtn{
      min-height:38px;
    }
    #settingsDrawer #settingsLogoutBtn{
      margin-top:2px;
      min-height:42px;
    }
    #settingsDrawer button:focus-visible{
      outline:3px solid color-mix(in srgb,var(--accent) 36%,transparent);
      outline-offset:2px;
    }
    @media(max-width:680px){
      #settingsDrawer.drawerShell{
        left:10px!important;
        right:10px!important;
        width:auto!important;
        top:10px!important;
        bottom:10px!important;
      }
      #settingsDrawer .drawerInner{padding:12px;}
      #settingsDrawer .drawerHead{padding:13px 14px;}
      #settingsDrawer .panel{padding:12px!important;}
      #settingsDrawer #setDarkBtn,
      #settingsDrawer #setLightBtn{flex-basis:100%;}
    }
    /* END SUPER_ADMIN_PHASE6_SETTINGS_FINAL_QA_V1 */
'''


def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        print('Phase 6 already applied; no changes made.')
        return

    if ANCHOR not in text:
        raise SystemExit('Phase 5.1 anchor not found; refusing to patch an unknown baseline.')

    if text.count(ANCHOR) != 1:
        raise SystemExit('Unexpected Phase 5.1 anchor count; refusing ambiguous patch application.')

    required_ids = [
        'id="settingsDrawer"',
        'id="setDarkBtn"',
        'id="setLightBtn"',
        'id="accountBox"',
        'id="developerHubPanel"',
        'id="sourceCodeBox"',
        'id="downloadSourceCodeBtn"',
        'id="refreshSourceCodeBtn"',
        'id="settingsLogoutBtn"',
    ]
    missing = [item for item in required_ids if item not in text]
    if missing:
        raise SystemExit('Settings baseline mismatch; missing: ' + ', '.join(missing))

    text = text.replace(ANCHOR, ANCHOR + '\n\n' + CSS, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Phase 6 Settings + Final QA presentation patch.')


if __name__ == '__main__':
    main()
