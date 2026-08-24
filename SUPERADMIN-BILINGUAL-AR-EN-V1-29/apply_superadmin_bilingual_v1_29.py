#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_29_GITHUB_SYNC_EN_FULL_PAGE_CLOSURE'
V128_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_28_ACTIVITY_EN_VIEW_ALL_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V128";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_29_GITHUB_SYNC_EN_FULL_PAGE_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V129";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V128';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V129';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v128.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v129.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V128';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V129';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v128', '?v=superadmin-bilingual-v129', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v128"', 'data-sa-bilingual-runtime="v129"', 'runtime asset marker', 1),
]

EN_ANCHOR = """  const v122EnglishPatterns=(value)=>{
    let out=String(value);"""
EN_INSERT = r"""  const v122EnglishPatterns=(value)=>{
    let out=String(value);
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_29_GITHUB_SYNC_EN_FULL_PAGE_CLOSURE
    // V1.28 evidence exposed the complete ordinary static Arabic/mixed set on GitHub Sync EN.
    // Runtime/domain data (URLs, IPs, timestamps, roles and audit payload values) remains untouched.
    const v129Pairs=[
      ["● Connected","● متصل"],
      ["⟳ Refresh status","⟳ تحديث الحالة"],
      ["Review & execute sync","Review وتنفيذ المزامنة"],
      ["Inspect changes, review Files, then run Commit and Push and verify the result.","افحص التغييرات، راجع Files، ثم نفّذ Commit وPush وتحقق من النتيجة."],
      ["Check","فحص"],
      ["Verify","تحقق"],
      ["Action","الإجراء"],
      ["Commit message","رسالة Commit"],
      ["Start with Preview Diff to display a summary of changes.","ابدأ بPreview Diff لعرض ملخص التغييرات."],
      ["Files will appear here after preview.","ستظهر Files هنا بعد المعاينة."],
      ["Sync status","حالة المزامنة"],
      ["Ready to execute","جاهز للتنفيذ"],
      ["No operation has started yet.","لم تبدأ أي عملية بعد."],
      ["Ready to execute.","جاهز للتنفيذ."],
      ["Technical Details","الDetails التقنية"],
      ["Repository information","معلومات المستودع"],
      ["Permission","الصلاحية"],
      ["Connection Status & PAT","Connection Status و PAT"],
      ["Connection","الاتصال"],
      ["Fine-grained PAT saved","Fine-grained PAT محفوظ"],
      ["Branch and release information","معلومات الفرع والإصدار"],
      ["Pending deployment","ينتظر النشر"],
      ["Source is synced with GitHub and there is an undeployed release.","المصدر متزامن مع GitHub ويوجد إصدار لم يُنشر بعد."],
      ["Save Repository and branch","حفظ Repository والفرع"],
      ["GitHub is ready. There is an unbuilt release; run Build then Restart at the appropriate deployment time.","GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ Build ثم Restart عند وقت النشر المناسب."],
      ["Brief description of changes","وصف مختصر للتغييرات"],
      ["Search operation, repository, or user","بحث في العملية أو المستودع أو المستخدم"]
    ];
    for(const [en,ar] of v129Pairs)if(out===ar)out=en;
    let v129AuditCount=out.match(/^(\d+)\s+من\s+(\d+)\s+عملية$/);
    if(v129AuditCount)out=v129AuditCount[1]+' of '+v129AuditCount[2]+' operations';"""

AR_ANCHOR = """  const v122ArabicPatterns=(value)=>{
    let out=String(value);"""
AR_INSERT = r"""  const v122ArabicPatterns=(value)=>{
    let out=String(value);
    // V1.29 reverse canonicalization for the GitHub Sync AR gate.
    const v129Pairs=[
      ["● Connected","● متصل"],
      ["⟳ Refresh status","⟳ تحديث الحالة"],
      ["Review & execute sync","Review وتنفيذ المزامنة"],
      ["Inspect changes, review Files, then run Commit and Push and verify the result.","افحص التغييرات، راجع Files، ثم نفّذ Commit وPush وتحقق من النتيجة."],
      ["Check","فحص"],
      ["Verify","تحقق"],
      ["Action","الإجراء"],
      ["Commit message","رسالة Commit"],
      ["Start with Preview Diff to display a summary of changes.","ابدأ بPreview Diff لعرض ملخص التغييرات."],
      ["Files will appear here after preview.","ستظهر Files هنا بعد المعاينة."],
      ["Sync status","حالة المزامنة"],
      ["Ready to execute","جاهز للتنفيذ"],
      ["No operation has started yet.","لم تبدأ أي عملية بعد."],
      ["Ready to execute.","جاهز للتنفيذ."],
      ["Technical Details","الDetails التقنية"],
      ["Repository information","معلومات المستودع"],
      ["Permission","الصلاحية"],
      ["Connection Status & PAT","Connection Status و PAT"],
      ["Connection","الاتصال"],
      ["Fine-grained PAT saved","Fine-grained PAT محفوظ"],
      ["Branch and release information","معلومات الفرع والإصدار"],
      ["Pending deployment","ينتظر النشر"],
      ["Source is synced with GitHub and there is an undeployed release.","المصدر متزامن مع GitHub ويوجد إصدار لم يُنشر بعد."],
      ["Save Repository and branch","حفظ Repository والفرع"],
      ["GitHub is ready. There is an unbuilt release; run Build then Restart at the appropriate deployment time.","GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ Build ثم Restart عند وقت النشر المناسب."],
      ["Brief description of changes","وصف مختصر للتغييرات"],
      ["Search operation, repository, or user","بحث في العملية أو المستودع أو المستخدم"]
    ];
    for(const [en,ar] of v129Pairs)if(out===en)out=ar;
    let v129AuditCount=out.match(/^(\d+)\s+of\s+(\d+)\s+operations$/i);
    if(v129AuditCount)out=v129AuditCount[1]+' من '+v129AuditCount[2]+' عملية';"""

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.29 GitHub Sync EN full-page closure already applied; no changes made.')
        return
    if V128_MARKER not in text:
        raise SystemExit('Bilingual V1.28 Activity EN View all closure marker not found; apply V1.28 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_ANCHOR) != 1:
        raise SystemExit(f'V1.29 English pattern anchor count is {text.count(EN_ANCHOR)}; refusing unknown baseline.')
    if text.count(AR_ANCHOR) != 1:
        raise SystemExit(f'V1.29 Arabic pattern anchor count is {text.count(AR_ANCHOR)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = replace_once(text, EN_ANCHOR, EN_INSERT, 'V1.29 GitHub Sync English patterns')
    text = replace_once(text, AR_ANCHOR, AR_INSERT, 'V1.29 GitHub Sync Arabic reverse patterns')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.29 GitHub Sync EN full-page closure runtime.')

if __name__ == '__main__':
    main()
