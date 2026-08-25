#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_40_EVOLUTION_API_EN_STATIC_CLOSURE'
V139_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_39_GITHUB_SYNC_AR_SAFE_CLEANUP_OPTION_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V139";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_40_EVOLUTION_API_EN_STATIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V140";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V139';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V140';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v139.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v140.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V139';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V140';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v139', '?v=superadmin-bilingual-v140', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v139"', 'data-sa-bilingual-runtime="v140"', 'runtime asset marker', 1),
]

PIN_ANCHOR = """    if(v139CleanupOption)v139CleanupOption.textContent=(root.lang==='ar'?'إلغاء آمن':'Safe Cleanup');
  }};"""

PIN_REPLACEMENT = """    if(v139CleanupOption)v139CleanupOption.textContent=(root.lang==='ar'?'إلغاء آمن':'Safe Cleanup');
  }
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_40_EVOLUTION_API_EN_STATIC_CLOSURE
  // V1.39 Full Audit evidence: close the entire evidence-backed ordinary static set on Evolution API.
  if(typeof location!=='undefined' && location.hash==='#evolution-api'){
    const v140EvolutionPairs=[
      ['One central setup used by platform companies. Available only to the platform owner, and secrets are not shown after saving.','إعداد مركزي واحد تستخدمه شركات المنصة. متاح لمالك المنصة فقط ولا تُعرض الأسرار بعد حفظها.'],
      ['Disabling it prevents connections and sending across the platform.','إيقافه يمنع الاتصال والإرسال على مستوى المنصة.'],
      ['Loading settings...','جاري تحميل الإعدادات...'],
      ['Automatic setup','الإعداد التلقائي'],
      ['Checking automatic management capability...','جاري فحص إمكانية الإدارة التلقائية...'],
      ['Refresh status','تحديث الحالة'],
      ['Generate and connect credentials','توليد وربط البيانات'],
      ['Rotate credentials','تدوير البيانات']
    ];
    const v140EvolutionMap=new Map();
    for(const [en,ar] of v140EvolutionPairs){
      v140EvolutionMap.set(root.lang==='ar'?en:ar,root.lang==='ar'?ar:en);
    }
    const v140EvolutionSelector='p.muted,div.muted,h3,#evolutionStatusGrid .empty,#evolutionManagedCapability,#evolutionRefreshBtn,#evolutionGenerateBtn,#evolutionRotateBtn';
    document.querySelectorAll(v140EvolutionSelector).forEach((el)=>{
      const key=(el.textContent||'').trim();
      const next=v140EvolutionMap.get(key);
      if(next)el.textContent=next;
    });
  }};"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.40 Evolution API EN static closure already applied; no changes made.')
        return
    if V139_MARKER not in text:
        raise SystemExit('Bilingual V1.39 GitHub Sync AR Safe Cleanup option closure marker not found; apply V1.39 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    pin_count = text.count(PIN_ANCHOR)
    if pin_count != 1:
        raise SystemExit(f'V1.40 standalone runtime Evolution anchor count is {pin_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(PIN_ANCHOR, PIN_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.40 Evolution API EN static closure runtime.')

if __name__ == '__main__':
    main()
