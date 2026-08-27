#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_57_COMMERCIAL_FULL_STATIC_DYNAMIC_CLOSURE'
V156_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_56_EVOLUTION_CREDENTIALS_STATUS_LABELS_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V156";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_57_COMMERCIAL_FULL_STATIC_DYNAMIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V157";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V156';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V157';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v156.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v157.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V156';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V157';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v156', '?v=superadmin-bilingual-v157', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v156"', 'data-sa-bilingual-runtime="v157"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

REPLACEMENT = r"""      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_57_COMMERCIAL_FULL_STATIC_DYNAMIC_CLOSURE
      // Full page-scoped closure for Commercial Operations. Only ordinary UI copy is
      // canonicalized; company/plan/add-on names, invoices, ids, dates, statuses,
      // metrics, prices and other runtime/domain values remain untouched.
      if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
        const commercialRoot=document.querySelector('#commercialView');
        if(commercialRoot){
          const commercialPairs=[
            ['Commercial Operations','التشغيل التجاري'],
            ['Operations, Subscriptions & Billing','التشغيل والاشتراكات والفوترة'],
            ['Track rollout, usage, subscription lifecycle, and billing with actionable indicators.','متابعة التفعيل والاستهلاك ودورة الاشتراك والفواتير بمؤشرات قابلة للتنفيذ.'],
            ['Operations Center','مركز التشغيل'],
            ['Commercial Operations Dashboard','لوحة التشغيل التجاري'],
            ['Controlled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout','فرض مُتحكم به · الاستخدام · دورة الاشتراك · الفوترة · الخدمة الذاتية · التفعيل التدريجي'],
            ['Run Reconcile Now','تشغيل Reconcile الآن'],
            ['Refresh','تحديث'],
            ['Global Safety Controls','مفاتيح الأمان العامة'],
            ['Any enablement requires explicit confirmation. Kill Switch returns all companies to shadow.','أي تفعيل يحتاج تأكيدًا صريحًا. Kill Switch يعيد كل الشركات إلى shadow.'],
            ['Enable Enforcement','تفعيل Enforcement'],
            ['Subscription Lifecycle Automation','دورة الاشتراك الآلية'],
            ['Automatic Invoice Generation','إنشاء الفواتير آليًا'],
            ['Customer Portal','بوابة العميل'],
            ['Emergency Stop (Kill Switch)','مفتاح الإيقاف الطارئ (Kill Switch)'],
            ['Canary %','نسبة Canary %'],
            ['Currency','العملة'],
            ['Grace Days','أيام السماح'],
            ['Save Safety Settings','حفظ إعدادات الأمان'],
            ['Companies & Subscriptions','الشركات والاشتراكات'],
            ['Select a company to manage subscription, rollout, and usage.','اختر شركة لإدارة الاشتراك والتفعيل والاستهلاك.'],
            ['Search','بحث'],
            ['Company or plan','الشركة أو الباقة'],
            ['No data.','لا توجد بيانات.'],
            ['No results.','لا توجد نتائج.'],
            ['Select a company','اختر شركة'],
            ['Full commercial and operational details.','التفاصيل التجارية والتشغيلية الكاملة.'],
            ['Select a company from the list.','اختر شركة من القائمة.'],
            ['Subscription','الاشتراك'],
            ['Plan','الباقة'],
            ['Status','الحالة'],
            ['Cycle','الدورة'],
            ['Period Start','بداية الفترة'],
            ['Period End','نهاية الفترة'],
            ['Trial End','نهاية التجربة'],
            ['Grace End','نهاية السماح'],
            ['Auto Renew','تجديد تلقائي'],
            ['Save Subscription','حفظ الاشتراك'],
            ['Rollout & Rollback','التفعيل التدريجي والرجوع'],
            ['Stage','المرحلة'],
            ['Target Mode','الوضع المستهدف'],
            ['Health','الصحة'],
            ['Batch','الدفعة (Batch)'],
            ['Rollback Reason','سبب Rollback'],
            ['Required for rollback','إلزامي عند الرجوع'],
            ['Apply Stage','تطبيق المرحلة'],
            ['Roll back to shadow','الرجوع إلى shadow'],
            ['Usage & Alerts','الاستهلاك والتنبيهات'],
            ['Acknowledge','إقرار'],
            ['No alerts.','لا توجد تنبيهات.'],
            ['Invoices & Payments','الفواتير والمدفوعات'],
            ['Due Days','مهلة الاستحقاق'],
            ['Discount (minor units)','خصم بوحدة Minor'],
            ['Tax (minor units)','ضريبة بوحدة Minor'],
            ['Generate Invoice','إنشاء فاتورة'],
            ['Mark Paid','تسجيل مدفوعة'],
            ['No invoices.','لا توجد فواتير.'],
            ['Add-ons','الإضافات'],
            ['Save Add-ons','حفظ الإضافات'],
            ['No published add-ons.','لا توجد إضافات منشورة.'],
            ['Customer Requests','طلبات العميل'],
            ['Approve','موافقة'],
            ['Reject','رفض'],
            ['No requests.','لا توجد طلبات.'],
            ['Plan Pricing','تسعير الباقات'],
            ['Values are in minor currency units such as fils/cents.','القيم بوحدة Minor مثل الفلس/السنت.'],
            ['Price (minor units)','السعر بوحدة Minor'],
            ['Setup Fee (minor units)','رسوم التأسيس بوحدة Minor'],
            ['Price Active','السعر نشط'],
            ['Save Price','حفظ السعر'],
            ['Add-on Catalog','كتالوج الإضافات'],
            ['Features and limits as documented JSON.','الخصائص والحدود بصيغة JSON موثقة.'],
            ['Arabic Name','الاسم العربي'],
            ['English Name','الاسم الإنجليزي'],
            ['Feature Overrides JSON','استثناءات الخصائص JSON'],
            ['Limit Overrides JSON','استثناءات الحدود JSON'],
            ['Save Add-on','حفظ الإضافة'],
            ['No add-ons.','لا توجد إضافات.'],
            ['Active Subscriptions','اشتراكات نشطة'],
            ['At-risk Subscriptions','اشتراكات معرضة'],
            ['Overdue Invoices','فواتير متأخرة'],
            ['Total Open Invoices','إجمالي الفواتير المفتوحة'],
            ['Enabled Companies','شركات مفعلة'],
            ['Usage Alerts','تنبيهات استخدام'],
            ['Pending Requests','طلبات معلقة'],
            ['Ready for rollout','جاهز للتفعيل'],
            ['Loading subscription data…','جاري تحميل بيانات الاشتراك…'],
            ['Company data loaded','تم تحميل بيانات الشركة']
          ];
          const commercialMap=new Map();
          for(const pair of commercialPairs){
            commercialMap.set(pair[0],[pair[0],pair[1]]);
            commercialMap.set(pair[1],[pair[0],pair[1]]);
          }
          const commercialAliases=new Map([
            ['متابعة التفعيل والاستهلاك ودورة الاشتراك وBilling بمؤشرات قابلة للتنفيذ.',commercialPairs[2]],
            ['متابعة التفعيل والاستهلاك ودورة الاشتراك وInvoices بمؤشرات قابلة للتنفيذ.',commercialPairs[2]],
            ['Operations والاشتراكات والفوترة',commercialPairs[1]],
            ['الشركات وSubscriptions',commercialPairs[19]],
            ['Save إعدادات الأمان',commercialPairs[18]],
            ['Save الاشتراك',commercialPairs[37]],
            ['Rollback إلى shadow',commercialPairs[46]],
            ['Save الإضافات',commercialPairs[58]],
            ['Save السعر',commercialPairs[69]],
            ['Features وLimits بصيغة JSON موثقة.',commercialPairs[71]],
            ['Save الإضافة',commercialPairs[76]]
          ]);
          const canonicalCommercial=(raw)=>{
            const key=String(raw||'').trim().replace(/\s+/g,' ');
            const pair=commercialMap.get(key)||commercialAliases.get(key);
            if(!pair)return null;
            return root.lang==='ar'?pair[1]:pair[0];
          };
          const commercialWalker=document.createTreeWalker(commercialRoot,NodeFilter.SHOW_TEXT);
          let commercialNode=commercialWalker.nextNode();
          while(commercialNode){
            const parent=commercialNode.parentElement;
            if(parent&&!/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(parent.tagName)){
              const cur=commercialNode.nodeValue||'',trimmed=cur.trim(),next=canonicalCommercial(trimmed);
              if(next&&next!==trimmed){
                const lead=(cur.match(/^\s*/)||[''])[0],trail=(cur.match(/\s*$/)||[''])[0];
                commercialNode.nodeValue=lead+next+trail;
              }
            }
            commercialNode=commercialWalker.nextNode();
          }
          commercialRoot.querySelectorAll('[placeholder],[title],[aria-label]').forEach((el)=>{
            ['placeholder','title','aria-label'].forEach((name)=>{
              if(!el.hasAttribute(name))return;
              const cur=el.getAttribute(name)||'',next=canonicalCommercial(cur);
              if(next&&next!==cur.trim())el.setAttribute(name,next);
            });
          });

          // Force the primary intro by selector so it remains canonical even if an
          // earlier generic sweep partially translated a fragment before this finalizer.
          const force=(sel,en,ar)=>{
            const el=document.querySelector(sel);
            if(el instanceof HTMLElement)el.textContent=(root.lang==='ar'?ar:en);
          };
          force('#commercialView .commercialIntro .viewEyebrow','Commercial Operations','التشغيل التجاري');
          force('#commercialView .commercialIntro h2','Operations, Subscriptions & Billing','التشغيل والاشتراكات والفوترة');
          force('#commercialView .commercialIntro p','Track rollout, usage, subscription lifecycle, and billing with actionable indicators.','متابعة التفعيل والاستهلاك ودورة الاشتراك والفواتير بمؤشرات قابلة للتنفيذ.');
          force('#commercialView .commercialIntro .viewIntroBadge','Operations Center','مركز التشغيل');
          force('#commercialTab .tabText b','Operations, Subscriptions & Billing','التشغيل والاشتراكات والفوترة');
          force('#commercialTab .tabText small','Rollout, usage & collections','التفعيل والاستهلاك والتحصيل');

          const search=document.querySelector('#commercialTenantSearch');
          if(search){
            const p=root.lang==='ar'?'الشركة أو الباقة':'Company or plan';
            if(search.getAttribute('placeholder')!==p)search.setAttribute('placeholder',p);
          }
          const rollbackReason=document.querySelector('#rollbackReason');
          if(rollbackReason){
            const p=root.lang==='ar'?'إلزامي عند الرجوع':'Required for rollback';
            if(rollbackReason.getAttribute('placeholder')!==p)rollbackReason.setAttribute('placeholder',p);
          }

          const readiness=document.querySelector('#rolloutReadiness');
          if(readiness instanceof HTMLElement){
            const raw=(readiness.textContent||'').trim();
            if(raw==='جاهز للتفعيل'||raw==='Ready for rollout'){
              readiness.textContent=(root.lang==='ar'?'جاهز للتفعيل':'Ready for rollout');
            }else{
              let m=raw.match(/^غير جاهز:\s*(.*)$/);
              if(!m)m=raw.match(/^Not ready:\s*(.*)$/);
              if(m)readiness.textContent=(root.lang==='ar'?'غير جاهز: ':'Not ready: ')+m[1];
            }
          }

          if(!commercialRoot.classList.contains('hidden')){
            const statusEl=document.querySelector('#status');
            if(statusEl instanceof HTMLElement){
              const raw=(statusEl.textContent||'').trim();
              const statusPairs=[
                ['Loading subscription data…','جاري تحميل بيانات الاشتراك…'],
                ['Company data loaded','تم تحميل بيانات الشركة']
              ];
              for(const pair of statusPairs){
                if(raw===pair[0]||raw===pair[1]){
                  statusEl.textContent=(root.lang==='ar'?pair[1]:pair[0]);
                  break;
                }
              }
            }
          }
        }
      }
      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.57 Commercial full static/dynamic closure already applied; no changes made.')
        return
    if V156_MARKER not in text:
        raise SystemExit('Bilingual V1.56 Evolution credentials/status labels closure marker not found; apply V1.56 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(ANCHOR)
    if count != 1:
        raise SystemExit(f'V1.57 Plans document-title anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.57 Commercial full static/dynamic closure.')

if __name__ == '__main__':
    main()
