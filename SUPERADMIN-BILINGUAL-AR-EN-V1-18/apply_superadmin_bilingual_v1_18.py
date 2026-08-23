#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_18_USERS_MIXED_HEADER_CLOSURE'
V117_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE'
V117_HOTFIX_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_STARTUP_HOTFIX'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V117";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_18_USERS_MIXED_HEADER_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V118";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V117';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V118';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v117.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v118.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V117';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V118';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v117', '?v=superadmin-bilingual-v118', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v117"', 'data-sa-bilingual-runtime="v118"', 'runtime asset marker', 1),
]

ANCHOR = "  v117Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_18_USERS_MIXED_HEADER_CLOSURE
  const v118Pairs=[
    ['Unified management for all companies','إدارة موحدة لكل الشركات'],
    ['Last Login','آخر تسجيل دخول'],
    ['Login Details','بيانات تسجيل الدخول']
  ];
  v118Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});

  arToEn.set('إدارة موحدة لAll companies','Unified management for all companies');
  arToEn.set('آخر Login','Last Login');
  arToEn.set('آخر LOGIN','Last Login');
  arToEn.set('بيانات الLogin','Login Details');
  arToEn.set('بيانات الLOGIN','Login Details');

  const v118EnglishPatterns=(value)=>{
    let out=String(value);
    if(/^إدارة موحدة ل(?:All companies|كل الشركات)$/i.test(out))out='Unified management for all companies';
    if(/^آخر\s+Login$/i.test(out))out='Last Login';
    if(/^بيانات الLogin$/i.test(out))out='Login Details';
    return out;
  };

  const v118ArabicPatterns=(value)=>{
    let out=String(value);
    if(/^Unified management for all companies$/i.test(out))out='إدارة موحدة لكل الشركات';
    if(/^Last Login$/i.test(out))out='آخر تسجيل دخول';
    if(/^Login Details$/i.test(out))out='بيانات تسجيل الدخول';
    return out;
  };
'''

TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);return v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out))));}const exact=arToEn.get(raw);if(exact)return v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact)))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);return v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out)))));};"

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact)))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);return v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out)))));}const exact=arToEn.get(raw);if(exact)return v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);return v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out))))));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.18 Users mixed header closure already applied; no changes made.')
        return
    if V117_MARKER not in text:
        raise SystemExit('Bilingual V1.17 Users EN full closure marker not found; apply V1.17 first.')
    if V117_HOTFIX_MARKER not in text:
        raise SystemExit('Bilingual V1.17 startup hotfix marker not found; apply V1.17 startup hotfix first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.18 dictionary anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.18 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.18 Users mixed dictionary/patterns')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.18 translator')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.18 Users mixed header closure runtime.')

if __name__ == '__main__':
    main()
