#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_23_PLATFORM_ADMINS_EN_FULL_PAGE_CLOSURE'
V122_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_22_PLATFORM_ADMINS_EN_COUNT_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V122";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_23_PLATFORM_ADMINS_EN_FULL_PAGE_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V123";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V122';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V123';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v122.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v123.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V122';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V123';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v122', '?v=superadmin-bilingual-v123', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v122"', 'data-sa-bilingual-runtime="v123"', 'runtime asset marker', 1),
]

ANCHOR = "  const v122EnglishPatterns=(value)=>{"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_23_PLATFORM_ADMINS_EN_FULL_PAGE_CLOSURE
  // V1.22 raw scan proved the remaining Platform Admins EN leaks are ordinary static UI.
  // Keep person/company names, dates, emails, role values and other runtime data untouched.
  const v123Pairs=[
    ['Total admins','إجمالي المسؤولين'],
    ['All Platform Admin accounts','كل حسابات مسؤولي المنصة'],
    ['Active admins','المسؤولون النشطون'],
    ['Accounts available for login','حسابات متاحة لتسجيل الدخول'],
    ['Unassigned companies','شركات غير مسندة'],
    ['Need assignment to a platform admin','تحتاج ربطها بمسؤول منصة'],
    ['Platform Admin Directory','دليل مسؤولي المنصة'],
    ['Accounts, assigned companies, last login, and status.','الحسابات، الشركات المسندة، آخر تسجيل دخول والحالة.'],
    ['Central permissions','صلاحيات مركزية'],
    ['Admin','المسؤول'],
    ['Created by','أنشأه'],
    ['Not assigned to any company','غير مسند لأي شركة'],
    ['Edit & assign companies','تعديل وربط الشركات']
  ];
  v123Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});

  // Normalize mixed intermediate forms evidenced by the V1.22 full-page raw scan.
  arToEn.set('كل حسابات Platform Administration','All Platform Admin accounts');
  arToEn.set('كل حسابات Platform Admin','All Platform Admin accounts');
  arToEn.set('حسابات متاحة لتسجيل الLogin','Accounts available for login');
  arToEn.set('حسابات متاحة لتسجيل الLOGIN','Accounts available for login');
  arToEn.set('الحسابات، الشركات المسندة، آخر Login والحالة.','Accounts, assigned companies, last login, and status.');
  arToEn.set('الحسابات، الشركات المسندة، آخر LOGIN والحالة.','Accounts, assigned companies, last login, and status.');
'''

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.23 Platform Admins EN full-page closure already applied; no changes made.')
        return
    if V122_MARKER not in text:
        raise SystemExit('Bilingual V1.22 Platform Admins EN count closure marker not found; apply V1.22 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.23 mapping anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, EXTRA_JS + '\n' + ANCHOR, 'V1.23 Platform Admins EN full-page mappings')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.23 Platform Admins EN full-page closure runtime.')

if __name__ == '__main__':
    main()
