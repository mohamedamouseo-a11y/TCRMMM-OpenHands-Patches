#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_11_OVERVIEW_AR_CLOSURE'
V110_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_10_OVERVIEW_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V110";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_11_OVERVIEW_AR_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V111";',
     'UI version'),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V110';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V111';",
     'legacy UI runtime version'),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v110.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v111.js";',
     'runtime path'),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V110';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V111';",
     'standalone runtime version'),
    ('?v=superadmin-bilingual-v110', '?v=superadmin-bilingual-v111', 'asset cache key'),
    ('data-sa-bilingual-runtime="v110"', 'data-sa-bilingual-runtime="v111"', 'runtime asset marker'),
]

ANCHOR = "  const v110AsciiDigits=(value)=>String(value).replace(/[٠-٩]/g,(ch)=>'0123456789'['٠١٢٣٤٥٦٧٨٩'.indexOf(ch)]);"
TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return exact;let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);return out;}const exact=arToEn.get(raw);if(exact)return v110EnglishPatterns(exact);let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);return v110EnglishPatterns(out);};"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_11_OVERVIEW_AR_CLOSURE
  // Audited Overview AR closure from the V1.10 unique-string evidence.
  const v111Pairs=[
    ['Organizations','المؤسسات'],
    ['Users & Access','المستخدمون والصلاحيات'],
    ['Plans & Commercial','الباقات والتشغيل التجاري'],
    ['Platform Administration','إدارة المنصة'],
    ['Tenant ID','معرّف الشركة'],
    ['Add Admin','إضافة مسؤول'],
    ['Save Admin & Company Permissions','حفظ المسؤول وصلاحيات الشركات'],
    ['Use Ctrl/Cmd to select multiple companies','استخدم مفتاح التحكم أو مفتاح الأوامر لاختيار أكثر من شركة']
  ];
  v111Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  const v111PhraseArToEn=v111Pairs.map((p)=>[p[1],p[0]]).sort((a,b)=>b[0].length-a[0].length);
  const v111PhraseEnToAr=v111Pairs.slice().sort((a,b)=>b[0].length-a[0].length);

  const v111ArabicPatterns=(value)=>{
    let out=String(value);
    if(out==='إضافة Admin')out='إضافة مسؤول';
    if(out==='حفظ Admin وصلاحيات الشركات')out='حفظ المسؤول وصلاحيات الشركات';
    if(out==='استخدم Ctrl/Cmd لاختيار أكثر من شركة')out='استخدم مفتاح التحكم أو مفتاح الأوامر لاختيار أكثر من شركة';

    let m=out.match(/^Health\s+(\d+)%\s*·\s*expired$/i);
    if(m)out='الصحة '+m[1]+'% · منتهي';
    m=out.match(/^(\d+)\s+active\s+of\s+(\d+)$/i);
    if(m)out=m[1]+' نشط من '+m[2];
    m=out.match(/^(\d+)\s+paid companies$/i);
    if(m)out=m[1]+' شركة مدفوعة';
    m=out.match(/^(\d+)\s+suspended\s*·\s*(\d+)\s+ending soon$/i);
    if(m)out=m[1]+' موقوفة · '+m[2]+' تنتهي قريبًا';
    return out;
  };

  const v111EnglishPatterns=(value)=>{
    let out=String(value);
    if(out==='إضافة مسؤول')out='Add Admin';
    if(out==='حفظ المسؤول وصلاحيات الشركات')out='Save Admin & Company Permissions';
    if(out==='استخدم مفتاح التحكم أو مفتاح الأوامر لاختيار أكثر من شركة')out='Use Ctrl/Cmd to select multiple companies';

    let m=out.match(/^الصحة\s+(\d+)%\s*·\s*منتهي$/);
    if(m)out='Health '+m[1]+'% · expired';
    m=out.match(/^(\d+)\s+نشط\s+من\s+(\d+)$/);
    if(m)out=m[1]+' active of '+m[2];
    m=out.match(/^(\d+)\s+شركة\s+مدفوعة$/);
    if(m)out=m[1]+' paid companies';
    m=out.match(/^(\d+)\s+موقوفة\s*·\s*(\d+)\s+تنتهي\s+قريبًا$/);
    if(m)out=m[1]+' suspended · '+m[2]+' ending soon';
    return out;
  };
'''

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v111ArabicPatterns(exact);let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);return v111ArabicPatterns(out);}const exact=arToEn.get(raw);if(exact)return v110EnglishPatterns(v111EnglishPatterns(exact));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);return v110EnglishPatterns(v111EnglishPatterns(out));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.11 Overview AR closure already applied; no changes made.')
        return
    if V110_MARKER not in text:
        raise SystemExit('Bilingual V1.10 Overview closure marker not found; apply V1.10 first.')

    for old, new, label in REPLACES:
        count = text.count(old)
        expected = 3 if label == 'asset cache key' else 1
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.11 runtime anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.11 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, label in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.11 Overview AR dictionary/patterns')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.11 translator')

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.11 Overview AR closure runtime.')

if __name__ == '__main__':
    main()
