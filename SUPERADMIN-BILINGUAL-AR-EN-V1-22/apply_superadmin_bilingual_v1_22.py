#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_22_PLATFORM_ADMINS_EN_COUNT_CLOSURE'
V121_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_21_PLATFORM_ADMINS_AR_FULL_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V121";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_22_PLATFORM_ADMINS_EN_COUNT_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V122";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V121';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V122';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v121.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v122.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V121';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V122';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v121', '?v=superadmin-bilingual-v122', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v121"', 'data-sa-bilingual-runtime="v122"', 'runtime asset marker', 1),
]

ANCHOR = "  v121Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_22_PLATFORM_ADMINS_EN_COUNT_CLOSURE
  // V1.21 evidence proved a dynamic count + static Arabic summary remained in English mode.
  // Preserve the numeric count as runtime data and translate only the sentence around it.
  const v122EnglishPatterns=(value)=>{
    let out=String(value);
    let m=out.match(/^(\d+)\s+مسؤول منصة\s*·\s*كل مسؤول يرى الشركات المسندة له فقط\.$/);
    if(m)out=m[1]+' platform admins · each admin sees only their assigned companies.';
    return out;
  };

  const v122ArabicPatterns=(value)=>{
    let out=String(value);
    let m=out.match(/^(\d+)\s+platform admins?\s*·\s*each admin sees only their assigned companies\.$/i);
    if(m)out=m[1]+' مسؤول منصة · كل مسؤول يرى الشركات المسندة له فقط.';
    return out;
  };
'''

TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v121ArabicPatterns(v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact))))))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);out=v19Replace(out,v119PhraseEnToAr);out=v19Replace(out,v120PhraseEnToAr);out=v19Replace(out,v121PhraseEnToAr);return v121ArabicPatterns(v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out))))))));}const exact=arToEn.get(raw);if(exact)return v121EnglishPatterns(v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact)))))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);out=v19Replace(out,v119PhraseArToEn);out=v19Replace(out,v120PhraseArToEn);out=v19Replace(out,v121PhraseArToEn);return v121EnglishPatterns(v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out)))))))));};"

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v122ArabicPatterns(v121ArabicPatterns(v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact)))))))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);out=v19Replace(out,v119PhraseEnToAr);out=v19Replace(out,v120PhraseEnToAr);out=v19Replace(out,v121PhraseEnToAr);return v122ArabicPatterns(v121ArabicPatterns(v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out)))))))));}const exact=arToEn.get(raw);if(exact)return v122EnglishPatterns(v121EnglishPatterns(v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact))))))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);out=v19Replace(out,v119PhraseArToEn);out=v19Replace(out,v120PhraseArToEn);out=v19Replace(out,v121PhraseArToEn);return v122EnglishPatterns(v121EnglishPatterns(v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out))))))))));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.22 Platform Admins EN count closure already applied; no changes made.')
        return
    if V121_MARKER not in text:
        raise SystemExit('Bilingual V1.21 Platform Admins AR full closure marker not found; apply V1.21 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.22 pattern anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.22 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.22 Platform Admins dynamic count patterns')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.22 translator')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.22 Platform Admins EN count closure runtime.')

if __name__ == '__main__':
    main()
