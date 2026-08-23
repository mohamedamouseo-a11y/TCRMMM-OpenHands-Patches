#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_7_CACHE_BUST'
V16_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_6'

OLD_UI_VERSION = 'const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2";'
NEW_UI_VERSION = '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_7_CACHE_BUST\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V17";'

OLD_RUNTIME_VERSION = "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2';"
NEW_RUNTIME_VERSION = "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V17';"

OLD_STYLE_TAG = '  const styleTag = `<link rel="stylesheet" href="${CSS_PATH}" data-sa-polish="${UI_VERSION}"${nonceAttribute}>`;'
NEW_STYLE_TAG = '  const styleTag = `<link rel="stylesheet" href="${CSS_PATH}?v=superadmin-bilingual-v17" data-sa-polish="${UI_VERSION}"${nonceAttribute}>`;'

OLD_SCRIPT_TAG = '  const scriptTag = `<script src="${JS_PATH}" defer data-sa-polish="${UI_VERSION}"${nonceAttribute}></script>`;'
NEW_SCRIPT_TAG = '  const scriptTag = `<script src="${JS_PATH}?v=superadmin-bilingual-v17" defer data-sa-polish="${UI_VERSION}"${nonceAttribute}></script>`;'

OLD_CACHE = '  res.setHeader("Cache-Control", "public, max-age=3600");'
NEW_CACHE = '  res.setHeader("Cache-Control", "no-store, max-age=0, must-revalidate");\n  res.setHeader("Pragma", "no-cache");'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.7 cache-bust patch already applied; no changes made.')
        return
    if V16_MARKER not in text:
        raise SystemExit('Bilingual V1.6 marker not found; apply V1 through V1.6 first.')

    for label, anchor in [
        ('UI version', OLD_UI_VERSION),
        ('runtime version', OLD_RUNTIME_VERSION),
        ('style asset injection', OLD_STYLE_TAG),
        ('script asset injection', OLD_SCRIPT_TAG),
        ('asset cache header', OLD_CACHE),
    ]:
        if text.count(anchor) != 1:
            raise SystemExit(f'{label} anchor count is {text.count(anchor)}; refusing unknown baseline.')

    text = replace_once(text, OLD_UI_VERSION, NEW_UI_VERSION, 'UI version')
    text = replace_once(text, OLD_RUNTIME_VERSION, NEW_RUNTIME_VERSION, 'runtime version')
    text = replace_once(text, OLD_STYLE_TAG, NEW_STYLE_TAG, 'style cache bust')
    text = replace_once(text, OLD_SCRIPT_TAG, NEW_SCRIPT_TAG, 'script cache bust')
    text = replace_once(text, OLD_CACHE, NEW_CACHE, 'asset no-store')

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual Arabic / English V1.7 asset cache-bust and no-store runtime fix.')


if __name__ == '__main__':
    main()
