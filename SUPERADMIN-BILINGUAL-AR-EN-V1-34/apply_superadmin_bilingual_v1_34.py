#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_34_TENANT_DETAILS_EN_PROVISIONING_STATIC_CLOSURE'
V133_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_33_COMPANIES_EN_RETRY_AUDIT_EN_OPTIONS_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V133";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_34_TENANT_DETAILS_EN_PROVISIONING_STATIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V134";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V133';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V134';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v133.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v134.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V133';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V134';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v133', '?v=superadmin-bilingual-v134', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v133"', 'data-sa-bilingual-runtime="v134"', 'runtime asset marker', 1),
]

EN_START = "  const v122EnglishPatterns=(value)=>{"
AR_START = "  const v122ArabicPatterns=(value)=>{"
AR_END = "  const v121PhraseArToEn="
RETURN_ANCHOR = "    return out;\n  };"

EN_FINAL = r'''    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_34_TENANT_DETAILS_EN_PROVISIONING_STATIC_CLOSURE
    // V1.33 post-restart browser evidence: close only ordinary static provisioning copy
    // inside the Tenants/Tenant Details surface. Runtime status/error/domain data remains untouched.
    if(typeof location!=='undefined' && location.hash==='#tenants'){
      const v134TenantDetailsEnFinal=new Map([
        ["تعذر تجهيز الشركة","Company provisioning failed"],
        ["عامل التجهيز يعمل كخدمة PM2 مستقلة ويعالج قائمة الانتظار تلقائيًا.","The provisioning worker runs as an independent PM2 service and processes the queue automatically."],
        ["رقم المهمة","Job ID"],
        ["المحاولات","Attempts"],
        ["إعادة محاولة التجهيز","Retry provisioning"],
        ["إعادة المحاولة تستخدم نفس المهمة بأمان ولا تنشئ شركة مكررة.","Retry safely reuses the same job and does not create a duplicate company."]
      ]);
      if(v134TenantDetailsEnFinal.has(out))out=v134TenantDetailsEnFinal.get(out);
    }
'''

AR_FINAL = r'''    // V1.34 reverse canonicalization for the same Tenant Details static copy.
    if(typeof location!=='undefined' && location.hash==='#tenants'){
      const v134TenantDetailsArFinal=new Map([
        ["Company provisioning failed","تعذر تجهيز الشركة"],
        ["The provisioning worker runs as an independent PM2 service and processes the queue automatically.","عامل التجهيز يعمل كخدمة PM2 مستقلة ويعالج قائمة الانتظار تلقائيًا."],
        ["Job ID","رقم المهمة"],
        ["Attempts","المحاولات"],
        ["Retry provisioning","إعادة محاولة التجهيز"],
        ["Retry safely reuses the same job and does not create a duplicate company.","إعادة المحاولة تستخدم نفس المهمة بأمان ولا تنشئ شركة مكررة."]
      ]);
      if(v134TenantDetailsArFinal.has(out))out=v134TenantDetailsArFinal.get(out);
    }
'''

def insert_before_return(text, start_anchor, end_anchor, payload, label):
    start = text.find(start_anchor)
    if start < 0:
        raise SystemExit(f'{label} start anchor not found; refusing unknown baseline.')
    end = text.find(end_anchor, start + len(start_anchor)) if end_anchor else len(text)
    if end < 0:
        raise SystemExit(f'{label} end anchor not found; refusing unknown baseline.')
    segment = text[start:end]
    count = segment.count(RETURN_ANCHOR)
    if count != 1:
        raise SystemExit(f'{label} return anchor count is {count}; expected 1.')
    segment = segment.replace(RETURN_ANCHOR, payload + RETURN_ANCHOR, 1)
    return text[:start] + segment + text[end:]

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.34 Tenant Details EN provisioning static closure already applied; no changes made.')
        return
    if V133_MARKER not in text:
        raise SystemExit('Bilingual V1.33 Companies/Audit closure marker not found; apply V1.33 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_START) != 1:
        raise SystemExit(f'V1.34 English function anchor count is {text.count(EN_START)}; refusing unknown baseline.')
    if text.count(AR_START) != 1:
        raise SystemExit(f'V1.34 Arabic function anchor count is {text.count(AR_START)}; refusing unknown baseline.')
    if text.count(AR_END) != 1:
        raise SystemExit(f'V1.34 Arabic end anchor count is {text.count(AR_END)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = insert_before_return(text, EN_START, AR_START, EN_FINAL, 'V1.34 English finalizer')
    text = insert_before_return(text, AR_START, AR_END, AR_FINAL, 'V1.34 Arabic finalizer')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.34 Tenant Details EN provisioning static closure runtime.')

if __name__ == '__main__':
    main()
