#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_13_OVERVIEW_MIXED_STATUS_CLOSURE'
V112_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_12_COMPANIES_EN_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V112";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_13_OVERVIEW_MIXED_STATUS_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V113";',
     'UI version'),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V112';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V113';",
     'legacy UI runtime version'),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v112.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v113.js";',
     'runtime path'),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V112';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V113';",
     'standalone runtime version'),
    ('?v=superadmin-bilingual-v112', '?v=superadmin-bilingual-v113', 'asset cache key'),
    ('data-sa-bilingual-runtime="v112"', 'data-sa-bilingual-runtime="v113"', 'runtime asset marker'),
]

OLD_PATTERNS = r'''  const v112EnglishPatterns=(value)=>{
    let out=String(value);
    let m=out.match(/^Server-side pagination\s*·\s*(\d+)\s+سجل$/i);
    if(m)out='Server-side pagination · '+m[1]+' records';
    m=out.match(/^Server-side pagination\s*·\s*(\d+)\s+records$/i);
    if(m)out='Server-side pagination · '+m[1]+' records';
    return out;
  };'''

NEW_PATTERNS = r'''  const v112EnglishPatterns=(value)=>{
    let out=String(value);

    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_13_OVERVIEW_MIXED_STATUS_CLOSURE
    // V1.12 regression evidence showed that an earlier phrase pass can convert
    // "الصحة" to "Health" before the V1.11 Arabic-status regex sees the value,
    // leaving "Health N% · منتهي". Close that mixed intermediate form here.
    let m=out.match(/^Health\s+(\d+)%\s*·\s*منتهي$/i);
    if(m)out='Health '+m[1]+'% · expired';

    m=out.match(/^Server-side pagination\s*·\s*(\d+)\s+سجل$/i);
    if(m)out='Server-side pagination · '+m[1]+' records';
    m=out.match(/^Server-side pagination\s*·\s*(\d+)\s+records$/i);
    if(m)out='Server-side pagination · '+m[1]+' records';
    return out;
  };'''

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.13 Overview mixed-status closure already applied; no changes made.')
        return
    if V112_MARKER not in text:
        raise SystemExit('Bilingual V1.12 Companies EN closure marker not found; apply V1.12 first.')

    for old, new, label in REPLACES:
        count = text.count(old)
        expected = 3 if label == 'asset cache key' else 1
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    if text.count(OLD_PATTERNS) != 1:
        raise SystemExit(f'V1.13 English-pattern anchor count is {text.count(OLD_PATTERNS)}; refusing unknown baseline.')

    for old, new, _label in REPLACES:
        text = text.replace(old, new)
    text = text.replace(OLD_PATTERNS, NEW_PATTERNS, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.13 Overview mixed-status closure runtime.')

if __name__ == '__main__':
    main()
