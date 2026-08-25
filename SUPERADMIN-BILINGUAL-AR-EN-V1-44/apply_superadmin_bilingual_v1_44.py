#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_44_EVOLUTION_API_EN_RUNTIME_STATUS_HINTS_CLOSURE'
V143_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_43_EVOLUTION_API_AR_ENABLE_INTEGRATION_CANONICALIZATION'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V143";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_44_EVOLUTION_API_EN_RUNTIME_STATUS_HINTS_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V144";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V143';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V144';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v143.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v144.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V143';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V144';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v143', '?v=superadmin-bilingual-v144', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v143"', 'data-sa-bilingual-runtime="v144"', 'runtime asset marker', 1),
]

EVOLUTION_ANCHOR = """    const v143EvolutionEnableLabel=document.querySelector('div.evolutionToggleRow > div > b');
    if(v143EvolutionEnableLabel){
      v143EvolutionEnableLabel.textContent=(root.lang==='ar'?'تفعيل تكامل Evolution API':'Enable Evolution API integration');
    }
  }};"""

EVOLUTION_REPLACEMENT = """    const v143EvolutionEnableLabel=document.querySelector('div.evolutionToggleRow > div > b');
    if(v143EvolutionEnableLabel){
      v143EvolutionEnableLabel.textContent=(root.lang==='ar'?'تفعيل تكامل Evolution API':'Enable Evolution API integration');
    }
    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_44_EVOLUTION_API_EN_RUNTIME_STATUS_HINTS_CLOSURE
    // V1.43 evidence: final canonicalization for ordinary status/help text while preserving masked/runtime suffixes.
    const v144ConnectionBadge=document.querySelector('#evolutionConnectionBadge');
    if(v144ConnectionBadge){
      const key=(v144ConnectionBadge.textContent||'').trim();
      if(key==='مُعد وجاهز'||key==='Configured and ready'){
        v144ConnectionBadge.textContent=(root.lang==='ar'?'مُعد وجاهز':'Configured and ready');
      }
    }
    ['#evolutionApiTokenHint','#evolutionWebhookSecretHint'].forEach((selector)=>{
      const el=document.querySelector(selector);
      if(!el)return;
      const raw=(el.textContent||'').trim();
      const savedMatch=raw.match(/^(?:محفوظ:|Saved:)\\s*(.*)$/u);
      if(savedMatch){
        el.textContent=(root.lang==='ar'?'محفوظ: ':'Saved: ')+savedMatch[1];
      }
    });
    const v144ManagedCapability=document.querySelector('#evolutionManagedCapability');
    if(v144ManagedCapability){
      const key=(v144ManagedCapability.textContent||'').trim();
      const ar='الإعداد التلقائي متاح على السيرفر. سيتم تحديث ملف الخدمة وإعادة تشغيل Evolution API بأمان.';
      const en='Automatic setup is available on the server. The service file will be updated and Evolution API restarted safely.';
      if(key===ar||key===en)v144ManagedCapability.textContent=(root.lang==='ar'?ar:en);
    }
  }};"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.44 Evolution API EN runtime status hints closure already applied; no changes made.')
        return
    if V143_MARKER not in text:
        raise SystemExit('Bilingual V1.43 Evolution API AR enable-integration canonicalization marker not found; apply V1.43 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    anchor_count = text.count(EVOLUTION_ANCHOR)
    if anchor_count != 1:
        raise SystemExit(f'V1.44 Evolution final status/hints anchor count is {anchor_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(EVOLUTION_ANCHOR, EVOLUTION_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.44 Evolution API EN runtime status hints closure.')

if __name__ == '__main__':
    main()
