#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_25_AUDIT_LOG_EN_FULL_CLOSURE'
V124_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_24_ACTIVITY_EN_HEADER_LAST_ACTIVITY_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V124";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_25_AUDIT_LOG_EN_FULL_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V125";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V124';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V125';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v124.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v125.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V124';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V125';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v124', '?v=superadmin-bilingual-v125', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v124"', 'data-sa-bilingual-runtime="v125"', 'runtime asset marker', 1),
]

EN_ANCHOR = """  const v122EnglishPatterns=(value)=>{
    let out=String(value);"""

EN_INSERT = r"""  const v122EnglishPatterns=(value)=>{
    let out=String(value);
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_25_AUDIT_LOG_EN_FULL_CLOSURE
    // V1.24 evidence proved six genuine ordinary Audit Log EN static leaks.
    // Translate only these UI labels; leave events, emails, IPs, dates and other runtime data untouched.
    if(out==='الأمان وسجل التدقيق')out='Security & Audit Log';
    if(out==='تصدير السجل')out='Export Log';
    if(out==='نوع الإجراء')out='Action Type';
    if(out==='الحدث')out='Event';
    if(out==='الأحداث المسجلة')out='Recorded Events';
    if(out==='آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم')out='Latest administrative operations ordered from newest to oldest';"""

AR_ANCHOR = """  const v122ArabicPatterns=(value)=>{
    let out=String(value);"""

AR_INSERT = r"""  const v122ArabicPatterns=(value)=>{
    let out=String(value);
    // V1.25 reverse canonicalization for Audit Log AR regression.
    if(out==='Security & Audit Log')out='الأمان وسجل التدقيق';
    if(out==='Export Log')out='تصدير السجل';
    if(out==='Action Type')out='نوع الإجراء';
    if(out==='Event')out='الحدث';
    if(out==='Recorded Events')out='الأحداث المسجلة';
    if(out==='Latest administrative operations ordered from newest to oldest')out='آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم';"""

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.25 Audit Log EN full closure already applied; no changes made.')
        return
    if V124_MARKER not in text:
        raise SystemExit('Bilingual V1.24 Activity EN closure marker not found; apply V1.24 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_ANCHOR) != 1:
        raise SystemExit(f'V1.25 English pattern anchor count is {text.count(EN_ANCHOR)}; refusing unknown baseline.')
    if text.count(AR_ANCHOR) != 1:
        raise SystemExit(f'V1.25 Arabic pattern anchor count is {text.count(AR_ANCHOR)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, EN_ANCHOR, EN_INSERT, 'V1.25 Audit Log English patterns')
    text = replace_once(text, AR_ANCHOR, AR_INSERT, 'V1.25 Audit Log Arabic patterns')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.25 Audit Log EN full closure runtime.')

if __name__ == '__main__':
    main()
