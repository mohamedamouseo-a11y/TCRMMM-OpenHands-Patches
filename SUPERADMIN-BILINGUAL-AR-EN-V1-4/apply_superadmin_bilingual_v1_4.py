#!/usr/bin/env python3
from pathlib import Path

TARGET=Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER='SUPER_ADMIN_BILINGUAL_AR_EN_V1_4'
V13='SUPER_ADMIN_BILINGUAL_AR_EN_V1_3'
JS_ANCHOR='  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_3\n'
OLD_NEXT="    const next=translateV13Phrases(next1,currentLanguage());"
DOC_ANCHOR="    applyV12CriticalOverrides();\n    applyV13CriticalOverrides();\n    syncLanguageControls();"

JS=r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_4
  const V14_PAIRS=[
    ['منصة الإدارة','Administration Platform'],['توسيع القائمة','Expand navigation'],['التنقل الرئيسي','Main navigation'],
    ['بحث عام: شركة / فاتورة / نشاط','Global search: company / invoice / activity'],['بحث باسم شركة / فاتورة / نشاط','Search by company / invoice / activity'],
    ['تحديث بيانات لوحة الControl','Refresh dashboard data'],['Add Company جديدة','Add Company'],['فتح إدارة مسؤولي المنصة','Open Platform Admins'],
    ['فتح مركز Download Source','Open Download Source Center'],['تبديل المظهر','Toggle theme'],['التبديل إلى العربية','Switch to Arabic'],
    ['سبب التحديث','Update reason'],['اسم المسؤول','Admin name'],['نسخ المسار','Copy path'],
    ['متأخر / منتهي','Overdue / expired'],['كل الحسابات','All accounts'],['نشاط المنصة','Platform activity'],['الإيراد الشهري','Monthly revenue'],['يتطلب متابعة','Needs attention'],
    ['اعثر على الشركة المطلوبة بسرعة.','Find the company you need quickly.'],['فلاتر الشركات','Company filters'],['اسم الشركة، المسار أو البريد','Company name, path, or email'],
    ['From date الإنشاء','Created from'],['To date الإنشاء','Created to'],['عدد Rows','Number of rows'],
    ['إدارة المستخدمين والصلاحيات عبر جميع الشركات','Manage users and permissions across all companies'],['إجمالي الحسابات','Total accounts'],['مديرو الشركات','Company admins'],
    ['لديهم كلمة مرور','Have a password'],['البحث والتصفية','Search & filtering'],['تصفية المستخدمين حسب الشركة والدور والحالة.','Filter users by company, role, and status.'],
    ['دليل المستخدمين','User directory'],['الحساب، الشركة، الصلاحية والحالة.','Account, company, permission, and status.'],['مفعّلة','Enabled'],['كلمة مرور جديدة','New password'],
    ['إيقاف','Suspend'],['محذوف','Deleted'],['فلاتر المستخدمين','User filters'],['الاسم، البريد أو الدور','Name, email, or role'],
    ['أحدث العمليات والتغييرات المسجلة على المنصة','Latest operations and changes recorded on the platform'],['أحدث الشركات والحركة المهمة على المنصة.','Latest companies and important platform activity.'],
    ['Review sensitive events وتتبع العمليات الإدارية','Review sensitive events and track administrative operations'],['مراقبة مباشرة','Live monitoring'],['حسب الشركة أو نوع الحدث','By company or event type'],
    ['الحدث','Event'],['آخر العمليات الإدارية مرتبة من الأحدث إلى الأقدم','Latest administrative operations ordered newest to oldest'],['سجل محمي','Protected log'],
    ['فلاتر سجل التدقيق','Audit log filters'],['معرّف الشركة','Company ID'],['مثل subscription أو github.sync','e.g. subscription or github.sync'],['نوع الحدث','Event type'],
    ['مReviewة Source المنصة وتنفيذ المزامنة بSecurity','Review platform source and sync securely'],['الفرع النشط','Active branch'],['موجودة','Present'],['توجد تغييرات تحتاج مReviewة','Changes need review'],
    ['افحص التغييرات، Review الملفات، ثم نفّذ Commit وPush وتحقق من النتيجة.','Inspect changes, review files, then run Commit and Push and verify the result.'],['◉ معاينة الفروق','◉ Preview Diff'],
    ['🚀 مReviewة ومزامنة','🚀 Review & Sync'],['المصدر متزامن مع GitHub ويوجد إصدار لم يُنشر بعد.','Source is synced with GitHub and a revision is awaiting deployment.'],
    ['إدارة الاتصال والمستودع','Manage Connection & Repository'],['تحقق واربط','Verify & Connect'],['حفظ Repository والفرع','Save Repository & Branch'],['فصل GitHub','Disconnect GitHub'],
    ['GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ Build ثم Restart عند وقت النشر المناسب.','GitHub is ready. A revision has not been built yet; run Build then Restart when ready to deploy.'],
    ['↻ سجل عمليات GitHub','↻ GitHub Operations Log'],['تحديث السجل','Refresh Log'],['أخرى','Other'],['مراحل مزامنة GitHub','GitHub Sync Stages'],['بحث في سجل GitHub','Search GitHub Log'],
    ['بحث في العملية أو المستودع أو المستخدم','Search by operation, repository, or user'],['تصفية سجل GitHub','Filter GitHub Log'],
    ['إدارة اتصال WhatsApp المركزي واختبار الخدمة','Manage the central WhatsApp connection and test the service'],
    ['إعداد مركزي واحد تستخدمه شركات المنصة. متاح لمالك المنصة فقط ولا تُعرض الأسرار بعد حفظها.','One central configuration used by platform companies. Available only to the platform owner; secrets are not shown after saving.'],
    ['محفوظ: ••••••••','Saved: ••••••••'],['تم تحميل إعدادات المنصة.','Platform settings loaded.'],['آخر اختبار','Last test'],['آخر نجاح','Last success'],
    ['توليد أو تدوير بيانات الربط وإعادة تشغيل خدمة Evolution API.','Generate or rotate connection data and restart the Evolution API service.'],['تفعيل Evolution API','Enable Evolution API'],
    ['إدارة الإصدارات والاشتراكات وحدود الاستخدام','Manage versions, subscriptions, and usage limits'],
    ['تطبيق القيود والفوترة الآلية ودورة الاشتراك متوقف افتراضيًا. يتوفر إيقاف طارئ ورجوع فوري لكل شركة عند الحاجة.','Enforcement, automated billing, and subscription lifecycle are disabled by default. Emergency stop and immediate per-company rollback are available when needed.'],
    ['جاهز — جميع مفاتيح التشغيل تبدأ بSecurity ويمكن تفعيلها تدريجيًا','Ready — all rollout controls start secure and can be enabled gradually'],['الشركات والاستثناءات','Companies & Overrides'],
    ['إدارة الإصدارات','Version Management'],['المنشورة والمسودات والإصدارات المؤرشفة.','Published, draft, and archived versions.'],['إدارة المنصة','Platform Administration'],
    ['Companies Management والباقات على مستوى المنصة.','Company management and plans at platform level.'],['الوكيل الاجتماعي الداخلي','Internal Social Agent'],
    ['الوكيل الاجتماعي الحالي داخل النظام؛ منفصل عن الوكيل الخارجي المستقبلي.','The current in-system social agent; separate from the future external agent.'],
    ['تقارير متقدمة','Advanced Reports'],['تقارير وتحليلات متقدمة.','Advanced reports and analytics.'],['لوحات مخصصة','Custom Dashboards'],['إنشاء لوحات مؤشرات مخصصة.','Create custom dashboards.'],
    ['لوحة المؤشرات الأساسية.','Core dashboard.'],['التقارير','Reports'],['التقارير الأساسية للنظام.','Core system reports.'],['إدارة محادثات واتساب داخل الشركة.','Manage WhatsApp conversations within the company.'],
    ['وسائط واتساب','WhatsApp Media'],['رفع واستقبال وتخزين وسائط واتساب.','Upload, receive, and store WhatsApp media.'],['حسابات واتساب متعددة','Multiple WhatsApp Accounts'],
    ['تشغيل أكثر من حساب واتساب للشركة.','Run more than one WhatsApp account per company.'],['الأتمتة','Automation'],['التقويم','Calendar'],['التقويم والمواعيد والتكاملات المرتبطة.','Calendar, appointments, and related integrations.'],
    ['نظام إدارة Clients','Client Management System'],['الأساس التشغيلي لإدارة Clients والمبيعات.','Operational core for client and sales management.'],['الخدمات الديناميكية','Dynamic Services'],
    ['إدارة الخدمات الديناميكية للعملاء.','Manage dynamic services for clients.'],['سير العمل الديناميكي','Dynamic Workflow'],['سير عمل ديناميكي ومهام مؤتمتة.','Dynamic workflows and automated tasks.'],
    ['الملفات','Files'],['تخزين وإدارة ملفات النظام.','Store and manage system files.'],['الاستيراد والتصدير','Import & Export'],['استيراد وتصدير بيانات النظام.','Import and export system data.'],
    ['الوصول إلى API','API Access'],['الوصول البرمجي إلى واجهات النظام.','Programmatic access to system APIs.'],['ربط الملفات بمساحة Google Drive الخاصة بالشركة.','Connect files to the company Google Drive space.'],
    ['تكاملات الأنظمة الخارجية.','External system integrations.'],['إرسال واستقبال أحداث التكامل الخارجي.','Send and receive external integration events.'],
    ['بهجت — مساعد السوشيال ميديا','Bahgat — Social Media Assistant'],['إنشاء واعتماد وجدولة ونشر المحتوى عبر Postiz مع موافقة بشرية إلزامية.','Create, approve, schedule, and publish content via Postiz with mandatory human approval.'],
    ['التسويق بالبريد','Email Marketing'],['إدارة حملات البريد الإلكتروني.','Manage email campaigns.'],['إعلانات Google','Google Ads'],['تكامل حملات وإحصاءات Google Ads.','Google Ads campaign and analytics integration.'],
    ['إعلانات LinkedIn','LinkedIn Ads'],['تكامل حملات LinkedIn.','LinkedIn campaign integration.'],['إعلانات Meta','Meta Ads'],['تكامل حملات Meta.','Meta campaign integration.'],
    ['إعلانات Snapchat','Snapchat Ads'],['تكامل حملات Snapchat.','Snapchat campaign integration.'],['إعلانات TikTok','TikTok Ads'],['تكامل حملات TikTok.','TikTok campaign integration.'],
    ['المهام والمتابعات والأنشطة المرتبطة بClients.','Tasks, follow-ups, and activities linked to clients.'],['تطوير الأعمال','Business Development'],['إدارة عمليات تطوير الأعمال.','Manage business development operations.'],
    ['إدارة Clients الحاليين وملفاتهم.','Manage current clients and their profiles.'],['الصفقات','Deals'],['إدارة مسار الصفقات والمدفوعات.','Manage deal pipeline and payments.'],
    ['إدارة Clients المحتملين والتوزيع والمتابعة.','Manage leads, assignment, and follow-up.'],['دعم أولوية','Priority Support'],['أولوية في استقبال ومعالجة طلبات الدعم.','Priority handling of support requests.'],
    ['جداول مساحة العمل.','Workspace spreadsheets.'],['عروض مساحة العمل.','Workspace presentations.'],['مساحة العمل','Workspace'],['مستندات وجداول وعروض مساحة العمل.','Workspace documents, spreadsheets, and presentations.'],
    ['وكيل الذكاء الاصطناعي','AI Agent'],['تعريف مستقبلي لربط نظام الوكيل الخارجي.','Future definition for connecting the external agent system.'],['مستقبلي — غير قابل للتفعيل','Future — not activatable'],
    ['التحويل لموظف','Handoff to Employee'],['تعريف مستقبلي لتحويل المحادثة من الوكيل إلى موظف.','Future definition for handing a conversation from the agent to an employee.'],
    ['ردود إنستجرام بالذكاء الاصطناعي','AI Instagram Replies'],['تعريف مستقبلي لردود Instagram عبر الوكيل الخارجي.','Future definition for Instagram replies through the external agent.'],
    ['قاعدة معرفة الوكيل','Agent Knowledge Base'],['تعريف مستقبلي لقواعد معرفة الوكيل الخارجي.','Future definition for external agent knowledge bases.'],
    ['توزيع Clients بالذكاء الاصطناعي','AI Client Assignment'],['تعريف مستقبلي لتأهيل وتوزيع Clients المحتملين.','Future definition for lead qualification and assignment.'],
    ['ردود واتساب بالذكاء الاصطناعي','AI WhatsApp Replies'],['تعريف مستقبلي لردود واتساب عبر الوكيل الخارجي.','Future definition for WhatsApp replies through the external agent.'],
    ['يمكن Save Draft ناقصة، لكن النشر يتطلب قرارًا صريحًا لكل حد.','A draft can be saved incomplete, but publishing requires an explicit decision for every limit.'],
    ['لوحات الControl المخصصة','Custom Dashboards'],['عدد الملفات','File Count'],['الحد الأقصى لFile Size','Maximum File Size'],['استدعاءات API الشهرية','Monthly API Calls'],
    ['صفوف التصدير الشهرية','Monthly Export Rows'],['صفوف الاستيراد الشهرية','Monthly Import Rows'],['محادثات واتساب الشهرية','Monthly WhatsApp Conversations'],['رسائل واتساب الشهرية','Monthly WhatsApp Messages'],
    ['مساحة التخزين','Storage Space'],['إجمالي Clients','Total Clients'],['إجمالي الصفقات','Total Deals'],['إجمالي Clients المحتملين','Total Leads'],['حسابات واتساب','WhatsApp Accounts'],
    ['عدد وكلاء الذكاء الاصطناعي','AI Agent Count'],['قنوات الوكيل','Agent Channels'],['قواعد معرفة الوكيل','Agent Knowledge Bases'],['محادثات الوكيل الشهرية','Monthly Agent Conversations'],
    ['رسائل الوكيل الشهرية','Monthly Agent Messages'],['ميزانية Tokens الشهرية','Monthly Token Budget'],['الإصدارات المنشورة والمؤرشفة للقراءة فقط؛ أنشئ مسودة للتعديل.','Published and archived versions are read-only; create a draft to edit.'],
    ['نشر الإصدار','Publish Version'],['أقسام إدارة الباقات','Plan Management Sections'],
    ['تشغيل Reconcile الآن','Run Reconcile Now'],['إجمالي الفواتير المفتوحة','Total Open Invoices'],['تنبيهات استخدام','Usage Alerts'],['تفعيل Enforcement','Enable Enforcement'],
    ['دورة الاشتراك الآلية','Automated Subscription Lifecycle'],['إنشاء الفواتير آليًا','Automated Invoice Creation'],['بوابة العميل','Customer Portal'],['حفظ إعدادات الSecurity','Save Security Settings'],
    ['اختر شركة لإدارة الاشتراك والتفعيل والاستهلاك.','Select a company to manage subscription, activation, and usage.'],['اختر شركة','Select Company'],['اختر شركة من القائمة.','Select a company from the list.'],
    ['تسعير الباقات','Plan Pricing'],['القيم بوحدة Minor مثل الفلس/السنت.','Values are in minor units such as fils/cents.'],['الدورة','Cycle'],['السعر Minor','Minor-unit Price'],
    ['رسوم التأسيس Minor','Minor-unit Setup Fee'],['السعر نشط','Price Active'],['حفظ السعر','Save Price'],['كتالوج الإضافات','Add-on Catalog'],['Features وLimits بصيغة JSON موثقة.','Features and Limits in documented JSON format.'],
    ['حفظ الإضافة','Save Add-on'],['لا توجد إضافات.','No add-ons.'],['الشركة أو الباقة','Company or plan']
  ];
  const I18N_V14_AR_EN=Object.freeze(Object.fromEntries(V14_PAIRS));
  const I18N_V14_EN_AR=Object.freeze(Object.assign(Object.fromEntries(V14_PAIRS.map(pair=>[pair[1],pair[0]])),{
    'ATTENTION':'يحتاج متابعة','Create a new Workspace':'إنشاء مساحة عمل جديدة','Back to Command Center':'العودة إلى مركز القيادة','Refresh Data':'تحديث البيانات','View details':'عرض التفاصيل',
    'Switch to English':'التبديل إلى الإنجليزية','Tenant ID':'معرّف الشركة','Add Admin':'إضافة مسؤول','Use Ctrl/Cmd to select multiple companies':'استخدم Ctrl/Cmd لاختيار أكثر من شركة',
    'Save Admin & Company Permissions':'حفظ المسؤول وصلاحيات الشركات','Controlled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout':'التحكم · التفعيل · الاستخدام · دورة الاشتراك · الفوترة · الخدمة الذاتية · التشغيل التدريجي',
    'تحكمled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout':'التحكم · التفعيل · الاستخدام · دورة الاشتراك · الفوترة · الخدمة الذاتية · التشغيل التدريجي',
    'Run Reconcile Now':'تشغيل المطابقة الآن','Kill Switch':'مفتاح الإيقاف الطارئ','Canary %':'نسبة Canary %','Grace Days':'أيام السماح',
    'Features and Limits in documented JSON format.':'الخصائص والحدود بصيغة JSON موثقة.','Feature Overrides JSON':'تجاوزات الخصائص JSON','Limit Overrides JSON':'تجاوزات الحدود JSON','Central المستخدمون':'المستخدمون المركزيون'
  }));
  const translateV14Phrases=(value,lang)=>{
    const raw=String(value==null?'':value).trim().replace(/\\s+/g,' ');
    const direct=lang==='ar'?I18N_V14_EN_AR[raw]:I18N_V14_AR_EN[raw];
    if(direct)return direct;
    if(lang==='en'){
      let m=raw.match(/^(\\d+) shown of (\\d+) · صفحة (\\d+)\\/(\\d+)$/);if(m)return m[1]+' shown of '+m[2]+' · Page '+m[3]+'/'+m[4];
      m=raw.match(/^Server-side pagination · (\\d+) سجل$/);if(m)return 'Server-side pagination · '+m[1]+' records';
      m=raw.match(/^(\\d+) حساب مسجل عبر (\\d+) Companies$/);if(m)return m[1]+' accounts registered across '+m[2]+' companies';
      m=raw.match(/^(\\d+) حساب$/);if(m)return m[1]+' accounts';
      m=raw.match(/^(\\d+) Companies مدفوعة$/);if(m)return m[1]+' paid companies';
      m=raw.match(/^(\\d+) موقوفة · (\\d+) تنتهي قريبًا$/);if(m)return m[1]+' suspended · '+m[2]+' ending soon';
      m=raw.match(/^(\\d+) من (\\d+) عملية$/);if(m)return m[1]+' of '+m[2]+' operations';
      m=raw.match(/^(\\d+) إصدار · (\\d+) منشور$/);if(m)return m[1]+' versions · '+m[2]+' published';
      m=raw.match(/^المعرّف (.+?) · الإصدار (.+)$/);if(m)return 'ID '+m[1]+' · Version '+m[2];
    }
    return raw;
  };
  const setV14Attr=(selector,name,en,ar)=>{const el=document.querySelector(selector);if(!(el instanceof Element))return;const v=currentLanguage()==='ar'?ar:en;if(el.getAttribute(name)!==v)el.setAttribute(name,v)};
  const applyV14CriticalOverrides=()=>{
    setV14Attr('#topGlobalSearch','aria-label','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط');setV14Attr('#topGlobalSearch','placeholder','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط');
    setV14Attr('#globalSearchBox','aria-label','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');setV14Attr('#globalSearchBox','placeholder','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');
    setV14Attr('#refreshBtn','aria-label','Refresh dashboard data','تحديث بيانات لوحة التحكم');setV14Attr('#createTenantOpenBtn','aria-label','Add Company','إضافة شركة');
    setV14Attr('#openPlatformAdminsTopBtn','aria-label','Open Platform Admins','فتح إدارة مسؤولي المنصة');setV14Attr('#openSettingsBtn','aria-label','Open Download Source Center','فتح مركز تحميل السورس');
    setV14Attr('#themeToggleBtn','aria-label','Toggle theme','تبديل المظهر');setV14Attr('#tenantSearch','placeholder','Company name, path, or email','اسم الشركة، المسار أو البريد');
    setV14Attr('#createdFrom','title','Created from','من تاريخ الإنشاء');setV14Attr('#createdTo','title','Created to','إلى تاريخ الإنشاء');setV14Attr('#tenantPageSize','aria-label','Number of rows','عدد الصفوف');
    setV14Attr('#platformUserSearch','placeholder','Name, email, or role','الاسم، البريد أو الدور');setV14Attr('#platformUserRole','aria-label','Role','الدور');setV14Attr('#platformUserStatus','aria-label','Status','الحالة');
    setV14Attr('#subNotes','aria-label','Update reason','سبب التحديث');setV14Attr('#subNotes','placeholder','Update reason','سبب التحديث');setV14Attr('#platformAdminName','aria-label','Admin name','اسم المسؤول');setV14Attr('#platformAdminName','placeholder','Admin name','اسم المسؤول');
  };
  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_4
'''

def once(text,old,new,label):
    c=text.count(old)
    if c!=1: raise SystemExit(f'{label} anchor count is {c}; refusing unknown baseline.')
    return text.replace(old,new,1)

def main():
    text=TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.4 already applied; no changes made.');return
    if V13 not in text: raise SystemExit('Bilingual V1.3 marker not found; apply V1 through V1.3 first.')
    for label,a in [('V1.3 JS end',JS_ANCHOR),('V1.3 result',OLD_NEXT),('override chain',DOC_ANCHOR)]:
        if text.count(a)!=1: raise SystemExit(f'{label} anchor count is {text.count(a)}; refusing unknown baseline.')
    text=once(text,JS_ANCHOR,JS_ANCHOR+JS+'\n','V1.4 JS')
    text=once(text,OLD_NEXT,"    const next2=translateV13Phrases(next1,currentLanguage());\n    const next=translateV14Phrases(next2,currentLanguage());",'V1.4 translator')
    text=once(text,DOC_ANCHOR,"    applyV12CriticalOverrides();\n    applyV13CriticalOverrides();\n    applyV14CriticalOverrides();\n    syncLanguageControls();",'V1.4 overrides')
    TARGET.write_text(text,encoding='utf-8')
    print('Applied Super Admin Bilingual Arabic / English V1.4 final translation sweep.')

if __name__=='__main__': main()
