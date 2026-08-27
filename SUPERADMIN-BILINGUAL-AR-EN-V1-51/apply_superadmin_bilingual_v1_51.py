#!/usr/bin/env python3
from pathlib import Path

POLISH = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
CORE = Path('/var/www/TCRMMT/server/_core/index.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_51_PLANS_LANGUAGE_NAV_PERSISTENCE'
V150_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_50_TARA_LANGUAGE_ATTRIBUTE_RESWEEP'
V146_CORE_MARKER = 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V150";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_51_PLANS_LANGUAGE_NAV_PERSISTENCE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V151";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V150';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V151';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v150.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v151.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V150';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V151';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v150', '?v=superadmin-bilingual-v151', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v150"', 'data-sa-bilingual-runtime="v151"', 'runtime asset marker', 1),
]

BOOT_OLD = """  const boot=()=>{root.dataset.saBilingualRuntime=VERSION;const initial=read();write(initial);apply(initial,false);ensureControls();burst();const observer=new MutationObserver(schedule);"""

BOOT_NEW = """  const boot=()=>{root.dataset.saBilingualRuntime=VERSION;
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_51_PLANS_LANGUAGE_NAV_PERSISTENCE
  // The standalone Plans HTML is Arabic by default. Normal navigation from the main
  // console now carries ?lang=ar|en; honor that explicit handoff before the first sweep.
  let requestedLang=null;
  if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
    try{const q=new URLSearchParams(location.search).get('lang');if(q==='ar'||q==='en')requestedLang=q;}catch{}
  }
  const initial=requestedLang||read();write(initial);apply(initial,false);ensureControls();burst();const observer=new MutationObserver(schedule);"""

CORE_OLD = "$('plansManagementNav')?.addEventListener('click',function(){location.assign('/super-admin/plans');});"

CORE_NEW = """// SUPER_ADMIN_BILINGUAL_AR_EN_V1_51_PLANS_LANGUAGE_NAV_PERSISTENCE
  $('plansManagementNav')?.addEventListener('click',function(){
    let plansLang=document.documentElement.dataset.saLang;
    if(plansLang!=='ar'&&plansLang!=='en'){
      try{const stored=localStorage.getItem('tcrm-super-admin-language');if(stored==='ar'||stored==='en')plansLang=stored;}catch{}
    }
    if(plansLang!=='ar'&&plansLang!=='en')plansLang='en';
    location.assign('/super-admin/plans?lang='+encodeURIComponent(plansLang));
  });"""

def main():
    polish = POLISH.read_text(encoding='utf-8')
    core = CORE.read_text(encoding='utf-8')

    if MARKER in polish and MARKER in core:
        print('Super Admin bilingual V1.51 Plans language navigation persistence already applied; no changes made.')
        return
    if MARKER in polish or MARKER in core:
        raise SystemExit('V1.51 marker is present in only one target; refusing partial/unknown state.')
    if V150_MARKER not in polish:
        raise SystemExit('Bilingual V1.50 Tara language-attribute resweep marker not found; apply V1.50 first.')
    if V146_CORE_MARKER not in core:
        raise SystemExit('Evolution V1.46 direct-hash restore marker not found in core; refusing unknown baseline.')

    for old, _new, label, expected in REPLACES:
        count = polish.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if polish.count(BOOT_OLD) != 1:
        raise SystemExit(f'V1.51 Plans boot-language anchor count is {polish.count(BOOT_OLD)}; expected 1.')
    if core.count(CORE_OLD) != 1:
        raise SystemExit(f'V1.51 Plans navigation anchor count is {core.count(CORE_OLD)}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        polish = polish.replace(old, new)
    polish = polish.replace(BOOT_OLD, BOOT_NEW, 1)
    core = core.replace(CORE_OLD, CORE_NEW, 1)

    POLISH.write_text(polish, encoding='utf-8')
    CORE.write_text(core, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.51 Plans language navigation persistence.')

if __name__ == '__main__':
    main()
