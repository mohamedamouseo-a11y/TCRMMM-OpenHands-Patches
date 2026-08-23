#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
HOTFIX_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_STARTUP_HOTFIX'
V117_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE'

BROKEN = '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE\\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V117";'
FIXED = '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_USERS_EN_FULL_CLOSURE\n// SUPER_ADMIN_BILINGUAL_AR_EN_V1_17_STARTUP_HOTFIX\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V117";'


def main():
    text = TARGET.read_text(encoding='utf-8')
    if HOTFIX_MARKER in text:
        print('Super Admin bilingual V1.17 startup hotfix already applied; no changes made.')
        return
    if V117_MARKER not in text:
        raise SystemExit('V1.17 Users EN closure marker not found; apply V1.17 first.')
    count = text.count(BROKEN)
    if count != 1:
        raise SystemExit(f'V1.17 broken UI_VERSION newline anchor count is {count}; refusing unknown baseline.')

    text = text.replace(BROKEN, FIXED, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin bilingual V1.17 startup hotfix.')


if __name__ == '__main__':
    main()
