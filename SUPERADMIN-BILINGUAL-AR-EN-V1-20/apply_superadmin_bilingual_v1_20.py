#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_20_PLATFORM_ADMINS_AR_CLOSURE'
V119_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_19_COMPANIES_AR_PLAN_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V119";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_20_PLATFORM_ADMINS_AR_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V120";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V119';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V120';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v119.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v120.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V119';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V120';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v119', '?v=superadmin-bilingual-v120', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v119"', 'data-sa-bilingual-runtime="v120"', 'runtime asset marker', 1),
]

ANCHOR = "  v119Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_20_PLATFORM_ADMINS_AR_CLOSURE
  const v120Pairs=[
    ['Platform Admin','مسؤول المنصة'],
    ['Manage Platform Admin accounts and company assignments','إدارة حسابات مسؤولي المنصة وتوزيع الشركات']
  ];
  v120Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  const v120PhraseArToEn=v120Pairs.map((p)=>[p[1],p[0]]).sort((a,b)=>b[0].length-a[0].length);
  const v120PhraseEnToAr=v120Pairs.slice().sort((a,b)=>b[0].length-a[0].length);

  // The audited V1.19 finding is an intermediate mixed phrase created after
  // earlier phrase translations. Canonicalize it in both language directions.
  arToEn.set('إدارة حسابات Platform Admin وتوزيع الشركات','Manage Platform Admin accounts and company assignments');
  arToEn.set('إدارة حسابات مسؤول المنصة وتوزيع الشركات','Manage Platform Admin accounts and company assignments');

  const v120EnglishPatterns=(value)=>{
    let out=String(value);
    if(out==='إدارة حسابات Platform Admin وتوزيع الشركات' ||
       out==='إدارة حسابات مسؤول المنصة وتوزيع الشركات' ||
       out==='إدارة حسابات مسؤولي المنصة وتوزيع الشركات'){
      out='Manage Platform Admin accounts and company assignments';
    }
    return out;
  };

  const v120ArabicPatterns=(value)=>{
    let out=String(value);
    if(out==='Manage Platform Admin accounts and company assignments' ||
       out==='إدارة حسابات Platform Admin وتوزيع الشركات' ||
       out==='إدارة حسابات مسؤول المنصة وتوزيع الشركات'){
      out='إدارة حسابات مسؤولي المنصة وتوزيع الشركات';
    }
    return out;
  };
'''

TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact))))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);out=v19Replace(out,v119PhraseEnToAr);return v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out))))));}const exact=arToEn.get(raw);if(exact)return v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact)))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);out=v19Replace(out,v119PhraseArToEn);return v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out)))))));};"

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact)))))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);out=v19Replace(out,v119PhraseEnToAr);out=v19Replace(out,v120PhraseEnToAr);return v120ArabicPatterns(v119ArabicPatterns(v118ArabicPatterns(v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out)))))));}const exact=arToEn.get(raw);if(exact)return v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact))))))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);out=v19Replace(out,v119PhraseArToEn);out=v19Replace(out,v120PhraseArToEn);return v120EnglishPatterns(v119EnglishPatterns(v118EnglishPatterns(v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out))))))));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.20 Platform Admins AR closure already applied; no changes made.')
        return
    if V119_MARKER not in text:
        raise SystemExit('Bilingual V1.19 Companies AR Plan closure marker not found; apply V1.19 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.20 dictionary anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.20 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.20 Platform Admin mappings')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.20 translator')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.20 Platform Admins AR closure runtime.')

if __name__ == '__main__':
    main()
