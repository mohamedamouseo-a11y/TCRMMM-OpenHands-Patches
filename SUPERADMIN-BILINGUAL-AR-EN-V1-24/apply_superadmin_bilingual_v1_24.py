#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_24_ACTIVITY_EN_HEADER_LAST_ACTIVITY_CLOSURE'
V123_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_23_PLATFORM_ADMINS_EN_FULL_PAGE_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V123";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_24_ACTIVITY_EN_HEADER_LAST_ACTIVITY_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V124";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V123';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V124';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v123.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v124.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V123';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V124';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v123', '?v=superadmin-bilingual-v124', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v123"', 'data-sa-bilingual-runtime="v124"', 'runtime asset marker', 1),
]

EN_ANCHOR = """  const v122EnglishPatterns=(value)=>{
    let out=String(value);"""

EN_INSERT = r"""  const v122EnglishPatterns=(value)=>{
    let out=String(value);
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_24_ACTIVITY_EN_HEADER_LAST_ACTIVITY_CLOSURE
    // V1.23 evidence: Activity EN leaked the static heading and the static label
    // that prefixes a runtime timestamp. Preserve the timestamp bytes exactly.
    if(out==='آخر الأنشطة')out='Latest Activity';
    let v124Activity=out.match(/^آخر نشاط:\s*(.+)$/);
    if(v124Activity)out='Last activity: '+v124Activity[1];"""

AR_ANCHOR = """  const v122ArabicPatterns=(value)=>{
    let out=String(value);"""

AR_INSERT = r"""  const v122ArabicPatterns=(value)=>{
    let out=String(value);
    // V1.24 reverse canonicalization for Activity AR regressions.
    if(out==='Latest Activity')out='آخر الأنشطة';
    let v124Activity=out.match(/^Last activity:\s*(.+)$/i);
    if(v124Activity)out='آخر نشاط: '+v124Activity[1];"""

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.24 Activity EN header/last-activity closure already applied; no changes made.')
        return
    if V123_MARKER not in text:
        raise SystemExit('Bilingual V1.23 Platform Admins EN full-page closure marker not found; apply V1.23 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_ANCHOR) != 1:
        raise SystemExit(f'V1.24 English pattern anchor count is {text.count(EN_ANCHOR)}; refusing unknown baseline.')
    if text.count(AR_ANCHOR) != 1:
        raise SystemExit(f'V1.24 Arabic pattern anchor count is {text.count(AR_ANCHOR)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, EN_ANCHOR, EN_INSERT, 'V1.24 Activity English patterns')
    text = replace_once(text, AR_ANCHOR, AR_INSERT, 'V1.24 Activity Arabic patterns')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.24 Activity EN header/last-activity closure runtime.')

if __name__ == '__main__':
    main()
