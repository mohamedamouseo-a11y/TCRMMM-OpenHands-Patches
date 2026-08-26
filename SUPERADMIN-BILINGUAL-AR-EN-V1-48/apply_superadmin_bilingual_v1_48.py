#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_48_PLANS_CATALOG_EDITOR_FULL_STATIC_CLOSURE'
V147_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_47_TARA_APIS_FULL_STATIC_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V147";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_48_PLANS_CATALOG_EDITOR_FULL_STATIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V148";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V147';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V148';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v147.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v148.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V147';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V148';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v147', '?v=superadmin-bilingual-v148', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v147"', 'data-sa-bilingual-runtime="v148"', 'runtime asset marker', 1),
]

ANCHOR = """      document.title=(root.lang==='ar'?'تكاملات تارا · إدارة المنصة':'Tara Integrations · Platform Administration');
    }
  };"""

REPLACEMENT = r"""      document.title=(root.lang==='ar'?'تكاملات تارا · إدارة المنصة':'Tara Integrations · Platform Administration');
    }

    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_48_PLANS_CATALOG_EDITOR_FULL_STATIC_CLOSURE
    // V1.47 Full Audit + source audit: close the visible Plans Catalog + Plan Editor surface.
    if(typeof location!=='undefined' && location.pathname==='/super-admin/plans'){
      const v148Pairs=[
        ['Plans & Limits Management','إدارة الباقات والحدود'],
        ['Manage versions, subscriptions, and usage limits','إدارة الإصدارات والاشتراكات وحدود الاستخدام'],
        ['Back to Command Center','العودة لمركز القيادة'],
        ['Refresh Data','تحديث البيانات'],
        ['Progressive rollout is enabled to protect companies','التشغيل التدريجي مفعّل لحماية الشركات'],
        ['Sensitive settings only take effect after explicit confirmation.','الإعدادات الحساسة لا تعمل إلا بعد تأكيد صريح.'],
        ['Show details','عرض التفاصيل'],
        ['Hide details','إخفاء التفاصيل'],
        ['Limits enforcement, automated billing, and subscription lifecycle are disabled by default. Emergency stop and instant rollback are available for every company when needed.','تطبيق القيود والفوترة الآلية ودورة الاشتراك متوقف افتراضيًا. يتوفر إيقاف طارئ ورجوع فوري لكل شركة عند الحاجة.'],
        ['Checking permissions and loading data…','جاري التحقق من الصلاحية وتحميل البيانات…'],
        ['Plans','الباقات'],
        ['Versions, features, and limits','الإصدارات والخصائص والحدود'],
        ['Companies & Overrides','الشركات والاستثناءات'],
        ['Assignment and per-company limits','التعيين وحدود كل شركة'],
        ['Operations, Subscriptions & Billing','التشغيل والاشتراكات والفوترة'],
        ['Activation, usage, and collection','التفعيل والاستهلاك والتحصيل'],
        ['Plans Management','إدارة الباقات'],
        ['Plans Catalog','كتالوج الباقات'],
        ['Manage versions, features, and limits from one clear workspace.','إدارة الإصدارات والخصائص والحدود من مساحة عمل واحدة واضحة.'],
        ['Version Management','إدارة الإصدارات'],
        ['Plan Versions','إصدارات الباقات'],
        ['Published, draft, and archived versions.','المنشورة والمسودات والإصدارات المؤرشفة.'],
        ['Search plans','بحث داخل الباقات'],
        ['No data available.','لا توجد بيانات.'],
        ['Select a plan','اختر باقة'],
        ['Only drafts can be edited.','يمكن تعديل المسودات فقط.'],
        ['Select a plan to view its details','اختر باقة لعرض تفاصيلها'],
        ['The first plan will open automatically when the page loads.','سيتم فتح أول باقة تلقائيًا عند تحميل الصفحة.'],
        ['Status','الحالة'],
        ['Version','الإصدار'],
        ['Companies','الشركات'],
        ['Arabic name','الاسم العربي'],
        ['English name','الاسم الإنجليزي'],
        ['New version identifier','معرّف النسخة الجديدة'],
        ['Version information','معلومة الإصدار'],
        ['Features','الخصائص'],
        ['Future features are locked and are not currently active.','الخصائص المستقبلية مقفولة ولا تعمل حاليًا.'],
        ['Limits','الحدود'],
        ['A draft may be saved incomplete, but publishing requires an explicit decision for every limit.','يمكن حفظ المسودة ناقصة، لكن النشر يتطلب قرارًا صريحًا لكل حد.'],
        ['Clone to draft','نسخ إلى مسودة'],
        ['Save draft','حفظ المسودة'],
        ['Publish version','نشر الإصدار'],
        ['Published','منشورة'],
        ['Draft','مسودة'],
        ['Archived','مؤرشفة'],
        ['Unlimited','غير محدود'],
        ['Not set','غير محدد'],
        ['Undefined','غير معرفة'],
        ['Value','قيمة'],
        ['No plans match your search.','لا توجد باقات مطابقة للبحث.'],
        ['Requires:','يتطلب:'],
        ['Future — cannot be enabled','مستقبلي — غير قابل للتفعيل'],
        ['Loading plan…','جاري تحميل الباقة…'],
        ['Plan loaded','تم تحميل الباقة'],
        ['Review dependencies, then save or publish.','راجع الاعتمادات ثم احفظ أو انشر.'],
        ['Published and archived versions are read-only; create a draft to edit.','الإصدارات المنشورة والمؤرشفة للقراءة فقط؛ أنشئ مسودة للتعديل.']
      ];
      const v148Map=new Map();
      for(const [en,ar] of v148Pairs)v148Map.set(root.lang==='ar'?en:ar,root.lang==='ar'?ar:en);
      // Earlier bilingual sweeps can partially translate embedded product tokens before
      // this standalone-page finalizer runs. Collapse observed mixed variants back to
      // their canonical Arabic source key before the exact final mapping.
      const v148Aliases=new Map([
        ['إدارة Plans & Limits','إدارة الباقات والحدود'],
        ['العودة لCommand Center','العودة لمركز القيادة'],
        ['إدارة Versions, features, and limits من مساحة عمل واحدة واضحة.','إدارة الإصدارات والخصائص والحدود من مساحة عمل واحدة واضحة.'],
        ['إدارة Versions, features, and limits من مساحة عمل واحدة واضحة','إدارة الإصدارات والخصائص والحدود من مساحة عمل واحدة واضحة.'],
        ['Versions, features, and limits','الإصدارات والخصائص والحدود'],
        ['Plans Catalog','كتالوج الباقات']
      ]);
      const v148CanonicalKey=(value)=>{
        const key=String(value||'').trim();
        return v148Aliases.get(key)||key;
      };

      const v148TranslateLeaf=(el)=>{
        if(!el || el.children.length)return;
        const key=v148CanonicalKey(el.textContent||'');
        const next=v148Map.get(key);
        if(next)el.textContent=next;
      };
      document.querySelectorAll('body *').forEach(v148TranslateLeaf);

      const v148Root=document.documentElement;
      if(v148Root){v148Root.lang=root.lang==='ar'?'ar':'en';v148Root.dir=root.lang==='ar'?'rtl':'ltr';}
      const v148Body=document.body;
      if(v148Body)v148Body.style.textAlign='';

      const v148Tabs=document.querySelector('.tabs');
      if(v148Tabs)v148Tabs.setAttribute('aria-label',root.lang==='ar'?'أقسام إدارة الباقات':'Plans management sections');
      const v148PlanSummary=document.querySelector('#planQuickSummary');
      if(v148PlanSummary)v148PlanSummary.setAttribute('aria-label',root.lang==='ar'?'ملخص الباقة':'Plan summary');
      const v148Search=document.querySelector('#planSearch');
      if(v148Search)v148Search.setAttribute('placeholder',root.lang==='ar'?'ابحث بالاسم أو المعرّف':'Search by name or identifier');

      const v148Stats=document.querySelector('#planListStats');
      if(v148Stats){
        const raw=(v148Stats.textContent||'').trim();
        if(root.lang==='en'){
          let m=raw.match(/^([0-9٠-٩]+)\s+(?:إصدار|versions?)\s+·\s+([0-9٠-٩]+)\s+(?:منشور|published)$/iu);
          if(m)v148Stats.textContent=m[1]+' versions · '+m[2]+' published';
        }else{
          let m=raw.match(/^([0-9٠-٩]+)\s+(?:versions?|إصدار)\s+·\s+([0-9٠-٩]+)\s+(?:published|منشور)$/iu);
          if(m)v148Stats.textContent=m[1]+' إصدار · '+m[2]+' منشور';
        }
      }

      document.querySelectorAll('.planItemMetrics').forEach((el)=>{
        for(const span of Array.from(el.querySelectorAll(':scope > span'))){
          const raw=(span.textContent||'').trim();
          if(root.lang==='en'){
            let m=raw.match(/^الإصدار\s+(.+)$/u); if(m){span.childNodes[0].nodeValue='Version ';continue;}
            m=raw.match(/^([0-9٠-٩]+)\s+شركة$/u); if(m)span.innerHTML='<strong>'+m[1]+'</strong> companies';
          }else{
            let m=raw.match(/^Version\s+(.+)$/iu); if(m){span.childNodes[0].nodeValue='الإصدار ';continue;}
            m=raw.match(/^([0-9٠-٩]+)\s+companies$/iu); if(m)span.innerHTML='<strong>'+m[1]+'</strong> شركة';
          }
        }
      });

      const v148EditorSub=document.querySelector('#planEditorSub');
      if(v148EditorSub){
        const raw=(v148EditorSub.textContent||'').trim();
        if(root.lang==='en'){
          const m=raw.match(/^المعرّف\s+(.+)\s+·\s+الإصدار\s+(.+)$/u);
          if(m)v148EditorSub.textContent='Identifier '+m[1]+' · Version '+m[2];
        }else{
          const m=raw.match(/^Identifier\s+(.+)\s+·\s+Version\s+(.+)$/iu);
          if(m)v148EditorSub.textContent='المعرّف '+m[1]+' · الإصدار '+m[2];
        }
      }

      const v148QuickTenants=document.querySelector('#planQuickTenants');
      if(v148QuickTenants){
        const raw=(v148QuickTenants.textContent||'').trim();
        if(root.lang==='en'){
          const m=raw.match(/^([0-9٠-٩]+)\s+(?:شركة|companies?)$/iu); if(m)v148QuickTenants.textContent=m[1]+' companies';
        }else{
          const m=raw.match(/^([0-9٠-٩]+)\s+(?:companies?|شركة)$/iu); if(m)v148QuickTenants.textContent=m[1]+' شركة';
        }
      }

      document.querySelectorAll('#planFeatures .featureRow p').forEach((el)=>{
        let html=el.innerHTML;
        if(root.lang==='en'){
          html=html.replace(/يتطلب:\s*/gu,'Requires: ').replace(/مستقبلي — غير قابل للتفعيل/gu,'Future — cannot be enabled');
        }else{
          html=html.replace(/Requires:\s*/giu,'يتطلب: ').replace(/Future — cannot be enabled/giu,'مستقبلي — غير قابل للتفعيل');
        }
        el.innerHTML=html;
      });

      const v148StyleId='superAdminBilingualV148PlansPseudo';
      let v148Style=document.getElementById(v148StyleId);
      if(!v148Style){v148Style=document.createElement('style');v148Style.id=v148StyleId;document.head.appendChild(v148Style);}
      v148Style.textContent=root.lang==='ar'
        ? '.identity:after{content:"إدارة المنصة"!important}.safetyNotice[open] .noticeAction:after{content:"إخفاء التفاصيل"!important}'
        : '.identity:after{content:"Platform Administration"!important}.safetyNotice[open] .noticeAction:after{content:"Hide details"!important}';

      document.title=(root.lang==='ar'?'إدارة الباقات والحدود · TCRM':'Plans & Limits Management · TCRM');
    }
  };"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.48 Plans Catalog/Editor full static closure already applied; no changes made.')
        return
    if V147_MARKER not in text:
        raise SystemExit('Bilingual V1.47 Tara APIs full static closure marker not found; apply V1.47 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    anchor_count = text.count(ANCHOR)
    if anchor_count != 1:
        raise SystemExit(f'V1.48 Plans finalizer anchor count is {anchor_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.48 Plans Catalog/Editor full static closure runtime.')

if __name__ == '__main__':
    main()
