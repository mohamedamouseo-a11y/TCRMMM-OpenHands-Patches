#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1'
CSS_ANCHOR = "\n`;\n\nconst SUPER_ADMIN_JS = String.raw`"
LANG_KEY_ANCHOR = "  const densityKey='tcrm-super-admin-density';\n"
TOP_BUTTON_ANCHOR = "    const top=document.createElement('button');"
DOCK_APPEND_ANCHOR = "    dock.append(theme,density,top);"
ENHANCE_ANCHOR = "      improveTabs();\n      improveForms();"
BOOT_ANCHOR = "  const boot=()=>{\n    applyTheme(readStored(themeKey,preferredTheme()));\n    applyDensity(readStored(densityKey,'comfortable'));"
OBSERVER_ANCHOR = "    observer.observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['class','aria-selected','aria-busy','hidden']});"

CSS = r'''

/* SUPER_ADMIN_BILINGUAL_AR_EN_V1 */
html[data-sa-lang="ar"] body{direction:rtl!important}
html[data-sa-lang="en"] body{direction:ltr!important}
html[data-sa-lang="ar"] #appShell{direction:rtl!important}
html[data-sa-lang="en"] #appShell{direction:ltr!important}
html[data-sa-lang="ar"] #appShell th,
html[data-sa-lang="ar"] #appShell td{text-align:right!important}
html[data-sa-lang="en"] #appShell th,
html[data-sa-lang="en"] #appShell td{text-align:left!important}
html[data-sa-lang="ar"] #appShell input:not([type="email"]):not([type="url"]):not([type="tel"]):not([type="number"]),
html[data-sa-lang="ar"] #appShell textarea{text-align:right}
html[data-sa-lang="en"] #appShell input:not([type="email"]):not([type="url"]):not([type="tel"]):not([type="number"]),
html[data-sa-lang="en"] #appShell textarea{text-align:left}
html[data-sa-lang="ar"] #loginView .tamiyouzLoginShell,
html[data-sa-lang="ar"] #loginView .tamiyouzLoginBrandPanel,
html[data-sa-lang="ar"] #loginView .tamiyouzLoginMain,
html[data-sa-lang="ar"] #loginView .tamiyouzLoginCard,
html[data-sa-lang="ar"] #loginView .tamiyouzLoginForm,
html[data-sa-lang="ar"] #loginView .tamiyouzRecoveryPanel{direction:rtl!important;text-align:right!important}
html[data-sa-lang="en"] #loginView .tamiyouzLoginShell,
html[data-sa-lang="en"] #loginView .tamiyouzLoginBrandPanel,
html[data-sa-lang="en"] #loginView .tamiyouzLoginMain,
html[data-sa-lang="en"] #loginView .tamiyouzLoginCard,
html[data-sa-lang="en"] #loginView .tamiyouzLoginForm,
html[data-sa-lang="en"] #loginView .tamiyouzRecoveryPanel{direction:ltr!important;text-align:left!important}
html[data-sa-lang="ar"] #loginView .tamiyouzRecoveryRow{direction:rtl!important;justify-content:flex-start!important}
html[data-sa-lang="en"] #loginView .tamiyouzRecoveryRow{direction:ltr!important;justify-content:flex-end!important}
html[data-sa-lang="ar"] #loginView .tamiyouzInputWrap input,
html[data-sa-lang="en"] #loginView .tamiyouzInputWrap input{direction:ltr!important;text-align:left!important}
.sa-language-inline{
  min-height:34px;padding:6px 10px;border:1px solid var(--sa-line,#dce4ef);border-radius:10px;
  background:var(--sa-surface,#fff);color:var(--sa-text,#102038);font:inherit;font-size:11px;font-weight:850;
  cursor:pointer;white-space:nowrap;box-shadow:var(--sa-shadow-1,0 1px 2px rgba(15,23,42,.05));
}
.sa-language-inline:hover{border-color:color-mix(in srgb,var(--sa-primary,#3357dc) 35%,var(--sa-line,#dce4ef));color:var(--sa-primary,#3357dc)}
html[data-sa-theme="dark"] .sa-language-inline,
html[data-theme="dark"] .sa-language-inline{background:#142238;border-color:#2d4059;color:#eef4fb}
html[data-sa-lang="ar"] .sa-ui-dock{direction:rtl}
html[data-sa-lang="en"] .sa-ui-dock{direction:ltr}
/* END SUPER_ADMIN_BILINGUAL_AR_EN_V1 */
'''

JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1
  const languageKey='tcrm-super-admin-language';
  const I18N_EN_AR=Object.freeze({
    'Overview':'نظرة عامة','Dashboard':'لوحة التحكم','Executive Command Center':'مركز القيادة التنفيذي',
    'Companies':'الشركات','Company':'الشركة','Company Details':'تفاصيل الشركة','Tenant Details':'تفاصيل الشركة','Tenants':'الشركات',
    'Users':'المستخدمون','User':'المستخدم','Platform Admins':'مسؤولو المنصة','Platform Admin':'مسؤول المنصة',
    'Plans':'الباقات','Plans Catalog':'دليل الباقات','Plan Catalog':'دليل الباقات','Plans Editor':'محرر الباقات','Plan Editor':'محرر الباقة',
    'Company Overrides':'استثناءات الشركات','Companies Overrides':'استثناءات الشركات','Commercial':'التجاري','Billing':'الفوترة','Subscriptions':'الاشتراكات','Subscription':'الاشتراك',
    'Activity':'النشاط','Recent Activity':'النشاط الأخير','Audit':'التدقيق','Audit Log':'سجل التدقيق','Operations':'العمليات','Integrations':'التكاملات',
    'GitHub Sync':'مزامنة GitHub','Evolution API':'Evolution API','Tara APIs':'واجهات Tara API','System Settings':'إعدادات النظام','Settings':'الإعدادات',
    'General':'عام','Account':'الحساب','Appearance':'المظهر','Source Code':'الكود المصدري','Owner Only':'للمالك فقط','OWNER ONLY':'للمالك فقط',
    'Security':'الأمان','Security Review':'مراجعة الأمان','Usage':'الاستخدام','Usage Overview':'نظرة على الاستخدام','Alerts':'التنبيهات','Notifications':'الإشعارات',
    'Quick Actions':'إجراءات سريعة','Global Search':'البحث الشامل','Search':'بحث','Search companies':'بحث في الشركات','Search users':'بحث في المستخدمين',
    'Recent Tenants':'الشركات الأخيرة','Recent Companies':'الشركات الأخيرة','Status':'الحالة','Health':'الحالة الصحية','Role':'الدور','Roles':'الأدوار','Permissions':'الصلاحيات',
    'Name':'الاسم','Email':'البريد الإلكتروني','Email address':'عنوان البريد الإلكتروني','Phone':'الهاتف','Domain':'النطاق','Slug':'المعرّف','ID':'المعرّف',
    'Created':'تاريخ الإنشاء','Created At':'تاريخ الإنشاء','Updated':'آخر تحديث','Last Updated':'آخر تحديث','Last Login':'آخر تسجيل دخول','Last Activity':'آخر نشاط',
    'Active':'نشط','Inactive':'غير نشط','Suspended':'موقوف','Cancelled':'ملغي','Expired':'منتهي','Pending':'قيد الانتظار','Trial':'تجريبي','Trialing':'تجريبي',
    'Paid':'مدفوع','Open':'مفتوح','Failed':'فشل','Success':'نجاح','Healthy':'سليم','Warning':'تحذير','Error':'خطأ','Ready':'جاهز','Not ready':'غير جاهز',
    'Actions':'الإجراءات','Action':'إجراء','View':'عرض','Open':'فتح','Edit':'تعديل','Save':'حفظ','Save Changes':'حفظ التغييرات','Cancel':'إلغاء','Close':'إغلاق',
    'Delete':'حذف','Remove':'إزالة','Add':'إضافة','Create':'إنشاء','Update':'تحديث','Refresh':'تحديث','Retry':'إعادة المحاولة','Apply':'تطبيق','Reset':'إعادة ضبط',
    'Download':'تنزيل','Download Source Code':'تنزيل الكود المصدري','Refresh Source Code':'تحديث الكود المصدري','Export':'تصدير','Import':'استيراد','Copy':'نسخ',
    'Enable':'تفعيل','Disable':'تعطيل','Enabled':'مفعّل','Disabled':'معطّل','Connect':'اتصال','Disconnect':'قطع الاتصال','Connected':'متصل','Disconnected':'غير متصل',
    'Light':'فاتح','Dark':'داكن','Light Mode':'الوضع الفاتح','Dark Mode':'الوضع الداكن','Theme':'المظهر','Help':'مساعدة','Logout':'تسجيل الخروج','Sign Out':'تسجيل الخروج',
    'Details':'التفاصيل','Summary':'الملخص','Metrics':'المؤشرات','Insights':'الرؤى','Smart Insights':'رؤى ذكية','Operations Pulse':'نبض العمليات','Command Details':'تفاصيل القيادة',
    'Plan':'الباقة','Current Plan':'الباقة الحالية','New Plan':'الباقة الجديدة','Price':'السعر','Monthly':'شهري','Yearly':'سنوي','Monthly Price':'السعر الشهري','Annual Price':'السعر السنوي',
    'Currency':'العملة','Limit':'الحد','Limits':'الحدود','Feature':'الميزة','Features':'المميزات','Seats':'المقاعد','Storage':'التخزين','API':'واجهة API',
    'Company Name':'اسم الشركة','Company Status':'حالة الشركة','User Name':'اسم المستخدم','User Status':'حالة المستخدم','Super Admin':'Super Admin','Primary Super Admin':'Super Admin الرئيسي',
    'SUPER ADMIN ACCESS':'دخول SUPER ADMIN','SUPER ADMIN ACCESS · OWNER ONLY':'دخول SUPER ADMIN · للمالك فقط',
    'Welcome back':'مرحباً بعودتك','Sign in to your TCRMMT workspace.':'سجّل الدخول إلى مساحة عمل TCRMMT.',
    'Password':'كلمة المرور','Show':'إظهار','Hide':'إخفاء','Show password':'إظهار كلمة المرور','Hide password':'إخفاء كلمة المرور',
    'Forgot password?':'هل نسيت كلمة المرور؟','Sign In':'تسجيل الدخول','Reset your password':'إعادة تعيين كلمة المرور',
    'Back to sign in':'العودة لتسجيل الدخول','Send reset link':'إرسال رابط الاستعادة','Reset Password':'إعادة تعيين كلمة المرور',
    'New password':'كلمة المرور الجديدة','Confirm password':'تأكيد كلمة المرور','Protected administration':'إدارة محمية',
    'Your session is protected with secure authentication.':'جلستك محمية بمصادقة آمنة.',
    'Platform administration. Simplified.':'إدارة المنصة. ببساطة.','Multi-tenant platform':'منصة متعددة الشركات',
    'Loading':'جارٍ التحميل','Loading...':'جارٍ التحميل...','No data':'لا توجد بيانات','No results':'لا توجد نتائج','No results found':'لا توجد نتائج',
    'Select':'اختر','All':'الكل','All statuses':'كل الحالات','Filter':'تصفية','Clear':'مسح','Clear filters':'مسح عوامل التصفية','Previous':'السابق','Next':'التالي',
    'Page':'صفحة','Rows per page':'صفوف لكل صفحة','Total':'الإجمالي','Total Companies':'إجمالي الشركات','Total Users':'إجمالي المستخدمين','Active Companies':'الشركات النشطة',
    'Active Users':'المستخدمون النشطون','MRR':'الإيراد الشهري المتكرر','Revenue':'الإيرادات','System Health':'صحة النظام','Platform Health':'صحة المنصة',
    'Today':'اليوم','This Week':'هذا الأسبوع','This Month':'هذا الشهر','Last 7 days':'آخر 7 أيام','Last 30 days':'آخر 30 يوماً',
    'GitHub':'GitHub','Repository':'المستودع','Branch':'الفرع','Commit':'Commit','Sync':'مزامنة','Sync Now':'مزامنة الآن','Last Sync':'آخر مزامنة',
    'API Status':'حالة API','Endpoint':'نقطة النهاية','Token':'Token','Instance':'Instance','Webhook':'Webhook','Webhooks':'Webhooks',
    'Settings saved successfully.':'تم حفظ الإعدادات بنجاح.','Changes saved successfully.':'تم حفظ التغييرات بنجاح.','Unable to load data.':'تعذر تحميل البيانات.',
    'Try again':'حاول مرة أخرى','Confirm':'تأكيد','Are you sure?':'هل أنت متأكد؟',
    'Skip to content':'تخطي إلى المحتوى','Appearance tools':'أدوات المظهر','Back to top':'العودة لأعلى الصفحة',
    'Enable light mode':'تفعيل الوضع الفاتح','Enable dark mode':'تفعيل الوضع الداكن','Use comfortable density':'تفعيل المسافات المريحة','Use compact density':'تفعيل العرض المضغوط',
    'تخطي إلى المحتوى':'تخطي إلى المحتوى','أدوات المظهر':'أدوات المظهر','العودة لأعلى الصفحة':'العودة لأعلى الصفحة',
    'تفعيل الوضع الفاتح':'تفعيل الوضع الفاتح','تفعيل الوضع الداكن':'تفعيل الوضع الداكن','تفعيل المسافات المريحة':'تفعيل المسافات المريحة','تفعيل العرض المضغوط':'تفعيل العرض المضغوط',
    'الإعدادات':'الإعدادات','المظهر، الحساب، وتحميل السورس كود.':'المظهر، الحساب، وتنزيل الكود المصدري.','الحساب':'الحساب','الكود المصدري':'الكود المصدري','غير جاهز':'غير جاهز'
  });
  const I18N_AR_EN=Object.freeze(Object.entries(I18N_EN_AR).reduce((acc,pair)=>{if(!acc[pair[1]])acc[pair[1]]=pair[0];return acc},{}));
  const textSource=new WeakMap();
  const textRendered=new WeakMap();
  const attrState=new WeakMap();
  const currentLanguage=()=>root.dataset.saLang==='ar'?'ar':'en';
  const translateExact=value=>{
    const raw=String(value==null?'':value);
    const trimmed=raw.trim();
    if(!trimmed)return raw;
    const english=I18N_AR_EN[trimmed]||trimmed;
    const next=currentLanguage()==='ar'?(I18N_EN_AR[english]||trimmed):english;
    return next;
  };
  const translatePreservingSpace=value=>{
    const raw=String(value==null?'':value);
    const match=raw.match(/^(\s*)([\s\S]*?)(\s*)$/);
    if(!match)return translateExact(raw);
    return match[1]+translateExact(match[2])+match[3];
  };
  const translateTextNode=node=>{
    const parent=node.parentElement;
    if(!parent||/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(parent.tagName))return;
    const current=node.nodeValue||'';
    let source=textSource.get(node);
    const last=textRendered.get(node);
    if(source===undefined||(last!==undefined&&current!==last)){source=current;textSource.set(node,source)}
    const desired=translatePreservingSpace(source);
    if(current!==desired)node.nodeValue=desired;
    textRendered.set(node,desired);
  };
  const translateAttributes=element=>{
    if(!(element instanceof Element))return;
    const attrs=['placeholder','title','aria-label'];
    if(element instanceof HTMLInputElement&&(element.type==='button'||element.type==='submit'||element.type==='reset'))attrs.push('value');
    let state=attrState.get(element);
    if(!state){state={source:{},rendered:{}};attrState.set(element,state)}
    attrs.forEach(name=>{
      if(!element.hasAttribute(name))return;
      const current=element.getAttribute(name)||'';
      if(state.source[name]===undefined||(state.rendered[name]!==undefined&&current!==state.rendered[name]))state.source[name]=current;
      const desired=translateExact(state.source[name]);
      if(current!==desired)element.setAttribute(name,desired);
      state.rendered[name]=desired;
    });
  };
  const translateDocument=()=>{
    if(!document.body)return;
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    let node=walker.nextNode();
    while(node){translateTextNode(node);node=walker.nextNode()}
    document.querySelectorAll('[placeholder],[title],[aria-label],input[type="button"],input[type="submit"],input[type="reset"]').forEach(translateAttributes);
    syncLanguageControls();
  };
  const syncLanguageControls=()=>{
    const ar=currentLanguage()==='ar';
    document.querySelectorAll('[data-sa-language-toggle],[data-sa-language-inline]').forEach(button=>{
      if(!(button instanceof HTMLElement))return;
      button.textContent=ar?'EN':'AR';
      button.title=ar?'Switch to English':'التبديل إلى العربية';
      button.setAttribute('aria-label',button.title);
    });
  };
  const applyLanguage=value=>{
    const lang=value==='ar'?'ar':'en';
    root.dataset.saLang=lang;
    root.lang=lang;
    root.dir=lang==='ar'?'rtl':'ltr';
    if(document.body)document.body.dir=root.dir;
    translateDocument();
  };
  const toggleLanguage=()=>{
    const next=currentLanguage()==='ar'?'en':'ar';
    try{localStorage.setItem(languageKey,next)}catch{}
    applyLanguage(next);
  };
  const ensureLanguageControls=()=>{
    [document.querySelector('#loginView .tamiyouzLoginUtility'),document.querySelector('#appShell .topbarActions')].forEach(host=>{
      if(!(host instanceof HTMLElement)||host.querySelector('[data-sa-language-inline]'))return;
      const button=document.createElement('button');
      button.type='button';button.className='sa-language-inline';button.dataset.saLanguageInline='1';
      button.addEventListener('click',toggleLanguage);
      host.appendChild(button);
    });
    syncLanguageControls();
  };
  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1
'''

LANG_BUTTON = r'''    const language=document.createElement('button');
    language.type='button';language.dataset.saLanguageToggle='1';
    language.addEventListener('click',toggleLanguage);
'''


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing ambiguous patch application.')
    return text.replace(old, new, 1)


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual AR/EN V1 already applied; no changes made.')
        return

    for token in [CSS_ANCHOR, LANG_KEY_ANCHOR, TOP_BUTTON_ANCHOR, DOCK_APPEND_ANCHOR, ENHANCE_ANCHOR, BOOT_ANCHOR, OBSERVER_ANCHOR]:
        if token not in text:
            raise SystemExit('Expected Super Admin UI polish baseline anchor is missing; refusing unknown baseline.')

    text = replace_once(text, CSS_ANCHOR, CSS + CSS_ANCHOR, 'CSS')
    text = replace_once(text, LANG_KEY_ANCHOR, LANG_KEY_ANCHOR + JS, 'language engine')
    text = replace_once(text, TOP_BUTTON_ANCHOR, LANG_BUTTON + TOP_BUTTON_ANCHOR, 'dock language button')
    text = replace_once(text, DOCK_APPEND_ANCHOR, "    dock.append(theme,density,language,top);", 'dock append')
    text = replace_once(text, ENHANCE_ANCHOR, ENHANCE_ANCHOR + "\n      ensureLanguageControls();\n      translateDocument();", 'enhance localization')
    text = replace_once(text, BOOT_ANCHOR, BOOT_ANCHOR + "\n    applyLanguage(readStored(languageKey,'en'));", 'boot localization')
    text = replace_once(
        text,
        OBSERVER_ANCHOR,
        "    observer.observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['class','aria-selected','aria-busy','hidden','placeholder','title','aria-label','value']});",
        'observer localization',
    )

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin bilingual Arabic/English V1 localization layer.')


if __name__ == '__main__':
    main()
