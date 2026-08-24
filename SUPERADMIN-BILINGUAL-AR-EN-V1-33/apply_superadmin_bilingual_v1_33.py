#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_33_COMPANIES_EN_RETRY_AUDIT_EN_OPTIONS_CLOSURE'
V132_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_32_GITHUB_SYNC_AR_REMAINING_STATIC_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V132";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_33_COMPANIES_EN_RETRY_AUDIT_EN_OPTIONS_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V133";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V132';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V133';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v132.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v133.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V132';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V133';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v132', '?v=superadmin-bilingual-v133', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v132"', 'data-sa-bilingual-runtime="v133"', 'runtime asset marker', 1),
]

EN_START = "  const v122EnglishPatterns=(value)=>{"
AR_START = "  const v122ArabicPatterns=(value)=>{"
AR_END = "  const v121PhraseArToEn="
RETURN_ANCHOR = "    return out;\n  };"

EN_FINAL = r'''    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_33_COMPANIES_EN_RETRY_AUDIT_EN_OPTIONS_CLOSURE
    // V1.32 evidence: page-scoped closure for ordinary static action/filter labels.
    // Operational/domain data such as provisioning status values remains untouched.
    if(typeof location!=='undefined' && location.hash==='#tenants'){
      const v133TenantsEnFinal=new Map([
        ["إعادة التجهيز","Retry provisioning"]
      ]);
      if(v133TenantsEnFinal.has(out))out=v133TenantsEnFinal.get(out);
    }
    if(typeof location!=='undefined' && location.hash==='#audit'){
      const v133AuditEnFinal=new Map([
        ["كل الأحداث","All events"],
        ["مدفوعات","Payments"],
        ["فواتير","Invoices"],
        ["Login كأدمن","Admin login"],
        ["دخول كأدمن","Admin login"],
        ["خطر","Risk"]
      ]);
      if(v133AuditEnFinal.has(out))out=v133AuditEnFinal.get(out);
    }
'''

AR_FINAL = r'''    // V1.33 reverse canonicalization for Companies/Audit Arabic gates.
    if(typeof location!=='undefined' && location.hash==='#tenants'){
      const v133TenantsArFinal=new Map([
        ["Retry provisioning","إعادة التجهيز"]
      ]);
      if(v133TenantsArFinal.has(out))out=v133TenantsArFinal.get(out);
    }
    if(typeof location!=='undefined' && location.hash==='#audit'){
      const v133AuditArFinal=new Map([
        ["All events","كل الأحداث"],
        ["Payments","مدفوعات"],
        ["Invoices","فواتير"],
        ["Admin login","دخول كأدمن"],
        ["Risk","خطر"]
      ]);
      if(v133AuditArFinal.has(out))out=v133AuditArFinal.get(out);
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
        print('Super Admin bilingual V1.33 Companies EN retry + Audit EN options closure already applied; no changes made.')
        return
    if V132_MARKER not in text:
        raise SystemExit('Bilingual V1.32 GitHub Sync AR remaining static closure marker not found; apply V1.32 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_START) != 1:
        raise SystemExit(f'V1.33 English function anchor count is {text.count(EN_START)}; refusing unknown baseline.')
    if text.count(AR_START) != 1:
        raise SystemExit(f'V1.33 Arabic function anchor count is {text.count(AR_START)}; refusing unknown baseline.')
    if text.count(AR_END) != 1:
        raise SystemExit(f'V1.33 Arabic end anchor count is {text.count(AR_END)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = insert_before_return(text, EN_START, AR_START, EN_FINAL, 'V1.33 English finalizer')
    text = insert_before_return(text, AR_START, AR_END, AR_FINAL, 'V1.33 Arabic finalizer')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.33 Companies EN retry + Audit EN options closure runtime.')

if __name__ == '__main__':
    main()
