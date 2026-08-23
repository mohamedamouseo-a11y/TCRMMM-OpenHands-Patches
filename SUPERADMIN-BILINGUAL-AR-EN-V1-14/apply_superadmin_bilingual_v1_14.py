#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_14_COMPANIES_ACTION_COUNTER_CLOSURE'
V113_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_13_OVERVIEW_MIXED_STATUS_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V113";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_14_COMPANIES_ACTION_COUNTER_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V114";',
     'UI version'),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V113';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V114';",
     'legacy UI runtime version'),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v113.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v114.js";',
     'runtime path'),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V113';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V114';",
     'standalone runtime version'),
    ('?v=superadmin-bilingual-v113', '?v=superadmin-bilingual-v114', 'asset cache key'),
    ('data-sa-bilingual-runtime="v113"', 'data-sa-bilingual-runtime="v114"', 'runtime asset marker'),
]

ANCHOR = "  const v112PhraseEnToAr=v112Pairs.slice().sort((a,b)=>b[0].length-a[0].length);"
TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v112ArabicPatterns(v111ArabicPatterns(exact));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);return v112ArabicPatterns(v111ArabicPatterns(out));}const exact=arToEn.get(raw);if(exact)return v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact)));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);return v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out)));};"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_14_COMPANIES_ACTION_COUNTER_CLOSURE
  // Audited Companies EN closure from the V1.13 unique-string evidence.
  const v114Pairs=[
    ['Copy Path','نسخ المسار'],
    ['Details','تفاصيل'],
    ['Renew','تجديد'],
    ['Login','دخول'],
    ['Risk','خطر']
  ];
  v114Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  const v114PhraseArToEn=v114Pairs.map((p)=>[p[1],p[0]]).sort((a,b)=>b[0].length-a[0].length);
  const v114PhraseEnToAr=v114Pairs.slice().sort((a,b)=>b[0].length-a[0].length);

  const v114EnglishPatterns=(value)=>{
    let out=String(value);
    if(out==='نسخ Path'||out==='نسخ المسار')out='Copy Path';
    if(out==='تفاصيل')out='Details';
    if(out==='تجديد')out='Renew';
    if(out==='دخول')out='Login';
    if(out==='خطر')out='Risk';

    let m=out.match(/^(\d+)\s+shown of\s+(\d+)\s*·\s*صفحة\s+(\d+)\/(\d+)$/i);
    if(m)out=m[1]+' shown of '+m[2]+' · page '+m[3]+'/'+m[4];
    m=out.match(/^(\d+)\s+shown of\s+(\d+)\s*·\s*page\s+(\d+)\/(\d+)$/i);
    if(m)out=m[1]+' shown of '+m[2]+' · page '+m[3]+'/'+m[4];
    return out;
  };

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

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact)));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);return v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out)));}const exact=arToEn.get(raw);if(exact)return v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);return v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out))));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.14 Companies action/counter closure already applied; no changes made.')
        return
    if V113_MARKER not in text:
        raise SystemExit('Bilingual V1.13 mixed-status marker not found; apply V1.13 first.')

    for old, _new, label in REPLACES:
        count = text.count(old)
        expected = 3 if label == 'asset cache key' else 1
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.14 runtime anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.14 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, _label in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.14 Companies action/counter mappings')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.14 translator')

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.14 Companies action/counter closure runtime.')

if __name__ == '__main__':
    main()
