#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_26_AUDIT_LOG_EN_MIXED_H2_CLOSURE'
V125_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_25_AUDIT_LOG_EN_FULL_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V125";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_26_AUDIT_LOG_EN_MIXED_H2_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V126";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V125';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V126';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v125.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v126.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V125';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V126';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v125', '?v=superadmin-bilingual-v126', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v125"', 'data-sa-bilingual-runtime="v126"', 'runtime asset marker', 1),
]

EN_ANCHOR = """    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_25_AUDIT_LOG_EN_FULL_CLOSURE
    // V1.24 evidence proved six genuine ordinary Audit Log EN static leaks."""

EN_INSERT = """    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_25_AUDIT_LOG_EN_FULL_CLOSURE
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_26_AUDIT_LOG_EN_MIXED_H2_CLOSURE
    // V1.25 browser evidence proved one post-translation mixed H2 in Audit Log EN.
    // Close only that ordinary static UI result; runtime/domain data remains untouched.
    if(out==='أمان & Audit Log')out='Security & Audit Log';
    // V1.24 evidence proved six genuine ordinary Audit Log EN static leaks."""

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.26 Audit Log EN mixed H2 closure already applied; no changes made.')
        return
    if V125_MARKER not in text:
        raise SystemExit('Bilingual V1.25 Audit Log EN full closure marker not found; apply V1.25 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_ANCHOR) != 1:
        raise SystemExit(f'V1.26 Audit Log EN H2 anchor count is {text.count(EN_ANCHOR)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, EN_ANCHOR, EN_INSERT, 'V1.26 Audit Log EN mixed H2 pattern')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.26 Audit Log EN mixed H2 closure runtime.')

if __name__ == '__main__':
    main()
