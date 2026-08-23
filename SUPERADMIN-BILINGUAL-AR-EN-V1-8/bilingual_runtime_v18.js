(()=>{
  'use strict';
  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V18';
  const KEY='tcrm-super-admin-language';
  const root=document.documentElement;
  const pairs=[
    ['Overview','نظرة عامة'],['Dashboard','لوحة التحكم'],['Executive Command Center','مركز القيادة التنفيذي'],
    ['Companies','الشركات'],['Company','الشركة'],['Company Details','تفاصيل الشركة'],['Tenant Details','تفاصيل الشركة'],['Tenants','الشركات'],
    ['Users','المستخدمون'],['User','المستخدم'],['Platform Admins','مسؤولو المنصة'],['Platform Admin','مسؤول المنصة'],
    ['Plans','الباقات'],['Plans Catalog','دليل الباقات'],['Plan Catalog','دليل الباقات'],['Plans Editor','محرر الباقات'],['Plan Editor','محرر الباقة'],
    ['Company Overrides','استثناءات الشركات'],['Companies & Overrides','الشركات والاستثناءات'],['Commercial','التجاري'],['Billing','الفوترة'],['Subscriptions','الاشتراكات'],['Subscription','الاشتراك'],
    ['Activity','النشاط'],['Recent Activity','النشاط الأخير'],['Audit','التدقيق'],['Audit Log','سجل التدقيق'],['Operations','العمليات'],['Integrations','التكاملات'],
    ['GitHub Sync','مزامنة GitHub'],['Evolution API','Evolution API'],['Tara APIs','واجهات Tara API'],['System Settings','إعدادات النظام'],['Settings','الإعدادات'],
    ['General','عام'],['Account','الحساب'],['Appearance','المظهر'],['Source Code','الكود المصدري'],['Owner Only','للمالك فقط'],['OWNER ONLY','للمالك فقط'],
    ['Security','الأمان'],['Security Review','مراجعة الأمان'],['Usage','الاستخدام'],['Usage Overview','نظرة على الاستخدام'],['Alerts','التنبيهات'],['Notifications','الإشعارات'],
    ['Quick Actions','إجراءات سريعة'],['Quick Commands','أوامر سريعة'],['Global Search','البحث الشامل'],['Search','بحث'],['Search companies','بحث في الشركات'],['Search users','بحث في المستخدمين'],
    ['Recent Tenants','الشركات الأخيرة'],['Recent Companies','الشركات الأخيرة'],['Status','الحالة'],['Health','الحالة الصحية'],['Role','الدور'],['Roles','الأدوار'],['Permissions','الصلاحيات'],
    ['Name','الاسم'],['Email','البريد الإلكتروني'],['Email address','عنوان البريد الإلكتروني'],['Phone','الهاتف'],['Domain','النطاق'],['Slug','المعرّف'],['ID','المعرّف'],
    ['Created','تاريخ الإنشاء'],['Created At','تاريخ الإنشاء'],['Updated','آخر تحديث'],['Last Updated','آخر تحديث'],['Last Login','آخر تسجيل دخول'],['Last Activity','آخر نشاط'],
    ['Active','نشط'],['Inactive','غير نشط'],['Suspended','موقوف'],['Cancelled','ملغي'],['Expired','منتهي'],['Pending','قيد الانتظار'],['Trial','تجريبي'],['Trialing','تجريبي'],
    ['Paid','مدفوع'],['Failed','فشل'],['Success','نجاح'],['Healthy','سليم'],['Warning','تحذير'],['Error','خطأ'],['Ready','جاهز'],['Not ready','غير جاهز'],
    ['Actions','الإجراءات'],['Action','إجراء'],['View','عرض'],['Open','فتح'],['Edit','تعديل'],['Save','حفظ'],['Save Changes','حفظ التغييرات'],['Cancel','إلغاء'],['Close','إغلاق'],
    ['Delete','حذف'],['Remove','إزالة'],['Add','إضافة'],['Create','إنشاء'],['Update','تحديث'],['Refresh','تحديث'],['Retry','إعادة المحاولة'],['Apply','تطبيق'],['Reset','إعادة ضبط'],
    ['Download','تنزيل'],['Download Source Code','تنزيل الكود المصدري'],['Refresh Source Code','تحديث الكود المصدري'],['Export','تصدير'],['Import','استيراد'],['Copy','نسخ'],
    ['Enable','تفعيل'],['Disable','تعطيل'],['Enabled','مفعّل'],['Disabled','معطّل'],['Connect','اتصال'],['Disconnect','قطع الاتصال'],['Connected','متصل'],['Disconnected','غير متصل'],
    ['Light','فاتح'],['Dark','داكن'],['Light Mode','الوضع الفاتح'],['Dark Mode','الوضع الداكن'],['Theme','المظهر'],['Help','مساعدة'],['Logout','تسجيل الخروج'],['Sign Out','تسجيل الخروج'],
    ['Details','التفاصيل'],['Summary','الملخص'],['Metrics','المؤشرات'],['Insights','الرؤى'],['Smart Insights','رؤى ذكية'],['Operations Pulse','نبض العمليات'],['Command Details','تفاصيل القيادة'],
    ['Plan','الباقة'],['Current Plan','الباقة الحالية'],['New Plan','الباقة الجديدة'],['Price','السعر'],['Monthly','شهري'],['Yearly','سنوي'],['Monthly Price','السعر الشهري'],['Annual Price','السعر السنوي'],
    ['Currency','العملة'],['Limit','الحد'],['Limits','الحدود'],['Feature','الميزة'],['Features','المميزات'],['Seats','المقاعد'],['Storage','التخزين'],
    ['Company Name','اسم الشركة'],['Company Status','حالة الشركة'],['User Name','اسم المستخدم'],['User Status','حالة المستخدم'],['Primary Super Admin','Super Admin الرئيسي'],
    ['SUPER ADMIN ACCESS','دخول SUPER ADMIN'],['SUPER ADMIN ACCESS · OWNER ONLY','دخول SUPER ADMIN · للمالك فقط'],
    ['Welcome back','مرحباً بعودتك'],['Sign in to your TCRMMT workspace.','سجّل الدخول إلى مساحة عمل TCRMMT.'],
    ['Password','كلمة المرور'],['Show','إظهار'],['Hide','إخفاء'],['Show password','إظهار كلمة المرور'],['Hide password','إخفاء كلمة المرور'],
    ['Forgot password?','هل نسيت كلمة المرور؟'],['Sign In','تسجيل الدخول'],['Reset your password','إعادة تعيين كلمة المرور'],
    ['Back to sign in','العودة لتسجيل الدخول'],['Send reset link','إرسال رابط الاستعادة'],['Reset Password','إعادة تعيين كلمة المرور'],
    ['New password','كلمة المرور الجديدة'],['Confirm password','تأكيد كلمة المرور'],['Protected administration','إدارة محمية'],
    ['Your session is protected with secure authentication.','جلستك محمية بمصادقة آمنة.'],
    ['Platform administration, simplified.','إدارة المنصة، ببساطة.'],['Platform administration. Simplified.','إدارة المنصة، ببساطة.'],
    ['Secure, multi-tenant control for your entire TCRMMT ecosystem.','تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.'],
    ['Loading','جارٍ التحميل'],['Loading...','جارٍ التحميل...'],['No data','لا توجد بيانات'],['No results','لا توجد نتائج'],['No results found','لا توجد نتائج'],
    ['Select','اختر'],['All','الكل'],['All statuses','كل الحالات'],['Filter','تصفية'],['Clear','مسح'],['Clear filters','مسح عوامل التصفية'],['Previous','السابق'],['Next','التالي'],
    ['Page','صفحة'],['Rows per page','صفوف لكل صفحة'],['Total','الإجمالي'],['Total Companies','إجمالي الشركات'],['Total Users','إجمالي المستخدمين'],['Active Companies','الشركات النشطة'],
    ['Active Users','المستخدمون النشطون'],['MRR','الإيراد الشهري المتكرر'],['Revenue','الإيرادات'],['System Health','صحة النظام'],['Platform Health','صحة المنصة'],
    ['Today','اليوم'],['This Week','هذا الأسبوع'],['This Month','هذا الشهر'],['Last 7 days','آخر 7 أيام'],['Last 30 days','آخر 30 يوماً'],
    ['Repository','المستودع'],['Branch','الفرع'],['Sync','مزامنة'],['Sync Now','مزامنة الآن'],['Last Sync','آخر مزامنة'],
    ['API Status','حالة API'],['Endpoint','نقطة النهاية'],['Instance','Instance'],['Webhook','Webhook'],['Webhooks','Webhooks'],
    ['Settings saved successfully.','تم حفظ الإعدادات بنجاح.'],['Changes saved successfully.','تم حفظ التغييرات بنجاح.'],['Unable to load data.','تعذر تحميل البيانات.'],
    ['Try again','حاول مرة أخرى'],['Confirm','تأكيد'],['Are you sure?','هل أنت متأكد؟'],['Skip to content','تخطي إلى المحتوى'],['Appearance tools','أدوات المظهر'],['Back to top','العودة لأعلى الصفحة'],
    ['PLATFORM OVERVIEW','نظرة عامة على المنصة'],['QUICK COMMANDS','أوامر سريعة'],['ATTENTION','يحتاج متابعة'],['USAGE','الاستخدام'],['GLOBAL SEARCH','البحث الشامل'],['SECURITY','الأمان'],['ORGANIZATIONS','المؤسسات'],
    ['Create a new Workspace','إنشاء مساحة عمل جديدة'],['Provisioning Queue','قائمة التجهيز'],['Save Admin & Company Permissions','حفظ المسؤول وصلاحيات الشركات'],
    ['Back to Command Center','العودة إلى مركز القيادة'],['Refresh Data','تحديث البيانات'],['View details','عرض التفاصيل'],
    ['Kill Switch','مفتاح الإيقاف الطارئ'],['Canary %','نسبة النشر التجريبي %'],['Grace Days','أيام السماح'],['Feature Overrides JSON','تجاوزات الخصائص JSON'],['Limit Overrides JSON','تجاوزات الحدود JSON'],
    ['Controlled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout','التحكم · التفعيل · الاستخدام · دورة الاشتراك · الفوترة · الخدمة الذاتية · التشغيل التدريجي'],
    ['Overdue / expired','متأخر / منتهي'],['All accounts','كل الحسابات'],['Platform activity','نشاط المنصة'],['Monthly revenue','الإيراد الشهري'],['Needs attention','يتطلب متابعة'],
    ['Manage users and permissions across all companies','إدارة المستخدمين والصلاحيات عبر جميع الشركات'],
    ['Latest operations and changes recorded on the platform','أحدث العمليات والتغييرات المسجلة على المنصة'],
    ['Review sensitive events and track administrative operations','مراجعة الأحداث الحساسة وتتبع العمليات الإدارية'],
    ['Active branch','الفرع النشط'],['Present','موجودة'],['Manage the central WhatsApp connection and test the service','إدارة اتصال WhatsApp المركزي واختبار الخدمة'],
    ['Save Security Settings','حفظ إعدادات الأمان'],['Repository Connection Details','تفاصيل الاتصال والمستودع'],
    ['Current repository status, GitHub PAT, and selected branch.','الحالة الحالية للمستودع وGitHub PAT والفرع المحدد.'],
    ['Loading GitHub status...','جاري تحميل حالة GitHub...'],['Connection Status','حالة الاتصال'],['Last Successful Check','آخر فحص ناجح'],['Current Branch','الفرع الحالي'],['Local Changes','التغييرات المحلية'],['Unpushed Commits','الالتزامات غير المدفوعة'],
    ['Preview Diff','معاينة الفروق'],['Review & Sync','مراجعة ومزامنة'],['Manage Connection & Repository','إدارة الاتصال والمستودع'],['Verify & Connect','تحقق واربط'],['Disconnect GitHub','فصل GitHub'],
    ['Evolution API — Platform Settings','Evolution API — إعدادات المنصة'],['Not configured','غير معد'],['Not saved','غير محفوظ'],['Save Platform Settings','حفظ إعدادات المنصة'],['Test Connection','اختبار الاتصال'],['Current Status','الحالة الحالية'],['Last test','آخر اختبار'],['Last success','آخر نجاح'],
    ['Plan Management','إدارة الباقات'],['Version Management','إدارة الإصدارات'],['Published','منشورة'],['Draft','مسودة'],['Archived','مؤرشف'],['Only drafts can be edited','يمكن تعديل المسودات فقط'],['Search by name or ID','ابحث بالاسم أو المعرف'],['Arabic Name','الاسم العربي'],['English Name','الاسم الإنجليزي'],['Unlimited','غير محدود'],['Undefined','غير معرفة'],['Value','قيمة'],['Save Draft','حفظ المسودة'],['Publish Version','نشر الإصدار'],
    ['Commercial Operations','التشغيل التجاري'],['Commercial Operations Dashboard','لوحة التشغيل التجاري'],['At-risk subscriptions','اشتراكات معرضة'],['Overdue invoices','فواتير متأخرة'],['Enabled companies','شركات مفعلة'],['Usage assignments','تعيينات استخدام'],['Total outstanding invoices','إجمالي الفواتير المستحقة'],['Global Safety Controls','مفاتيح الأمان العامة'],['Run Reconcile Now','تشغيل المطابقة الآن'],['Usage Alerts','تنبيهات استخدام'],['Enable Enforcement','تفعيل Enforcement'],['Automated Subscription Lifecycle','دورة الاشتراك الآلية'],['Automated Invoice Creation','إنشاء الفواتير آليًا'],['Customer Portal','بوابة العميل'],['Plan Pricing','تسعير الباقات'],['Add-on Catalog','كتالوج الإضافات']
  ];
  const enToAr=new Map(pairs);
  const arToEn=new Map(pairs.map((p)=>[p[1],p[0]]));
  const norm=(v)=>String(v==null?'':v).trim().replace(/\s+/g,' ');
  const read=()=>{try{const v=localStorage.getItem(KEY);return v==='ar'||v==='en'?v:'en';}catch{return 'en';}};
  const write=(v)=>{try{localStorage.setItem(KEY,v);}catch{}};
  const current=()=>root.dataset.saLang==='ar'?'ar':'en';
  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar')return enToAr.get(raw)||raw;return arToEn.get(raw)||raw;};
  const translateText=(node)=>{const p=node&&node.parentElement;if(!p||/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(p.tagName))return;const cur=node.nodeValue||'';const trimmed=cur.trim();if(!trimmed)return;const next=translate(trimmed);if(next===trimmed)return;const lead=(cur.match(/^\s*/)||[''])[0],trail=(cur.match(/\s*$/)||[''])[0];node.nodeValue=lead+next+trail;};
  const translateAttrs=(el)=>{if(!(el instanceof Element))return;['placeholder','title','aria-label'].forEach((name)=>{if(!el.hasAttribute(name))return;const cur=el.getAttribute(name)||'';const next=translate(cur);if(next!==norm(cur))el.setAttribute(name,next);});};
  const syncButton=(b)=>{if(!(b instanceof HTMLButtonElement))return;const ar=current()==='ar';b.textContent=ar?'EN':'AR';const label=ar?'التبديل إلى الإنجليزية':'Switch to Arabic';b.title=label;b.setAttribute('aria-label',label);};
  const makeButton=(host,kind)=>{if(!(host instanceof HTMLElement))return null;let b=host.querySelector('[data-sa-language-v18="'+kind+'"]');if(!(b instanceof HTMLButtonElement)){b=document.createElement('button');b.type='button';b.className='sa-language-inline sa-language-v18';b.dataset.saLanguageV18=kind;b.addEventListener('click',(e)=>{e.preventDefault();e.stopPropagation();apply(current()==='ar'?'en':'ar',true);burst();});host.appendChild(b);}syncButton(b);return b;};
  const ensureControls=()=>{const login=document.querySelector('#loginView');if(login instanceof HTMLElement&&!login.classList.contains('hidden')){let host=login.querySelector('.tamiyouzLoginUtility');if(!(host instanceof HTMLElement)){host=login.querySelector('.sa-language-v18-login-host');if(!(host instanceof HTMLElement)){host=document.createElement('div');host.className='sa-language-v18-login-host';Object.assign(host.style,{position:'absolute',top:'18px',right:'22px',zIndex:'100000',display:'flex',alignItems:'center',gap:'8px'});login.appendChild(host);}}makeButton(host,'login');}const shell=document.querySelector('#appShell');if(shell instanceof HTMLElement&&!shell.classList.contains('hidden')){let top=shell.querySelector('.topbarActions');if(!(top instanceof HTMLElement))top=shell.querySelector('.topbar');if(top instanceof HTMLElement)makeButton(top,'topbar');let dock=document.querySelector('.sa-ui-dock');if(!(dock instanceof HTMLElement)){dock=document.createElement('div');dock.className='sa-ui-dock sa-ui-dock-v18';document.body.appendChild(dock);}makeButton(dock,'dock');}};
  const pinCritical=()=>{const setText=(sel,en,ar)=>{const el=document.querySelector(sel);if(!(el instanceof HTMLElement))return;const v=current()==='ar'?ar:en;if(norm(el.textContent)!==v)el.textContent=v;};const setAttr=(sel,name,en,ar)=>{const el=document.querySelector(sel);if(!(el instanceof Element))return;const v=current()==='ar'?ar:en;if(el.getAttribute(name)!==v)el.setAttribute(name,v);};setText('#loginView .tamiyouzBrandContent h1','Platform administration, simplified.','إدارة المنصة، ببساطة.');setText('#loginView .tamiyouzBrandContent p','Secure, multi-tenant control for your entire TCRMMT ecosystem.','تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.');setAttr('#topGlobalSearch','placeholder','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط');setAttr('#topGlobalSearch','aria-label','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط');setAttr('#globalSearchBox','placeholder','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');setAttr('#globalSearchBox','aria-label','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');};
  const sweep=()=>{if(!document.body)return;const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n=w.nextNode();while(n){translateText(n);n=w.nextNode();}document.querySelectorAll('[placeholder],[title],[aria-label]').forEach(translateAttrs);pinCritical();ensureControls();};
  const apply=(lang,persist)=>{const v=lang==='ar'?'ar':'en';root.dataset.saLang=v;root.lang=v;root.dir=v==='ar'?'rtl':'ltr';if(document.body)document.body.dir=root.dir;if(persist)write(v);sweep();};
  let timer=0;const schedule=()=>{if(timer)return;timer=window.setTimeout(()=>{timer=0;sweep();},40);};
  const burst=()=>{[0,60,250,900,2000].forEach((d)=>window.setTimeout(sweep,d));};
  const boot=()=>{root.dataset.saBilingualRuntime=VERSION;const initial=read();write(initial);apply(initial,false);ensureControls();burst();const observer=new MutationObserver(schedule);observer.observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['class','hidden','aria-selected','placeholder','title','aria-label']});window.addEventListener('pageshow',burst);window.addEventListener('focus',schedule);};
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();
})();
