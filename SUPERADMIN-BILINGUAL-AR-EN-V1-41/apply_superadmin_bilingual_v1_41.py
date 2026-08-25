#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_41_EVOLUTION_API_EN_REMAINING_STATIC_CLOSURE'
V140_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_40_EVOLUTION_API_EN_STATIC_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V140";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_41_EVOLUTION_API_EN_REMAINING_STATIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V141";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V140';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V141';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v140.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v141.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V140';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V141';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v140', '?v=superadmin-bilingual-v141', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v140"', 'data-sa-bilingual-runtime="v141"', 'runtime asset marker', 1),
]

PAIR_ANCHOR = """      ['Rotate credentials','تدوير البيانات']
    ];"""
PAIR_REPLACEMENT = """      ['Rotate credentials','تدوير البيانات'],
      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_41_EVOLUTION_API_EN_REMAINING_STATIC_CLOSURE
      ['Enable Evolution API integration','تفعيل تكامل Evolution API'],
      ['Generate or rotate connection credentials and restart the Evolution API service.','توليد أو تدوير بيانات الربط وإعادة تشغيل خدمة Evolution API.']
    ];"""

SELECTOR_ANCHOR = """    const v140EvolutionSelector='p.muted,div.muted,h3,#evolutionStatusGrid .empty,#evolutionManagedCapability,#evolutionRefreshBtn,#evolutionGenerateBtn,#evolutionRotateBtn';"""
SELECTOR_REPLACEMENT = """    const v140EvolutionSelector='b,p.muted,div.muted,h3,#evolutionStatusGrid .empty,#evolutionManagedCapability,#evolutionRefreshBtn,#evolutionGenerateBtn,#evolutionRotateBtn';"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.41 Evolution API EN remaining static closure already applied; no changes made.')
        return
    if V140_MARKER not in text:
        raise SystemExit('Bilingual V1.40 Evolution API EN static closure marker not found; apply V1.40 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(PAIR_ANCHOR) != 1:
        raise SystemExit(f'V1.41 Evolution pair anchor count is {text.count(PAIR_ANCHOR)}; expected 1.')
    if text.count(SELECTOR_ANCHOR) != 1:
        raise SystemExit(f'V1.41 Evolution selector anchor count is {text.count(SELECTOR_ANCHOR)}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(PAIR_ANCHOR, PAIR_REPLACEMENT, 1)
    text = text.replace(SELECTOR_ANCHOR, SELECTOR_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.41 Evolution API EN remaining static closure runtime.')

if __name__ == '__main__':
    main()
