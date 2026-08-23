#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_19_COMPANIES_AR_PLAN_CLOSURE'
V118_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_18_USERS_MIXED_HEADER_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V118";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_19_COMPANIES_AR_PLAN_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V119";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V118';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V119';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v118.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v119.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V118';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V119';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v118', '?v=superadmin-bilingual-v119', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v118"', 'data-sa-bilingual-runtime="v119"', 'runtime asset marker', 1),
]

ANCHOR = "  v118Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_19_COMPANIES_AR_PLAN_CLOSURE
  const v119Pairs=[
    ['Plan','الخطة']
  ];
  v119Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  const v119PhraseArToEn=v119Pairs.map((p)=>[p[1],p[0]]).sort((a,b)=>b[0].length-a[0].length);
  const v119PhraseEnToAr=v119Pairs.slice().sort((a,b)=>b[0].length-a[0].length);

  const v119EnglishPatterns=(value)=>String(value);
  const v119ArabicPatterns=(value)=>String(value);
'''

TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact)))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);return v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out)))));}const exact=arToEn.get(raw);if(exact)return v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);return v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out))))));};"

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact))))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);out=v19Replace(out,v119PhraseEnToAr);return v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out))))));}const exact=arToEn.get(raw);if(exact)return v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact)))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);out=v19Replace(out,v119PhraseArToEn);return v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out)))))));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.19 Companies AR Plan closure already applied; no changes made.')
        return
    if V118_MARKER not in text:
        raise SystemExit('Bilingual V1.18 Users mixed header closure marker not found; apply V1.18 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.19 dictionary anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.19 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.19 Companies AR Plan mapping')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.19 translator')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.19 Companies AR Plan closure runtime.')

if __name__ == '__main__':
    main()
