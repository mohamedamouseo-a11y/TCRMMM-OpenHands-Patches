#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_32_GITHUB_SYNC_AR_REMAINING_STATIC_CLOSURE'
V131_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_31_GITHUB_SYNC_FINAL_CANONICALIZATION'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V131";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_32_GITHUB_SYNC_AR_REMAINING_STATIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V132";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V131';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V132';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v131.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v132.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V131';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V132';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v131', '?v=superadmin-bilingual-v132', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v131"', 'data-sa-bilingual-runtime="v132"', 'runtime asset marker', 1),
]

EN_START = "  const v122EnglishPatterns=(value)=>{"
AR_START = "  const v122ArabicPatterns=(value)=>{"
AR_END = "  const v121PhraseArToEn="
RETURN_ANCHOR = "    return out;\n  };"

EN_FINAL = r'''    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_32_GITHUB_SYNC_AR_REMAINING_STATIC_CLOSURE
    // V1.31 evidence: preserve canonical English for the remaining GitHub page labels.
    if(typeof location!=='undefined' && location.hash==='#github'){
      const v132GithubEnFinal=new Map([
        ["مزامنة GitHub المتقدمة","GitHub Advanced Sync"],
        ["مراجعة مصدر المنصة وتنفيذ المزامنة بأمان","Review platform source and execute sync safely"],
        ["مراجعة platform source and execute sync safely","Review platform source and execute sync safely"],
        ["الالتزام","Commit"],
        ["الدفع","Push"],
        ["رمز الوصول","Token"],
        ["النشر","Deployment"]
      ]);
      if(v132GithubEnFinal.has(out))out=v132GithubEnFinal.get(out);
    }
'''

AR_FINAL = r'''    // V1.32 final Arabic closure for remaining ordinary static GitHub Sync labels.
    // GitHub/PAT and runtime/domain data remain untouched.
    if(typeof location!=='undefined' && location.hash==='#github'){
      const v132GithubArFinal=new Map([
        ["GitHub Advanced Sync","مزامنة GitHub المتقدمة"],
        ["Review platform source and execute sync safely","مراجعة مصدر المنصة وتنفيذ المزامنة بأمان"],
        ["مراجعة platform source and execute sync safely","مراجعة مصدر المنصة وتنفيذ المزامنة بأمان"],
        ["Commit","الالتزام"],
        ["Push","الدفع"],
        ["Token","رمز الوصول"],
        ["Deployment","النشر"]
      ]);
      if(v132GithubArFinal.has(out))out=v132GithubArFinal.get(out);
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
        print('Super Admin bilingual V1.32 GitHub Sync AR remaining static closure already applied; no changes made.')
        return
    if V131_MARKER not in text:
        raise SystemExit('Bilingual V1.31 GitHub Sync final canonicalization marker not found; apply corrected V1.31 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_START) != 1:
        raise SystemExit(f'V1.32 English function anchor count is {text.count(EN_START)}; refusing unknown baseline.')
    if text.count(AR_START) != 1:
        raise SystemExit(f'V1.32 Arabic function anchor count is {text.count(AR_START)}; refusing unknown baseline.')
    if text.count(AR_END) != 1:
        raise SystemExit(f'V1.32 Arabic end anchor count is {text.count(AR_END)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = insert_before_return(text, EN_START, AR_START, EN_FINAL, 'V1.32 English finalizer')
    text = insert_before_return(text, AR_START, AR_END, AR_FINAL, 'V1.32 Arabic finalizer')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.32 GitHub Sync AR remaining static closure runtime.')

if __name__ == '__main__':
    main()
