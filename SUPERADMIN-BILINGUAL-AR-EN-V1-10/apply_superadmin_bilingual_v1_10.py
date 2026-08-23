#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_10_OVERVIEW_CLOSURE'
V19_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_9_PHRASE_RUNTIME'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V19";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_10_OVERVIEW_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V110";',
     'UI version'),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V19';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V110';",
     'legacy UI runtime version'),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v19.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v110.js";',
     'runtime path'),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V19';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V110';",
     'standalone runtime version'),
    ('?v=superadmin-bilingual-v19', '?v=superadmin-bilingual-v110', 'asset cache key'),
    ('data-sa-bilingual-runtime="v19"', 'data-sa-bilingual-runtime="v110"', 'runtime asset marker'),
]

ANCHOR = "  const v19Replace=(raw,list)=>{let out=raw;for(const p of list){if(out.includes(p[0]))out=out.split(p[0]).join(p[1]);}return out;};"
TRANSLATE_OLD = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return exact;return v19Replace(raw,v19PhraseEnToAr);}const exact=arToEn.get(raw);if(exact)return exact;return v19Replace(raw,v19PhraseArToEn);};"

EXTRA_JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_10_OVERVIEW_CLOSURE
  // Audited Overview EN closure from the V1.9 unique-string evidence.
  const v110Pairs=[
    ['Main Dashboard','لوحة التحكم الرئيسية'],
    ['Collapse navigation','طي القائمة'],
    ['Main navigation','التنقل الرئيسي'],
    ['Logout','خروج'],
    ['Platform metrics and executive decisions in one view','مؤشرات المنصة والقرارات التنفيذية في شاشة واحدة'],
    ['Refresh dashboard data','تحديث بيانات لوحة التحكم'],
    ['Add Company','Add Company جديدة'],
    ['Open Platform Admins','فتح إدارة مسؤولي المنصة'],
    ['Open Download Source Center','فتح مركز Download Source'],
    ['Toggle theme','تبديل المظهر'],
    ['Key operating metrics, risks, and decisions in one clear view.','أهم مؤشرات التشغيل والمخاطر والقرارات في شاشة واحدة واضحة.'],
    ['Health or operational status','صحة أو حالة تشغيلية'],
    ['Within 7 days','خلال 7 أيام'],
    ['Overdue or expired','متأخر أو منتهي'],
    ['Active status','حالة نشطة'],
    ['Revenue, readiness, subscriptions, and other operating metrics','الإيرادات، الجاهزية، الاشتراكات وباقي الأرقام التشغيلية'],
    ['Quick decisions','القرارات السريعة'],
    ['Most-used actions without opening extra screens.','أكثر الإجراءات استخداماً بدون فتح شاشات إضافية.'],
    ['From platform settings','من إعدادات المنصة'],
    ['All companies','كل الشركات'],
    ['Active','نشطة'],
    ['Trials ending soon','تجارب قريبة'],
    ['Review payments','مراجعة المدفوعات'],
    ['Pending','معلقة'],
    ['High risk','مخاطر عالية'],
    ['Review','مراجعة'],
    ['Usage analytics','تحليلات الاستخدام'],
    ['Stable','مستقر'],
    ['Latest sign-ins and sensitive actions.','آخر الدخول والإجراءات الحساسة.'],
    ['Security','أمان'],
    ['Plan','الخطة'],
    ['The request will be created in the Queue without blocking the dashboard.','سيتم إنشاء الطلب داخل Queue بدون تعطيل اللوحة.'],
    ['Renew / Update Subscription','تجديد / تحديث الاشتراك'],
    ['Update plan, status, and expiration date.','تعديل الخطة والحالة وتاريخ الانتهاء.'],
    ['Update reason','سبب التحديث'],
    ['The admin only sees assigned companies and cannot see other platform admins.','المسؤول يرى الشركات المسندة له فقط ولا يرى مسؤولي المنصة الآخرين.'],
    ['Admin name','اسم المسؤول'],
    ['Assigned companies','الشركات التابعة'],
    ['Appearance, account, and Download Source Code.','المظهر، الحساب، وDownload Source كود.'],
    ['🌙 Dark','🌙 داكن'],
    ['☀ Light','☀ فاتح'],
    ['Download Source Code','Download Source كود'],
    ['Download a real copy of the current SaaS source.','تحميل نسخة حقيقية من السورس الحالي للـ SaaS.'],
    ['Loading source data...','جاري تحميل بيانات السورس...']
  ];
  v110Pairs.forEach((p)=>{enToAr.set(p[0],p[1]);arToEn.set(p[1],p[0]);});
  const v110PhraseArToEn=v110Pairs.map((p)=>[p[1],p[0]]).filter((p)=>p[0].length>=5).sort((a,b)=>b[0].length-a[0].length);
  const v110PhraseEnToAr=v110Pairs.filter((p)=>p[0].length>=5).sort((a,b)=>b[0].length-a[0].length);
  const v110AsciiDigits=(value)=>String(value).replace(/[٠-٩]/g,(ch)=>'0123456789'['٠١٢٣٤٥٦٧٨٩'.indexOf(ch)]);
  const v110EnglishPatterns=(value)=>{
    let out=v110AsciiDigits(value);
    let m=out.match(/^راجع\s+(.+)$/);if(m)out='Review '+m[1];
    m=out.match(/^الصحة\s+(\d+)%\s*·\s*منتهي$/);if(m)out='Health '+m[1]+'% · expired';
    m=out.match(/^(\d+)\s+نشط\s+من\s+(\d+)$/);if(m)out=m[1]+' active of '+m[2];
    m=out.match(/^(\d+)\s+شركة\s+مدفوعة$/);if(m)out=m[1]+' paid companies';
    m=out.match(/^(\d+)\s+موقوفة\s*·\s*(\d+)\s+تنتهي\s+قريبًا$/);if(m)out=m[1]+' suspended · '+m[2]+' ending soon';
    m=out.match(/^المستخدمون\s+(\d+)%\s*·\s*Clients\s+(\d+)%\s*·\s*(.+)$/);if(m)out='Users '+m[1]+'% · Clients '+m[2]+'% · '+m[3];
    return out;
  };
'''

TRANSLATE_NEW = "  const translate=(value)=>{const raw=norm(value);if(!raw)return raw;if(current()==='ar'){const exact=enToAr.get(raw);if(exact)return exact;let out=v19Replace(raw,v19PhraseEnToAr);out=v19Replace(out,v110PhraseEnToAr);return out;}const exact=arToEn.get(raw);if(exact)return v110EnglishPatterns(exact);let out=v19Replace(raw,v19PhraseArToEn);out=v19Replace(out,v110PhraseArToEn);return v110EnglishPatterns(out);};"

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.10 Overview closure already applied; no changes made.')
        return
    if V19_MARKER not in text:
        raise SystemExit('Bilingual V1.9 phrase runtime marker not found; apply V1.9 first.')

    for old, new, label in REPLACES:
        count = text.count(old)
        expected = 3 if label == 'asset cache key' else 1
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(ANCHOR) != 1:
        raise SystemExit(f'V1.10 runtime anchor count is {text.count(ANCHOR)}; refusing unknown baseline.')
    if text.count(TRANSLATE_OLD) != 1:
        raise SystemExit(f'V1.10 translator anchor count is {text.count(TRANSLATE_OLD)}; refusing unknown baseline.')

    for old, new, label in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, ANCHOR, ANCHOR + '\n' + EXTRA_JS, 'V1.10 Overview dictionary/patterns')
    text = replace_once(text, TRANSLATE_OLD, TRANSLATE_NEW, 'V1.10 translator')

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.10 Overview EN closure runtime.')

if __name__ == '__main__':
    main()
