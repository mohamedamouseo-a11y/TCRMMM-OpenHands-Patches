#!/usr/bin/env python3
from pathlib import Path

TARGET=Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER='SUPER_ADMIN_BILINGUAL_AR_EN_V1_9_PHRASE_RUNTIME'
V18='SUPER_ADMIN_BILINGUAL_AR_EN_V1_8_STANDALONE_RUNTIME'

REPLACES=[
('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V18";','// SUPER_ADMIN_BILINGUAL_AR_EN_V1_9_PHRASE_RUNTIME\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V19";','UI version'),
("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V18';","  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V19';",'legacy UI runtime version'),
('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v18.js";','const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v19.js";','runtime path'),
("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V18';","  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V19';",'standalone runtime version'),
('?v=superadmin-bilingual-v18','?v=superadmin-bilingual-v19','asset cache key'),
('data-sa-bilingual-runtime="v18"','data-sa-bilingual-runtime="v19"','runtime asset marker'),
]

MAP_ANCHOR="  const enToAr=new Map(pairs),arToEn=new Map(pairs.map((p)=>[p[1],p[0]]));"
TRANSLATE_OLD="  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar')return enToAr.get(raw)||raw;return arToEn.get(raw)||raw;};"

EXTRA_JS=r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_9_PHRASE_RUNTIME — audited static-copy coverage.
  const v19ExtraPairs=[
    ['Command Center','مركز القيادة'],['Administration Platform','منصة الإدارة'],['Plans & Limits','الباقات والحدود'],['Actions & Analytics','الإجراءات والتحليلات'],['Activity Impact','أثر الأنشطة'],
    ['Executive Platform Overview','نظرة تنفيذية على المنصة'],['Command Details','تفاصيل المؤشرات'],['Live data','بيانات مباشرة'],['Risks need attention','مخاطر تحتاج متابعة'],['Trials ending soon','تجارب تنتهي قريبًا'],['Overdue subscriptions','اشتراكات متأخرة'],['Companies active now','شركات تعمل الآن'],
    ['Today’s decision','قرار اليوم'],['Subscription indicator','مؤشر الاشتراكات'],['Operational stability','ثبات التشغيل'],['Create a new Workspace','إنشاء Workspace جديد'],['Open Companies','فتح قائمة الشركات'],
    ['Review sensitive events','مراجعة الأحداث الحساسة'],['Refresh Usage','تحديث الاستخدام'],['Refresh plan metrics','تحديث مؤشرات الخطط'],['View current alerts','عرض التنبيهات الحالية'],
    ['Execution priority and current risks.','أولوية التنفيذ والمخاطر الحالية.'],['Company usage versus plan limits.','استهلاك الشركات مقابل حدود الباقات.'],['Company, invoice, or activity.','شركة، فاتورة أو نشاط.'],['Enter at least two words to search.','اكتب كلمتين على الأقل للبحث.'],
    ['Add Company','إضافة شركة'],['Download Source','تحميل السورس'],['Review','راجع'],['Control','تحكم'],['Clients','العملاء'],
    ['Companies Management','إدارة الشركات'],['Search and track subscriptions and operational status for every company','بحث ومتابعة الاشتراكات والحالة التشغيلية لكل شركة'],['shown of','معروضة من أصل'],['Risks','مخاطر'],['All plans','كل الخطط'],['From date','من تاريخ'],['To date','إلى تاريخ'],['Rows','الصفوف'],['Comfortable view','عرض مريح'],['Companies list','قائمة الشركات'],['Server-side pagination','ترقيم صفحات من الخادم'],
    ['Create New Company','إنشاء شركة جديدة'],['The request will be sent to the Provisioning Queue.','سيتم إرسال الطلب إلى Provisioning Queue.'],['Admin Email','إيميل الأدمن'],['Admin Name','اسم الأدمن'],['Strong Password','كلمة مرور قوية'],['Duration in days','المدة بالأيام'],['Subscription End','نهاية الاشتراك'],['Note (optional)','ملاحظة (اختياري)'],['Save Subscription','حفظ الاشتراك'],
    ['Company Profile','ملف الشركة'],['Smart view of company, subscription, and billing data.','عرض ذكي لبيانات الشركة والاشتراك والفواتير.'],['Sign in as Company Admin','دخول كأدمن الشركة'],['Billing & Payments','الفواتير والدفع'],['Company Log','سجل الشركة'],['Operational Status','حالة التشغيل'],['Account Health','صحة الحساب'],['Trial End','نهاية التجربة'],['Leads','العملاء المحتملون'],['Usage vs Plan','الاستخدام مقابل الخطة'],['Activate Company','تفعيل الشركة'],['Suspend','إيقاف مؤقت'],['Resend Welcome Credentials','إعادة إرسال بيانات الترحيب'],
    ['Add Admin','إضافة Admin'],['Required when creating','إلزامية عند الإنشاء'],['Use Ctrl/Cmd to select multiple companies','استخدم Ctrl/Cmd لاختيار أكثر من شركة'],['Save Admin & Company Permissions','حفظ Admin وصلاحيات الشركات'],['Shown only once and never stored as plain text.','تظهر مرة واحدة فقط ولا يتم حفظها كنص صريح.'],
    ['File Name','اسم الملف'],['File Size','حجم الملف'],['Calculated on download','يُحسب عند التنزيل'],['Last Verified Build','آخر Build موثّق'],['Source Fingerprint','بصمة السورس'],['Counted Source Files','ملفات السورس المحتسبة'],['Actual Runtime Path','مسار التشغيل الفعلي'],['Configured Path','المسار المضبوط'],
    ['Connection Status','حالة الاتصال'],['Last Successful Check','آخر فحص ناجح'],['Current Branch','الفرع الحالي'],['Local Changes','التغييرات المحلية'],['Unpushed Commits','الالتزامات غير المدفوعة'],['Ready to Sync','جاهزة للمزامنة'],['Preview Diff','معاينة الفروق'],['Review & Sync','مراجعة ومزامنة'],['Manage Connection & Repository','إدارة الاتصال والمستودع'],['Verify & Connect','تحقق واربط'],['Disconnect GitHub','فصل GitHub'],['GitHub Operations Log','سجل عمليات GitHub'],['Refresh Log','تحديث السجل'],['GitHub Sync Stages','مراحل مزامنة GitHub'],['Search GitHub Log','بحث في سجل GitHub'],['Filter GitHub Log','تصفية سجل GitHub'],
    ['Evolution API — Platform Settings','Evolution API — إعدادات المنصة'],['Not configured','غير مُعد'],['Not saved','غير محفوظ'],['Save Platform Settings','حفظ إعدادات المنصة'],['Test Connection','اختبار الاتصال'],['Current Status','الحالة الحالية'],['Safe values without exposing secrets.','قيم آمنة بدون إظهار الأسرار.'],['Loading Evolution API settings...','جاري تحميل إعدادات Evolution API...'],['Last test','آخر اختبار'],['Last success','آخر نجاح'],['Enable Evolution API','تفعيل Evolution API'],
    ['Gradual rollout is enabled to protect companies','التشغيل التدريجي مفعّل لحماية الشركات'],['Sensitive settings only take effect after explicit confirmation.','الإعدادات الحساسة لا تعمل إلا بعد تأكيد صريح.'],['Versions, features, and limits','الإصدارات والخصائص والحدود'],['Assignment and per-company limits','التعيين وحدود كل شركة'],['Activation, usage, and collections','التفعيل والاستهلاك والتحصيل'],['Only drafts can be edited','يمكن تعديل المسودات فقط'],['Future features are locked and currently inactive.','الخصائص المستقبلية مقفولة ولا تعمل حاليًا.'],['Search by name or ID','ابحث بالاسم أو المعرف'],['Arabic Name','الاسم العربي'],['English Name','الاسم الإنجليزي'],['New Version ID','معرّف النسخة الجديدة'],['Version Metadata','معلومة الإصدار'],['Features','الخصائص'],['Limits','الحدود'],['Undefined','غير معرفة'],['Value','قيمة'],['Unlimited','غير محدود'],['Copy to Draft','نسخ إلى مسودة'],['Save Draft','حفظ المسودة'],['Manage Subscriptions','إدارة الاشتراكات'],
    ['Commercial Operations','التشغيل التجاري'],['Commercial Operations Dashboard','لوحة التشغيل التجاري'],['At-risk subscriptions','اشتراكات معرضة'],['Overdue invoices','فواتير متأخرة'],['Enabled companies','شركات مفعلة'],['Usage assignments','تعيينات استخدام'],['Total outstanding invoices','إجمالي الفواتير المستحقة'],['Global Safety Controls','مفاتيح الأمان العامة'],['Run Reconcile Now','تشغيل المطابقة الآن'],['Kill Switch','مفتاح الإيقاف الطارئ'],['Canary %','نسبة النشر التجريبي %'],['Grace Days','أيام السماح'],['Feature Overrides JSON','تجاوزات الخصائص JSON'],['Limit Overrides JSON','تجاوزات الحدود JSON'],['Save Security Settings','حفظ إعدادات الأمان'],
    ['Manage users and permissions across all companies','إدارة المستخدمين والصلاحيات عبر جميع الشركات'],['Total accounts','إجمالي الحسابات'],['Company admins','مديرو الشركات'],['Have a password','لديهم كلمة مرور'],['Search & filtering','البحث والتصفية'],['Filter users by company, role, and status.','تصفية المستخدمين حسب الشركة والدور والحالة.'],['User directory','دليل المستخدمين'],['Account, company, permission, and status.','الحساب، الشركة، الصلاحية والحالة.'],['User filters','فلاتر المستخدمين'],
    ['Latest operations and changes recorded on the platform','أحدث العمليات والتغييرات المسجلة على المنصة'],['Latest companies and important platform activity.','أحدث الشركات والحركة المهمة على المنصة.'],['Review sensitive events and track administrative operations','مراجعة الأحداث الحساسة وتتبع العمليات الإدارية'],['Live monitoring','مراقبة مباشرة'],['By company or event type','حسب الشركة أو نوع الحدث'],['Protected log','سجل محمي'],['Audit log filters','فلاتر سجل التدقيق'],['Company ID','معرّف الشركة'],['Event type','نوع الحدث'],
    ['Active branch','الفرع النشط'],['Present','موجودة'],['Changes need review','توجد تغييرات تحتاج مراجعة'],['Manage the central WhatsApp connection and test the service','إدارة اتصال WhatsApp المركزي واختبار الخدمة'],['Platform settings loaded.','تم تحميل إعدادات المنصة.'],
    ['Internal Social Agent','الوكيل الاجتماعي الداخلي'],['Advanced Reports','تقارير متقدمة'],['Custom Dashboards','لوحات مخصصة'],['Reports','التقارير'],['WhatsApp Media','وسائط واتساب'],['Multiple WhatsApp Accounts','حسابات واتساب متعددة'],['Automation','الأتمتة'],['Calendar','التقويم'],['Dynamic Services','الخدمات الديناميكية'],['Dynamic Workflow','سير العمل الديناميكي'],['Files','الملفات'],['Import & Export','الاستيراد والتصدير'],['API Access','الوصول إلى API'],['Email Marketing','التسويق بالبريد'],['Business Development','تطوير الأعمال'],['Deals','الصفقات'],['Priority Support','دعم أولوية'],['Workspace','مساحة العمل'],['AI Agent','وكيل الذكاء الاصطناعي'],['Handoff to Employee','التحويل لموظف'],['Agent Knowledge Base','قاعدة معرفة الوكيل'],
    ['Role: System administrator','دور: مدير النظام'],['System administrator','مدير النظام'],['Back to Command Center','العودة إلى مركز القيادة'],['Refresh Data','تحديث البيانات'],['View details','عرض التفاصيل'],['Overdue / expired','متأخر / منتهي'],['All accounts','كل الحسابات'],['Platform activity','نشاط المنصة'],['Monthly revenue','الإيراد الشهري'],['Needs attention','يتطلب متابعة']
  ];
  v19ExtraPairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  const v19PhraseArToEn=v19ExtraPairs.map((p)=>[p[1],p[0]]).filter((p)=>p[0].length>=7).sort((a,b)=>b[0].length-a[0].length);
  const v19PhraseEnToAr=v19ExtraPairs.filter((p)=>p[0].length>=7).sort((a,b)=>b[0].length-a[0].length);
  const v19Replace=(raw,list)=>{let out=raw;for(const p of list){if(out.includes(p[0]))out=out.split(p[0]).join(p[1]);}return out;};
'''

TRANSLATE_NEW="  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return exact;return v19Replace(raw,v19PhraseEnToAr);}const exact=arToEn.get(raw);if(exact)return exact;return v19Replace(raw,v19PhraseArToEn);};"


def once(text,old,new,label):
    c=text.count(old)
    if c!=1: raise SystemExit(f'{label} anchor count is {c}; refusing unknown baseline.')
    return text.replace(old,new,1)


def main():
    text=TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.9 already applied; no changes made.'); return
    if V18 not in text: raise SystemExit('V1.8 standalone marker missing.')
    for old,new,label in REPLACES:
        count=text.count(old)
        expected=3 if label=='asset cache key' else 1
        if count!=expected: raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
        text=text.replace(old,new)
    text=once(text,MAP_ANCHOR,MAP_ANCHOR+'\n'+EXTRA_JS,'V1.9 dictionary injection')
    text=once(text,TRANSLATE_OLD,TRANSLATE_NEW,'V1.9 phrase translator')
    TARGET.write_text(text,encoding='utf-8')
    print('Applied Super Admin Bilingual V1.9 phrase-level standalone translation runtime.')

if __name__=='__main__': main()
