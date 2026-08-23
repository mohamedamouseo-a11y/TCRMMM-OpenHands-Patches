#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
RUNTIME_FILE = Path(__file__).with_name('bilingual_runtime_v18.js')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_8_STANDALONE_RUNTIME'
V17_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_7_CACHE_BUST'

OLD_UI_VERSION = 'const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V17";'
NEW_UI_VERSION = '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_8_STANDALONE_RUNTIME\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V18";'
OLD_RUNTIME_VERSION = "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V17';"
NEW_RUNTIME_VERSION = "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V18';"
JS_PATH_ANCHOR = 'const JS_PATH = "/super-admin/ui-polish-v2.js";'
RUNTIME_PATH_DECL = 'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v18.js";'
FUNCTION_ANCHOR = '\nfunction requestPath(req: Request): string {'
OLD_STYLE_TAG = '  const styleTag = `<link rel="stylesheet" href="${CSS_PATH}?v=superadmin-bilingual-v17" data-sa-polish="${UI_VERSION}"${nonceAttribute}>`;'
NEW_STYLE_TAG = '  const styleTag = `<link rel="stylesheet" href="${CSS_PATH}?v=superadmin-bilingual-v18" data-sa-polish="${UI_VERSION}"${nonceAttribute}>`;'
OLD_SCRIPT_TAG = '  const scriptTag = `<script src="${JS_PATH}?v=superadmin-bilingual-v17" defer data-sa-polish="${UI_VERSION}"${nonceAttribute}></script>`;'
NEW_SCRIPT_TAG = '  const scriptTag = `<script src="${JS_PATH}?v=superadmin-bilingual-v18" defer data-sa-polish="${UI_VERSION}"${nonceAttribute}></script><script src="${BILINGUAL_RUNTIME_PATH}?v=superadmin-bilingual-v18" defer data-sa-bilingual-runtime="v18"${nonceAttribute}></script>`;'
ROUTER_ANCHOR = '  router.get([JS_PATH, LEGACY_JS_PATH, "/super-admin/plans/ui-polish-v2.js", "/super-admin/plans/ui-polish-v1.js"], (_req, res) =>\n    sendAsset(res, "application/javascript", SUPER_ADMIN_JS),\n  );'
ROUTER_REPLACEMENT = '  router.get([JS_PATH, LEGACY_JS_PATH, "/super-admin/plans/ui-polish-v2.js", "/super-admin/plans/ui-polish-v1.js"], (_req, res) =>\n    sendAsset(res, "application/javascript", SUPER_ADMIN_JS),\n  );\n  router.get(BILINGUAL_RUNTIME_PATH, (_req, res) =>\n    sendAsset(res, "application/javascript", SUPER_ADMIN_BILINGUAL_RUNTIME_V18),\n  );'
ASSET_LIST_OLD = '    const isAssetPath = [CSS_PATH, JS_PATH, LEGACY_CSS_PATH, LEGACY_JS_PATH].includes(pathName)'
ASSET_LIST_NEW = '    const isAssetPath = [CSS_PATH, JS_PATH, BILINGUAL_RUNTIME_PATH, LEGACY_CSS_PATH, LEGACY_JS_PATH].includes(pathName)'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.8 standalone runtime already applied; no changes made.')
        return
    if V17_MARKER not in text:
        raise SystemExit('Bilingual V1.7 cache-bust marker not found; apply V1 through V1.7 first.')
    if not RUNTIME_FILE.exists():
        raise SystemExit(f'Missing runtime file: {RUNTIME_FILE}')
    runtime_js = RUNTIME_FILE.read_text(encoding='utf-8')
    if 'SUPER_ADMIN_BILINGUAL_RUNTIME_V18' not in runtime_js:
        raise SystemExit('Runtime marker missing from bilingual_runtime_v18.js')
    if '`' in runtime_js:
        raise SystemExit('Runtime file contains a backtick; refusing unsafe String.raw embedding.')
    runtime_block = '\n\nconst SUPER_ADMIN_BILINGUAL_RUNTIME_V18 = String.raw`\n' + runtime_js + '\n`;\n'

    anchors = [
        ('UI version', OLD_UI_VERSION),
        ('legacy runtime version', OLD_RUNTIME_VERSION),
        ('JS path declaration', JS_PATH_ANCHOR),
        ('requestPath function', FUNCTION_ANCHOR),
        ('style tag', OLD_STYLE_TAG),
        ('script tag', OLD_SCRIPT_TAG),
        ('runtime route anchor', ROUTER_ANCHOR),
        ('asset path list', ASSET_LIST_OLD),
    ]
    for label, anchor in anchors:
        if text.count(anchor) != 1:
            raise SystemExit(f'{label} anchor count is {text.count(anchor)}; refusing unknown baseline.')

    text = replace_once(text, OLD_UI_VERSION, NEW_UI_VERSION, 'UI version')
    text = replace_once(text, OLD_RUNTIME_VERSION, NEW_RUNTIME_VERSION, 'legacy runtime version')
    text = replace_once(text, JS_PATH_ANCHOR, JS_PATH_ANCHOR + '\n' + RUNTIME_PATH_DECL, 'runtime path declaration')
    text = replace_once(text, FUNCTION_ANCHOR, runtime_block + FUNCTION_ANCHOR, 'standalone runtime source')
    text = replace_once(text, OLD_STYLE_TAG, NEW_STYLE_TAG, 'style cache bust V18')
    text = replace_once(text, OLD_SCRIPT_TAG, NEW_SCRIPT_TAG, 'script injection V18')
    text = replace_once(text, ROUTER_ANCHOR, ROUTER_REPLACEMENT, 'standalone runtime route')
    text = replace_once(text, ASSET_LIST_OLD, ASSET_LIST_NEW, 'runtime asset exclusion')

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.8 independent runtime asset with lifecycle, persistence, and translation fallback.')


if __name__ == '__main__':
    main()
