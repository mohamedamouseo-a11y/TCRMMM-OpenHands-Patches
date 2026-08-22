#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START = '/* SUPER_ADMIN_PHASE2_2_FINAL_DASHBOARD_COMPOSITION_V1 */'
END = '/* END SUPER_ADMIN_PHASE2_2_FINAL_DASHBOARD_COMPOSITION_V1 */'
ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'
REQUIRED = [
    '/* SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */',
    '/* SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1 */',
    '/* SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1 */',
    '/* SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1 */',
]

CSS = r'''
    /* SUPER_ADMIN_PHASE2_2_FINAL_DASHBOARD_COMPOSITION_V1 */
    /* Final executive composition pass: compact, balanced, masonry-like support deck, zero artificial white gaps. */

    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2,
    #appShell.platformPageMode #sec-widgets.overviewSupport{
      --dash-gap:10px;
      --dash-line:#dfe6ef;
      --dash-surface:#ffffff;
      --dash-soft:#f7f9fc;
      --dash-ink:#102744;
      --dash-muted:#6f7f94;
    }

    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2{gap:10px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero{
      padding:16px 17px!important;
      border-radius:16px!important;
      box-shadow:0 6px 20px rgba(17,39,68,.05)!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead{margin-bottom:11px!important;padding-bottom:10px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead h2{font-size:19px!important;margin-bottom:2px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead p{font-size:9.5px!important}

    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights{grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:8px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*{min-height:82px!important;padding:10px 12px!important;border-radius:12px!important;background:var(--dash-soft)!important}

    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon{grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:8px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon>*{min-height:62px!important;padding:9px 11px!important;border-radius:12px!important}

    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails>summary{min-height:42px!important;padding:8px 12px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails .commandDetailsBody{padding:10px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics{gap:7px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics>*{min-height:70px!important;padding:9px 10px!important}

    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid{
      display:block!important;
      column-count:2!important;
      column-gap:10px!important;
      width:100%!important;
      height:auto!important;
      min-height:0!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel{
      display:inline-block!important;
      width:100%!important;
      margin:0 0 10px!important;
      padding:12px!important;
      vertical-align:top!important;
      break-inside:avoid!important;
      break-inside:avoid-column!important;
      page-break-inside:avoid!important;
      border-radius:14px!important;
      box-shadow:0 4px 14px rgba(17,39,68,.04)!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:first-child{display:block!important;column-span:all!important;width:100%!important;margin-bottom:10px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(n){grid-column:auto!important;grid-row:auto!important}

    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:first-child>.panelHead{min-height:36px!important;margin-bottom:8px!important;padding-bottom:8px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{grid-template-columns:repeat(6,minmax(0,1fr))!important;gap:7px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .btn{min-height:50px!important;padding:7px 9px!important;border-radius:10px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionLabel b{font-size:10px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionLabel small{font-size:8px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionIcon{width:25px!important;height:25px!important;flex-basis:25px!important;border-radius:8px!important}

    #appShell.platformPageMode #sec-widgets.overviewSupport #commandFilters{margin-top:7px!important;gap:5px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport #commandAlerts{
      display:grid!important;
      grid-template-columns:repeat(2,minmax(0,1fr))!important;
      gap:6px!important;
      margin-top:7px!important;
      max-height:138px!important;
      overflow-y:auto!important;
      overflow-x:hidden!important;
      padding-inline-end:2px!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport #commandAlerts>.quickItem,
    #appShell.platformPageMode #sec-widgets.overviewSupport #commandAlerts>*{min-height:46px!important;margin:0!important;padding:7px 9px!important;border-radius:9px!important}

    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:not(:first-child)>.panelHead{min-height:35px!important;margin:0 0 8px!important;padding:0 0 8px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:not(:first-child)>.panelHead h2{font-size:13px!important;margin-bottom:1px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:not(:first-child)>.panelHead p{font-size:8.5px!important;line-height:1.35!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:not(:first-child) .btn{min-height:32px!important;height:32px!important;padding:5px 8px!important;font-size:9px!important}

    #appShell.platformPageMode #sec-widgets.overviewSupport .searchCard{min-height:0!important;height:auto!important;max-height:none!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .searchCard .toolbar{padding:7px!important;gap:6px!important;margin:0!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .searchCard #globalSearchResults{min-height:56px!important;max-height:150px!important;margin-top:7px!important}

    #appShell.platformPageMode #sec-widgets.overviewSupport #superAlerts,
    #appShell.platformPageMode #sec-widgets.overviewSupport #usageOverview,
    #appShell.platformPageMode #sec-widgets.overviewSupport #securityReview{max-height:210px!important;min-height:0!important;overflow-y:auto!important;overflow-x:hidden!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport #superAlerts>*,
    #appShell.platformPageMode #sec-widgets.overviewSupport #usageOverview>*,
    #appShell.platformPageMode #sec-widgets.overviewSupport #securityReview>*{min-height:44px!important;padding:7px 9px!important;margin-bottom:5px!important}

    #appShell.platformPageMode #sec-widgets.overviewSupport .quickList b,
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickList strong{font-size:10px!important;line-height:1.35!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickList small,
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickList .muted{font-size:8.5px!important;line-height:1.4!important}

    html[data-theme="dark"] #appShell.platformPageMode #sec-overview.executiveCommandCenterV2,
    html[data-theme="dark"] #appShell.platformPageMode #sec-widgets.overviewSupport{--dash-line:#2b3b51;--dash-surface:#111f33;--dash-soft:#14233a;--dash-ink:#eef4fb;--dash-muted:#9dadc1}
    html[data-theme="dark"] #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel{background:var(--dash-surface)!important;border-color:var(--dash-line)!important}

    @media(max-width:1260px){
      #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{grid-template-columns:repeat(3,minmax(0,1fr))!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport #commandAlerts{grid-template-columns:1fr!important;max-height:170px!important}
    }
    @media(max-width:980px){
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid{column-count:1!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel,
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:first-child{display:block!important;width:100%!important}
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights{grid-template-columns:repeat(2,minmax(0,1fr))!important}
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important}
    }
    @media(max-width:700px){
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights,
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon,
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics,
      #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid,
      #appShell.platformPageMode #sec-widgets.overviewSupport #commandAlerts{grid-template-columns:1fr!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport #commandAlerts{max-height:180px!important}
    }
    /* END SUPER_ADMIN_PHASE2_2_FINAL_DASHBOARD_COMPOSITION_V1 */
'''


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def main() -> int:
    if not TARGET.exists():
        print(f'ERROR: target not found: {TARGET}', file=sys.stderr)
        return 2
    text = TARGET.read_text(encoding='utf-8')
    if START in text:
        print('Phase 2.2 marker already present; nothing to do.')
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
        print('ERROR: Phase 2.2 insertion verification failed.', file=sys.stderr)
        return 5

    TARGET.write_text(patched, encoding='utf-8')
    print(f'Applied Phase 2.2 final dashboard composition to {TARGET}')
    print(f'before_sha256={before}')
    print(f'after_sha256={sha256(patched)}')
    print('Scope: presentation-only dashboard composition. No DB/API/Auth/Routes/Permissions/Business Logic/Data Handler changes.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
