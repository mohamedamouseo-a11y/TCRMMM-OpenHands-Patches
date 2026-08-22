#!/usr/bin/env python3
from pathlib import Path
import hashlib
import re
import sys

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START = '/* SUPER_ADMIN_PHASE2_5_GRID_READABILITY_FINAL_FIX_V1 */'
END = '/* END SUPER_ADMIN_PHASE2_5_GRID_READABILITY_FINAL_FIX_V1 */'
STYLE_ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'
REQUIRED = [
    '/* SUPER_ADMIN_PHASE2_4_STRUCTURAL_DASHBOARD_REBUILD_V1 */',
    'data-dashboard-ui="STRUCTURAL_DASHBOARD_V24"',
    'data-dashboard-support="STRUCTURAL_SUPPORT_V24"',
]

SUPPORT_RE = re.compile(
    r'        <div class="v24SupportGrid">.*?        </div>\n      </section>\n\n(?=      <section id="sec-tenants")',
    re.S,
)

NEW_SUPPORT = r'''        <div class="v25SupportGrid" data-support-layout="INDEPENDENT_COLUMNS_V25">
          <div class="v25SupportCol v25SupportColPrimary">
            <section class="panel v24SupportCard v24AttentionCard v25AttentionCard">
              <div class="v24SectionHead compact">
                <div><span class="v24Eyebrow">ATTENTION</span><h2>يحتاج متابعة</h2><p>أولوية التنفيذ والمخاطر الحالية.</p></div>
                <button class="btn" id="refreshAlertsBtn">تحديث</button>
              </div>
              <div id="commandFilters" class="filterChips"></div>
              <div id="commandAlerts" class="quickList v24List"></div>
              <div id="superAlerts" class="quickList v24List v24SecondaryList"></div>
            </section>

            <section class="panel v24SupportCard v24UsageCard v25UsageCard">
              <div class="v24SectionHead compact">
                <div><span class="v24Eyebrow">USAGE</span><h2>تحليلات الاستخدام</h2><p>استهلاك الشركات مقابل حدود الباقات.</p></div>
                <button class="btn" id="refreshUsageBtn">تحديث</button>
              </div>
              <div id="usageOverview" class="quickList v24List"></div>
            </section>
          </div>

          <div class="v25SupportCol v25SupportColSecondary">
            <section class="panel v24SupportCard v24SearchCard v25SearchCard searchCard">
              <div class="v24SectionHead compact">
                <div><span class="v24Eyebrow">GLOBAL SEARCH</span><h2>البحث الشامل</h2><p>شركة، فاتورة أو نشاط.</p></div>
              </div>
              <div class="v24SearchBar">
                <input id="globalSearchBox" placeholder="بحث باسم شركة / فاتورة / نشاط" />
                <button class="btn primary" id="globalSearchBtn">بحث</button>
              </div>
              <div id="globalSearchResults" class="quickList v24List"><div class="empty">اكتب كلمتين على الأقل للبحث.</div></div>
            </section>

            <section class="panel v24SupportCard v24SecurityCard v25SecurityCard" id="securityPanel">
              <div class="v24SectionHead compact">
                <div><span class="v24Eyebrow">SECURITY</span><h2>مراجعة الأمان</h2><p>آخر الدخول والإجراءات الحساسة.</p></div>
                <button class="btn danger" id="loadSecurityBtn">تحديث</button>
              </div>
              <div id="securityReview" class="quickList v24List"></div>
            </section>
          </div>
        </div>
      </section>

'''

CSS = r'''
    /* SUPER_ADMIN_PHASE2_5_GRID_READABILITY_FINAL_FIX_V1 */
    #appShell.platformPageMode .structuralDashboardV24,
    #appShell.platformPageMode .structuralSupportV24{--v25-ink:#162033;--v25-muted:#627087;--v25-line:#dbe3ec;--v25-soft:#f8fafc}

    #appShell.platformPageMode #sec-widgets.structuralSupportV24 .v25SupportGrid{display:grid!important;grid-template-columns:minmax(0,7fr) minmax(320px,5fr)!important;gap:10px!important;align-items:start!important;width:100%!important;min-width:0!important;height:auto!important;overflow:visible!important}
    #appShell.platformPageMode #sec-widgets.structuralSupportV24 .v25SupportCol{display:flex!important;flex-direction:column!important;gap:10px!important;min-width:0!important;align-self:start!important}
    #appShell.platformPageMode #sec-widgets.structuralSupportV24 .v25SupportCol>.v24SupportCard{width:100%!important;min-width:0!important;height:auto!important;min-height:0!important;margin:0!important;grid-column:auto!important;grid-row:auto!important;align-self:auto!important}
    #appShell.platformPageMode #sec-widgets.structuralSupportV24 .v25SupportGrid #securityPanel.v25SecurityCard{grid-column:auto!important;grid-row:auto!important;width:100%!important;max-width:none!important}
    #appShell.platformPageMode #sec-widgets.structuralSupportV24 .v25SearchCard{min-height:0!important;height:auto!important;max-height:none!important}
    #appShell.platformPageMode #sec-widgets.structuralSupportV24 .v25SearchCard #globalSearchResults{min-height:64px!important;max-height:170px!important;margin-top:8px!important}

    #appShell.platformPageMode .v24OverviewTitle h2{font-size:24px!important;line-height:1.22!important}
    #appShell.platformPageMode .v24OverviewTitle p{font-size:12px!important;line-height:1.5!important;color:var(--v25-muted)!important}
    #appShell.platformPageMode .v24Eyebrow{font-size:9px!important;letter-spacing:.10em!important}
    #appShell.platformPageMode .v24OverviewMeta{font-size:10px!important;padding:7px 11px!important}

    #appShell.platformPageMode #smartInsights.v24KpiGrid>*{min-height:98px!important;padding:14px!important}
    #appShell.platformPageMode #smartInsights.v24KpiGrid b,#appShell.platformPageMode #smartInsights.v24KpiGrid strong{font-size:23px!important;line-height:1.08!important;color:var(--v25-ink)!important}
    #appShell.platformPageMode #smartInsights.v24KpiGrid small,#appShell.platformPageMode #smartInsights.v24KpiGrid .muted{font-size:10px!important;line-height:1.45!important;color:var(--v25-muted)!important}

    #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon>*{min-height:76px!important;padding:12px!important}
    #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon b,#appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon strong{font-size:14px!important;color:var(--v25-ink)!important}
    #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon small,#appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon .muted{font-size:9.5px!important;line-height:1.4!important;color:var(--v25-muted)!important}

    #appShell.platformPageMode .v24SectionHead h2{font-size:16px!important;line-height:1.25!important;color:var(--v25-ink)!important}
    #appShell.platformPageMode .v24SectionHead p{font-size:9.5px!important;line-height:1.45!important;color:var(--v25-muted)!important}
    #appShell.platformPageMode .v24SectionHead .btn{font-size:10px!important;min-height:32px!important;height:32px!important}
    #appShell.platformPageMode .v24QuickActions .actionLabel b{font-size:10.5px!important;line-height:1.35!important}
    #appShell.platformPageMode .v24QuickActions .actionLabel small{font-size:8.5px!important;line-height:1.4!important}

    #appShell.platformPageMode .v24List{max-height:250px!important;scrollbar-gutter:stable!important}
    #appShell.platformPageMode .v24List>.quickItem,#appShell.platformPageMode .v24List>.searchResult,#appShell.platformPageMode .v24List>.securityItem,#appShell.platformPageMode .v24List>div:not(.empty){min-height:48px!important;padding:8px 9px!important}
    #appShell.platformPageMode .v24List b,#appShell.platformPageMode .v24List strong{font-size:10.5px!important;line-height:1.35!important;color:var(--v25-ink)!important}
    #appShell.platformPageMode .v24List small,#appShell.platformPageMode .v24List .muted{font-size:9px!important;line-height:1.45!important;color:var(--v25-muted)!important}

    #appShell.platformPageMode .navItem{font-size:11.5px!important}
    #appShell.platformPageMode .navGroupTitle{font-size:8.5px!important}
    #appShell.platformPageMode .sidebarBrand strong{font-size:12.5px!important}
    #appShell.platformPageMode .pageIdentity strong{font-size:16px!important}
    #appShell.platformPageMode .pageIdentity small{font-size:9px!important}
    #appShell.platformPageMode .mainContent{width:min(100%,1320px)!important;max-width:1320px!important;padding-inline:16px!important}

    html[data-theme="dark"] #appShell.platformPageMode .structuralDashboardV24,html[data-theme="dark"] #appShell.platformPageMode .structuralSupportV24{--v25-ink:#eef4fb;--v25-muted:#9cacc0;--v25-line:#2b3b50;--v25-soft:#142237}

    @media(max-width:1080px){#appShell.platformPageMode #sec-widgets.structuralSupportV24 .v25SupportGrid{grid-template-columns:minmax(0,1fr)!important}#appShell.platformPageMode #smartInsights.v24KpiGrid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
    @media(max-width:700px){#appShell.platformPageMode #smartInsights.v24KpiGrid{grid-template-columns:1fr!important}#appShell.platformPageMode .v24OverviewTitle h2{font-size:21px!important}#appShell.platformPageMode .v24OverviewTitle p{font-size:11px!important}}
    /* END SUPER_ADMIN_PHASE2_5_GRID_READABILITY_FINAL_FIX_V1 */
'''

PRESERVED_IDS = ['refreshAlertsBtn','commandFilters','commandAlerts','superAlerts','refreshUsageBtn','usageOverview','globalSearchBox','globalSearchBtn','globalSearchResults','securityPanel','loadSecurityBtn','securityReview']

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def main() -> int:
    if not TARGET.exists():
        print(f'ERROR: target not found: {TARGET}', file=sys.stderr); return 2
    text = TARGET.read_text(encoding='utf-8')
    if START in text or 'INDEPENDENT_COLUMNS_V25' in text:
        print('Phase 2.5 marker already present; nothing to do.'); return 0
    for marker in REQUIRED:
        if marker not in text:
            print(f'ERROR: required Phase 2.4 baseline missing: {marker}', file=sys.stderr); return 3
    if STYLE_ANCHOR not in text:
        print('ERROR: safe Super Admin style anchor not found.', file=sys.stderr); return 4
    matches = list(SUPPORT_RE.finditer(text))
    if len(matches) != 1:
        print(f'ERROR: expected exactly one Phase 2.4 support-grid block, found {len(matches)}.', file=sys.stderr); return 5
    match = matches[0]; old = match.group(0)
    for item_id in PRESERVED_IDS:
        if len(re.findall(rf'id="{re.escape(item_id)}"', old)) != 1:
            print(f'ERROR: expected one #{item_id} in old support block.', file=sys.stderr); return 6
        if NEW_SUPPORT.count(f'id="{item_id}"') != 1:
            print(f'ERROR: replacement does not preserve exactly one #{item_id}.', file=sys.stderr); return 7
    before = sha256(text)
    text = text[:match.start()] + NEW_SUPPORT + text[match.end():]
    text = text.replace(STYLE_ANCHOR, CSS + '\n' + STYLE_ANCHOR, 1)
    if START not in text or END not in text or 'INDEPENDENT_COLUMNS_V25' not in text:
        print('ERROR: Phase 2.5 final marker verification failed.', file=sys.stderr); return 8
    for item_id in PRESERVED_IDS:
        if len(re.findall(rf'id="{re.escape(item_id)}"', text)) != 1:
            print(f'ERROR: duplicate or missing preserved ID after patch: {item_id}', file=sys.stderr); return 9
    TARGET.write_text(text, encoding='utf-8')
    print(f'Applied Phase 2.5 grid/readability final fix to {TARGET}')
    print(f'before_sha256={before}')
    print(f'after_sha256={sha256(text)}')
    print('Scope: Support Grid structure + scoped readability CSS only. Existing handlers/data IDs preserved.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
