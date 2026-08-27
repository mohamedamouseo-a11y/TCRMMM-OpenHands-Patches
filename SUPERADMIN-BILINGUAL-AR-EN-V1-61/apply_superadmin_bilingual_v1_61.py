#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_61_COMMERCIAL_MONETIZATION_FORMS_HARD_CLOSURE'
V160_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_60_COMMERCIAL_TENANT_EDITOR_STATIC_HEADER_HARD_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V160";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_61_COMMERCIAL_MONETIZATION_FORMS_HARD_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V161";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V160';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V161';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v160.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v161.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V160';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V161';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v160', '?v=superadmin-bilingual-v161', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v160"', 'data-sa-bilingual-runtime="v161"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

REPLACEMENT = r"""      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_61_COMMERCIAL_MONETIZATION_FORMS_HARD_CLOSURE
      // V1.60 evidence found a partially translated fixed label in Plan Pricing
      // ("السعر Minor"). Hard-canonicalize the fixed Plan Pricing and Add-on
      // Catalog form copy by selector. Inputs, selected options and all monetary,
      // plan, add-on and runtime/domain values are intentionally untouched.
      if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
        const commercialRoot=document.querySelector('#commercialView');
        if(commercialRoot){
          const setText=(rootEl,sel,en,ar)=>{
            const el=rootEl.querySelector(sel);
            if(el instanceof HTMLElement)el.textContent=(root.lang==='ar'?ar:en);
          };
          const setFieldLabel=(rootEl,inputSelector,en,ar)=>{
            const input=rootEl.querySelector(inputSelector);
            const field=input?input.closest('.field'):null;
            const label=field?field.querySelector('label'):null;
            if(label instanceof HTMLElement)label.textContent=(root.lang==='ar'?ar:en);
          };
          const setCheckLabel=(rootEl,inputSelector,en,ar)=>{
            const input=rootEl.querySelector(inputSelector);
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

          const priceInput=commercialRoot.querySelector('#priceAmount');
          const priceCard=priceInput?priceInput.closest('.card'):null;
          if(priceCard instanceof HTMLElement){
            setText(priceCard,'.cardHead h2','Plan Pricing','تسعير الباقات');
            setText(priceCard,'.cardHead p','Values are in minor currency units such as fils/cents.','القيم بوحدة Minor مثل الفلس/السنت.');
            setFieldLabel(priceCard,'#pricePlan','Plan','الباقة');
            setFieldLabel(priceCard,'#priceCycle','Cycle','الدورة');
            setFieldLabel(priceCard,'#priceCurrency','Currency','العملة');
            setFieldLabel(priceCard,'#priceAmount','Price (minor units)','السعر بوحدة Minor');
            setFieldLabel(priceCard,'#priceSetup','Setup Fee (minor units)','رسوم التأسيس بوحدة Minor');
            setCheckLabel(priceCard,'#priceActive','Price Active','السعر نشط');
            const savePrice=priceCard.querySelector('#savePriceBtn');
            if(savePrice instanceof HTMLElement)savePrice.textContent=(root.lang==='ar'?'حفظ السعر':'Save Price');
          }

          const addonInput=commercialRoot.querySelector('#addonFeatures');
          const addonCard=addonInput?addonInput.closest('.card'):null;
          if(addonCard instanceof HTMLElement){
            setText(addonCard,'.cardHead h2','Add-on Catalog','كتالوج الإضافات');
            setText(addonCard,'.cardHead p','Features and limits as documented JSON.','الخصائص والحدود بصيغة JSON موثقة.');
            setFieldLabel(addonCard,'#addonSlug','Slug','المعرّف (Slug)');
            setFieldLabel(addonCard,'#addonStatus','Status','الحالة');
            setFieldLabel(addonCard,'#addonNameAr','Arabic Name','الاسم العربي');
            setFieldLabel(addonCard,'#addonNameEn','English Name','الاسم الإنجليزي');
            setFieldLabel(addonCard,'#addonCycle','Cycle','الدورة');
            setFieldLabel(addonCard,'#addonCurrency','Currency','العملة');
            setFieldLabel(addonCard,'#addonAmount','Price (minor units)','السعر بوحدة Minor');
            setFieldLabel(addonCard,'#addonFeatures','Feature Overrides JSON','استثناءات الخصائص JSON');
            setFieldLabel(addonCard,'#addonLimits','Limit Overrides JSON','استثناءات الحدود JSON');
            const saveAddon=addonCard.querySelector('#saveAddonBtn');
            if(saveAddon instanceof HTMLElement)saveAddon.textContent=(root.lang==='ar'?'حفظ الإضافة':'Save Add-on');
          }
        }
      }
      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.61 Commercial monetization forms hard closure already applied; no changes made.')
        return
    if V160_MARKER not in text:
        raise SystemExit('Bilingual V1.60 Commercial tenant editor static header hard closure marker not found; apply V1.60 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(ANCHOR)
    if count != 1:
        raise SystemExit(f'V1.61 Plans document-title anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.61 Commercial monetization forms hard closure.')

if __name__ == '__main__':
    main()
