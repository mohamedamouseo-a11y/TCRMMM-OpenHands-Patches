#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_21_PLATFORM_ADMINS_AR_FULL_CLOSURE'
V120_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_20_PLATFORM_ADMINS_AR_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V120";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_21_PLATFORM_ADMINS_AR_FULL_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V121";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V120';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V121';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v120.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v121.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V120';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V121';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v120', '?v=superadmin-bilingual-v121', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v120"', 'data-sa-bilingual-runtime="v121"', 'runtime asset marker', 1),
]

ANCHOR = "  v120Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_21_PLATFORM_ADMINS_AR_FULL_CLOSURE
  // Close the complete genuine Platform Admins AR static blockers evidenced by V1.20.
  const v121Pairs=[
    ['PLATFORM ADMINISTRATION','إدارة المنصة'],
    ['Add Admin','إضافة مسؤول']
  ];
  v121Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  const v121PhraseArToEn=v121Pairs.map((p)=>[p[1],p[0]]).sort((a,b)=>b[0].length-a[0].length);
  const v121PhraseEnToAr=v121Pairs.slice().sort((a,b)=>b[0].length-a[0].length);

  // V1.20 raw scan proved a mixed button label after prior translations.
  arToEn.set('+ إضافة Admin','+ Add Admin');
  arToEn.set('+ إضافة مسؤول','+ Add Admin');

  const v121EnglishPatterns=(value)=>{
    let out=String(value);
    if(out==='إدارة المنصة')out='PLATFORM ADMINISTRATION';
    if(out==='+ إضافة Admin' || out==='+ إضافة مسؤول' || out==='+ Add مسؤول')out='+ Add Admin';
    return out;
  };

  const v121ArabicPatterns=(value)=>{
    let out=String(value);
    if(out==='PLATFORM ADMINISTRATION')out='إدارة المنصة';
    if(out==='+ Add Admin' || out==='+ إضافة Admin' || out==='+ Add مسؤول')out='+ إضافة مسؤول';
    return out;
  };
'''

TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact)))))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);out=v19Replace(out,v119PhraseEnToAr);out=v19Replace(out,v120PhraseEnToAr);return v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out)))))));}const exact=arToEn.get(raw);if(exact)return v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact))))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);out=v19Replace(out,v119PhraseArToEn);out=v19Replace(out,v120PhraseArToEn);return v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out))))))));};"

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v121ArabicPatterns(v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact))))))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);out=v19Replace(out,v119PhraseEnToAr);out=v19Replace(out,v120PhraseEnToAr);out=v19Replace(out,v121PhraseEnToAr);return v121ArabicPatterns(v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out))))))));}const exact=arToEn.get(raw);if(exact)return v121EnglishPatterns(v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact)))))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);out=v19Replace(out,v119PhraseArToEn);out=v19Replace(out,v120PhraseArToEn);out=v19Replace(out,v121PhraseArToEn);return v121EnglishPatterns(v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out)))))))));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.21 Platform Admins AR full closure already applied; no changes made.')
        return
    if V120_MARKER not in text:
        raise SystemExit('Bilingual V1.20 Platform Admins AR closure marker not found; apply V1.20 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.21 dictionary anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.21 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.21 Platform Admins full mappings')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.21 translator')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.21 Platform Admins AR full closure runtime.')

if __name__ == '__main__':
    main()
