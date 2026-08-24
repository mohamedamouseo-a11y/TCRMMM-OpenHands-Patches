#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_27_AUDIT_LOG_AR_MIXED_H2_CLOSURE'
V126_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_26_AUDIT_LOG_EN_MIXED_H2_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V126";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_27_AUDIT_LOG_AR_MIXED_H2_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V127";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V126';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V127';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v126.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v127.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V126';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V127';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v126', '?v=superadmin-bilingual-v127', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v126"', 'data-sa-bilingual-runtime="v127"', 'runtime asset marker', 1),
]

AR_ANCHOR = """  const v122ArabicPatterns=(value)=>{
    let out=String(value);"""

AR_INSERT = """  const v122ArabicPatterns=(value)=>{
    let out=String(value);
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_27_AUDIT_LOG_AR_MIXED_H2_CLOSURE
    // V1.26 browser evidence proved Audit Log AR can end as a mixed post-translation H2.
    // Canonicalize only this ordinary static heading; runtime/domain data is untouched.
    if(out==='أمان & Audit Log' || out==='Security & Audit Log')out='الأمان وسجل التدقيق';"""

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.27 Audit Log AR mixed H2 closure already applied; no changes made.')
        return
    if V126_MARKER not in text:
        raise SystemExit('Bilingual V1.26 Audit Log EN mixed H2 closure marker not found; apply V1.26 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(AR_ANCHOR) != 1:
        raise SystemExit(f'V1.27 Audit Log AR H2 anchor count is {text.count(AR_ANCHOR)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, AR_ANCHOR, AR_INSERT, 'V1.27 Audit Log AR mixed H2 pattern')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.27 Audit Log AR mixed H2 closure runtime.')

if __name__ == '__main__':
    main()
