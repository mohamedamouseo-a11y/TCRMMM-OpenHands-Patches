#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_60_COMMERCIAL_TENANT_EDITOR_STATIC_HEADER_HARD_CLOSURE'
V159_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_59_COMMERCIAL_SAFETY_CONTROLS_HARD_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V159";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_60_COMMERCIAL_TENANT_EDITOR_STATIC_HEADER_HARD_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V160";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V159';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V160';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v159.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v160.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V159';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V160';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v159', '?v=superadmin-bilingual-v160', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v159"', 'data-sa-bilingual-runtime="v160"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

REPLACEMENT = r"""      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_60_COMMERCIAL_TENANT_EDITOR_STATIC_HEADER_HARD_CLOSURE
      // V1.59 evidence found the generic sweep partially translating the fixed
      // Commercial tenant-editor default subtitle ("الDetails ..."). Canonicalize
      // only fixed header/empty-state/search copy by selector. Dynamic tenant
      // identity/status text written after a company is selected is intentionally
      // left untouched.
      if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
        const commercialRoot=document.querySelector('#commercialView');
        if(commercialRoot){
          const setFixed=(sel,en,ar,aliases)=>{
            const el=commercialRoot.querySelector(sel);
            if(!(el instanceof HTMLElement))return;
            const raw=String(el.textContent||'').trim().replace(/\s+/g,' ');
            const accepted=new Set([en,ar].concat(aliases||[]));
            if(accepted.has(raw))el.textContent=(root.lang==='ar'?ar:en);
          };
          setFixed('#commercialTenantTitle','Select a company','اختر شركة',[]);
          setFixed('#commercialTenantSub','Full commercial and operational details.','التفاصيل التجارية والتشغيلية الكاملة.',[
            'الDetails التجارية والتشغيلية الكاملة.',
            'Details التجارية والتشغيلية الكاملة.',
            'التفاصيل commercial والتشغيلية الكاملة.',
            'التفاصيل التجارية وoperational الكاملة.'
          ]);
          setFixed('#commercialTenantEmpty','Select a company from the list.','اختر شركة من القائمة.',[
            'اختر Company من القائمة.',
            'Select شركة from the list.'
          ]);

          const listCard=commercialRoot.querySelector('.commercialGrid > aside.card');
          if(listCard instanceof HTMLElement){
            const setList=(sel,en,ar,aliases)=>{
              const el=listCard.querySelector(sel);
              if(!(el instanceof HTMLElement))return;
              const raw=String(el.textContent||'').trim().replace(/\s+/g,' ');
              const accepted=new Set([en,ar].concat(aliases||[]));
              if(accepted.has(raw))el.textContent=(root.lang==='ar'?ar:en);
            };
            setList('.cardHead h2','Companies & Subscriptions','الشركات والاشتراكات',[
              'Companies والاشتراكات',
              'الشركات & Subscriptions'
            ]);
            setList('.cardHead p','Select a company to manage subscription, rollout, and usage.','اختر شركة لإدارة الاشتراك والتفعيل والاستهلاك.',[
              'اختر شركة لإدارة Subscription والتفعيل والاستهلاك.',
              'Select a company لإدارة الاشتراك والتفعيل والاستهلاك.'
            ]);
            setList('.field label','Search','بحث',[]);
          }
          const search=commercialRoot.querySelector('#commercialTenantSearch');
          if(search instanceof HTMLInputElement){
            search.setAttribute('placeholder',root.lang==='ar'?'الشركة أو الباقة':'Company or plan');
          }
        }
      }
      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.60 Commercial tenant editor static header hard closure already applied; no changes made.')
        return
    if V159_MARKER not in text:
        raise SystemExit('Bilingual V1.59 Commercial safety controls hard closure marker not found; apply V1.59 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(ANCHOR)
    if count != 1:
        raise SystemExit(f'V1.60 Plans document-title anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.60 Commercial tenant editor static header hard closure.')

if __name__ == '__main__':
    main()
