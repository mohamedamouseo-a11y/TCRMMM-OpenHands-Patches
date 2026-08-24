#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_31_GITHUB_SYNC_FINAL_CANONICALIZATION'
V130_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_30_GITHUB_SYNC_AR_FULL_PAGE_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V130";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_31_GITHUB_SYNC_FINAL_CANONICALIZATION\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V131";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V130';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V131';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v130.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v131.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V130';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V131';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v130', '?v=superadmin-bilingual-v131', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v130"', 'data-sa-bilingual-runtime="v131"', 'runtime asset marker', 1),
]

EN_START = "  const v122EnglishPatterns=(value)=>{"
AR_START = "  const v122ArabicPatterns=(value)=>{"
RETURN_ANCHOR = "    return out;\n  };"

EN_FINAL = r'''    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_31_GITHUB_SYNC_FINAL_CANONICALIZATION
    // Final page-scoped pass after all generic substitutions.
    if(typeof location!=='undefined' && location.hash==='#github'){
      const v131GithubEnFinal=new Map([
        ["● متصل","● Connected"],["⟳ تحديث الحالة","⟳ Refresh status"],
        ["مراجعة مصدر المنصة وتنفيذ المزامنة بأمان","Review platform source and execute sync safely"],
        ["Review Source المنصة وتنفيذ المزامنة بأمان","Review platform source and execute sync safely"],
        ["مراجعة المزامنة وتنفيذها","Review & execute sync"],["Review المزامنة وتنفيذها","Review & execute sync"],["Review وتنفيذ المزامنة","Review & execute sync"],
        ["افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة.","Inspect changes, review Files, then run Commit and Push and verify the result."],
        ["افحص التغييرات، راجع Files، ثم نفّذ الالتزام والدفع وتحقق من النتيجة.","Inspect changes, review Files, then run Commit and Push and verify the result."],
        ["افحص التغييرات، راجع Files، ثم نفّذ Commit وPush وتحقق من النتيجة.","Inspect changes, review Files, then run Commit and Push and verify the result."],
        ["فحص","Check"],["تحقق","Verify"],["الإجراء","Action"],
        ["رسالة الالتزام","Commit message"],["رسالة Commit","Commit message"],
        ["ابدأ بمعاينة الفروق لعرض ملخص التغييرات.","Start with Preview Diff to display a summary of changes."],
        ["ابدأ بPreview Diff لعرض ملخص التغييرات.","Start with Preview Diff to display a summary of changes."],
        ["ستظهر الملفات هنا بعد المعاينة.","Files will appear here after preview."],["ستظهر Files هنا بعد المعاينة.","Files will appear here after preview."],
        ["حالة المزامنة","Sync status"],["جاهز للتنفيذ","Ready to execute"],["لم تبدأ أي عملية بعد.","No operation has started yet."],["جاهز للتنفيذ.","Ready to execute."],
        ["التفاصيل التقنية","Technical Details"],["Technical تفاصيل","Technical Details"],["الDetails التقنية","Technical Details"],
        ["معلومات المستودع","Repository information"],["الصلاحية","Permission"],
        ["حالة الاتصال وPAT","Connection Status & PAT"],["حالة الاتصال & PAT","Connection Status & PAT"],["Connection Status وPAT","Connection Status & PAT"],["Connection Status و PAT","Connection Status & PAT"],
        ["الاتصال","Connection"],["تم حفظ PAT دقيق الصلاحيات","Fine-grained PAT saved"],["Fine-grained PAT محفوظ","Fine-grained PAT saved"],
        ["معلومات الفرع والإصدار","Branch and release information"],["نشر معلّق","Pending deployment"],["ينتظر النشر","Pending deployment"],["معلقة deployment","Pending deployment"],
        ["المصدر متزامن مع GitHub ويوجد إصدار لم يُنشر بعد.","Source is synced with GitHub and there is an undeployed release."],
        ["حفظ المستودع والفرع","Save Repository and branch"],["حفظ Repository والفرع","Save Repository and branch"],
        ["GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ البناء ثم إعادة التشغيل عند وقت النشر المناسب.","GitHub is ready. There is an unbuilt release; run Build then Restart at the appropriate deployment time."],
        ["GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ Build ثم Restart عند وقت النشر المناسب.","GitHub is ready. There is an unbuilt release; run Build then Restart at the appropriate deployment time."],
        ["وصف مختصر للتغييرات","Brief description of changes"],["بحث في العملية أو المستودع أو المستخدم","Search operation, repository, or user"],["أخرى","Other"]
      ]);
      if(v131GithubEnFinal.has(out))out=v131GithubEnFinal.get(out);
      const v131AuditCount=out.match(/^(\d+)\s+من\s+(\d+)\s+عملية$/);
      if(v131AuditCount)out=v131AuditCount[1]+' of '+v131AuditCount[2]+' operations';
    }
'''

AR_FINAL = r'''    // V1.31 final page-scoped Arabic canonicalization for GitHub Sync.
    if(typeof location!=='undefined' && location.hash==='#github'){
      const v131GithubArFinal=new Map([
        ["● Connected","● متصل"],["⟳ Refresh status","⟳ تحديث الحالة"],
        ["Review platform source and execute sync safely","مراجعة مصدر المنصة وتنفيذ المزامنة بأمان"],["Review Source المنصة وتنفيذ المزامنة بأمان","مراجعة مصدر المنصة وتنفيذ المزامنة بأمان"],
        ["Review & execute sync","مراجعة المزامنة وتنفيذها"],["Review المزامنة وتنفيذها","مراجعة المزامنة وتنفيذها"],["Review وتنفيذ المزامنة","مراجعة المزامنة وتنفيذها"],
        ["Inspect changes, review Files, then run Commit and Push and verify the result.","افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة."],
        ["افحص التغييرات، راجع Files، ثم نفّذ الالتزام والدفع وتحقق من النتيجة.","افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة."],
        ["افحص التغييرات، راجع Files، ثم نفّذ Commit وPush وتحقق من النتيجة.","افحص التغييرات، راجع الملفات، ثم نفّذ الالتزام والدفع وتحقق من النتيجة."],
        ["Check","فحص"],["Verify","تحقق"],["Action","الإجراء"],["Commit message","رسالة الالتزام"],["رسالة Commit","رسالة الالتزام"],
        ["Start with Preview Diff to display a summary of changes.","ابدأ بمعاينة الفروق لعرض ملخص التغييرات."],["ابدأ بPreview Diff لعرض ملخص التغييرات.","ابدأ بمعاينة الفروق لعرض ملخص التغييرات."],
        ["Files will appear here after preview.","ستظهر الملفات هنا بعد المعاينة."],["ستظهر Files هنا بعد المعاينة.","ستظهر الملفات هنا بعد المعاينة."],
        ["Sync status","حالة المزامنة"],["Ready to execute","جاهز للتنفيذ"],["No operation has started yet.","لم تبدأ أي عملية بعد."],["Ready to execute.","جاهز للتنفيذ."],
        ["Technical Details","التفاصيل التقنية"],["Technical تفاصيل","التفاصيل التقنية"],["الDetails التقنية","التفاصيل التقنية"],
        ["Repository information","معلومات المستودع"],["Permission","الصلاحية"],
        ["Connection Status & PAT","حالة الاتصال وPAT"],["Connection Status وPAT","حالة الاتصال وPAT"],["Connection Status و PAT","حالة الاتصال وPAT"],["Connection","الاتصال"],
        ["Fine-grained PAT saved","تم حفظ PAT دقيق الصلاحيات"],["Fine-grained PAT محفوظ","تم حفظ PAT دقيق الصلاحيات"],["Branch and release information","معلومات الفرع والإصدار"],
        ["Pending deployment","نشر معلّق"],["ينتظر النشر","نشر معلّق"],["معلقة deployment","نشر معلّق"],
        ["Source is synced with GitHub and there is an undeployed release.","المصدر متزامن مع GitHub ويوجد إصدار لم يُنشر بعد."],
        ["Save Repository and branch","حفظ المستودع والفرع"],["حفظ Repository والفرع","حفظ المستودع والفرع"],
        ["GitHub is ready. There is an unbuilt release; run Build then Restart at the appropriate deployment time.","GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ البناء ثم إعادة التشغيل عند وقت النشر المناسب."],
        ["GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ Build ثم Restart عند وقت النشر المناسب.","GitHub جاهز. يوجد إصدار لم يُبنَ بعد؛ نفّذ البناء ثم إعادة التشغيل عند وقت النشر المناسب."],
        ["Brief description of changes","وصف مختصر للتغييرات"],["Search operation, repository, or user","بحث في العملية أو المستودع أو المستخدم"],["Other","أخرى"]
      ]);
      if(v131GithubArFinal.has(out))out=v131GithubArFinal.get(out);
      const v131AuditCount=out.match(/^(\d+)\s+of\s+(\d+)\s+operations$/i);
      if(v131AuditCount)out=v131AuditCount[1]+' من '+v131AuditCount[2]+' عملية';
    }
'''

def insert_before_return(text, start_anchor, end_anchor, payload, label):
    start = text.find(start_anchor)
    if start < 0:
        raise SystemExit(f'{label} start anchor not found; refusing unknown baseline.')
    end = text.find(end_anchor, start + len(start_anchor)) if end_anchor else len(text)
    if end < 0:
        raise SystemExit(f'{label} end anchor not found; refusing unknown baseline.')
    segment = text[start:end]
    count = segment.count(RETURN_ANCHOR)
    if count != 1:
        raise SystemExit(f'{label} return anchor count is {count}; expected 1.')
    segment = segment.replace(RETURN_ANCHOR, payload + RETURN_ANCHOR, 1)
    return text[:start] + segment + text[end:]

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.31 GitHub Sync final canonicalization already applied; no changes made.')
        return
    if V130_MARKER not in text:
        raise SystemExit('Bilingual V1.30 GitHub Sync AR full-page closure marker not found; apply V1.30 first.')
    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_START) != 1:
        raise SystemExit(f'V1.31 English function anchor count is {text.count(EN_START)}; refusing unknown baseline.')
    if text.count(AR_START) != 1:
        raise SystemExit(f'V1.31 Arabic function anchor count is {text.count(AR_START)}; refusing unknown baseline.')
    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = insert_before_return(text, EN_START, AR_START, EN_FINAL, 'V1.31 English finalizer')
    text = insert_before_return(text, AR_START, None, AR_FINAL, 'V1.31 Arabic finalizer')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.31 GitHub Sync final canonicalization runtime.')

if __name__ == '__main__':
    main()
