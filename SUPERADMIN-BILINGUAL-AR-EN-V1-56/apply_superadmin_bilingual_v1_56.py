#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_56_EVOLUTION_CREDENTIALS_STATUS_LABELS_CLOSURE'
V155_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_55_EVOLUTION_API_BASE_URL_LABEL_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V155";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_56_EVOLUTION_CREDENTIALS_STATUS_LABELS_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V156";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V155';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V156';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v155.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v156.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V155';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V156';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v155', '?v=superadmin-bilingual-v156', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v155"', 'data-sa-bilingual-runtime="v156"', 'runtime asset marker', 1),
]

PAIR_ANCHOR = """      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_55_EVOLUTION_API_BASE_URL_LABEL_CLOSURE
      ['Base URL','الرابط الأساسي']
    ];"""
PAIR_REPLACEMENT = """      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_55_EVOLUTION_API_BASE_URL_LABEL_CLOSURE
      ['Base URL','الرابط الأساسي'],
      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_56_EVOLUTION_CREDENTIALS_STATUS_LABELS_CLOSURE
      ['API Token','رمز API'],
      ['Webhook Signing Secret','سر توقيع Webhook'],
      ['Webhook Secret','سر Webhook']
    ];"""

SELECTOR_ANCHOR = """    const v140EvolutionSelector='b,p.muted,div.muted,h3,#evolutionStatusGrid .empty,#evolutionManagedCapability,#evolutionRefreshBtn,#evolutionGenerateBtn,#evolutionRotateBtn,.evolutionPlatformGrid .evolutionCard.stack .field > label';"""
SELECTOR_REPLACEMENT = """    const v140EvolutionSelector='b,p.muted,div.muted,h3,#evolutionStatusGrid .empty,#evolutionStatusGrid small,#evolutionManagedCapability,#evolutionRefreshBtn,#evolutionGenerateBtn,#evolutionRotateBtn,.evolutionPlatformGrid .evolutionCard.stack .field > label';"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.56 Evolution credentials/status labels closure already applied; no changes made.')
        return
    if V155_MARKER not in text:
        raise SystemExit('Bilingual V1.55 Evolution Base URL label closure marker not found; apply V1.55 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(PAIR_ANCHOR) != 1:
        raise SystemExit(f'V1.56 Evolution pair anchor count is {text.count(PAIR_ANCHOR)}; expected 1.')
    if text.count(SELECTOR_ANCHOR) != 1:
        raise SystemExit(f'V1.56 Evolution selector anchor count is {text.count(SELECTOR_ANCHOR)}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(PAIR_ANCHOR, PAIR_REPLACEMENT, 1)
    text = text.replace(SELECTOR_ANCHOR, SELECTOR_REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.56 Evolution credentials/status labels closure.')

if __name__ == '__main__':
    main()
