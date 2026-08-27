#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_59_COMMERCIAL_SAFETY_CONTROLS_HARD_CLOSURE'
V158_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_58_COMMERCIAL_KPI_SUMMARY_HARD_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V158";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_59_COMMERCIAL_SAFETY_CONTROLS_HARD_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V159";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V158';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V159';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v158.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v159.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V158';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V159';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v158', '?v=superadmin-bilingual-v159', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v158"', 'data-sa-bilingual-runtime="v159"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

REPLACEMENT = r"""      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_59_COMMERCIAL_SAFETY_CONTROLS_HARD_CLOSURE
      // V1.58 evidence proved the generic sweep can partially translate fragments inside
      // the Global Safety Controls helper before the Commercial exact-text canonicalizer
      // sees it ("All companies"). Hard-canonicalize this fixed static card by selector,
      // while preserving all form controls and their runtime values.
      if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
        const safetyGrid=document.querySelector('#commercialView .settingsGrid');
        const safetyCard=safetyGrid?safetyGrid.closest('.card'):null;
        if(safetyCard instanceof HTMLElement){
          const setText=(sel,en,ar)=>{
            const el=safetyCard.querySelector(sel);
            if(el instanceof HTMLElement)el.textContent=(root.lang==='ar'?ar:en);
          };
          const setFieldLabel=(inputSelector,en,ar)=>{
            const input=safetyCard.querySelector(inputSelector);
            const field=input?input.closest('.field'):null;
            const label=field?field.querySelector('label'):null;
            if(label instanceof HTMLElement)label.textContent=(root.lang==='ar'?ar:en);
          };
          const setCheckLabel=(inputSelector,en,ar)=>{
            const input=safetyCard.querySelector(inputSelector);
            const label=input?input.closest('label'):null;
            if(!(label instanceof HTMLElement))return;
            const wanted=(root.lang==='ar'?ar:en);
            let textNode=null;
            for(const node of label.childNodes){
              if(node.nodeType===Node.TEXT_NODE && String(node.nodeValue||'').trim()){
                textNode=node;
                break;
              }
            }
            if(textNode)textNode.nodeValue=' '+wanted;
            else label.appendChild(document.createTextNode(' '+wanted));
          };

          setText('.cardHead h2','Global Safety Controls','مفاتيح الأمان العامة');
          setText('.cardHead p','Any enablement requires explicit confirmation. Kill Switch returns all companies to shadow.','أي تفعيل يحتاج تأكيدًا صريحًا. Kill Switch يعيد كل الشركات إلى shadow.');

          setCheckLabel('#setEnforcement','Enable Enforcement','تفعيل Enforcement');
          setCheckLabel('#setLifecycle','Subscription Lifecycle Automation','دورة الاشتراك الآلية');
          setCheckLabel('#setBilling','Automatic Invoice Generation','إنشاء الفواتير آليًا');
          setCheckLabel('#setSelfService','Customer Portal','بوابة العميل');
          setCheckLabel('#setKillSwitch','Emergency Stop (Kill Switch)','مفتاح الإيقاف الطارئ (Kill Switch)');

          setFieldLabel('#setCanary','Canary %','نسبة Canary %');
          setFieldLabel('#setCurrency','Currency','العملة');
          setFieldLabel('#setGraceDays','Grace Days','أيام السماح');

          const save=safetyCard.querySelector('#saveCommercialSettingsBtn');
          if(save instanceof HTMLElement)save.textContent=(root.lang==='ar'?'حفظ إعدادات الأمان':'Save Safety Settings');
        }
      }
      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.59 Commercial safety controls hard closure already applied; no changes made.')
        return
    if V158_MARKER not in text:
        raise SystemExit('Bilingual V1.58 Commercial KPI summary hard closure marker not found; apply V1.58 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(ANCHOR)
    if count != 1:
        raise SystemExit(f'V1.59 Plans document-title anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.59 Commercial safety controls hard closure.')

if __name__ == '__main__':
    main()
