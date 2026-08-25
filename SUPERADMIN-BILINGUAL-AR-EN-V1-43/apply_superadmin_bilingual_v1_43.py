#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_43_EVOLUTION_API_AR_ENABLE_INTEGRATION_CANONICALIZATION'
V142_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_42_EVOLUTION_API_EN_SECRET_PLACEHOLDERS_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V142";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_43_EVOLUTION_API_AR_ENABLE_INTEGRATION_CANONICALIZATION\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V143";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V142';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V143';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v142.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v143.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V142';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V143';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v142', '?v=superadmin-bilingual-v143', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v142"', 'data-sa-bilingual-runtime="v143"', 'runtime asset marker', 1),
]

EVOLUTION_ANCHOR = """    ['#evolutionApiToken','#evolutionWebhookSecret'].forEach((selector)=>{
      const el=document.querySelector(selector);
      if(el)el.setAttribute('placeholder',v142EvolutionSecretPlaceholder);
    });
  }};"""

EVOLUTION_REPLACEMENT = """    ['#evolutionApiToken','#evolutionWebhookSecret'].forEach((selector)=>{
      const el=document.querySelector(selector);
      if(el)el.setAttribute('placeholder',v142EvolutionSecretPlaceholder);
    });
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_43_EVOLUTION_API_AR_ENABLE_INTEGRATION_CANONICALIZATION
    // V1.42 browser evidence: force the final canonical label after generic bilingual substitutions.
    const v143EvolutionEnableLabel=document.querySelector('div.evolutionToggleRow > div > b');
    if(v143EvolutionEnableLabel){
      v143EvolutionEnableLabel.textContent=(root.lang==='ar'?'تفعيل تكامل Evolution API':'Enable Evolution API integration');
    }
  }};"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.43 Evolution API AR enable-integration canonicalization already applied; no changes made.')
        return
    if V142_MARKER not in text:
        raise SystemExit('Bilingual V1.42 Evolution API secret placeholders closure marker not found; apply V1.42 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    anchor_count = text.count(EVOLUTION_ANCHOR)
    if anchor_count != 1:
        raise SystemExit(f'V1.43 Evolution final canonicalization anchor count is {anchor_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(EVOLUTION_ANCHOR, EVOLUTION_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.43 Evolution API AR enable-integration canonicalization runtime.')

if __name__ == '__main__':
    main()
