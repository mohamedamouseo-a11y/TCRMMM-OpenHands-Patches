#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START = '/* SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1 */'
END = '/* END SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1 */'
ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'
REQUIRED = [
    '/* SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */',
    '/* SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1 */',
    '/* SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1 */',
]

CSS = r'''
    /* SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1 */
    /* Responsive no-clipping corrective for the approved dashboard layout. Presentation only. */
    #appShell.platformPageMode,
    #appShell.platformPageMode .mainArea,
    #appShell.platformPageMode .mainContent,
    #appShell.platformPageMode .mainContent>section,
    #appShell.platformPageMode #sec-overview,
    #appShell.platformPageMode #sec-widgets,
    #appShell.platformPageMode #sec-widgets .widgetGrid,
    #appShell.platformPageMode #sec-activity,
    #appShell.platformPageMode #sec-activity #recentTenants{
      min-width:0!important;
      min-height:0!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
    }

    /* Main workspace: stable sidebar + fluid content without accidental crop. */
    #appShell.platformPageMode:not(.sidebarCollapsed){
      --sidebar-w:208px!important;
      grid-template-columns:208px minmax(0,1fr)!important;
    }
    #appShell.platformPageMode.sidebarCollapsed{
      --sidebar-w:68px!important;
      grid-template-columns:68px minmax(0,1fr)!important;
    }
    #appShell.platformPageMode .sidebar{
      min-width:0!important;
      overflow:hidden!important;
    }
    #appShell.platformPageMode .sidebarNav{
      overflow-y:auto!important;
      overflow-x:hidden!important;
    }
    #appShell.platformPageMode .mainArea{
      width:100%!important;
      max-width:100%!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode .mainContent{
      width:min(100%,1460px)!important;
      max-width:1460px!important;
      margin-inline:auto!important;
      padding:14px 14px 30px!important;
      box-sizing:border-box!important;
    }

    /* Overview must size from content, never from legacy fixed tracks/heights. */
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2{
      display:grid!important;
      grid-template-columns:minmax(0,1fr)!important;
      grid-auto-rows:auto!important;
      align-content:start!important;
      align-items:start!important;
      gap:12px!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2>*{
      min-width:0!important;
      min-height:0!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero{
      min-height:0!important;
      height:auto!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights{
      display:grid!important;
      grid-template-columns:repeat(4,minmax(0,1fr))!important;
      grid-auto-rows:auto!important;
      align-items:stretch!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*{
      min-width:0!important;
      min-height:96px!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
      word-break:break-word!important;
      overflow-wrap:anywhere!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon{
      display:grid!important;
      grid-template-columns:repeat(3,minmax(0,1fr))!important;
      grid-auto-rows:auto!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon>*{
      min-width:0!important;
      min-height:72px!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
      word-break:break-word!important;
      overflow-wrap:anywhere!important;
    }

    /* KPI details: content-driven height and no crop when expanded. */
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails{
      min-width:0!important;
      min-height:0!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails[open]{overflow:visible!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails .commandDetailsBody{
      min-height:0!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #operationsPulse,
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics{
      min-width:0!important;
      min-height:0!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics{
      display:grid!important;
      grid-template-columns:repeat(4,minmax(0,1fr))!important;
      grid-auto-rows:auto!important;
      align-items:stretch!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics>*{
      min-width:0!important;
      min-height:78px!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
    }

    /* Approved support layout: Quick Actions full-width then 2-column insight zone. */
    #appShell.platformPageMode #sec-widgets.overviewSupport{
      display:block!important;
      min-width:0!important;
      min-height:0!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
      padding:0!important;
      background:transparent!important;
      border:0!important;
      box-shadow:none!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid{
      display:grid!important;
      grid-template-columns:repeat(2,minmax(0,1fr))!important;
      grid-auto-rows:auto!important;
      grid-auto-flow:row!important;
      gap:12px!important;
      align-items:start!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel{
      min-width:0!important;
      min-height:0!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
      align-self:start!important;
      margin:0!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(1){grid-column:1/-1!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(2){grid-column:2!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(3){grid-column:1!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(4){grid-column:2!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(5){grid-column:1!important}

    /* Quick actions: compact, wrap-safe, no clipped labels. */
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{
      display:grid!important;
      grid-template-columns:repeat(6,minmax(0,1fr))!important;
      grid-auto-rows:auto!important;
      gap:8px!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .btn{
      min-width:0!important;
      min-height:58px!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
      white-space:normal!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionLabel{
      min-width:0!important;
      white-space:normal!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionLabel b,
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionLabel small{
      white-space:normal!important;
      overflow-wrap:anywhere!important;
    }

    /* Lists can scroll internally when long, but parent cards must never clip them. */
    #appShell.platformPageMode #sec-widgets.overviewSupport #commandAlerts,
    #appShell.platformPageMode #sec-widgets.overviewSupport #globalSearchResults,
    #appShell.platformPageMode #sec-widgets.overviewSupport #superAlerts,
    #appShell.platformPageMode #sec-widgets.overviewSupport #usageOverview,
    #appShell.platformPageMode #sec-widgets.overviewSupport #securityReview{
      min-width:0!important;
      min-height:0!important;
      height:auto!important;
      max-height:300px!important;
      overflow-y:auto!important;
      overflow-x:hidden!important;
      scrollbar-gutter:stable!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickItem,
    #appShell.platformPageMode #sec-widgets.overviewSupport .searchResult,
    #appShell.platformPageMode #sec-widgets.overviewSupport .securityItem{
      min-width:0!important;
      min-height:52px!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
      word-break:break-word!important;
      overflow-wrap:anywhere!important;
    }

    /* Activity lives after the dashboard and stays compact + readable. */
    #appShell.platformPageMode #sec-activity{
      min-width:0!important;
      min-height:0!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-activity #recentTenants{
      display:grid!important;
      grid-template-columns:repeat(2,minmax(0,1fr))!important;
      grid-auto-rows:auto!important;
      gap:8px!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-activity #recentTenants>*{
      min-width:0!important;
      min-height:62px!important;
      height:auto!important;
      max-height:none!important;
      overflow:visible!important;
      word-break:break-word!important;
      overflow-wrap:anywhere!important;
    }

    /* Topbar controls may shrink, but not crop labels or overflow the viewport. */
    #appShell.platformPageMode .topbar{
      min-width:0!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode .pageIdentity,
    #appShell.platformPageMode .topbarSearch,
    #appShell.platformPageMode .topbarActions{
      min-width:0!important;
    }
    #appShell.platformPageMode .topbarActions{flex-wrap:wrap!important;justify-content:flex-start!important}
    #appShell.platformPageMode .topbarSearch input{width:100%!important;min-width:0!important}

    /* Responsive breakpoints: 4/3/2/1 without clipping. */
    @media(max-width:1260px){
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights{grid-template-columns:repeat(2,minmax(0,1fr))!important}
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{grid-template-columns:repeat(3,minmax(0,1fr))!important}
    }
    @media(max-width:980px){
      #appShell.platformPageMode{display:block!important}
      #appShell.platformPageMode .mainContent{width:100%!important;max-width:none!important;padding:12px 10px 24px!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid{grid-template-columns:1fr!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(n){grid-column:1!important}
      #appShell.platformPageMode #sec-activity #recentTenants{grid-template-columns:1fr!important}
      #appShell.platformPageMode .topbarActions{justify-content:flex-end!important}
    }
    @media(max-width:700px){
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights,
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon,
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics,
      #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{grid-template-columns:1fr!important}
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead{align-items:flex-start!important;flex-direction:column!important}
    }
    /* END SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1 */
'''


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def main() -> int:
    if not TARGET.exists():
        print(f'ERROR: target not found: {TARGET}', file=sys.stderr)
        return 2
    text = TARGET.read_text(encoding='utf-8')
    if START in text:
        print('Phase 2.1 marker already present; nothing to do.')
        return 0
    for marker in REQUIRED:
        if marker not in text:
            print(f'ERROR: required baseline marker missing: {marker}', file=sys.stderr)
            return 3
    if ANCHOR not in text:
        print('ERROR: safe Super Admin style anchor not found.', file=sys.stderr)
        return 4
    before = sha256(text)
    patched = text.replace(ANCHOR, CSS + '\n' + ANCHOR, 1)
    if START not in patched or END not in patched:
        print('ERROR: Phase 2.1 insertion verification failed.', file=sys.stderr)
        return 5
    TARGET.write_text(patched, encoding='utf-8')
    print(f'Applied Phase 2.1 responsive no-clipping patch to {TARGET}')
    print(f'before_sha256={before}')
    print(f'after_sha256={sha256(patched)}')
    print('Scope: presentation-only responsive/layout overrides. No DB/API/Auth/Routes/Permissions/Business Logic changes.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
