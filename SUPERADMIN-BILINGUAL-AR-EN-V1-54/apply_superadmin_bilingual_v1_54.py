#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_COMPANY_OVERRIDES_FULL_STATIC_DYNAMIC_CLOSURE'
V153_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_53_PLANS_LIMITS_HELPER_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V153";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_COMPANY_OVERRIDES_FULL_STATIC_DYNAMIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V154";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V153';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V154';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v153.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v154.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V153';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V154';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v153', '?v=superadmin-bilingual-v154', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v153"', 'data-sa-bilingual-runtime="v154"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

REPLACEMENT = r"""      // SUPER_ADMIN_BILINGUAL_AR_EN_V1_54_COMPANY_OVERRIDES_FULL_STATIC_DYNAMIC_CLOSURE
      // Full page-scoped closure for the Companies & Overrides workspace. Only canonical
      // ordinary UI copy is rewritten; tenant names, plan/domain values, ids, slugs,
      // counts, feature/limit catalog data and runtime values are intentionally untouched.
      if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
        const tenantsRoot=document.querySelector('#tenantsView');
        if(tenantsRoot){
          const tenantPairs=[
            ['Companies Management','إدارة الشركات'],
            ['Companies & Overrides','الشركات والاستثناءات'],
            ['Assign plans, configure limits and overrides, and review the effective result for each company.','تعيين الباقات وضبط الحدود والاستثناءات ومراجعة النتيجة الفعلية لكل شركة.'],
            ['Per-company control','تحكم لكل شركة'],
            ['Companies','الشركات'],
            ['The legacy plan is preserved and is not modified here.','الباقة القديمة محفوظة ولا يتم تعديلها هنا.'],
            ['Search','بحث'],
            ['Select a company','اختر شركة'],
            ['View the effective plan and the sources of features and limits.','عرض الباقة الفعلية ومصادر الخصائص والحدود.'],
            ['Select a company from the list.','اختر شركة من القائمة.'],
            ['Assignment & Runtime Mode','التعيين ووضع التشغيل'],
            ['Published Plan','الباقة المنشورة'],
            ['Requested Mode','الوضع المطلوب'],
            ['shadow — comparison only','shadow — مقارنة فقط'],
            ['prefer_registry — Registry with Legacy fallback','prefer_registry — Registry مع Legacy fallback'],
            ['registry_only — fail closed when incomplete','registry_only — إغلاق آمن عند النقص'],
            ['Assign Plan','تعيين الباقة'],
            ['Save Mode','حفظ الوضع'],
            ['WhatsApp Account Limit for Company','حد حسابات WhatsApp للشركة'],
            ['Accounts Used','الحسابات المستخدمة'],
            ['Limit Method','طريقة تحديد الحد'],
            ['From plan','من الباقة'],
            ['Custom number','عدد مخصص'],
            ['Unlimited','غير محدود'],
            ['Allowed number','العدد المسموح'],
            ['Choose a custom number or use the plan limit.','اختر عددًا مخصصًا أو استخدم حد الباقة.'],
            ['AI Assistant Identity','هوية المساعد الذكي'],
            ["Choose the name and image shown only to this company's employees.",'اختيار الاسم والصورة الظاهرين لموظفي هذه الشركة فقط.'],
            ['Visible Identity','الهوية الظاهرة'],
            ['Rakan — Saudi identity','راكان — الهوية السعودية'],
            ['Wadie — Egyptian identity','وديع — الهوية المصرية'],
            ['The internal system and API name remains Rakan.','يظل الاسم الداخلي في النظام وواجهات API هو Rakan.'],
            ['Save Assistant Identity','حفظ هوية المساعد'],
            ['Company AI Assistant','مساعد الشركة الذكي'],
            ['Company Overrides','استثناءات الشركة'],
            ['Leave the selection on “From plan” to remove the override.','اترك الاختيار على “من الباقة” لإزالة الاستثناء.'],
            ['Change reason — required when saving','سبب التعديل — إلزامي عند الحفظ'],
            ['Save All Overrides','حفظ الاستثناءات كاملة'],
            ['Preview from saved configuration','المعاينة حسب الإعداد المحفوظ'],
            ['Current effective result','النتيجة الفعلية الحالية'],
            ['No results.','لا توجد نتائج.'],
            ['Unassigned','بدون تعيين'],
            ['Enabled','مفعلة'],
            ['Disabled','مقفولة'],
            ['Value','قيمة'],
            ['Mode','الوضع'],
            ['Plan','الباقة'],
            ['Uses Registry','يستخدم Registry'],
            ['Yes','نعم'],
            ['No','لا'],
            ['Users','المستخدمون'],
            ['WhatsApp Accounts','حسابات WhatsApp'],
            ['Differences','اختلافات'],
            ['Unavailable','غير متاح'],
            ['Registry Runtime enabled','Registry Runtime مفعل'],
            ['Runtime on shadow','Runtime على shadow'],
            ['Assistant identity is saved for this company. The internal name and APIs are unchanged.','الهوية محفوظة لهذه الشركة. الاسم الداخلي وواجهات API لم تتغير.'],
            ['This company uses Rakan by default until another identity is selected.','تستخدم الشركة راكان افتراضيًا حتى اختيار هوية أخرى.'],
            ['The assistant identity migration must be applied before saving.','يلزم تطبيق Migration هوية المساعد قبل الحفظ.']
          ];
          const tenantMap=new Map();
          for(const [en,ar] of tenantPairs){tenantMap.set(en,[en,ar]);tenantMap.set(ar,[en,ar]);}
          const tenantAliases=new Map([
            ['تعيين الباقات وضبط الحدود والاستثناءات وReview النتيجة الفعلية لكل شركة.',tenantPairs[2]],
            ['تعيين الباقات وضبط الحدود والاستثناءات و Review النتيجة الفعلية لكل شركة.',tenantPairs[2]],
            ['عرض الباقة الفعلية ومصادر Features والحدود.',tenantPairs[8]],
            ['The internal system and APIs name remains Rakan.',tenantPairs[30]]
          ]);
          const canonicalTenant=(raw)=>{
            const key=String(raw||'').trim().replace(/\s+/g,' ');
            const pair=tenantMap.get(key)||tenantAliases.get(key);
            if(!pair)return null;
            return root.lang==='ar'?pair[1]:pair[0];
          };
          const tenantWalker=document.createTreeWalker(tenantsRoot,NodeFilter.SHOW_TEXT);
          let tenantNode=tenantWalker.nextNode();
          while(tenantNode){
            const parent=tenantNode.parentElement;
            if(parent&&!/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(parent.tagName)){
              const cur=tenantNode.nodeValue||'',trimmed=cur.trim(),next=canonicalTenant(trimmed);
              if(next&&next!==trimmed){
                const lead=(cur.match(/^\s*/)||[''])[0],trail=(cur.match(/\s*$/)||[''])[0];
                tenantNode.nodeValue=lead+next+trail;
              }
            }
            tenantNode=tenantWalker.nextNode();
          }
          tenantsRoot.querySelectorAll('[placeholder],[title],[aria-label]').forEach((el)=>{
            ['placeholder','title','aria-label'].forEach((name)=>{
              if(!el.hasAttribute(name))return;
              const cur=el.getAttribute(name)||'',next=canonicalTenant(cur);
              if(next&&next!==cur.trim())el.setAttribute(name,next);
            });
          });
          const tenantSearch=document.querySelector('#tenantSearch');
          if(tenantSearch){
            const p=root.lang==='ar'?'الشركة أو البريد':'Company or email';
            if(tenantSearch.getAttribute('placeholder')!==p)tenantSearch.setAttribute('placeholder',p);
          }
          const overrideReason=document.querySelector('#overrideReason');
          if(overrideReason){
            const p=root.lang==='ar'?'مثال: اتفاق تجاري مؤقت':'Example: temporary commercial agreement';
            if(overrideReason.getAttribute('placeholder')!==p)overrideReason.setAttribute('placeholder',p);
          }

          const dynText=(sel,en,ar)=>{
            const el=document.querySelector(sel);if(!(el instanceof HTMLElement))return;
            const raw=(el.textContent||'').trim();
            if(raw===en||raw===ar)el.textContent=(root.lang==='ar'?ar:en);
          };
          dynText('#runtimeBadge','Registry Runtime enabled','Registry Runtime مفعل');
          dynText('#runtimeBadge','Runtime on shadow','Runtime على shadow');
          dynText('#rakanIdentityHint','Assistant identity is saved for this company. The internal name and APIs are unchanged.','الهوية محفوظة لهذه الشركة. الاسم الداخلي وواجهات API لم تتغير.');
          dynText('#rakanIdentityHint','This company uses Rakan by default until another identity is selected.','تستخدم الشركة راكان افتراضيًا حتى اختيار هوية أخرى.');
          dynText('#rakanIdentityHint','The assistant identity migration must be applied before saving.','يلزم تطبيق Migration هوية المساعد قبل الحفظ.');

          const legacy=document.querySelector('#legacyPlanLabel');
          if(legacy instanceof HTMLElement){
            const raw=(legacy.textContent||'').trim();
            let m=raw.match(/^Legacy محفوظ:\s*(.*)$/);if(!m)m=raw.match(/^Legacy saved:\s*(.*)$/);
            if(m)legacy.textContent=(root.lang==='ar'?'Legacy محفوظ: ':'Legacy saved: ')+m[1];
          }
          const source=document.querySelector('#whatsappAccountsSource');
          if(source instanceof HTMLElement){
            const raw=(source.textContent||'').trim();
            let m=raw.match(/^المصدر:\s*(.*)$/);if(!m)m=raw.match(/^Source:\s*(.*)$/);
            if(m)source.textContent=(root.lang==='ar'?'المصدر: ':'Source: ')+m[1];
          }
          const waHint=document.querySelector('#whatsappAccountsHint');
          if(waHint instanceof HTMLElement){
            const raw=(waHint.textContent||'').trim();
            let m=raw.match(/^المستخدم\s+(.+?)\s+من\s+(.+?)\s+·\s+الحد مطبق فعليًا$/);
            if(!m)m=raw.match(/^Used\s+(.+?)\s+of\s+(.+?)\s+·\s+limit is actively enforced$/);
            if(m)waHint.textContent=root.lang==='ar'?`المستخدم ${m[1]} من ${m[2]} · الحد مطبق فعليًا`:`Used ${m[1]} of ${m[2]} · limit is actively enforced`;
            else{
              m=raw.match(/^المستخدم\s+(.+?)\s+من\s+(.+?)\s+·\s+محفوظ، لكن التطبيق الفعلي يحتاج Registry Runtime ووضع شركة غير shadow$/);
              if(!m)m=raw.match(/^Used\s+(.+?)\s+of\s+(.+?)\s+·\s+saved, but enforcement requires Registry Runtime and a non-shadow company mode$/);
              if(m)waHint.textContent=root.lang==='ar'?`المستخدم ${m[1]} من ${m[2]} · محفوظ، لكن التطبيق الفعلي يحتاج Registry Runtime ووضع شركة غير shadow`:`Used ${m[1]} of ${m[2]} · saved, but enforcement requires Registry Runtime and a non-shadow company mode`;
            }
          }

          if(!tenantsRoot.classList.contains('hidden')){
            const statusEl=document.querySelector('#status');
            if(statusEl instanceof HTMLElement){
              const raw=(statusEl.textContent||'').trim();
              const statusPairs=[
                ['Loading company…','جاري تحميل الشركة…'],
                ['Company loaded','تم تحميل الشركة'],
                ['Company data loaded','تم تحميل بيانات الشركة']
              ];
              for(const [en,ar] of statusPairs){
                if(raw===en||raw===ar){statusEl.textContent=(root.lang==='ar'?ar:en);break;}
              }
            }
          }
        }
      }
      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.54 Company Overrides full static/dynamic closure already applied; no changes made.')
        return
    if V153_MARKER not in text:
        raise SystemExit('Bilingual V1.53 Plans Limits helper marker not found; apply V1.53 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    count = text.count(ANCHOR)
    if count != 1:
        raise SystemExit(f'V1.54 Plans document-title anchor count is {count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.54 Company Overrides full static/dynamic closure.')

if __name__ == '__main__':
    main()
