#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146'
V145_MARKER = 'SUPER_ADMIN_EVOLUTION_DIRECT_HASH_LOADER_V145'

WIRE_ANCHOR = """  /* ---------------- wiring ---------------- */
  initTheme();"""

WIRE_REPLACEMENT = """  /* ---------------- wiring ---------------- */
  // SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146
  // Capture the requested direct hash before initPlatformPageMode() can temporarily
  // fall back an owner-only page to Overview while account capabilities are unknown.
  const v146InitialPlatformHash=String(location.hash||'');
  initTheme();"""

LOADALL_ANCHOR = """  async function loadAll(){
    const role = await loadAccount();
    // SUPER_ADMIN_EVOLUTION_DIRECT_HASH_LOADER_V145
    // Direct #evolution-api navigation is resolved before account capabilities load.
    // Re-trigger the read-only loader after loadAccount() has established owner capability.
    if(location.hash==='#evolution-api' && currentPlatformCapabilities.canManageEvolution){
      await loadEvolutionPlatformSettings();
    }
    await loadPlans();"""

LOADALL_REPLACEMENT = """  async function loadAll(){
    const role = await loadAccount();
    // SUPER_ADMIN_EVOLUTION_DIRECT_HASH_LOADER_V145
    // Direct #evolution-api navigation is resolved before account capabilities load.
    // Re-trigger the read-only loader after loadAccount() has established owner capability.
    // SUPER_ADMIN_EVOLUTION_DIRECT_HASH_RESTORE_V146
    // initPlatformPageMode() may have replaced the visible hash with #overview before
    // owner capability was known. Recover the original direct request, restore the
    // requested section after loadAccount(), then run exactly one read-only loader cycle.
    const v146RequestedHash=v146InitialPlatformHash||String(location.hash||'');
    if(v146RequestedHash==='#evolution-api' && currentPlatformCapabilities.canManageEvolution){
      goToSection('sec-evolution-api',{skipHistory:false,instant:true});
      await loadEvolutionPlatformSettings();
    }
    await loadPlans();"""

def apply_text(text: str) -> str:
    if MARKER in text:
        return text
    if V145_MARKER not in text:
        raise SystemExit('Evolution V1.45 direct/hash loader marker not found; apply V1.45 first.')
    wire_count = text.count(WIRE_ANCHOR)
    if wire_count != 1:
        raise SystemExit(f'V1.46 wiring anchor count is {wire_count}; expected 1.')
    loadall_count = text.count(LOADALL_ANCHOR)
    if loadall_count != 1:
        raise SystemExit(f'V1.46 loadAll anchor count is {loadall_count}; expected 1.')
    text = text.replace(WIRE_ANCHOR, WIRE_REPLACEMENT, 1)
    text = text.replace(LOADALL_ANCHOR, LOADALL_REPLACEMENT, 1)
    return text

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin Evolution V1.46 direct hash restore already applied; no changes made.')
        return
    updated = apply_text(text)
    TARGET.write_text(updated, encoding='utf-8')
    print('Applied Super Admin Evolution V1.46 direct hash restore.')

if __name__ == '__main__':
    main()
