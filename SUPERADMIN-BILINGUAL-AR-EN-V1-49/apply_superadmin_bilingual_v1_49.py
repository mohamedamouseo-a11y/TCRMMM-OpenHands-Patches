#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_49_PLANS_RUNTIME_STATUS_EMPTY_STATE_CLOSURE'
V148_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_48_PLANS_CATALOG_EDITOR_FULL_STATIC_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V148";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_49_PLANS_RUNTIME_STATUS_EMPTY_STATE_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V149";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V148';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V149';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v148.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v149.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V148';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V149';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v148', '?v=superadmin-bilingual-v149', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v148"', 'data-sa-bilingual-runtime="v149"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');
    }
  };"""

REPLACEMENT = r"""      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');

      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_49_PLANS_RUNTIME_STATUS_EMPTY_STATE_CLOSURE
      // V1.48 evidence: late Plans status text is written after data loading and must be
      // canonicalized by the final standalone runtime sweep in both directions.
      const v149Status=document.querySelector('#status');
      if(v149Status){
        const raw=(v149Status.textContent||'').trim();
        const arReady='جاهز — جميع مفاتيح التشغيل تبدأ بأمان ويمكن تفعيلها تدريجيًا';
        const enReady='Ready — all operational controls start safely and can be enabled progressively.';
        if(raw===arReady||raw===enReady)v149Status.textContent=(root.lang==='ar'?arReady:enReady);
      }

      // V1.48 capture also observed this mixed legacy-sweep variant in the Plans empty
      // editor state. Pin only the exact ordinary UI variants; do not touch plan/domain data.
      document.querySelectorAll('#plansView .empty b').forEach((el)=>{
        const raw=(el.textContent||'').trim();
        const ar='اختر باقة لعرض تفاصيلها';
        const mixed='اختر باقة لعرض Detailsها';
        const en='Select a plan to view its details';
        if(raw===ar||raw===mixed||raw===en)el.textContent=(root.lang==='ar'?ar:en);
      });
    }
  };"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.49 Plans runtime status/empty-state closure already applied; no changes made.')
        return
    if V148_MARKER not in text:
        raise SystemExit('Bilingual V1.48 Plans Catalog/Editor full static closure marker not found; apply V1.48 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    anchor_count = text.count(ANCHOR)
    if anchor_count != 1:
        raise SystemExit(f'V1.49 Plans finalizer anchor count is {anchor_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.49 Plans runtime status/empty-state closure.')

if __name__ == '__main__':
    main()
