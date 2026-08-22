#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_PHASE5_1_TENANT_DRAWER_OVERFLOW_FIX_V1'
PHASE5_ANCHOR = '/* END SUPER_ADMIN_PHASE5_OPERATIONS_INTEGRATIONS_V1 */'

CSS = r'''
    /* SUPER_ADMIN_PHASE5_1_TENANT_DRAWER_OVERFLOW_FIX_V1 */
    /* A closed/inert tenant drawer must not contribute transformed off-screen
       geometry to the document scrollable overflow area. openDrawer()/closeDrawer()
       already keep .open and aria-hidden in sync, so remove only the dormant drawer
       from layout/paint while it is closed. */
    #tenantDrawer.drawerShell[aria-hidden="true"]:not(.open){
      display:none!important;
    }
    /* END SUPER_ADMIN_PHASE5_1_TENANT_DRAWER_OVERFLOW_FIX_V1 */
'''


def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        print('Phase 5.1 already applied; no changes made.')
        return

    if PHASE5_ANCHOR not in text:
        raise SystemExit(
            'Phase 5 marker not found. Apply/retain Phase 5 first; refusing to modify an unknown baseline.'
        )

    if text.count(PHASE5_ANCHOR) != 1:
        raise SystemExit('Unexpected Phase 5 anchor count; refusing ambiguous patch application.')

    text = text.replace(PHASE5_ANCHOR, PHASE5_ANCHOR + '\n' + CSS, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Phase 5.1 tenant drawer overflow fix.')


if __name__ == '__main__':
    main()
