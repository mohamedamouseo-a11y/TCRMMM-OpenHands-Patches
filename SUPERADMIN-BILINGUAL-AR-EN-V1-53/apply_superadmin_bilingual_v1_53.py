#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_53_PLANS_LIMITS_HELPER_CLOSURE'
V152_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_52_PLANS_MIXED_COMPANIES_PLATFORM_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V152";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_53_PLANS_LIMITS_HELPER_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V153";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V152';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V153';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v152.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v153.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V152';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V153';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v152', '?v=superadmin-bilingual-v153', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v152"', 'data-sa-bilingual-runtime="v153"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

REPLACEMENT = r"""      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_53_PLANS_LIMITS_HELPER_CLOSURE
      // V1.52 continuation evidence found the Limits helper partially translated by
      // the generic sweep ("Save Draft" inside the Arabic sentence). Canonicalize the
      // original Arabic, canonical English, and observed mixed alias in both directions.
      if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
        const arLimitsHelper='يمكن حفظ المسودة ناقصة، لكن النشر يتطلب قرارًا صريحًا لكل حد.';
        const enLimitsHelper='A draft can be saved incomplete, but publishing requires an explicit decision for every limit.';
        const mixedLimitsHelper='يمكن Save Draft ناقصة، لكن النشر يتطلب قرارًا صريحًا لكل حد.';
        const arLimitsHelperNoDot='يمكن حفظ المسودة ناقصة، لكن النشر يتطلب قرارًا صريحًا لكل حد';
        const enLimitsHelperNoDot='A draft can be saved incomplete, but publishing requires an explicit decision for every limit';
        const mixedLimitsHelperNoDot='يمكن Save Draft ناقصة، لكن النشر يتطلب قرارًا صريحًا لكل حد';
        document.querySelectorAll('body small').forEach((el)=>{
          if(el.children.length)return;
          const raw=(el.textContent||'').trim();
          if(raw===arLimitsHelper||raw===enLimitsHelper||raw===mixedLimitsHelper||
             raw===arLimitsHelperNoDot||raw===enLimitsHelperNoDot||raw===mixedLimitsHelperNoDot){
            el.textContent=(root.lang==='ar'?arLimitsHelper:enLimitsHelper);
          }
        });
      }
      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.53 Plans Limits helper closure already applied; no changes made.')
        return
    if V152_MARKER not in text:
        raise SystemExit('Bilingual V1.52 Plans mixed companies/platform closure marker not found; apply V1.52 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(ANCHOR)
    if count != 1:
        raise SystemExit(f'V1.53 Plans document-title anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.53 Plans Limits helper closure.')

if __name__ == '__main__':
    main()
