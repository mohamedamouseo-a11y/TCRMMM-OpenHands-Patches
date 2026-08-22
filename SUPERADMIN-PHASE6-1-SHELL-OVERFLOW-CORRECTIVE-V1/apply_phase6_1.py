#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_PHASE6_1_SHELL_OVERFLOW_CORRECTIVE_V1'
ANCHOR = '/* END SUPER_ADMIN_PHASE6_SETTINGS_FINAL_QA_V1 */'

CSS = r'''
    /* SUPER_ADMIN_PHASE6_1_SHELL_OVERFLOW_CORRECTIVE_V1 */
    /* Preserve the intended 10px desktop inset without making the stretched
       flex/grid topbar 20px wider than its mainArea. The previous desktop rule
       used margin-inline:10px while the stretched item still occupied 100%,
       producing a measured +10px document overflow at 1440px and 1024px. */
    @media(min-width:981px){
      #appShell.platformPageMode .topbar{
        box-sizing:border-box!important;
        width:calc(100% - 20px)!important;
        max-width:calc(100% - 20px)!important;
        margin-inline:10px!important;
      }
    }
    @media(max-width:980px){
      #appShell.platformPageMode .topbar{
        box-sizing:border-box!important;
        width:100%!important;
        max-width:100%!important;
      }
    }
    /* END SUPER_ADMIN_PHASE6_1_SHELL_OVERFLOW_CORRECTIVE_V1 */
'''


def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        print('Phase 6.1 already applied; no changes made.')
        return

    if ANCHOR not in text:
        raise SystemExit('Phase 6 marker not found; apply/retain Phase 6 first. Refusing unknown baseline.')

    if text.count(ANCHOR) != 1:
        raise SystemExit('Unexpected Phase 6 anchor count; refusing ambiguous patch application.')

    required = [
        '#appShell.platformPageMode .topbar',
        'margin:8px 10px 0!important',
        '@media(max-width:980px)',
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise SystemExit('Shell baseline mismatch; missing: ' + ', '.join(missing))

    text = text.replace(ANCHOR, ANCHOR + '\n\n' + CSS, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Phase 6.1 shell overflow corrective patch.')


if __name__ == '__main__':
    main()
