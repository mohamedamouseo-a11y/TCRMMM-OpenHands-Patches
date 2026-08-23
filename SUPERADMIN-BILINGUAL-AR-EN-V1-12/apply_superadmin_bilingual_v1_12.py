#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_12_COMPANIES_EN_CLOSURE'
V111_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_11_OVERVIEW_AR_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V111";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_12_COMPANIES_EN_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V112";',
     'UI version'),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V111';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V112';",
     'legacy UI runtime version'),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v111.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v112.js";',
     'runtime path'),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V111';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V112';",
     'standalone runtime version'),
    ('?v=superadmin-bilingual-v111', '?v=superadmin-bilingual-v112', 'asset cache key'),
    ('data-sa-bilingual-runtime="v111"', 'data-sa-bilingual-runtime="v112"', 'runtime asset marker'),
]

ANCHOR = "  const v111PhraseEnToAr=v111Pairs.slice().sort((a,b)=>b[0].length-a[0].length);"
TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v111ArabicPatterns(exact);let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);return v111ArabicPatterns(out);}const exact=arToEn.get(raw);if(exact)return v110EnglishPatterns(v111EnglishPatterns(exact));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);return v110EnglishPatterns(v111EnglishPatterns(out));};"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_12_COMPANIES_EN_CLOSURE
  // Audited Companies EN closure from the V1.11 unique-string evidence.
  const v112Pairs=[
    ['Shown','المعروض'],
    ['Company filters','فلاتر الشركات'],
    ['Search & filters','البحث والفلاتر'],
    ['Find the company you need quickly.','اعثر على الشركة المطلوبة بسرعة.'],
    ['Company name, path, or email','اسم الشركة، المسار أو البريد'],
    ['Created from','From date الإنشاء'],
    ['Created to','To date الإنشاء'],
    ['Number of rows','عدد الصفوف'],
    ['Clear filters','مسح الفلاتر'],
    ['Save view','حفظ العرض'],
    ['Status, Plan, health, and actions.','الحالة، Plan، الصحة والإجراءات.'],
    ['Scroll horizontally when needed','يمكن التمرير أفقياً عند الحاجة'],
    ['Path','المسار'],
    ['Health','الصحة'],
    ['Remaining','متبقي']
  ];
  v112Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  const v112PhraseArToEn=v112Pairs.map((p)=>[p[1],p[0]]).sort((a,b)=>b[0].length-a[0].length);
  const v112PhraseEnToAr=v112Pairs.slice().sort((a,b)=>b[0].length-a[0].length);

  const v112EnglishPatterns=(value)=>{
    let out=String(value);
    let m=out.match(/^Server-side pagination\s*·\s*(\d+)\s+سجل$/i);
    if(m)out='Server-side pagination · '+m[1]+' records';
    m=out.match(/^Server-side pagination\s*·\s*(\d+)\s+records$/i);
    if(m)out='Server-side pagination · '+m[1]+' records';
    return out;
  };

  const v112ArabicPatterns=(value)=>{
    let out=String(value);
    let m=out.match(/^Server-side pagination\s*·\s*(\d+)\s+records$/i);
    if(m)out='ترقيم صفحات من الخادم · '+m[1]+' سجل';
    return out;
  };
'''

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v112ArabicPatterns(v111ArabicPatterns(exact));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);return v112ArabicPatterns(v111ArabicPatterns(out));}const exact=arToEn.get(raw);if(exact)return v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact)));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);return v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out)));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.12 Companies EN closure already applied; no changes made.')
        return
    if V111_MARKER not in text:
        raise SystemExit('Bilingual V1.11 Overview AR closure marker not found; apply V1.11 first.')

    for old, new, label in REPLACES:
        count = text.count(old)
        expected = 3 if label == 'asset cache key' else 1
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.12 runtime anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.12 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, label in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.12 Companies dictionary/patterns')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.12 translator')

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.12 Companies EN closure runtime.')

if __name__ == '__main__':
    main()
