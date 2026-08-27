#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_55_EVOLUTION_API_BASE_URL_LABEL_CLOSURE'
V154_R1_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_R1_COMPANY_OVERRIDES_BUILD_SYNTAX_REPAIR'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V154";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_55_EVOLUTION_API_BASE_URL_LABEL_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V155";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V154';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V155';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v154.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v155.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V154';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V155';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v154', '?v=superadmin-bilingual-v155', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v154"', 'data-sa-bilingual-runtime="v155"', 'runtime asset marker', 1),
]

PAIR_ANCHOR = """      ['Enable Evolution API integration','تفعيل تكامل Evolution API'],
      ['Generate or rotate connection credentials and restart the Evolution API service.','توليد أو تدوير بيانات الربط وإعادة تشغيل خدمة Evolution API.']
    ];"""
PAIR_REPLACEMENT = """      ['Enable Evolution API integration','تفعيل تكامل Evolution API'],
      ['Generate or rotate connection credentials and restart the Evolution API service.','توليد أو تدوير بيانات الربط وإعادة تشغيل خدمة Evolution API.'],
      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_55_EVOLUTION_API_BASE_URL_LABEL_CLOSURE
      ['Base URL','الرابط الأساسي']
    ];"""

SELECTOR_ANCHOR = """    const v140EvolutionSelector='b,p.muted,div.muted,h3,#evolutionStatusGrid .empty,#evolutionManagedCapability,#evolutionRefreshBtn,#evolutionGenerateBtn,#evolutionRotateBtn';"""
SELECTOR_REPLACEMENT = """    const v140EvolutionSelector='b,p.muted,div.muted,h3,#evolutionStatusGrid .empty,#evolutionManagedCapability,#evolutionRefreshBtn,#evolutionGenerateBtn,#evolutionRotateBtn,.evolutionPlatformGrid .evolutionCard.stack .field > label';"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.55 Evolution API Base URL label closure already applied; no changes made.')
        return
    if V154_R1_MARKER not in text:
        raise SystemExit('Bilingual V1.54-R1 syntax repair marker not found; apply V1.54-R1 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(PAIR_ANCHOR) != 1:
        raise SystemExit(f'V1.55 Evolution pair anchor count is {text.count(PAIR_ANCHOR)}; expected 1.')
    if text.count(SELECTOR_ANCHOR) != 1:
        raise SystemExit(f'V1.55 Evolution selector anchor count is {text.count(SELECTOR_ANCHOR)}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(PAIR_ANCHOR, PAIR_REPLACEMENT, 1)
    text = text.replace(SELECTOR_ANCHOR, SELECTOR_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.55 Evolution API Base URL label closure.')

if __name__ == '__main__':
    main()
