#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_3'
V12_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_2'
JS_ANCHOR = '  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_2\n'
OLD_NEXT = "    const next=translateV12Pattern(next0,currentLanguage());"
DOC_ANCHOR = "    applyV12CriticalOverrides();\n    syncLanguageControls();"

JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_3
  // Phrase-level translation coverage derived only from live V1.2 audit findings.
  // This deliberately targets static UI copy and avoids names, emails, IDs, URLs,
  // slugs, tokens, repository/branch values, plan identifiers and user-provided data.
  const I18N_V13_AR_EN=Object.freeze({
    // Overview / command center
    'مؤشرات المنصة والقرارات التنفيذية في شاشة واحدة':'Platform metrics and executive decisions in one screen',
    'أهم مؤشرات التشغيل والمخاطر والقرارات في شاشة واحدة واضحة.':'Key operational metrics, risks, and decisions in one clear screen.',
    'بيانات مباشرة':'Live data',
    'مخاطر تحتاج متابعة':'Risks need attention',
    'صحة أو حالة تشغيلية':'Health or operational status',
    'تجارب تنتهي قريبًا':'Trials ending soon',
    'خلال 7 أيام':'Within 7 days',
    'اشتراكات متأخرة':'Overdue subscriptions',
    'متأخر أو منتهي':'Overdue or expired',
    'شركات تعمل الآن':'Companies active now',
    'قرار اليوم':'Today’s decision',
    'مؤشر الاشتراكات':'Subscription indicator',
    'ثبات التشغيل':'Operational stability',
    'الإيرادات، الجاهزية، الاشتراكات وباقي الأرقام التشغيلية':'Revenue, readiness, subscriptions, and other operational metrics',
    'إنشاء Workspace جديد':'Create a new Workspace',
    'فتح قائمة الشركات':'Open Companies',
    'مراجعة الأحداث الحساسة':'Review sensitive events',
    'من إعدادات المنصة':'From platform settings',
    'تحديث الاستخدام':'Refresh Usage',
    'تحديث مؤشرات الخطط':'Refresh plan metrics',
    'عرض التنبيهات الحالية':'View current alerts',
    'أولوية التنفيذ والمخاطر الحالية.':'Execution priority and current risks.',
    'استهلاك الشركات مقابل حدود الباقات.':'Company usage versus plan limits.',
    'شركة، فاتورة أو نشاط.':'Company, invoice, or activity.',
    'اكتب كلمتين على الأقل للبحث.':'Enter at least two words to search.',
    'إضافة شركة':'Add Company',
    'تحميل السورس':'Download Source',
    'راجع':'Review',
    'تحكم':'Control',
    'المستخدمون':'Users',
    'العملاء':'Clients',
    'أمان':'Security',

    // Companies / drawers / tenant details
    'إدارة الشركات':'Companies Management',
    'بحث ومتابعة الاشتراكات والحالة التشغيلية لكل شركة':'Search and track subscriptions and operational status for every company',
    'معروضة من أصل':'shown of',
    'مخاطر':'Risks',
    'كل الخطط':'All plans',
    'من تاريخ':'From date',
    'إلى تاريخ':'To date',
    'الصفوف':'Rows',
    'عرض مريح':'Comfortable view',
    'قائمة الشركات':'Companies list',
    'ترقيم صفحات من الخادم':'Server-side pagination',
    'إنشاء شركة جديدة':'Create New Company',
    'سيتم إرسال الطلب إلى Provisioning Queue.':'The request will be sent to the Provisioning Queue.',
    'إيميل الأدمن':'Admin Email',
    'اسم الأدمن':'Admin Name',
    'كلمة مرور قوية':'Strong Password',
    'المدة بالأيام':'Duration in days',
    'سيتم إنشاء الطلب داخل Queue بدون تعطيل اللوحة.':'The request will be created in the Queue without blocking the dashboard.',
    'نهاية الاشتراك':'Subscription End',
    'ملاحظة (اختياري)':'Note (optional)',
    'حفظ الاشتراك':'Save Subscription',
    'ملف الشركة':'Company Profile',
    'عرض ذكي لبيانات الشركة والاشتراك والفواتير.':'Smart view of company, subscription, and billing data.',
    'دخول كأدمن الشركة':'Sign in as Company Admin',
    'الفواتير والدفع':'Billing & Payments',
    'سجل الشركة':'Company Log',
    'حالة التشغيل':'Operational Status',
    'صحة الحساب':'Account Health',
    'نهاية التجربة':'Trial End',
    'العملاء المحتملون':'Leads',
    'الاستخدام مقابل الخطة':'Usage vs Plan',
    'تفعيل الشركة':'Activate Company',
    'إيقاف مؤقت':'Suspend',
    'إعادة إرسال بيانات الترحيب':'Resend Welcome Credentials',
    'إضافة Admin':'Add Admin',
    'إلزامية عند الإنشاء':'Required when creating',
    'استخدم Ctrl/Cmd لاختيار أكثر من شركة':'Use Ctrl/Cmd to select multiple companies',
    'حفظ Admin وصلاحيات الشركات':'Save Admin & Company Permissions',
    'تظهر مرة واحدة فقط ولا يتم حفظها كنص صريح.':'Shown only once and never stored as plain text.',

    // Settings / source-code drawer
    'اسم الملف':'File Name',
    'حجم الملف':'File Size',
    'يُحسب عند التنزيل':'Calculated on download',
    'آخر Build موثّق':'Last Verified Build',
    'بصمة السورس':'Source Fingerprint',
    'ملفات السورس المحتسبة':'Counted Source Files',
    'مسار التشغيل الفعلي':'Actual Runtime Path',
    'المسار المضبوط':'Configured Path',
    'السورس على القرص لا يطابق النسخة المبنية العاملة. شغّل Build ثم Restart.':'Source on disk does not match the running build. Run Build then Restart.',

    // GitHub Sync live status copy
    '● متصل':'● Connected',
    '⟳ تحديث الحالة':'⟳ Refresh Status',
    'حالة الاتصال':'Connection Status',
    'آخر فحص ناجح':'Last Successful Check',
    'الفرع الحالي':'Current Branch',
    'التغييرات المحلية موجودة':'Local Changes Present',
    'التغييرات المحلية':'Local Changes',
    'يوجد تغييرات تحتاج مراجعة':'Changes need review',
    'الالتزامات غير المدفوعة':'Unpushed Commits',
    'جاهزة للمزامنة':'Ready to Sync',
    'Fine-grained PAT محفوظ':'Fine-grained PAT saved',
    'ينتظر النشر':'Awaiting deployment',
    'التغييرات محلية على الخادم. لم يتم تنفيذ أي نشر بعد.':'Changes are local on the server. No deployment has been performed yet.',
    'ابدأ بمعاينة الفروق لعرض ملخص التغييرات.':'Start by previewing the diff to show a change summary.',

    // Evolution API live status/helper copy
    'Evolution API — إعدادات المنصة':'Evolution API — Platform Settings',
    'إعداد مركزي واحد تستخدمه شركات المنصة. متاح لمالك المنصة فقط ولا تعرض الأسرار بعد حفظها.':'One central configuration used by platform companies. Available only to the platform owner; secrets are not shown after saving.',
    'غير مُعد':'Not configured',
    'غير معد':'Not configured',
    'إيقافه يمنع الاتصال والإرسال على مستوى المنصة.':'Disabling it prevents platform-wide connection and sending.',
    'إيقافه يمنع الاتصال والإرسال على مستوى المنصة':'Disabling it prevents platform-wide connection and sending',
    'غير محفوظ':'Not saved',
    'حفظ إعدادات المنصة':'Save Platform Settings',
    'اختبار الاتصال':'Test Connection',
    'تحديث الحالة':'Refresh Status',
    'الحالة الحالية':'Current Status',
    'قيم آمنة بدون إظهار الأسرار.':'Safe values without exposing secrets.',
    'قيم آمنة بدون إظهار الأسرار':'Safe values without exposing secrets',
    'جاري تحميل إعدادات Evolution API...':'Loading Evolution API settings...',
    'يقيّم إمكانية توليد وإدارة بيانات الربط بأمان.':'Evaluates whether connection data can be generated and managed safely.',
    'يقيم إمكانية توليد وإدارة بيانات الربط بأمان.':'Evaluates whether connection data can be generated and managed safely.',

    // Plans / catalog / editor
    'التشغيل التدريجي مفعّل لحماية الشركات':'Gradual rollout is enabled to protect companies',
    'التشغيل التجريبي مفعّل لحماية الشركات':'Trial mode is enabled to protect companies',
    'الإعدادات الحساسة لا تعمل إلا بعد تأكيد صريح.':'Sensitive settings only take effect after explicit confirmation.',
    'إدارة الإصدارات والخصائص والحدود':'Manage versions, features, and limits',
    'إدارة الإصدارات والخصائص والحدود من مساحة عمل واحدة واضحة':'Manage versions, features, and limits from one clear workspace',
    'الإصدارات والخصائص والحدود':'Versions, features, and limits',
    'التعيين وحدود كل شركة':'Assignment and per-company limits',
    'التفعيل والاستهلاك والتحصيل':'Activation, usage, and collections',
    'التفعيل والاستهلاك والتحصيل':'Activation, usage, and collections',
    'التفعيل والاستهلاك والفوترة':'Activation, usage, and billing',
    'يمكن تعديل المسودات فقط':'Only drafts can be edited',
    'الخصائص المستقبلية مقفولة ولا تعمل حاليًا.':'Future features are locked and currently inactive.',
    'الخصائص المستقبلية مقفولة ولا تعمل حاليا.':'Future features are locked and currently inactive.',
    'ابحث بالاسم أو المعرف':'Search by name or ID',
    'ابحث بالاسم أو المحتوى':'Search by name or content',
    'الاسم العربي':'Arabic Name',
    'الاسم الإنجليزي':'English Name',
    'معرّف النسخة الجديدة':'New Version ID',
    'معلومة الإصدار':'Version Metadata',
    'الخصائص':'Features',
    'الحدود':'Limits',
    'غير معرفة':'Undefined',
    'قيمة':'Value',
    'غير محدود':'Unlimited',
    'نسخ إلى مسودة':'Copy to Draft',
    'حفظ المسودة':'Save Draft',
    'إدارة الاشتراكات':'Manage Subscriptions',
    'إدارة الباقات والاشتراكات وحدود الاستخدام':'Manage plans, subscriptions, and usage limits',
    'المنشورة والمسودات والإصدارات التاريخية':'Published, drafts, and historical versions',

    // Commercial / billing / subscriptions
    'التشغيل التجاري':'Commercial Operations',
    'لوحة التشغيل التجاري':'Commercial Operations Dashboard',
    'متابعة التفعيل والاستهلاك ودورة الاشتراك والفواتير بمؤشرات قابلة للتنفيذ':'Monitor activation, usage, subscription lifecycle, and billing with actionable metrics',
    'اشتراكات معرضة':'At-risk subscriptions',
    'فواتير متأخرة':'Overdue invoices',
    'شركات مفعلة':'Enabled companies',
    'تعيينات استخدام':'Usage assignments',
    'إجمالي الفواتير المستحقة':'Total outstanding invoices',
    'مفاتيح الأمان العامة':'Global Safety Controls',
    'التفعيل والاستهلاك ودورة الاشتراك':'Activation, usage, and subscription lifecycle',
    'أي تفعيل يحتاج تأكيدًا صريحًا.':'Any activation requires explicit confirmation.',
    'مركز التشغيل':'Operations Center'
  });

  const I18N_V13_EN_AR=Object.freeze(Object.entries(I18N_V13_AR_EN).reduce((acc,pair)=>{
    if(!acc[pair[1]])acc[pair[1]]=pair[0];
    return acc;
  },{}));

  const V13_AR_KEYS=Object.keys(I18N_V13_AR_EN).sort((a,b)=>b.length-a.length);
  const V13_EN_KEYS=Object.keys(I18N_V13_EN_AR).sort((a,b)=>b.length-a.length);
  const replaceAllLiteral=(value,from,to)=>String(value).split(from).join(to);

  const translateV13Phrases=(value,lang)=>{
    let out=String(value==null?'':value);
    const map=lang==='ar'?I18N_V13_EN_AR:I18N_V13_AR_EN;
    const keys=lang==='ar'?V13_EN_KEYS:V13_AR_KEYS;
    keys.forEach(key=>{
      if(out.indexOf(key)>=0)out=replaceAllLiteral(out,key,map[key]);
    });
    if(lang==='en'){
      out=out.replace(/(\d+)\s+شركة(?=\s|$)/g,'$1 Companies');
      out=out.replace(/(\d+)\s+نشط\s+من\s+(\d+)/g,'$1 active of $2');
      out=out.replace(/الصحة\s+([0-9٠-٩]+)%/g,'Health $1%');
      out=out.replace(/\bمنتهي\b/g,'Expired');
      out=out.replace(/\bنشط\b/g,'Active');
    }else{
      out=out.replace(/(\d+)\s+Companies(?=\s|$)/g,'$1 شركة');
      out=out.replace(/(\d+)\s+active\s+of\s+(\d+)/gi,'$1 نشط من $2');
    }
    return out;
  };

  const setV13LocalizedText=(selector,en,ar)=>{
    document.querySelectorAll(selector).forEach(element=>{
      if(!(element instanceof HTMLElement))return;
      const desired=currentLanguage()==='ar'?ar:en;
      if(element.textContent!==desired)element.textContent=desired;
    });
  };

  const applyV13CriticalOverrides=()=>{
    setV13LocalizedText('#githubConnectionBadge','● Connected','● متصل');
    setV13LocalizedText('#githubRefreshBtn','⟳ Refresh Status','⟳ تحديث الحالة');
    setV13LocalizedText('#evolutionConnectionBadge','Not configured','غير مُعد');
    setV13LocalizedText('#evolutionSaveBtn','Save Platform Settings','حفظ إعدادات المنصة');
    setV13LocalizedText('#evolutionTestBtn','Test Connection','اختبار الاتصال');
    setV13LocalizedText('#evolutionStatusGrid .empty','Loading Evolution API settings...','جاري تحميل إعدادات Evolution API...');
  };
  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_3
'''


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing ambiguous patch application.')
    return text.replace(old, new, 1)


def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        print('Super Admin bilingual V1.3 already applied; no changes made.')
        return

    if V12_MARKER not in text:
        raise SystemExit('Bilingual V1.2 marker not found; apply V1, V1.1 and V1.2 first.')

    for label, anchor in [
        ('V1.2 JS end', JS_ANCHOR),
        ('V1.2 translation result', OLD_NEXT),
        ('translation document override chain', DOC_ANCHOR),
    ]:
        if text.count(anchor) != 1:
            raise SystemExit(f'{label} anchor count is {text.count(anchor)}; refusing unknown baseline.')

    text = replace_once(text, JS_ANCHOR, JS_ANCHOR + JS + '\n', 'V1.3 JS coverage')
    text = replace_once(
        text,
        OLD_NEXT,
        "    const next1=translateV12Pattern(next0,currentLanguage());\n    const next=translateV13Phrases(next1,currentLanguage());",
        'V1.3 phrase translator',
    )
    text = replace_once(
        text,
        DOC_ANCHOR,
        "    applyV12CriticalOverrides();\n    applyV13CriticalOverrides();\n    syncLanguageControls();",
        'V1.3 critical overrides',
    )

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual Arabic / English V1.3 full coverage corrective patch.')


if __name__ == '__main__':
    main()
