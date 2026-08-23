#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_16_USERS_AR_HEADER_CLOSURE'
V115_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_15_COMPANIES_AR_COUNTER_PAGER_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V115";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_16_USERS_AR_HEADER_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V116";',
     'UI version'),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V115';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V116';",
     'legacy UI runtime version'),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v115.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v116.js";',
     'runtime path'),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V115';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V116';",
     'standalone runtime version'),
    ('?v=superadmin-bilingual-v115', '?v=superadmin-bilingual-v116', 'asset cache key'),
    ('data-sa-bilingual-runtime="v115"', 'data-sa-bilingual-runtime="v116"', 'runtime asset marker'),
]

ANCHOR = "  const v114PhraseEnToAr=v114Pairs.slice().sort((a,b)=>b[0].length-a[0].length);"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_16_USERS_AR_HEADER_CLOSURE
  // Audited Users AR header/badge closure from V1.15 evidence.
  const v116Pairs=[
    ['USERS & ACCESS','المستخدمون والصلاحيات'],
    ['Central Users','المستخدمون المركزيون']
  ];
  v116Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
'''

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.16 Users AR header closure already applied; no changes made.')
        return
    if V115_MARKER not in text:
        raise SystemExit('Bilingual V1.15 Companies AR counter/pager marker not found; apply V1.15 first.')

    for old, _new, label in REPLACES:
        count = text.count(old)
        expected = 3 if label == 'asset cache key' else 1
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.16 dictionary anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')

    for old, new, _label in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, ANCHOR + '\n' + EXTRA_JS, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.16 Users AR header closure runtime.')

if __name__ == '__main__':
    main()
