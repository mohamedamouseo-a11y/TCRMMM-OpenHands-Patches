#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START = '/* SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1 */'
END = '/* END SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1 */'
STYLE_ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'
OLD_OVERVIEW = '<section id="sec-overview" class="stack commandCenterV1">'
NEW_OVERVIEW = '<section id="sec-overview" class="stack commandCenterV1 executiveCommandCenterV2" data-dashboard-ui="EXECUTIVE_COMMAND_CENTER_V2">'
REQUIRED = [
    '/* SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */',
    '/* SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1 */',
]

CSS = r'''
    /* SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1 */
    /* Executive dashboard redesign only. Existing IDs, handlers, APIs and data rendering stay intact. */
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2{
      --exec-navy:#102744;
      --exec-navy-2:#17365d;
      --exec-gold:#c49a4a;
      --exec-line:#e2e8f0;
      --exec-soft:#f7f9fc;
      --exec-muted:#6b7b90;
      display:grid!important;
      grid-template-columns:minmax(0,1fr)!important;
      gap:12px!important;
      width:100%!important;
      min-width:0!important;
    }

    /* Executive masthead */
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero{
      position:relative!important;
      min-height:0!important;
      padding:20px!important;
      border:1px solid #dbe3ed!important;
      border-radius:18px!important;
      background:#fff!important;
      box-shadow:0 8px 28px rgba(17,39,68,.06)!important;
      overflow:hidden!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero:before{
      content:"";position:absolute;inset-block:0;inset-inline-start:0;width:4px;background:var(--exec-gold);
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead{
      margin:0 0 16px!important;padding:0 0 13px!important;border-bottom:1px solid var(--exec-line)!important;align-items:center!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead h2{
      margin:0 0 3px!important;font-size:21px!important;line-height:1.25!important;color:var(--exec-navy)!important;letter-spacing:-.02em!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead p{
      max-width:760px!important;margin:0!important;font-size:10.5px!important;line-height:1.55!important;color:var(--exec-muted)!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead>.badge{
      min-height:28px!important;padding:5px 10px!important;border:1px solid rgba(196,154,74,.28)!important;background:#fffaf0!important;color:#8a6426!important;font-size:9px!important;font-weight:850!important;
    }

    /* Primary executive signals */
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights{
      display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:10px!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*{
      position:relative!important;min-width:0!important;min-height:94px!important;padding:13px 14px!important;border:1px solid var(--exec-line)!important;border-radius:14px!important;background:var(--exec-soft)!important;box-shadow:none!important;overflow:hidden!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*:before{
      content:"";position:absolute;inset-inline-start:0;inset-block:12px;width:3px;border-radius:99px;background:#8ea0b8;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*:nth-child(1):before{background:#16a27a}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*:nth-child(2):before{background:#3867dc}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*:nth-child(3):before{background:#d18a21}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*:nth-child(4):before{background:#9a5bd8}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights strong,
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights b{color:var(--exec-navy)!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights small,
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights .muted{color:var(--exec-muted)!important}

    /* Secondary ribbon becomes a compact executive strip. */
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon{
      display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:10px!important;margin:0!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon>*{
      min-height:76px!important;padding:12px 14px!important;border:1px solid var(--exec-line)!important;border-radius:14px!important;background:#fff!important;box-shadow:0 3px 12px rgba(17,39,68,.035)!important;
    }

    /* Detailed KPIs are available on demand instead of dominating the first viewport. */
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails{
      margin:0!important;border:1px solid var(--exec-line)!important;border-radius:14px!important;background:#fff!important;box-shadow:none!important;overflow:hidden!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails>summary{
      min-height:48px!important;padding:10px 14px!important;background:#fbfcfe!important;border:0!important;cursor:pointer!important;
    }
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails>summary b{font-size:12px!important;color:var(--exec-navy)!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails>summary small{font-size:9px!important;color:var(--exec-muted)!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails .commandDetailsBody{padding:12px!important;border-top:1px solid var(--exec-line)!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #operationsPulse{gap:8px!important;margin-bottom:10px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics{grid-template-columns:repeat(6,minmax(0,1fr))!important;gap:8px!important}
    #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics>*{min-height:82px!important;padding:11px!important;border-radius:12px!important;box-shadow:none!important}

    /* Overview support deck: deliberate 12-column information architecture. */
    #appShell.platformPageMode #sec-widgets.overviewSupport{
      display:block!important;width:100%!important;margin:0!important;padding:0!important;background:transparent!important;border:0!important;box-shadow:none!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid{
      display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr))!important;gap:10px!important;align-items:start!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel{
      min-width:0!important;margin:0!important;padding:14px!important;border:1px solid var(--exec-line)!important;border-radius:15px!important;background:#fff!important;box-shadow:0 5px 18px rgba(17,39,68,.045)!important;transform:none!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(1){grid-column:1/-1!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(2){grid-column:span 5!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(3){grid-column:span 7!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(4){grid-column:span 6!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(5){grid-column:span 6!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .panelHead{
      min-height:40px!important;margin:0 0 10px!important;padding:0 0 9px!important;border-bottom:1px solid var(--exec-line)!important;align-items:center!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .panelHead h2{font-size:14px!important;margin:0 0 2px!important;color:var(--exec-navy)!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .panelHead p{font-size:9px!important;line-height:1.4!important;margin:0!important;color:var(--exec-muted)!important}

    /* Quick actions should feel like a command palette, not large feature cards. */
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{
      display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:8px!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .btn{
      min-height:58px!important;padding:9px 10px!important;border-radius:12px!important;box-shadow:none!important;justify-content:space-between!important;gap:7px!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionLabel b{font-size:10.5px!important;line-height:1.3!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionLabel small{font-size:8.5px!important;line-height:1.35!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid .actionIcon{width:28px!important;height:28px!important;flex:0 0 28px!important;border-radius:9px!important;font-size:12px!important}

    /* Alerts, usage and security stay scannable instead of expanding indefinitely. */
    #appShell.platformPageMode #sec-widgets.overviewSupport #commandAlerts,
    #appShell.platformPageMode #sec-widgets.overviewSupport #globalSearchResults,
    #appShell.platformPageMode #sec-widgets.overviewSupport #superAlerts,
    #appShell.platformPageMode #sec-widgets.overviewSupport #usageOverview,
    #appShell.platformPageMode #sec-widgets.overviewSupport #securityReview{
      max-height:240px!important;overflow:auto!important;scrollbar-gutter:stable!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .quickItem,
    #appShell.platformPageMode #sec-widgets.overviewSupport .searchResult,
    #appShell.platformPageMode #sec-widgets.overviewSupport .securityItem{
      min-height:52px!important;padding:9px 10px!important;border-radius:10px!important;box-shadow:none!important;transform:none!important;
    }
    #appShell.platformPageMode #sec-widgets.overviewSupport .toolbar{padding:8px!important;gap:7px!important;border-radius:11px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .toolbar input{min-height:36px!important;height:36px!important;font-size:10.5px!important}
    #appShell.platformPageMode #sec-widgets.overviewSupport .toolbar .btn{min-height:36px!important;height:36px!important;padding:6px 11px!important;font-size:10px!important}

    /* Dark mode keeps hierarchy without bright cards. */
    html[data-theme="dark"] #appShell.platformPageMode #sec-overview.executiveCommandCenterV2{--exec-line:#2a3a50;--exec-soft:#14233a;--exec-muted:#9dadc1;--exec-navy:#eef4fb}
    html[data-theme="dark"] #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero,
    html[data-theme="dark"] #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon>*,
    html[data-theme="dark"] #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails,
    html[data-theme="dark"] #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel{background:#111f33!important;border-color:#2a3a50!important}
    html[data-theme="dark"] #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights>*{background:#14233a!important;border-color:#2a3a50!important}
    html[data-theme="dark"] #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #commandDetails>summary{background:#14233a!important}

    @media(max-width:1180px){
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights{grid-template-columns:repeat(2,minmax(0,1fr))!important}
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics{grid-template-columns:repeat(3,minmax(0,1fr))!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{grid-template-columns:repeat(3,minmax(0,1fr))!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(2),
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(3),
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(4),
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(5){grid-column:span 6!important}
    }
    @media(max-width:820px){
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero{padding:15px!important}
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights,
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon,
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid{grid-template-columns:1fr!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .widgetGrid>.panel:nth-child(n){grid-column:1!important}
      #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{grid-template-columns:repeat(2,minmax(0,1fr))!important}
    }
    @media(max-width:520px){
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #smartInsights,
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #executiveRibbon,
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 #metrics,
      #appShell.platformPageMode #sec-widgets.overviewSupport .quickDecisionGrid{grid-template-columns:1fr!important}
      #appShell.platformPageMode #sec-overview.executiveCommandCenterV2 .commandHero>.panelHead{align-items:flex-start!important;flex-direction:column!important}
    }
    /* END SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1 */
'''


def digest(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def main() -> int:
    if not TARGET.exists():
        print(f'ERROR: target not found: {TARGET}', file=sys.stderr)
        return 2
    text = TARGET.read_text(encoding='utf-8')
    if START in text:
        print('Phase 2 marker already present; nothing to do.')
        return 0
    for marker in REQUIRED:
        if marker not in text:
            print(f'ERROR: required baseline marker missing: {marker}', file=sys.stderr)
            return 3
    if STYLE_ANCHOR not in text:
        print('ERROR: Phase 1 shell style anchor not found.', file=sys.stderr)
        return 4
    if OLD_OVERVIEW not in text and NEW_OVERVIEW not in text:
        print('ERROR: Overview section anchor not found.', file=sys.stderr)
        return 5

    before = digest(text)
    if OLD_OVERVIEW in text:
        text = text.replace(OLD_OVERVIEW, NEW_OVERVIEW, 1)
    text = text.replace(STYLE_ANCHOR, CSS + '\n' + STYLE_ANCHOR, 1)
    if START not in text or END not in text or NEW_OVERVIEW not in text:
        print('ERROR: Phase 2 insertion verification failed.', file=sys.stderr)
        return 6
    TARGET.write_text(text, encoding='utf-8')
    print(f'Applied Phase 2 Executive Command Center to {TARGET}')
    print(f'before_sha256={before}')
    print(f'after_sha256={digest(text)}')
    print('Scope: Super Admin overview HTML marker + presentation-only CSS. Existing data IDs and handlers preserved.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
