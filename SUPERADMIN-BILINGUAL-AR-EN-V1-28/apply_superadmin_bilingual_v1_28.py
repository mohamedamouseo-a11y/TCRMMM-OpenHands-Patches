#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_28_ACTIVITY_EN_VIEW_ALL_CLOSURE'
V127_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_27_AUDIT_LOG_AR_MIXED_H2_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V127";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_28_ACTIVITY_EN_VIEW_ALL_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V128";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V127';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V128';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v127.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v128.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V127';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V128';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v127', '?v=superadmin-bilingual-v128', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v127"', 'data-sa-bilingual-runtime="v128"', 'runtime asset marker', 1),
]

EN_ANCHOR = """  const v122EnglishPatterns=(value)=>{
    let out=String(value);"""
EN_INSERT = """  const v122EnglishPatterns=(value)=>{
    let out=String(value);
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_28_ACTIVITY_EN_VIEW_ALL_CLOSURE
    // V1.27 regression evidence: Activity EN refresh/view-all action remained Arabic.
    if(out==='عرض الكل')out='View all';"""

AR_ANCHOR = """  const v122ArabicPatterns=(value)=>{
    let out=String(value);"""
AR_INSERT = """  const v122ArabicPatterns=(value)=>{
    let out=String(value);
    // V1.28 reverse canonicalization for Activity AR.
    if(out==='View all')out='عرض الكل';"""

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.28 Activity EN View all closure already applied; no changes made.')
        return
    if V127_MARKER not in text:
        raise SystemExit('Bilingual V1.27 Audit Log AR mixed H2 closure marker not found; apply V1.27 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_ANCHOR) != 1:
        raise SystemExit(f'V1.28 English pattern anchor count is {text.count(EN_ANCHOR)}; refusing unknown baseline.')
    if text.count(AR_ANCHOR) != 1:
        raise SystemExit(f'V1.28 Arabic pattern anchor count is {text.count(AR_ANCHOR)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, EN_ANCHOR, EN_INSERT, 'V1.28 Activity EN View all pattern')
    text = replace_once(text, AR_ANCHOR, AR_INSERT, 'V1.28 Activity AR View all reverse pattern')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.28 Activity EN View all closure runtime.')

if __name__ == '__main__':
    main()
