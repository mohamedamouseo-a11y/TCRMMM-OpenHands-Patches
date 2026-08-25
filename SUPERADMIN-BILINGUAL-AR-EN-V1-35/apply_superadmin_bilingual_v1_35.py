#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_35_GITHUB_SYNC_EN_REMAINING_STATIC_CLOSURE'
V134_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_34_TENANT_DETAILS_EN_PROVISIONING_STATIC_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V134";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_35_GITHUB_SYNC_EN_REMAINING_STATIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V135";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V134';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V135';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v134.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v135.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V134';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V135';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v134', '?v=superadmin-bilingual-v135', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v134"', 'data-sa-bilingual-runtime="v135"', 'runtime asset marker', 1),
]

EN_START = "  const v122EnglishPatterns=(value)=>{"
AR_START = "  const v122ArabicPatterns=(value)=>{"
AR_END = "  const v121PhraseArToEn="
RETURN_ANCHOR = "    return out;\n  };"

EN_FINAL = r'''    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_35_GITHUB_SYNC_EN_REMAINING_STATIC_CLOSURE
    // V1.34 raw browser scan: close only confirmed ordinary static GitHub Sync EN leaks.
    // Event payloads, URLs, IPs, timestamps, roles, repository/branch/SHA values remain data.
    if(typeof location!=='undefined' && location.hash==='#github'){
      const v135GithubEnFinal=new Map([
        ["Review مصدر المنصة وتنفيذ المزامنة بأمان","Review platform source and execute sync safely"],
        ["كل العمليات","All operations"],
        ["إلغاء آمن","Safe cancel"]
      ]);
      if(v135GithubEnFinal.has(out))out=v135GithubEnFinal.get(out);
    }
'''

AR_FINAL = r'''    // V1.35 reverse canonicalization for the same GitHub Sync ordinary static UI.
    if(typeof location!=='undefined' && location.hash==='#github'){
      const v135GithubArFinal=new Map([
        ["Review platform source and execute sync safely","مراجعة مصدر المنصة وتنفيذ المزامنة بأمان"],
        ["All operations","كل العمليات"],
        ["Safe cancel","إلغاء آمن"]
      ]);
      if(v135GithubArFinal.has(out))out=v135GithubArFinal.get(out);
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
        print('Super Admin bilingual V1.35 GitHub Sync EN remaining static closure already applied; no changes made.')
        return
    if V134_MARKER not in text:
        raise SystemExit('Bilingual V1.34 Tenant Details EN provisioning closure marker not found; apply V1.34 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_START) != 1:
        raise SystemExit(f'V1.35 English function anchor count is {text.count(EN_START)}; refusing unknown baseline.')
    if text.count(AR_START) != 1:
        raise SystemExit(f'V1.35 Arabic function anchor count is {text.count(AR_START)}; refusing unknown baseline.')
    if text.count(AR_END) != 1:
        raise SystemExit(f'V1.35 Arabic end anchor count is {text.count(AR_END)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = insert_before_return(text, EN_START, AR_START, EN_FINAL, 'V1.35 English finalizer')
    text = insert_before_return(text, AR_START, AR_END, AR_FINAL, 'V1.35 Arabic finalizer')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.35 GitHub Sync EN remaining static closure runtime.')

if __name__ == '__main__':
    main()
