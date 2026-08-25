#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_LOADER_V145'

LOADALL_ANCHOR = """  async function loadAll(){
    const role = await loadAccount();
    await loadPlans();"""

LOADALL_REPLACEMENT = """  async function loadAll(){
    const role = await loadAccount();
    // SUPER_ADMIN_EVOLUTION_DIRECT_HASH_LOADER_V145
    // Direct #evolution-api navigation is resolved before account capabilities load.
    // Re-trigger the read-only loader after loadAccount() has established owner capability.
    if(location.hash==='#evolution-api' && currentPlatformCapabilities.canManageEvolution){
      await loadEvolutionPlatformSettings();
    }
    await loadPlans();"""

HASH_ANCHOR = """  window.addEventListener('hashchange',function(){const id='sec-'+String(location.hash||'').replace(/^#/,'');if(PLATFORM_PAGE_META[id])goToSection(id,{skipHistory:true,instant:true});});"""

HASH_REPLACEMENT = """  window.addEventListener('hashchange',function(){
    const id='sec-'+String(location.hash||'').replace(/^#/,'');
    if(!PLATFORM_PAGE_META[id])return;
    goToSection(id,{skipHistory:true,instant:true});
    if(id==='sec-evolution-api' && currentPlatformCapabilities.canManageEvolution)loadEvolutionPlatformSettings();
  });"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin Evolution V1.45 direct/hash loader fix already applied; no changes made.')
        return

    if text.count(LOADALL_ANCHOR) != 1:
        raise SystemExit(f'V1.45 loadAll anchor count is {text.count(LOADALL_ANCHOR)}; expected 1.')
    if text.count(HASH_ANCHOR) != 1:
        raise SystemExit(f'V1.45 hashchange anchor count is {text.count(HASH_ANCHOR)}; expected 1.')

    text = text.replace(LOADALL_ANCHOR, LOADALL_REPLACEMENT, 1)
    text = text.replace(HASH_ANCHOR, HASH_REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Evolution V1.45 direct/hash loader fix.')

if __name__ == '__main__':
    main()
