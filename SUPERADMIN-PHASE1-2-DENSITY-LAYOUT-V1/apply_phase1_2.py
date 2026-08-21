#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys
TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START_MARKER = '/* SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1 */'
END_MARKER = '/* END SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1 */'
ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'
REQUIRED_BASELINE = '/* SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */'
CSS = r'''
    /* SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1 */
    #appShell.platformPageMode{--phase12-sidebar-w:208px;--phase12-content-max:1460px}
    #appShell.platformPageMode:not(.sidebarCollapsed){--sidebar-w:var(--phase12-sidebar-w)!important}
    #appShell.platformPageMode .sidebar{margin:8px 8px 8px 0!important;height:calc(100dvh - 16px)!important;max-height:calc(100dvh - 16px)!important;padding:10px 9px!important;gap:8px!important;border-radius:16px!important}
    #appShell.platformPageMode .sidebarBrand{min-height:52px!important;padding:7px 8px!important;gap:8px!important;border-radius:12px!important}
    #appShell.platformPageMode .sidebarBrand .logoMark{width:32px!important;height:32px!important;border-radius:10px!important}
    #appShell.platformPageMode .sidebarBrand strong{font-size:13px!important}
    #appShell.platformPageMode .sidebarBrand span{font-size:8.5px!important}
    #appShell.platformPageMode .navGroupTitle{margin:7px 7px 3px!important;font-size:8.5px!important;line-height:1.25!important;letter-spacing:.07em!important}
    #appShell.platformPageMode .navItem{min-height:36px!important;padding:6px 8px!important;border-radius:10px!important;font-size:11px!important;gap:7px!important}
    #appShell.platformPageMode .navIcon{width:24px!important;height:24px!important;border-radius:8px!important;font-size:11px!important}
    #appShell.platformPageMode .sidebarFooter{padding-top:6px!important}
    #appShell.platformPageMode .sidebarUser{padding:8px!important;border-radius:12px!important;min-height:48px!important}
    #appShell.platformPageMode #logoutBtnSide{min-height:36px!important}
    #appShell.platformPageMode .topbar{min-height:60px!important;margin:8px 10px 0!important;padding:7px 10px!important;border-radius:14px!important;grid-template-columns:minmax(205px,.82fr) minmax(280px,1.3fr) auto!important;grid-template-areas:'identity search actions'!important;column-gap:8px!important;row-gap:0!important}
    #appShell.platformPageMode .pageIdentity{gap:8px!important}
    #appShell.platformPageMode .pageIdentity strong{font-size:16px!important;line-height:1.2!important}
    #appShell.platformPageMode .pageIdentity small{font-size:9px!important;line-height:1.3!important;max-width:270px!important}
    #appShell.platformPageMode .titleShield{min-width:32px!important;height:28px!important;border-radius:9px!important;font-size:8.5px!important}
    #appShell.platformPageMode .topbarSearch input{height:36px!important;min-height:36px!important;font-size:10.5px!important}
    #appShell.platformPageMode .topbarActions{gap:4px!important;flex-wrap:nowrap!important}
    #appShell.platformPageMode .topbarActions .btn,#appShell.platformPageMode .topbarActions .iconBtn{height:34px!important;min-height:34px!important;padding:6px 8px!important;font-size:10.5px!important;border-radius:9px!important}
    #appShell.platformPageMode .lastRefreshLabel{display:none!important}
    #appShell.platformPageMode .mainContent{width:min(100%,var(--phase12-content-max))!important;max-width:var(--phase12-content-max)!important;margin-inline:auto!important;padding:14px 14px 28px!important;gap:12px!important}
    #appShell.platformPageMode #sec-activity{padding:13px!important;gap:9px!important;border-radius:15px!important}
    #appShell.platformPageMode #sec-activity>.panelHead:first-child{min-height:44px!important;margin:0 0 2px!important;padding:0 0 9px!important;align-items:center!important}
    #appShell.platformPageMode #sec-activity>.panelHead:first-child h2{font-size:16px!important;margin-bottom:2px!important}
    #appShell.platformPageMode #sec-activity>.panelHead:first-child p{font-size:9.5px!important;line-height:1.35!important}
    #appShell.platformPageMode #sec-activity #activityRefreshBtn{min-height:32px!important;height:32px!important;padding:5px 9px!important;font-size:10px!important}
    #appShell.platformPageMode #sec-activity #recentTenants{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:8px!important;max-height:none!important;min-height:0!important;overflow:visible!important;align-items:start!important}
    #appShell.platformPageMode #sec-activity #recentTenants>.quickItem,#appShell.platformPageMode #sec-activity #recentTenants>.activityItem{min-height:64px!important;height:auto!important;margin:0!important;padding:9px 11px!important;border-radius:11px!important;align-items:center!important;gap:9px!important;box-shadow:none!important}
    #appShell.platformPageMode #sec-activity #recentTenants b,#appShell.platformPageMode #sec-activity #recentTenants strong{font-size:11.5px!important;line-height:1.35!important}
    #appShell.platformPageMode #sec-activity #recentTenants small,#appShell.platformPageMode #sec-activity #recentTenants .muted{font-size:9px!important;line-height:1.4!important}
    #appShell.platformPageMode #sec-activity #recentTenants .badge{padding:4px 7px!important;font-size:8.5px!important;line-height:1.2!important}
    #appShell.platformPageMode #sec-activity #recentTenants>.empty{grid-column:1/-1;min-height:72px!important;padding:16px!important}
    #appShell.platformPageMode #sec-github{padding:12px!important;gap:10px!important}
    #appShell.platformPageMode #sec-github .githubStatusGrid{gap:7px!important}
    #appShell.platformPageMode #sec-github .githubMetric{min-height:74px!important;padding:9px 10px!important}
    #appShell.platformPageMode #sec-github .githubCard{padding:12px!important}
    #appShell.platformPageMode #sec-github .githubV5Quickbar{margin-bottom:7px!important}
    #appShell.platformPageMode.sidebarCollapsed{--sidebar-w:68px!important}
    @media(max-width:1180px){#appShell.platformPageMode:not(.sidebarCollapsed){--sidebar-w:194px!important}#appShell.platformPageMode #sec-activity #recentTenants{grid-template-columns:1fr!important}}
    @media(max-width:980px){#appShell.platformPageMode .topbar{min-height:auto!important;margin:0!important;border-radius:0!important;grid-template-columns:minmax(0,1fr) auto!important;grid-template-areas:'identity actions' 'search search'!important;row-gap:7px!important}#appShell.platformPageMode .mainContent{width:100%!important;padding:12px 10px 24px!important}#appShell.platformPageMode #sec-activity #recentTenants{grid-template-columns:1fr!important}}
    @media(max-width:620px){#appShell.platformPageMode .topbar{padding:7px 9px!important}#appShell.platformPageMode .pageIdentity small{display:none!important}#appShell.platformPageMode .mainContent{padding:9px 7px 20px!important}#appShell.platformPageMode #sec-activity{padding:10px!important}}
    /* END SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1 */
'''
def sha256(text): return hashlib.sha256(text.encode('utf-8')).hexdigest()
def main():
    if not TARGET.exists(): print(f'ERROR: target not found: {TARGET}', file=sys.stderr); return 2
    text = TARGET.read_text(encoding='utf-8')
    if START_MARKER in text: print('Phase 1.2 marker already present; nothing to do.'); return 0
    if REQUIRED_BASELINE not in text: print('ERROR: Phase 1.1 baseline marker not found.', file=sys.stderr); return 3
    if ANCHOR not in text: print('ERROR: Phase 1 anchor not found.', file=sys.stderr); return 4
    before = sha256(text)
    patched = text.replace(ANCHOR, CSS + '\n' + ANCHOR, 1)
    TARGET.write_text(patched, encoding='utf-8')
    print(f'Applied Phase 1.2 to {TARGET}')
    print(f'before_sha256={before}')
    print(f'after_sha256={sha256(patched)}')
    return 0
if __name__ == '__main__': raise SystemExit(main())
