#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_2'
V11_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_1'
JS_ANCHOR = '  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_1\n'
CSS_ANCHOR = 'html[data-sa-lang="en"] .sa-ui-dock{direction:ltr}\n/* END SUPER_ADMIN_BILINGUAL_AR_EN_V1 */'
OLD_TRIMMED = "    const trimmed=raw.trim();"
OLD_ENGLISH = "    const english=I18N_V11_AR_EN[trimmed]||I18N_AR_EN[trimmed]||trimmed;"
OLD_NEXT = "    const next=currentLanguage()==='ar'?(I18N_V11_EN_AR[english]||I18N_EN_AR[english]||trimmed):english;"
DOC_ANCHOR = "    document.querySelectorAll('[placeholder],[title],[aria-label],input[type=\"button\"],input[type=\"submit\"],input[type=\"reset\"]').forEach(translateAttributes);\n    syncLanguageControls();"

CSS = r'''

/* SUPER_ADMIN_BILINGUAL_AR_EN_V1_2 */
html[data-sa-lang="ar"] #loginView .tamiyouzFormKicker::after{content:' · للمالك فقط'!important}
html[data-sa-lang="en"] #loginView .tamiyouzFormKicker::after{content:' · OWNER ONLY'!important}
/* END SUPER_ADMIN_BILINGUAL_AR_EN_V1_2 */
'''

JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_2
  // Coverage map is intentionally limited to audited static Super Admin copy.
  // Record values, names, emails, URLs, slugs, tokens and product identifiers are not translated.
  const I18N_V12_AR_EN=Object.freeze({
    'تفاصيل المؤشرات':'Metric Details',
    'أكثر الإجراءات استخداماً بدون فتح شاشات إضافية.':'Most-used actions without opening additional screens.',
    'آخر الدخول والإجراءات الحساسة.':'Recent sign-ins and sensitive actions.',
    'تجديد / تحديث الاشتراك':'Renew / Update Subscription',
    'تعديل الخطة والحالة وتاريخ الانتهاء.':'Change the plan, status, and expiration date.',
    'المسؤول يرى الشركات المسندة له فقط ولا يرى مسؤولي المنصة الآخرين.':'The admin sees only assigned companies and cannot see other platform admins.',
    'المظهر، الحساب، وتحميل السورس كود.':'Appearance, Account, and Download Source Code.',
    '🌙 داكن':'🌙 Dark',
    '☀ فاتح':'☀ Light',
    'الحالة، الخطة، الصحة والإجراءات.':'Status, plan, health, and actions.',
    'حسابات نشطة':'Active accounts',
    'إجمالي المسؤولين':'Total admins',
    'المسؤولون النشطون':'Active admins',
    'حسابات متاحة لتسجيل الدخول':'Accounts available for sign-in',
    'الحسابات، الشركات المسندة، آخر دخول والحالة.':'Accounts, assigned companies, last sign-in, and status.',
    'نوع الإجراء':'Action type',
    'التفاصيل التقنية':'Technical details',
    'عرض التفاصيل':'View details',
    'تفاصيل الاتصال والمستودع':'Repository Connection Details',
    'الحالة الحالية للمستودع وGitHub PAT والفرع المحدد.':'Current repository status, GitHub PAT, and selected branch.',
    'اختر باقة لعرض تفاصيلها':'Select a plan to view its details',
    'اشتراكات نشطة':'Active subscriptions',
    'طلبات معلقة':'Pending requests',
    'أي تفعيل يحتاج تأكيدًا صريحًا. Kill Switch يعيد كل الشركات إلى shadow.':'Any activation requires explicit confirmation. Kill Switch returns all companies to shadow mode.',
    'التفاصيل التجارية والتشغيلية الكاملة.':'Complete commercial and operational details.',
    'حالة نشطة':'Active status',
    'أتمتة الإجراءات والتدفقات المتكررة.':'Automate recurring actions and workflows.',
    'الأنشطة':'Activities',
    'المهام والمتابعات والأنشطة المرتبطة بالعملاء.يتطلب: CRM_CORE':'Tasks, follow-ups, and activities linked to customers. Requires: CRM_CORE',
    'المهام والمتابعات والأنشطة المرتبطة بالعملاء. يتطلب: CRM_CORE':'Tasks, follow-ups, and activities linked to customers. Requires: CRM_CORE',
    'الأتمتات النشطة':'Active automations',
    'Webhooks النشطة':'Active Webhooks',
    'الإعداد التلقائي متاح على السيرفر. سيتم تحديث ملف الخدمة وإعادة تشغيل Evolution API بأمان.':'Automatic setup is available on the server. The service file will be updated and Evolution API restarted safely.',

    'تحميل نسخة حقيقية من السورس الحالي للـ SaaS.':'Download a real copy of the current SaaS source.',
    'تحميل نسخة حقيقية من السورس الحالي لـ SaaS.':'Download a real copy of the current SaaS source.',
    'جاري تحميل بيانات السورس...':'Loading source data...',

    'جاري تحميل حالة GitHub...':'Loading GitHub status...',
    'افحص التغييرات، راجع الملفات، ثم نفذ Commit وPush وتحقق من النتيجة.':'Inspect changes, review files, then run Commit and Push and verify the result.',
    'فحص':'Inspect',
    'مراجعة':'Review',
    'تحقق':'Verify',
    'وصف مختصر للتغييرات':'Short description of the changes',
    'ابدأ بمعاينة الفروق لعرض ملخص التغييرات':'Start by previewing the diff to show a change summary',
    'ستظهر الملفات هنا بعد المعاينة.':'Files will appear here after preview.',
    'حالة المزامنة':'Sync status',
    'جاهز للتنفيذ':'Ready to run',
    'لم تبدأ أي عملية بعد.':'No operation has started yet.',
    'جاهز للتنفيذ.':'Ready to run.',
    'معلومات المستودع':'Repository Information',
    'حالة الاتصال و PAT':'Connection & PAT Status',
    'حالة الاتصال وPAT':'Connection & PAT Status',
    'معلومات الفرع والإصدار':'Branch & Revision Information',
    'جاري التحقق من حالة المزامنة...':'Checking sync status...',
    'الصلاحية':'Permission',
    'الاتصال':'Connection',

    'إعداد تكامل Evolution API':'Configure Evolution API Integration',
    'إيقاف يمنع الاتصال والإرسال على مستوى المنصة':'Disabling it prevents platform-wide connection and sending',
    'إيقافه يمنع الاتصال والإرسال على مستوى المنصة':'Disabling it prevents platform-wide connection and sending',
    'جاري تحميل الإعدادات...':'Loading settings...',
    'جاري تحميل الإعدادات':'Loading settings',
    'إعداد مركزي واحد تستخدمه شركات المنصة. متاح لمالك المنصة فقط ولا تعرض الأسرار بعد حفظها.':'One central configuration used by platform companies. Available only to the platform owner; secrets are not shown after saving.',
    'غير معد':'Not configured',
    'تفعيل تكامل Evolution API':'Enable Evolution API integration',
    'اتركه فارغاً للاحتفاظ بالقيمة الحالية':'Leave blank to keep the current value',
    'اتركه فارغًا للاحتفاظ بالقيمة الحالية':'Leave blank to keep the current value',
    'غير محفوظ':'Not saved',
    'قيم آمنة بدون إظهار الأسرار':'Safe values without exposing secrets',
    'جاري فحص إمكانية الإدارة التلقائية...':'Checking automatic management capability...',
    'توليد وربط البيانات':'Generate & Link Data',
    'تدوير البيانات':'Rotate Data',

    'التشغيل التجريبي مفعّل لحماية الشركات':'Trial mode is enabled to protect companies',
    'لا يتم تنفيذ أي تغيير دائم إلا بعد تأكيد صريح':'No permanent change is executed without explicit confirmation',
    'جاري تحميل الباقات...':'Loading plans...',
    'الشركات والاشتراكات':'Companies & Subscriptions',
    'التشغيل والاشتراكات والفوترة':'Operations, Subscriptions & Billing',
    'التشغيل والاشتراكات والتحصيل':'Operations, Subscriptions & Collections',
    'إدارة الباقات':'Plan Management',
    'الإصدارات والخصائص والحدود من مساحة عمل واحدة':'Versions, features, and limits from one workspace',
    'المنشورة والمسودات والإصدارات التاريخية':'Published, draft, and historical versions',
    'يمكن تعديل المسودات فقط':'Only drafts can be edited',
    'ابحث بالاسم أو المعرف':'Search by name or ID',
    'منشورة':'Published',
    'الإصدار':'Version',
    'شركة':'Company',

    'إدارة منصة':'Platform Management',
    'لوحة التحكم الرئيسية':'Main dashboard',
    'دور: مدير النظام':'Role: System Admin'
  });

  const I18N_V12_EN_AR=Object.freeze(Object.assign(
    Object.entries(I18N_V12_AR_EN).reduce((acc,pair)=>{if(!acc[pair[1]])acc[pair[1]]=pair[0];return acc},{}),
    {
      'Platform administration, simplified.':'إدارة المنصة، ببساطة.',
      'Platform administration. Simplified.':'إدارة المنصة، ببساطة.',
      'Platform administration,':'إدارة المنصة،',
      'simplified.':'ببساطة.',
      'Secure, multi-tenant control for your entire TCRMMT ecosystem.':'تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.',
      'Secure platform administration':'إدارة منصة آمنة',
      'Theme':'المظهر',
      'Help':'مساعدة',
      'OWNER ONLY':'للمالك فقط'
    }
  ));

  const translateV12Pattern=(value,lang)=>{
    const raw=String(value==null?'':value);
    if(lang==='en'){
      let m=raw.match(/^الصحة\s+(.+?)\s+·\s+منتهي$/);
      if(m)return 'Health '+m[1]+' · Expired';
      m=raw.match(/^الصحة\s+(.+?)\s+·\s+نشط$/);
      if(m)return 'Health '+m[1]+' · Active';
    }else{
      let m=raw.match(/^Health\s+(.+?)\s+·\s+Expired$/i);
      if(m)return 'الصحة '+m[1]+' · منتهي';
      m=raw.match(/^Health\s+(.+?)\s+·\s+Active$/i);
      if(m)return 'الصحة '+m[1]+' · نشط';
    }
    return raw;
  };

  const setV12LocalizedText=(selector,en,ar)=>{
    const element=document.querySelector(selector);
    if(!(element instanceof HTMLElement))return;
    const desired=currentLanguage()==='ar'?ar:en;
    if(element.textContent!==desired)element.textContent=desired;
  };

  const applyV12CriticalOverrides=()=>{
    setV12LocalizedText('#loginView .tamiyouzBrandContent h1','Platform administration, simplified.','إدارة المنصة، ببساطة.');
    setV12LocalizedText('#loginView .tamiyouzBrandContent p','Secure, multi-tenant control for your entire TCRMMT ecosystem.','تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.');
    setV12LocalizedText('#loginView .tamiyouzLoginUtility span:nth-of-type(1)','◔ Theme','◔ المظهر');
    setV12LocalizedText('#loginView .tamiyouzLoginUtility span:nth-of-type(2)','ⓘ Help','ⓘ مساعدة');
    setV12LocalizedText('#setDarkBtn','🌙 Dark','🌙 داكن');
    setV12LocalizedText('#setLightBtn','☀ Light','☀ فاتح');
    setV12LocalizedText('#settingsDrawer .drawerHead .muted','Appearance, Account, and Download Source Code.','المظهر، الحساب، وتحميل السورس كود.');
    setV12LocalizedText('#sec-github .githubV5SideTitle','Repository Connection Details','تفاصيل الاتصال والمستودع');
    setV12LocalizedText('#sec-github .githubV5SideSubtitle','Current repository status, GitHub PAT, and selected branch.','الحالة الحالية للمستودع وGitHub PAT والفرع المحدد.');
  };
  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_2
'''


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing ambiguous patch application.')
    return text.replace(old, new, 1)


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.2 already applied; no changes made.')
        return
    if V11_MARKER not in text:
        raise SystemExit('Bilingual V1.1 marker not found; apply V1 and V1.1 first.')

    for label, anchor in [
        ('JS V1.1 end', JS_ANCHOR),
        ('CSS bilingual anchor', CSS_ANCHOR),
        ('translate trimmed', OLD_TRIMMED),
        ('translate english', OLD_ENGLISH),
        ('translate target', OLD_NEXT),
        ('translate document', DOC_ANCHOR),
    ]:
        if text.count(anchor) != 1:
            raise SystemExit(f'{label} anchor count is {text.count(anchor)}; refusing unknown baseline.')

    text = replace_once(text, CSS_ANCHOR, CSS_ANCHOR + CSS, 'CSS V1.2')
    text = replace_once(text, JS_ANCHOR, JS_ANCHOR + JS + '\n', 'JS V1.2')
    text = replace_once(text, OLD_TRIMMED, OLD_TRIMMED + "\n    const canonical=trimmed.replace(/\\s+/g,' ');", 'canonical text')
    text = replace_once(
        text,
        OLD_ENGLISH,
        "    const english=I18N_V12_AR_EN[canonical]||I18N_V11_AR_EN[canonical]||I18N_AR_EN[canonical]||canonical;",
        'V1.2 source lookup',
    )
    text = replace_once(
        text,
        OLD_NEXT,
        "    const next0=currentLanguage()==='ar'?(I18N_V12_EN_AR[english]||I18N_V11_EN_AR[english]||I18N_EN_AR[english]||canonical):english;\n    const next=translateV12Pattern(next0,currentLanguage());",
        'V1.2 target lookup',
    )
    text = replace_once(
        text,
        DOC_ANCHOR,
        DOC_ANCHOR.replace('    syncLanguageControls();', '    applyV12CriticalOverrides();\n    syncLanguageControls();'),
        'critical localization overrides',
    )

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual Arabic / English V1.2 coverage corrective patch.')


if __name__ == '__main__':
    main()
