#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_42_EVOLUTION_API_EN_SECRET_PLACEHOLDERS_CLOSURE'
V141_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_41_EVOLUTION_API_EN_REMAINING_STATIC_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V141";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_42_EVOLUTION_API_EN_SECRET_PLACEHOLDERS_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V142";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V141';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V142';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v141.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v142.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V141';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V142';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v141', '?v=superadmin-bilingual-v142', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v141"', 'data-sa-bilingual-runtime="v142"', 'runtime asset marker', 1),
]

EVOLUTION_ANCHOR = """    document.querySelectorAll(v140EvolutionSelector).forEach((el)=>{
      const key=(el.textContent||'').trim();
      const next=v140EvolutionMap.get(key);
      if(next)el.textContent=next;
    });
  }};"""

EVOLUTION_REPLACEMENT = """    document.querySelectorAll(v140EvolutionSelector).forEach((el)=>{
      const key=(el.textContent||'').trim();
      const next=v140EvolutionMap.get(key);
      if(next)el.textContent=next;
    });
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_42_EVOLUTION_API_EN_SECRET_PLACEHOLDERS_CLOSURE
    // V1.41 Resume QA evidence: these are static secret-field placeholders; never read or alter field values.
    const v142EvolutionSecretPlaceholder=(root.lang==='ar'?'اتركه فارغًا للاحتفاظ بالقيمة الحالية':'Leave blank to keep the current value');
    ['#evolutionApiToken','#evolutionWebhookSecret'].forEach((selector)=>{
      const el=document.querySelector(selector);
      if(el)el.setAttribute('placeholder',v142EvolutionSecretPlaceholder);
    });
  }};"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.42 Evolution API EN secret placeholders closure already applied; no changes made.')
        return
    if V141_MARKER not in text:
        raise SystemExit('Bilingual V1.41 Evolution API EN remaining static closure marker not found; apply V1.41 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    anchor_count = text.count(EVOLUTION_ANCHOR)
    if anchor_count != 1:
        raise SystemExit(f'V1.42 Evolution final sweep anchor count is {anchor_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(EVOLUTION_ANCHOR, EVOLUTION_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.42 Evolution API EN secret placeholders closure runtime.')

if __name__ == '__main__':
    main()
