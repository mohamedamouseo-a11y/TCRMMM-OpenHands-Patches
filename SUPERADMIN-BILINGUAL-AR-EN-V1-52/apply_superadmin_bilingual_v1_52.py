#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_52_PLANS_MIXED_COMPANIES_PLATFORM_CLOSURE'
V151_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_51_PLANS_LANGUAGE_NAV_PERSISTENCE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V151";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_52_PLANS_MIXED_COMPANIES_PLATFORM_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V152";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V151';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V152';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v151.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v152.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V151';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V152';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v151', '?v=superadmin-bilingual-v152', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v151"', 'data-sa-bilingual-runtime="v152"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

REPLACEMENT = r"""      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_52_PLANS_MIXED_COMPANIES_PLATFORM_CLOSURE
      // V1.51 evidence: the generic sweep can partially translate the Arabic prefix
      // "إدارة الشركات" before the Plans finalizer sees the full ordinary sentence.
      // Collapse both the source and the observed mixed form to one canonical pair.
      if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
        const ar='إدارة الشركات والباقات على مستوى المنصة.';
        const en='Manage companies and plans across the platform.';
        const mixed='Companies Management والباقات على مستوى المنصة.';
        const arNoDot='إدارة الشركات والباقات على مستوى المنصة';
        const enNoDot='Manage companies and plans across the platform';
        const mixedNoDot='Companies Management والباقات على مستوى المنصة';
        document.querySelectorAll('body p').forEach((el)=>{
          if(el.children.length)return;
          const raw=(el.textContent||'').trim();
          if(raw===ar||raw===en||raw===mixed||raw===arNoDot||raw===enNoDot||raw===mixedNoDot){
            el.textContent=(root.lang==='ar'?ar:en);
          }
        });
      }
      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.52 Plans mixed companies/platform closure already applied; no changes made.')
        return
    if V151_MARKER not in text:
        raise SystemExit('Bilingual V1.51 Plans language navigation persistence marker not found; apply V1.51 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(ANCHOR)
    if count != 1:
        raise SystemExit(f'V1.52 Plans document-title anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.52 Plans mixed companies/platform closure.')

if __name__ == '__main__':
    main()
