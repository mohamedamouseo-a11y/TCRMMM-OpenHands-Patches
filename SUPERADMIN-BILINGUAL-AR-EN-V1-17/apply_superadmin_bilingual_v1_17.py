#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE'
V116_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_16_USERS_AR_HEADER_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V116";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE\\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V117";',
     'UI version'),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V116';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V117';",
     'legacy UI runtime version'),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v116.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v117.js";',
     'runtime path'),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V116';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V117';",
     'standalone runtime version'),
    ('?v=superadmin-bilingual-v116', '?v=superadmin-bilingual-v117', 'asset cache key'),
    ('data-sa-bilingual-runtime="v116"', 'data-sa-bilingual-runtime="v117"', 'runtime asset marker'),
]

ANCHOR = "  v116Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});"
TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact)));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);return v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out)));}const exact=arToEn.get(raw);if(exact)return v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);return v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out))));};"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE
  // Audited Users EN closure from the complete V1.16 raw browser evidence and screenshot.
  const v117Pairs=[
    ['Company Users','مستخدمو الشركات'],
    ['Active accounts','حسابات نشطة'],
    ['All roles','كل الأدوار'],
    ['Deleted','محذوف'],
    ['Show results','عرض النتائج'],
    ['Last Login','آخر LOGIN'],
    ['Login Details','بيانات الLOGIN'],
    ['New password','كلمة مرور جديدة'],
    ['Suspend','إيقاف'],
    ['Name, email, or role','الاسم، البريد أو الدور']
  ];
  v117Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  // Arabic aliases seen in runtime data/status rendering. Do not overwrite the
  // canonical EN->AR mapping globally; only guarantee clean English output.
  arToEn.set('مفعّلة','Enabled');
  arToEn.set('متوقف','Suspended');

  const v117EnglishPatterns=(value)=>{
    let out=String(value);
    let m=out.match(/^(\d+)\s+حساب(?:ات)?\s+مسجل(?:ة)?\s+عبر\s+(\d+)\s+شركة$/);
    if(m)out=m[1]+' registered accounts across '+m[2]+' companies';
    return out;
  };

  const v117ArabicPatterns=(value)=>{
    let out=String(value);
    let m=out.match(/^(\d+)\s+registered accounts across\s+(\d+)\s+companies$/i);
    if(m)out=m[1]+' حساب مسجل عبر '+m[2]+' شركة';
    return out;
  };
'''

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(exact))));let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);out=v19Replace(out,v111PhraseEnToAr);out=v19Replace(out,v112PhraseEnToAr);out=v19Replace(out,v114PhraseEnToAr);return v117ArabicPatterns(v114ArabicPatterns(v112ArabicPatterns(v111ArabicPatterns(out))));}const exact=arToEn.get(raw);if(exact)return v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(exact)))));let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);out=v19Replace(out,v111PhraseArToEn);out=v19Replace(out,v112PhraseArToEn);out=v19Replace(out,v114PhraseArToEn);return v117EnglishPatterns(v114EnglishPatterns(v112EnglishPatterns(v110EnglishPatterns(v111EnglishPatterns(out)))));};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.17 Users EN full closure already applied; no changes made.')
        return
    if V116_MARKER not in text:
        raise SystemExit('Bilingual V1.16 Users AR header marker not found; apply V1.16 first.')

    for old, _new, label in REPLACES:
        count = text.count(old)
        expected = 3 if label == 'asset cache key' else 1
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.17 dictionary anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.17 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, _label in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.17 Users EN dictionary/patterns')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.17 translator')

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.17 Users EN full closure runtime.')

if __name__ == '__main__':
    main()
