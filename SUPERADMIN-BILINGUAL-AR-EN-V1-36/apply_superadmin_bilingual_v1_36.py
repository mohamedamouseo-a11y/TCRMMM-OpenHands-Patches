#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_36_USERS_EN_DYNAMIC_ACCOUNT_COUNT_CLOSURE'
V135_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_35_GITHUB_SYNC_EN_REMAINING_STATIC_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V135";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_36_USERS_EN_DYNAMIC_ACCOUNT_COUNT_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V136";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V135';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V136';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v135.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v136.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V135';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V136';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v135', '?v=superadmin-bilingual-v136', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v135"', 'data-sa-bilingual-runtime="v136"', 'runtime asset marker', 1),
]

EN_START = "  const v122EnglishPatterns=(value)=>{"
AR_START = "  const v122ArabicPatterns=(value)=>{"
AR_END = "  const v121PhraseArToEn="
RETURN_ANCHOR = "    return out;\n  };"

EN_FINAL = r'''    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_36_USERS_EN_DYNAMIC_ACCOUNT_COUNT_CLOSURE
    // V1.35 browser evidence: preserve the runtime count while translating the static noun.
    if(typeof location!=='undefined' && location.hash==='#users'){
      const v136UsersEnCount=out.match(/^([0-9٠-٩]+)\s+حساب$/u);
      if(v136UsersEnCount){
        const n=v136UsersEnCount[1];
        out=n+' '+(n==='1'?'account':'accounts');
      }
    }
'''

AR_FINAL = r'''    // V1.36 reverse canonicalization for the Users pager count label.
    if(typeof location!=='undefined' && location.hash==='#users'){
      const v136UsersArCount=out.match(/^([0-9٠-٩]+)\s+accounts?$/iu);
      if(v136UsersArCount)out=v136UsersArCount[1]+' حساب';
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
        print('Super Admin bilingual V1.36 Users EN dynamic account count closure already applied; no changes made.')
        return
    if V135_MARKER not in text:
        raise SystemExit('Bilingual V1.35 GitHub Sync EN remaining static closure marker not found; apply V1.35 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(EN_START) != 1:
        raise SystemExit(f'V1.36 English function anchor count is {text.count(EN_START)}; refusing unknown baseline.')
    if text.count(AR_START) != 1:
        raise SystemExit(f'V1.36 Arabic function anchor count is {text.count(AR_START)}; refusing unknown baseline.')
    if text.count(AR_END) != 1:
        raise SystemExit(f'V1.36 Arabic end anchor count is {text.count(AR_END)}; refusing unknown baseline.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = insert_before_return(text, EN_START, AR_START, EN_FINAL, 'V1.36 English finalizer')
    text = insert_before_return(text, AR_START, AR_END, AR_FINAL, 'V1.36 Arabic finalizer')
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.36 Users EN dynamic account count closure runtime.')

if __name__ == '__main__':
    main()
