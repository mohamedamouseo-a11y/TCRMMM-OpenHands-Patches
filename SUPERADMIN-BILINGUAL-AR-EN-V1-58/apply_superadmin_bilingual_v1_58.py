#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_58_COMMERCIAL_KPI_SUMMARY_HARD_CLOSURE'
V157_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_57_COMMERCIAL_FULL_STATIC_DYNAMIC_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V157";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_58_COMMERCIAL_KPI_SUMMARY_HARD_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V158";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V157';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V158';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v157.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v158.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V157';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V158';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v157', '?v=superadmin-bilingual-v158', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v157"', 'data-sa-bilingual-runtime="v158"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

REPLACEMENT = r"""      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_58_COMMERCIAL_KPI_SUMMARY_HARD_CLOSURE
      // V1.57 evidence proved the generic sweep can partially translate one Arabic KPI
      // token before the Commercial canonicalizer sees the whole label ("طلبات Pending").
      // The Commercial summary has a fixed eight-label static schema, while the sibling
      // <b> values are runtime/domain data. Canonicalize only the label spans by position.
      if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
        const commercialSummary=document.querySelector('#commercialView #commercialSummary');
        if(commercialSummary){
          const commercialKpiPairs=[
            ['Active Subscriptions','اشتراكات نشطة'],
            ['At-risk Subscriptions','اشتراكات معرضة'],
            ['Overdue Invoices','فواتير متأخرة'],
            ['Total Open Invoices','إجمالي الفواتير المفتوحة'],
            ['Enabled Companies','شركات مفعلة'],
            ['Usage Alerts','تنبيهات استخدام'],
            ['Pending Requests','طلبات معلقة'],
            ['Kill Switch','مفتاح الإيقاف']
          ];
          const labels=commercialSummary.querySelectorAll('.summaryCard > span:first-child');
          if(labels.length>=commercialKpiPairs.length){
            commercialKpiPairs.forEach((pair,index)=>{
              const el=labels[index];
              if(el)el.textContent=(root.lang==='ar'?pair[1]:pair[0]);
            });
          }
        }
      }
      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.58 Commercial KPI summary hard closure already applied; no changes made.')
        return
    if V157_MARKER not in text:
        raise SystemExit('Bilingual V1.57 Commercial full static/dynamic closure marker not found; apply V1.57 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(ANCHOR)
    if count != 1:
        raise SystemExit(f'V1.58 Plans document-title anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.58 Commercial KPI summary hard closure.')

if __name__ == '__main__':
    main()
