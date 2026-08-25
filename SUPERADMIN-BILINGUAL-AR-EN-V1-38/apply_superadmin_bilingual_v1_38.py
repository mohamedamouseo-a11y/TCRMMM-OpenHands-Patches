#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_38_AUDIT_LOG_EN_ACTION_PLACEHOLDER_FINAL_RUNTIME_PIN'
V137_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_37_GITHUB_SYNC_EN_AUDIT_ACTION_PLACEHOLDER_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V137";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_38_AUDIT_LOG_EN_ACTION_PLACEHOLDER_FINAL_RUNTIME_PIN\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V138";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V137';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V138';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v137.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v138.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V137';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V138';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v137', '?v=superadmin-bilingual-v138', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v137"', 'data-sa-bilingual-runtime="v138"', 'runtime asset marker', 1),
]

PIN_ANCHOR = """setAttr('#globalSearchBox','aria-label','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');};"""
PIN_REPLACEMENT = """setAttr('#globalSearchBox','aria-label','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_38_AUDIT_LOG_EN_ACTION_PLACEHOLDER_FINAL_RUNTIME_PIN
  // V1.37 recheck evidence: pin the Audit Log action placeholder in the standalone runtime's final sweep.
  setAttr('#auditAction','placeholder','e.g. subscription or github.sync','مثل subscription أو github.sync');};"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.38 Audit Log EN action placeholder final runtime pin already applied; no changes made.')
        return
    if V137_MARKER not in text:
        raise SystemExit('Bilingual V1.37 Audit action placeholder closure marker not found; apply V1.37 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    pin_count = text.count(PIN_ANCHOR)
    if pin_count != 1:
        raise SystemExit(f'V1.38 standalone runtime pin anchor count is {pin_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(PIN_ANCHOR, PIN_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.38 Audit Log EN action placeholder final runtime pin.')

if __name__ == '__main__':
    main()
