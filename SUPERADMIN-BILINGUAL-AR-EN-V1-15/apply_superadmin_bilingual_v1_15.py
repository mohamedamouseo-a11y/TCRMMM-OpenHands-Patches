#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_15_COMPANIES_AR_COUNTER_PAGER_CLOSURE'
V114_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_14_COMPANIES_ACTION_COUNTER_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V114";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_15_COMPANIES_AR_COUNTER_PAGER_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V115";',
     'UI version'),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V114';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V115';",
     'legacy UI runtime version'),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v114.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v115.js";',
     'runtime path'),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V114';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V115';",
     'standalone runtime version'),
    ('?v=superadmin-bilingual-v114', '?v=superadmin-bilingual-v115', 'asset cache key'),
    ('data-sa-bilingual-runtime="v114"', 'data-sa-bilingual-runtime="v115"', 'runtime asset marker'),
]

OLD_PATTERNS = r'''
  const v114ArabicPatterns=(value)=>{
    let out=String(value);
    if(out==='Copy Path')out='نسخ المسار';
    if(out==='Details')out='تفاصيل';
    if(out==='Renew')out='تجديد';
    if(out==='Login')out='دخول';
    if(out==='Risk')out='خطر';

    let m=out.match(/^(\d+)\s+shown of\s+(\d+)\s*·\s*page\s+(\d+)\/(\d+)$/i);
    if(m)out=m[1]+' معروض من '+m[2]+' · صفحة '+m[3]+'/'+m[4];
    return out;
  };
'''

NEW_PATTERNS = r'''
  const v114ArabicPatterns=(value)=>{
    let out=String(value);
    if(out==='Copy Path')out='نسخ المسار';
    if(out==='Details')out='تفاصيل';
    if(out==='Renew')out='تجديد';
    if(out==='Login')out='دخول';
    if(out==='Risk')out='خطر';

    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_15_COMPANIES_AR_COUNTER_PAGER_CLOSURE
    // Close mixed intermediate forms produced by earlier phrase passes.
    let m=out.match(/^(\d+)\s+(?:معروضة|معروض)\s+من\s+أصل\s+(\d+)\s*·\s*page\s+(\d+)\/(\d+)$/i);
    if(m)out=m[1]+' معروضة من أصل '+m[2]+' · صفحة '+m[3]+'/'+m[4];

    m=out.match(/^ترقيم صفحات من الخادم\s*·\s*(\d+)\s+records$/i);
    if(m)out='ترقيم صفحات من الخادم · '+m[1]+' سجل';

    m=out.match(/^(\d+)\s+shown of\s+(\d+)\s*·\s*page\s+(\d+)\/(\d+)$/i);
    if(m)out=m[1]+' معروضة من أصل '+m[2]+' · صفحة '+m[3]+'/'+m[4];
    return out;
  };
'''

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.15 Companies AR counter/pager closure already applied; no changes made.')
        return
    if V114_MARKER not in text:
        raise SystemExit('Bilingual V1.14 Companies action/counter marker not found; apply V1.14 first.')

    for old, _new, label in REPLACES:
        count = text.count(old)
        expected = 3 if label == 'asset cache key' else 1
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(OLD_PATTERNS) != 1:
        raise SystemExit(f'V1.15 Arabic-pattern anchor count is {text.count(OLD_PATTERNS)}; refusing unknown baseline.')

    for old, new, _label in REPLACES:
        text = text.replace(old, new)
    text = text.replace(OLD_PATTERNS, NEW_PATTERNS, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.15 Companies AR counter/pager closure runtime.')

if __name__ == '__main__':
    main()
