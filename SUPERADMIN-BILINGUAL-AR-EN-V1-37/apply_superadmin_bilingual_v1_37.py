#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_37_GITHUB_SYNC_EN_AUDIT_ACTION_PLACEHOLDER_CLOSURE'
V136_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_36_USERS_EN_DYNAMIC_ACCOUNT_COUNT_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V136";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_37_GITHUB_SYNC_EN_AUDIT_ACTION_PLACEHOLDER_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V137";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V136';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V137';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v136.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v137.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V136';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V137';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v136', '?v=superadmin-bilingual-v137', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v136"', 'data-sa-bilingual-runtime="v137"', 'runtime asset marker', 1),
]

ATTR_ANCHOR = """    setV14Attr('#subNotes','aria-label','Update reason','سبب التحديث');setV14Attr('#subNotes','placeholder','Update reason','سبب التحديث');setV14Attr('#platformAdminName','aria-label','Admin name','اسم المسؤول');setV14Attr('#platformAdminName','placeholder','Admin name','اسم المسؤول');"""
ATTR_REPLACEMENT = ATTR_ANCHOR + """
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_37_GITHUB_SYNC_EN_AUDIT_ACTION_PLACEHOLDER_CLOSURE
    // V1.36 browser evidence: this static placeholder is an attribute and must be forced after render.
    setV14Attr('#auditAction','placeholder','e.g. subscription or github.sync','مثل subscription أو github.sync');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.37 GitHub Sync EN audit action placeholder closure already applied; no changes made.')
        return
    if V136_MARKER not in text:
        raise SystemExit('Bilingual V1.36 Users EN dynamic account count closure marker not found; apply V1.36 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    attr_count = text.count(ATTR_ANCHOR)
    if attr_count != 1:
        raise SystemExit(f'V1.37 attribute override anchor count is {attr_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ATTR_ANCHOR, ATTR_REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.37 GitHub Sync EN audit action placeholder closure runtime.')

if __name__ == '__main__':
    main()
