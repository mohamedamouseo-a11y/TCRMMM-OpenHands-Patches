#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_1'
V1_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1'
DICT_ANCHOR = "  const textSource=new WeakMap();"
OLD_ENGLISH = "    const english=I18N_AR_EN[trimmed]||trimmed;"
OLD_NEXT = "    const next=currentLanguage()==='ar'?(I18N_EN_AR[english]||trimmed):english;"

JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_1
  // Translation coverage expansion derived from the V1 live audit.
  // Technical product/data values remain untouched unless they are static UI labels.
  const I18N_V11_AR_EN=Object.freeze({
    'مركز القيادة':'Command Center',
    'الباقات والحدود':'Plans & Limits',
    'الإجراءات والتحليلات':'Actions & Analytics',
    'أثر الأنشطة':'Activity Trail',
    'خروج':'Logout',
    'نظرة تنفيذية على المنصة':'Executive Platform Overview',
    'القرارات السريعة':'Quick Decisions',
    'يحتاج متابعة':'Needs Attention',
    'تحليلات الاستخدام':'Usage Analytics',
    '+ إضافة شركة':'+ Add Company',
    'كل الشركات':'All Companies',
    'نشطة':'Active',
    'تجارب قريبة':'Trials Ending Soon',
    'مراجعة المدفوعات':'Payment Review',
    'معلقة':'Pending',
    'مخاطر عالية':'High Risk',
    'مسح الفلاتر':'Clear Filters',
    'حفظ العرض':'Save View',
    'يمكن التمرير أفقياً عند الحاجة':'Scroll horizontally when needed',
    'المسار':'Path',
    'الخطة':'Plan',
    'الصحة':'Health',
    'متبقي':'Remaining',
    'مستقر':'Stable',
    'تفاصيل':'Details',
    'تجديد':'Renew',
    'دخول':'Enter',
    'خطر':'Risk',
    'مستخدمو الشركات':'Company Users',
    'عرض النتائج':'Show Results',
    'إدارة موحدة لكل الشركات':'Unified management across all companies',
    'آخر دخول':'Last Login',
    'بيانات الدخول':'Login Details',
    '+ إضافة مسؤول':'+ Add Admin',
    'صلاحيات مركزية':'Centralized Permissions',
    'المسؤول':'Admin',
    'أنشأه':'Created By',
    'الشركات التابعة':'Assigned Companies',
    'آخر الأنشطة':'Recent Activity',
    'عرض الكل':'View All',
    'الأمان وسجل التدقيق':'Security & Audit Log',
    'تصدير السجل':'Export Log',
    'الأحداث المسجلة':'Logged Events',
    'إدارة الباقات والحدود':'Plans & Limits Management',
    'العودة لمركز القيادة':'Back to Command Center',
    'تحديث البيانات':'Refresh Data',
    'كتالوج الباقات':'Plans Catalog',
    'إصدارات الباقات':'Plan Versions',
    'بحث داخل الباقات':'Search Plans',
    'اختر باقة':'Select a Plan',
    '⟳ تحديث الحالة':'⟳ Refresh Status',
    'مراجعة وتنفيذ المزامنة':'Review & Run Sync',
    'الإجراء':'Action',
    'رسالة Commit':'Commit Message',
    'Evolution API — إعدادات المنصة':'Evolution API — Platform Settings',
    'حفظ إعدادات المنصة':'Save Platform Settings',
    'اختبار الاتصال':'Test Connection',
    'تحديث الحالة':'Refresh Status',
    'الحالة الحالية':'Current Status',
    'الإعداد التلقائي':'Automatic Setup',
    'تكاملات تارا':'Tara Integrations',
    'العودة إلى لوحة الإدارة':'Back to Admin Dashboard',
    'إعدادات بهجت':'Bahgat Settings',
    'إضافة تكامل':'Add Integration',
    'إجمالي التكاملات':'Total Integrations',
    'التكاملات المفعّلة':'Enabled Integrations',
    'بيانات الاتصال المكتملة':'Complete Connection Data',
    'اختبارات ناجحة':'Successful Tests',
    'التكاملات والواجهات البرمجية':'Integrations & APIs',
    'البحث والفلاتر':'Search & Filters',
    'المعروض':'Showing',
    'داكن':'Dark',
    'فاتح':'Light',
    'تحميل السورس كود':'Download Source Code',
    'تحميل نسخة حقيقية من السورس الحالي لـ SaaS.':'Download a real copy of the current SaaS source.',
    'جاري تحميل بيانات السورس...':'Loading source data...'
  });
  const I18N_V11_EN_AR=Object.freeze({
    'Command Center':'مركز القيادة',
    'Plans & Limits':'الباقات والحدود',
    'Actions & Analytics':'الإجراءات والتحليلات',
    'Activity Trail':'أثر الأنشطة',
    'Executive Platform Overview':'نظرة تنفيذية على المنصة',
    'Quick Decisions':'القرارات السريعة',
    'Needs Attention':'يحتاج متابعة',
    'Usage Analytics':'تحليلات الاستخدام',
    'All Companies':'كل الشركات',
    'Trials Ending Soon':'تجارب قريبة',
    'Payment Review':'مراجعة المدفوعات',
    'High Risk':'مخاطر عالية',
    'Save View':'حفظ العرض',
    'Scroll horizontally when needed':'يمكن التمرير أفقياً عند الحاجة',
    'Remaining':'متبقي',
    'Stable':'مستقر',
    'Renew':'تجديد',
    'Company Users':'مستخدمو الشركات',
    'Show Results':'عرض النتائج',
    'Unified management across all companies':'إدارة موحدة لكل الشركات',
    'Login Details':'بيانات الدخول',
    'Centralized Permissions':'صلاحيات مركزية',
    'Created By':'أنشأه',
    'Assigned Companies':'الشركات التابعة',
    'Security & Audit Log':'الأمان وسجل التدقيق',
    'Export Log':'تصدير السجل',
    'Logged Events':'الأحداث المسجلة',
    'Plans & Limits Management':'إدارة الباقات والحدود',
    'Back to Command Center':'العودة لمركز القيادة',
    'Refresh Data':'تحديث البيانات',
    'Plan Versions':'إصدارات الباقات',
    'Search Plans':'بحث داخل الباقات',
    'Select a Plan':'اختر باقة',
    'Review & Run Sync':'مراجعة وتنفيذ المزامنة',
    'Commit Message':'رسالة Commit',
    'Evolution API — Platform Settings':'Evolution API — إعدادات المنصة',
    'Save Platform Settings':'حفظ إعدادات المنصة',
    'Test Connection':'اختبار الاتصال',
    'Current Status':'الحالة الحالية',
    'Automatic Setup':'الإعداد التلقائي',
    'Tara Integrations':'تكاملات تارا',
    'Back to Admin Dashboard':'العودة إلى لوحة الإدارة',
    'Bahgat Settings':'إعدادات بهجت',
    'Add Integration':'إضافة تكامل',
    'Total Integrations':'إجمالي التكاملات',
    'Enabled Integrations':'التكاملات المفعّلة',
    'Complete Connection Data':'بيانات الاتصال المكتملة',
    'Successful Tests':'اختبارات ناجحة',
    'Integrations & APIs':'التكاملات والواجهات البرمجية',
    'Search & Filters':'البحث والفلاتر',
    'Showing':'المعروض',
    'Organizations':'المؤسسات',
    'Users & Access':'المستخدمون والصلاحيات',
    'Plans & Commercial':'الباقات والتجاري',
    'Platform Administration':'إدارة المنصة',
    'ORGANIZATIONS':'المؤسسات',
    'USERS & ACCESS':'المستخدمون والصلاحيات',
    'PLANS & COMMERCIAL':'الباقات والتجاري',
    'PLATFORM ADMINISTRATION':'إدارة المنصة',
    'PLATFORM OVERVIEW':'نظرة عامة على المنصة',
    'QUICK COMMANDS':'أوامر سريعة',
    'GLOBAL SEARCH':'البحث الشامل',
    'USAGE':'الاستخدام',
    'SECURITY':'الأمان',
    'ENTERPRISE':'المؤسسات',
    'Base URL':'الرابط الأساسي',
    'Webhook Signing Secret':'مفتاح توقيع Webhook',
    'Platform administration, simplified.':'إدارة المنصة، ببساطة.',
    'Platform administration. Simplified.':'إدارة المنصة. ببساطة.',
    'Secure, multi-tenant control for your entire TCRMMT ecosystem.':'تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.',
    'Download Source Code':'تحميل السورس كود',
    'Download a real copy of the current SaaS source.':'تحميل نسخة حقيقية من السورس الحالي لـ SaaS.',
    'Loading source data...':'جاري تحميل بيانات السورس...'
  });
  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_1
'''


def main():
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        print('Super Admin bilingual V1.1 already applied; no changes made.')
        return

    if V1_MARKER not in text:
        raise SystemExit('Bilingual V1 marker not found; apply V1 first.')

    for anchor in (DICT_ANCHOR, OLD_ENGLISH, OLD_NEXT):
        if text.count(anchor) != 1:
            raise SystemExit(f'Expected exactly one bilingual V1 anchor, got {text.count(anchor)}: {anchor}')

    text = text.replace(DICT_ANCHOR, JS + '\n' + DICT_ANCHOR, 1)
    text = text.replace(
        OLD_ENGLISH,
        "    const english=I18N_V11_AR_EN[trimmed]||I18N_AR_EN[trimmed]||trimmed;",
        1,
    )
    text = text.replace(
        OLD_NEXT,
        "    const next=currentLanguage()==='ar'?(I18N_V11_EN_AR[english]||I18N_EN_AR[english]||trimmed):english;",
        1,
    )

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual Arabic / English V1.1 translation coverage corrective patch.')


if __name__ == '__main__':
    main()
