#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_50_TARA_LANGUAGE_ATTRIBUTE_RESWEEP'
V149_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_49_PLANS_RUNTIME_STATUS_EMPTY_STATE_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V149";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_50_TARA_LANGUAGE_ATTRIBUTE_RESWEEP\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V150";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V149';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V150';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v149.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v150.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V149';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V150';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v149', '?v=superadmin-bilingual-v150', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v149"', 'data-sa-bilingual-runtime="v150"', 'runtime asset marker', 1),
]

OBSERVER_OLD = """  const boot=()=>{root.dataset.saBilingualRuntime=VERSION;const initial=read();write(initial);apply(initial,false);ensureControls();burst();const observer=new MutationObserver(schedule);observer.observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['class','hidden','aria-selected','placeholder','title','aria-label']});window.addEventListener('pageshow',burst);window.addEventListener('focus',schedule);};"""

OBSERVER_NEW = """  const boot=()=>{root.dataset.saBilingualRuntime=VERSION;const initial=read();write(initial);apply(initial,false);ensureControls();burst();const observer=new MutationObserver(schedule);observer.observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['class','hidden','aria-selected','placeholder','title','aria-label']});
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_50_TARA_LANGUAGE_ATTRIBUTE_RESWEEP
  // Standalone pages can restore html language metadata after the deferred bilingual runtime
  // has already swept their initial Arabic markup. Re-sweep whenever the root language
  // attributes change so Tara and every other page-scoped finalizer sees the final language.
  const languageObserver=new MutationObserver(schedule);
  languageObserver.observe(root,{attributes:true,attributeFilter:['lang','dir','data-sa-lang']});
  window.addEventListener('pageshow',burst);window.addEventListener('focus',schedule);};"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.50 Tara language-attribute resweep already applied; no changes made.')
        return
    if V149_MARKER not in text:
        raise SystemExit('Bilingual V1.49 Plans runtime status/empty-state marker not found; apply V1.49 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(OBSERVER_OLD)
    if count != 1:
        raise SystemExit(f'V1.50 runtime observer anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(OBSERVER_OLD, OBSERVER_NEW, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.50 Tara language-attribute resweep runtime.')

if __name__ == '__main__':
    main()
