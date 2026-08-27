#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_R1_COMPANY_OVERRIDES_BUILD_SYNTAX_REPAIR'
V154_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_COMPANY_OVERRIDES_FULL_STATIC_DYNAMIC_CLOSURE'

BROKEN = [
"""            if(m)waHint.textContent=root.lang==='ar'?`المستخدم ${m[1]} من ${m[2]} · الحد مطبق فعليًا`:`Used ${m[1]} of ${m[2]} · limit is actively enforced`;""",
"""              if(m)waHint.textContent=root.lang==='ar'?`المستخدم ${m[1]} من ${m[2]} · محفوظ، لكن التطبيق الفعلي يحتاج Registry Runtime ووضع شركة غير shadow`:`Used ${m[1]} of ${m[2]} · saved, but enforcement requires Registry Runtime and a non-shadow company mode`;""",
]

FIXED = [
"""            if(m)waHint.textContent=root.lang==='ar'?('المستخدم '+m[1]+' من '+m[2]+' · الحد مطبق فعليًا'):('Used '+m[1]+' of '+m[2]+' · limit is actively enforced');""",
"""              if(m)waHint.textContent=root.lang==='ar'?('المستخدم '+m[1]+' من '+m[2]+' · محفوظ، لكن التطبيق الفعلي يحتاج Registry Runtime ووضع شركة غير shadow'):('Used '+m[1]+' of '+m[2]+' · saved, but enforcement requires Registry Runtime and a non-shadow company mode');""",
]

def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        if any(line in text for line in BROKEN):
            raise SystemExit('V1.54-R1 marker exists but broken template-literal form remains; refusing inconsistent state.')
        print('Super Admin bilingual V1.54-R1 Company Overrides build syntax repair already applied; no changes made.')
        return

    if V154_MARKER not in text:
        raise SystemExit('Bilingual V1.54 Company Overrides marker not found; apply V1.54 first.')

    for index, broken in enumerate(BROKEN, 1):
        count = text.count(broken)
        if count != 1:
            raise SystemExit(f'V1.54-R1 broken waHint anchor {index} count is {count}; expected 1.')

    for broken, fixed in zip(BROKEN, FIXED):
        text = text.replace(broken, fixed, 1)

    marker_anchor = FIXED[0]
    replacement = (
        "            // SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_R1_COMPANY_OVERRIDES_BUILD_SYNTAX_REPAIR\n"
        + marker_anchor
    )
    text = text.replace(marker_anchor, replacement, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.54-R1 Company Overrides build syntax repair.')

if __name__ == '__main__':
    main()
