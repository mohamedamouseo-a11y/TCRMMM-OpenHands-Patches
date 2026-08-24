#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_30_GITHUB_SYNC_AR_FULL_PAGE_CLOSURE'
V129_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_29_GITHUB_SYNC_EN_FULL_PAGE_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V129";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_30_GITHUB_SYNC_AR_FULL_PAGE_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V130";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V129';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V130';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v129.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v130.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V129';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V130';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v129', '?v=superadmin-bilingual-v130', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v129"', 'data-sa-bilingual-runtime="v130"', 'runtime asset marker', 1),
]

EN_ANCHOR = """  const v122EnglishPatterns=(value)=>{
    let out=String(value);"""
EN_INSERT = r"""  const v122EnglishPatterns=(value)=>{
    let out=String(value);
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_30_GITHUB_SYNC_AR_FULL_PAGE_CLOSURE
    // V1.29 evidence exposed the complete ordinary mixed/static set in GitHub Sync AR.
    // Brand/technical tokens GitHub and PAT remain unchanged; runtime/domain data remains untouched.
    const v130Pairs=[
      ["Review platform source and execute sync safely","مراجعة مصدر المنصة وتنفيذ المزامنة بأمان"],
      ["Review & execute sync","مراجعة المزامنة وتنفيذها"],
      ["Inspect changes, review Files, then run Commit and Push and verify the result.","افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة."],
      ["Commit message","رسالة الالتزام"],
      ["Start with Preview Diff to display a summary of changes.","ابدأ بمعاينة الفروق لعرض ملخص التغييرات."],
      ["Files will appear here after preview.","ستظهر الملفات هنا بعد المعاينة."],
      ["Technical Details","التفاصيل التقنية"],
      ["Connection Status & PAT","حالة الاتصال وPAT"],
      ["Fine-grained PAT saved","تم حفظ PAT دقيق الصلاحيات"],
      ["Pending deployment","نشر معلّق"],
      ["Save Repository and branch","حفظ المستودع والفرع"],
      ["GitHub is ready. There is an unbuilt release; run Build then Restart at the appropriate deployment time.","GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ البناء ثم إعادة التشغيل عند وقت النشر المناسب."]
    ];
    for(const [en,ar] of v130Pairs)if(out===ar)out=en;"""

AR_ANCHOR = """  const v122ArabicPatterns=(value)=>{
    let out=String(value);"""
AR_INSERT = r"""  const v122ArabicPatterns=(value)=>{
    let out=String(value);
    // V1.30 canonical Arabic closure for GitHub Sync AR.
    const v130Pairs=[
      ["Review platform source and execute sync safely","مراجعة مصدر المنصة وتنفيذ المزامنة بأمان"],
      ["Review & execute sync","مراجعة المزامنة وتنفيذها"],
      ["Inspect changes, review Files, then run Commit and Push and verify the result.","افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة."],
      ["Commit message","رسالة الالتزام"],
      ["Start with Preview Diff to display a summary of changes.","ابدأ بمعاينة الفروق لعرض ملخص التغييرات."],
      ["Files will appear here after preview.","ستظهر الملفات هنا بعد المعاينة."],
      ["Technical Details","التفاصيل التقنية"],
      ["Connection Status & PAT","حالة الاتصال وPAT"],
      ["Fine-grained PAT saved","تم حفظ PAT دقيق الصلاحيات"],
      ["Pending deployment","نشر معلّق"],
      ["Save Repository and branch","حفظ المستودع والفرع"],
      ["GitHub is ready. There is an unbuilt release; run Build then Restart at the appropriate deployment time.","GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ البناء ثم إعادة التشغيل عند وقت النشر المناسب."]
    ];
    for(const [en,ar] of v130Pairs)if(out===en)out=ar;
    // Canonicalize exact mixed forms observed in V1.29 AR browser evidence.
    const v130MixedToArabic=new Map([
      ["مراجعة Source المنصة وتنفيذ المزامنة بأمان","مراجعة مصدر المنصة وتنفيذ المزامنة بأمان"],
      ["مراجعة & execute sync","مراجعة المزامنة وتنفيذها"],
      ["افحص التغييرات، راجع Files، ثم نفّذ Commit وPush وتحقق من النتيجة.","افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة."],
      ["رسالة Commit","رسالة الالتزام"],
      ["Start with معاينة الفروق to display a summary of changes.","ابدأ بمعاينة الفروق لعرض ملخص التغييرات."],
      ["ابدأ بPreview Diff لعرض ملخص التغييرات.","ابدأ بمعاينة الفروق لعرض ملخص التغييرات."],
      ["ستظهر Files هنا بعد المعاينة.","ستظهر الملفات هنا بعد المعاينة."],
      ["Technical تفاصيل","التفاصيل التقنية"],
      ["الDetails التقنية","التفاصيل التقنية"],
      ["حالة الاتصال & PAT","حالة الاتصال وPAT"],
      ["Connection Status و PAT","حالة الاتصال وPAT"],
      ["Fine-grained PAT محفوظ","تم حفظ PAT دقيق الصلاحيات"],
      ["معلقة deployment","نشر معلّق"],
      ["حفظ Repository والفرع","حفظ المستودع والفرع"],
      ["GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ Build ثم Restart عند وقت النشر المناسب.","GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ البناء ثم إعادة التشغيل عند وقت النشر المناسب."]
    ]);
    if(v130MixedToArabic.has(out))out=v130MixedToArabic.get(out);"""

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.30 GitHub Sync AR full-page closure already applied; no changes made.')
        return
    if V129_MARKER not in text:
        raise SystemExit('Bilingual V1.29 GitHub Sync EN full-page closure marker not found; apply V1.29 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_ANCHOR) != 1:
        raise SystemExit(f'V1.30 English pattern anchor count is {text.count(EN_ANCHOR)}; refusing unknown baseline.')
    if text.count(AR_ANCHOR) != 1:
        raise SystemExit(f'V1.30 Arabic pattern anchor count is {text.count(AR_ANCHOR)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, EN_ANCHOR, EN_INSERT, 'V1.30 GitHub Sync English reverse patterns')
    text = replace_once(text, AR_ANCHOR, AR_INSERT, 'V1.30 GitHub Sync Arabic full-page patterns')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.30 GitHub Sync AR full-page closure runtime.')

if __name__ == '__main__':
    main()
