#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_39_GITHUB_SYNC_AR_SAFE_CLEANUP_OPTION_CLOSURE'
V138_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_38_AUDIT_LOG_EN_ACTION_PLACEHOLDER_FINAL_RUNTIME_PIN'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V138";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_39_GITHUB_SYNC_AR_SAFE_CLEANUP_OPTION_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V139";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V138';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V139';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v138.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v139.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V138';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V139';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v138', '?v=superadmin-bilingual-v139', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v138"', 'data-sa-bilingual-runtime="v139"', 'runtime asset marker', 1),
]

PIN_ANCHOR = """  setAttr('#auditAction','placeholder','e.g. subscription or github.sync','مثل subscription أو github.sync');};"""
PIN_REPLACEMENT = """  setAttr('#auditAction','placeholder','e.g. subscription or github.sync','مثل subscription أو github.sync');
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_39_GITHUB_SYNC_AR_SAFE_CLEANUP_OPTION_CLOSURE
  // V1.38 browser evidence: pin the ordinary cleanup action option after the standalone translation sweep.
  if(typeof location!=='undefined' && location.hash==='#github'){
    const v139CleanupOption=document.querySelector('#githubAction option[value="cleanup"]');
    if(v139CleanupOption)v139CleanupOption.textContent=(root.lang==='ar'?'إلغاء آمن':'Safe Cleanup');
  }};"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.39 GitHub Sync AR Safe Cleanup option closure already applied; no changes made.')
        return
    if V138_MARKER not in text:
        raise SystemExit('Bilingual V1.38 Audit Log action placeholder final runtime pin marker not found; apply V1.38 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    pin_count = text.count(PIN_ANCHOR)
    if pin_count != 1:
        raise SystemExit(f'V1.39 standalone runtime cleanup option anchor count is {pin_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(PIN_ANCHOR, PIN_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.39 GitHub Sync AR Safe Cleanup option closure runtime.')

if __name__ == '__main__':
    main()
