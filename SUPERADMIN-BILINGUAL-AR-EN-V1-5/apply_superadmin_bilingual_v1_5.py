#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_5'
V14_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_4'
JS_ANCHOR = '  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_4\n'
DOC_ANCHOR = "    applyV12CriticalOverrides();\n    applyV13CriticalOverrides();\n    applyV14CriticalOverrides();\n    syncLanguageControls();"

JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_5
  // Final-gate post-render localization sweep.
  // This runs after the existing source-aware translation pipeline so late-rendered
  // dynamic labels/attributes cannot re-introduce mixed Arabic/English static UI.
  // Exact dictionaries only touch known static UI copy; business/user data stays untouched.
  const V15_PAIRS=[
    // V1.4 audit leftovers — English target
    ['متأخر / منتهي','Overdue / expired'],
    ['كل الحسابات','All accounts'],
    ['نشاط المنصة','Platform activity'],
    ['الإيراد الشهري','Monthly revenue'],
    ['يتطلب متابعة','Needs attention'],
    ['منصة الإدارة','Administration Platform'],
    ['توسيع القائمة','Expand navigation'],
    ['التنقل الرئيسي','Main navigation'],
    ['بحث عام: شركة / فاتورة / نشاط','Global search: company / invoice / activity'],
    ['بحث باسم شركة / فاتورة / نشاط','Search by company / invoice / activity'],
    ['تحديث بيانات لوحة الControl','Refresh dashboard data'],
    ['تحديث بيانات لوحة التحكم','Refresh dashboard data'],
    ['Add Company جديدة','Add Company'],
    ['فتح إدارة مسؤولي المنصة','Open Platform Admins'],
    ['فتح مركز Download Source','Open Download Source Center'],
    ['فتح مركز تحميل السورس','Open Download Source Center'],
    ['تبديل المظهر','Toggle theme'],
    ['التبديل إلى العربية','Switch to Arabic'],
    ['سبب التحديث','Update reason'],
    ['اسم المسؤول','Admin name'],
    ['اعثر على الشركة المطلوبة بسرعة.','Find the company you need quickly.'],
    ['From date الإنشاء','Created from'],
    ['To date الإنشاء','Created to'],
    ['عدد Rows','Number of rows'],
    ['عدد الصفوف','Number of rows'],
    ['إدارة المستخدمين والصلاحيات عبر جميع الشركات','Manage users and permissions across all companies'],
    ['إجمالي الحسابات','Total accounts'],
    ['مديرو الشركات','Company admins'],
    ['لديهم كلمة مرور','Have a password'],
    ['البحث والتصفية','Search & filtering'],
    ['تصفية المستخدمين حسب الشركة والدور والحالة.','Filter users by company, role, and status.'],
    ['دليل المستخدمين','User directory'],
    ['الحساب، الشركة، الصلاحية والحالة.','Account, company, permission, and status.'],
    ['أحدث العمليات والتغييرات المسجلة على المنصة','Latest operations and changes recorded on the platform'],
    ['أحدث الشركات والحركة المهمة على المنصة.','Latest companies and important platform activity.'],
    ['Review sensitive events وتتبع العمليات الإدارية','Review sensitive events and track administrative operations'],
    ['مراقبة مباشرة','Live monitoring'],
    ['حسب الشركة أو نوع الحدث','By company or event type'],
    ['سجل محمي','Protected log'],
    ['فلاتر سجل التدقيق','Audit log filters'],
    ['مReviewة Source المنصة وتنفيذ المزامنة بSecurity','Review platform source and sync securely'],
    ['الفرع النشط','Active branch'],
    ['موجودة','Present'],
    ['توجد تغييرات تحتاج مReviewة','Changes need review'],
    ['◉ معاينة الفروق','◉ Preview Diff'],
    ['🚀 مReviewة ومزامنة','🚀 Review & Sync'],
    ['المصدر متزامن مع GitHub ويوجد إصدار لم يُنشر بعد.','Source is synced with GitHub and a revision is awaiting deployment.'],
    ['إدارة الاتصال والمستودع','Manage Connection & Repository'],
    ['تحقق واربط','Verify & Connect'],
    ['حفظ Repository والفرع','Save Repository & Branch'],
    ['فصل GitHub','Disconnect GitHub'],
    ['تحديث السجل','Refresh Log'],
    ['أخرى','Other'],
    ['مراحل مزامنة GitHub','GitHub Sync Stages'],
    ['بحث في سجل GitHub','Search GitHub Log'],
    ['بحث في العملية أو المستودع أو المستخدم','Search by operation, repository, or user'],
    ['تصفية سجل GitHub','Filter GitHub Log'],
    ['إدارة اتصال WhatsApp المركزي واختبار الخدمة','Manage the central WhatsApp connection and test the service'],
    ['محفوظ: ••••••••','Saved: ••••••••'],
    ['تم تحميل إعدادات المنصة.','Platform settings loaded.'],
    ['آخر اختبار','Last test'],
    ['آخر نجاح','Last success'],
    ['توليد أو تدوير بيانات الربط وإعادة تشغيل خدمة Evolution API.','Generate or rotate connection data and restart the Evolution API service.'],
    ['جاهز — جميع مفاتيح التشغيل تبدأ بSecurity ويمكن تفعيلها تدريجيًا','Ready — all rollout controls start secure and can be enabled gradually'],
    ['Companies Management والباقات على مستوى المنصة.','Company management and plans at platform level.'],
    ['نظام إدارة Clients','Client Management System'],
    ['الأساس التشغيلي لإدارة Clients والمبيعات.','Operational core for client and sales management.'],
    ['تشغيل Reconcile الآن','Run Reconcile Now'],
    ['حفظ إعدادات الSecurity','Save Security Settings'],
    ['القيم بوحدة Minor مثل الفلس/السنت.','Values are in minor units such as fils/cents.'],

    // Common plan/catalog static labels that were still reported by the scanner
    ['إدارة الإصدارات','Version Management'],
    ['الشركات والاستثناءات','Companies & Overrides'],
    ['إدارة المنصة','Platform Administration'],
    ['الوكيل الاجتماعي الداخلي','Internal Social Agent'],
    ['تقارير متقدمة','Advanced Reports'],
    ['لوحات مخصصة','Custom Dashboards'],
    ['التقارير','Reports'],
    ['وسائط واتساب','WhatsApp Media'],
    ['حسابات واتساب متعددة','Multiple WhatsApp Accounts'],
    ['الأتمتة','Automation'],
    ['التقويم','Calendar'],
    ['الخدمات الديناميكية','Dynamic Services'],
    ['سير العمل الديناميكي','Dynamic Workflow'],
    ['الملفات','Files'],
    ['الاستيراد والتصدير','Import & Export'],
    ['الوصول إلى API','API Access'],
    ['التسويق بالبريد','Email Marketing'],
    ['إعلانات Google','Google Ads'],
    ['إعلانات LinkedIn','LinkedIn Ads'],
    ['إعلانات Meta','Meta Ads'],
    ['إعلانات Snapchat','Snapchat Ads'],
    ['إعلانات TikTok','TikTok Ads'],
    ['تطوير الأعمال','Business Development'],
    ['الصفقات','Deals'],
    ['دعم أولوية','Priority Support'],
    ['مساحة العمل','Workspace'],
    ['وكيل الذكاء الاصطناعي','AI Agent'],
    ['التحويل لموظف','Handoff to Employee'],
    ['ردود إنستجرام بالذكاء الاصطناعي','AI Instagram Replies'],
    ['قاعدة معرفة الوكيل','Agent Knowledge Base'],
    ['توزيع Clients بالذكاء الاصطناعي','AI Client Assignment'],
    ['Webhooks النشطة','Active Webhooks'],
    ['استدعاءات API الشهرية','Monthly API Calls'],
    ['ميزانية Tokens الشهرية','Monthly Token Budget'],

    // Arabic target — explicit final gate items
    ['Platform administration, simplified.','إدارة المنصة، ببساطة.'],
    ['Platform administration. Simplified.','إدارة المنصة، ببساطة.'],
    ['Secure, multi-tenant control for your entire TCRMMT ecosystem.','تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.'],
    ['ATTENTION','يحتاج متابعة'],
    ['Back to Command Center','العودة إلى مركز القيادة'],
    ['Refresh Data','تحديث البيانات'],
    ['View details','عرض التفاصيل'],
    ['Controlled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout','التحكم · التفعيل · الاستخدام · دورة الاشتراك · الفوترة · الخدمة الذاتية · التشغيل التدريجي'],
    ['تحكمled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout','التحكم · التفعيل · الاستخدام · دورة الاشتراك · الفوترة · الخدمة الذاتية · التشغيل التدريجي'],
    ['Kill Switch','مفتاح الإيقاف الطارئ'],
    ['Canary %','نسبة Canary %'],
    ['Grace Days','أيام السماح'],
    ['Feature Overrides JSON','تجاوزات الخصائص JSON'],
    ['Limit Overrides JSON','تجاوزات الحدود JSON'],
    ['Switch to English','التبديل إلى الإنجليزية']
  ];

  const I18N_V15_AR_EN=Object.freeze(Object.fromEntries(V15_PAIRS.filter(pair=>/[\u0600-\u06FF]/.test(pair[0])).map(pair=>[pair[0],pair[1]])));
  const I18N_V15_EN_AR=Object.freeze(Object.assign(
    Object.fromEntries(V15_PAIRS.filter(pair=>!/[\u0600-\u06FF]/.test(pair[0])).map(pair=>[pair[0],pair[1]])),
    {
      'Run Reconcile Now':'تشغيل المطابقة الآن',
      'Save Security Settings':'حفظ إعدادات الأمان',
      'Values are in minor units such as fils/cents.':'القيم بوحدة أصغر مثل الفلس/السنت.'
    }
  ));

  const v15AsciiDigits=value=>String(value).replace(/[٠-٩]/g,ch=>'0123456789'['٠١٢٣٤٥٦٧٨٩'.indexOf(ch)]);
  const v15Normalize=value=>String(value==null?'':value).trim().replace(/\s+/g,' ');

  const v15TranslatePost=(value,lang)=>{
    let raw=v15Normalize(value);
    if(!raw)return raw;

    // First re-run ALL existing exact dictionaries directly against the rendered value.
    // This bypasses WeakMap/source-cache behavior that caused V1.4 late-render misses.
    if(lang==='en'){
      const exact=I18N_V15_AR_EN[raw]
        ||(typeof I18N_V14_AR_EN!=='undefined'&&I18N_V14_AR_EN[raw])
        ||(typeof I18N_V13_AR_EN!=='undefined'&&I18N_V13_AR_EN[raw])
        ||(typeof I18N_V12_AR_EN!=='undefined'&&I18N_V12_AR_EN[raw])
        ||(typeof I18N_V11_AR_EN!=='undefined'&&I18N_V11_AR_EN[raw])
        ||(typeof I18N_AR_EN!=='undefined'&&I18N_AR_EN[raw]);
      if(exact)raw=exact;

      let m=raw.match(/^(\d+) shown of (\d+) · صفحة (\d+)\/(\d+)$/);if(m)raw=m[1]+' shown of '+m[2]+' · Page '+m[3]+'/'+m[4];
      m=raw.match(/^Server-side pagination · (\d+) سجل$/);if(m)raw='Server-side pagination · '+m[1]+' records';
      m=raw.match(/^(\d+) Companies مدفوعة$/);if(m)raw=m[1]+' paid companies';
      m=raw.match(/^(\d+) موقوفة · (\d+) تنتهي قريبًا$/);if(m)raw=m[1]+' suspended · '+m[2]+' ending soon';
      m=raw.match(/^(\d+) من (\d+) عملية$/);if(m)raw=m[1]+' of '+m[2]+' operations';
      m=raw.match(/^(.+?) · (\d+) سجل$/);if(m&&!/[\u0600-\u06FF]/.test(m[1]))raw=m[1]+' · '+m[2]+' records';
      raw=v15AsciiDigits(raw);
      return raw;
    }

    const exact=I18N_V15_EN_AR[raw]
      ||(typeof I18N_V14_EN_AR!=='undefined'&&I18N_V14_EN_AR[raw])
      ||(typeof I18N_V13_EN_AR!=='undefined'&&I18N_V13_EN_AR[raw])
      ||(typeof I18N_V12_EN_AR!=='undefined'&&I18N_V12_EN_AR[raw])
      ||(typeof I18N_V11_EN_AR!=='undefined'&&I18N_V11_EN_AR[raw])
      ||(typeof I18N_EN_AR!=='undefined'&&I18N_EN_AR[raw]);
    return exact||raw;
  };

  const v15TranslateTextNode=node=>{
    const parent=node&&node.parentElement;
    if(!parent||/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(parent.tagName))return;
    const current=node.nodeValue||'';
    const trimmed=current.trim();
    if(!trimmed)return;
    const desired=v15TranslatePost(trimmed,currentLanguage());
    if(desired===trimmed)return;
    const leading=(current.match(/^\s*/)||[''])[0];
    const trailing=(current.match(/\s*$/)||[''])[0];
    node.nodeValue=leading+desired+trailing;
  };

  const v15TranslateElementAttrs=element=>{
    if(!(element instanceof Element))return;
    ['placeholder','title','aria-label'].forEach(name=>{
      if(!element.hasAttribute(name))return;
      const current=element.getAttribute(name)||'';
      const desired=v15TranslatePost(current,currentLanguage());
      if(desired!==v15Normalize(current))element.setAttribute(name,desired);
    });
  };

  const v15SetText=(selector,en,ar)=>{
    const el=document.querySelector(selector);
    if(!(el instanceof HTMLElement))return;
    const desired=currentLanguage()==='ar'?ar:en;
    if(v15Normalize(el.textContent)!==desired)el.textContent=desired;
  };
  const v15SetAttr=(selector,name,en,ar)=>{
    const el=document.querySelector(selector);
    if(!(el instanceof Element))return;
    const desired=currentLanguage()==='ar'?ar:en;
    if(el.getAttribute(name)!==desired)el.setAttribute(name,desired);
  };

  const applyV15CriticalOverrides=()=>{
    // Login must always match the selected language after late recovery/login renders.
    v15SetText('#loginView .tamiyouzBrandContent h1','Platform administration, simplified.','إدارة المنصة، ببساطة.');
    v15SetText('#loginView .tamiyouzBrandContent p','Secure, multi-tenant control for your entire TCRMMT ecosystem.','تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.');

    // Global attributes that repeatedly re-render after data refreshes.
    v15SetAttr('#topGlobalSearch','aria-label','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط');
    v15SetAttr('#topGlobalSearch','placeholder','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط');
    v15SetAttr('#globalSearchBox','aria-label','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');
    v15SetAttr('#globalSearchBox','placeholder','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');
    v15SetAttr('#refreshBtn','aria-label','Refresh dashboard data','تحديث بيانات لوحة التحكم');
    v15SetAttr('#createTenantOpenBtn','aria-label','Add Company','إضافة شركة');
    v15SetAttr('#openPlatformAdminsTopBtn','aria-label','Open Platform Admins','فتح إدارة مسؤولي المنصة');
    v15SetAttr('#openSettingsBtn','aria-label','Open Download Source Center','فتح مركز تحميل السورس');
    v15SetAttr('#themeToggleBtn','aria-label','Toggle theme','تبديل المظهر');
    v15SetAttr('#createdFrom','title','Created from','من تاريخ الإنشاء');
    v15SetAttr('#createdTo','title','Created to','إلى تاريخ الإنشاء');
    v15SetAttr('#tenantPageSize','aria-label','Number of rows','عدد الصفوف');
    v15SetAttr('#subNotes','aria-label','Update reason','سبب التحديث');
    v15SetAttr('#subNotes','placeholder','Update reason','سبب التحديث');
    v15SetAttr('#platformAdminName','aria-label','Admin name','اسم المسؤول');
    v15SetAttr('#platformAdminName','placeholder','Admin name','اسم المسؤول');

    // Language-toggle accessibility copy must itself be localized.
    document.querySelectorAll('[data-sa-language-toggle],[data-sa-language-inline]').forEach(button=>{
      if(!(button instanceof HTMLElement))return;
      const ar=currentLanguage()==='ar';
      const title=ar?'التبديل إلى الإنجليزية':'Switch to Arabic';
      button.title=title;
      button.setAttribute('aria-label',title);
    });
  };

  const applyV15PostSweep=()=>{
    if(!document.body)return;
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    let node=walker.nextNode();
    while(node){v15TranslateTextNode(node);node=walker.nextNode()}
    document.querySelectorAll('[placeholder],[title],[aria-label]').forEach(v15TranslateElementAttrs);
    applyV15CriticalOverrides();
  };
  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_5
'''


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.5 already applied; no changes made.')
        return
    if V14_MARKER not in text:
        raise SystemExit('Bilingual V1.4 marker not found; apply V1 through V1.4 first.')

    for label, anchor in [('V1.4 JS end', JS_ANCHOR), ('translation document chain', DOC_ANCHOR)]:
        if text.count(anchor) != 1:
            raise SystemExit(f'{label} anchor count is {text.count(anchor)}; refusing unknown baseline.')

    text = replace_once(text, JS_ANCHOR, JS_ANCHOR + JS + '\n', 'V1.5 JS')
    text = replace_once(
        text,
        DOC_ANCHOR,
        "    applyV12CriticalOverrides();\n    applyV13CriticalOverrides();\n    applyV14CriticalOverrides();\n    applyV15PostSweep();\n    syncLanguageControls();",
        'V1.5 post-render sweep hook',
    )

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual Arabic / English V1.5 final-gate post-render localization sweep.')


if __name__ == '__main__':
    main()
