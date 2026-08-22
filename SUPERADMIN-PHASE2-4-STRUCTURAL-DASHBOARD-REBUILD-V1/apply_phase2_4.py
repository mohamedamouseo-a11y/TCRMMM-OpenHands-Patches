#!/usr/bin/env python3
from pathlib import Path
import hashlib
import re
import sys

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START = '/* SUPER_ADMIN_PHASE2_4_STRUCTURAL_DASHBOARD_REBUILD_V1 */'
END = '/* END SUPER_ADMIN_PHASE2_4_STRUCTURAL_DASHBOARD_REBUILD_V1 */'
STYLE_ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'
REQUIRED = [
    '/* SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */',
    '/* SUPER_ADMIN_PHASE1_2_DENSITY_LAYOUT_CORRECTIVE_V1 */',
    '/* SUPER_ADMIN_PHASE2_EXECUTIVE_COMMAND_CENTER_V1 */',
    '/* SUPER_ADMIN_PHASE2_1_RESPONSIVE_NO_CLIPPING_V1 */',
    '/* SUPER_ADMIN_PHASE2_2_FINAL_DASHBOARD_COMPOSITION_V1 */',
    '/* SUPER_ADMIN_PHASE2_3_VISUAL_REBUILD_V1 */',
]

BLOCK_RE = re.compile(r'      <section id="sec-overview".*?(?=      <section id="sec-tenants")', re.S)

HTML = r'''      <section id="sec-overview" class="stack commandCenterV1 executiveCommandCenterV2 structuralDashboardV24" data-dashboard-ui="STRUCTURAL_DASHBOARD_V24">
        <div class="v24OverviewHeader">
          <div class="v24OverviewTitle">
            <span class="v24Eyebrow">PLATFORM OVERVIEW</span>
            <h2>نظرة تنفيذية على المنصة</h2>
            <p>أهم مؤشرات التشغيل والمخاطر والقرارات في شاشة واحدة واضحة.</p>
          </div>
          <div class="v24OverviewMeta">
            <span class="v24LiveDot" aria-hidden="true"></span>
            <span>بيانات مباشرة</span>
          </div>
        </div>

        <div id="smartInsights" class="v24KpiGrid" aria-live="polite"></div>

        <div class="v24ExecutiveRow">
          <div id="executiveRibbon" class="v24ExecutiveRibbon" aria-live="polite"></div>
          <details id="commandDetails" class="v24KpiDetails">
            <summary>
              <span><b>تفاصيل المؤشرات</b><small>الإيرادات، الجاهزية، الاشتراكات وباقي الأرقام التشغيلية</small></span>
              <span class="commandDetailsChevron" aria-hidden="true">⌄</span>
            </summary>
            <div class="commandDetailsBody">
              <div id="operationsPulse" class="opsPulse" aria-live="polite"></div>
              <div id="metrics" class="kpiGrid"></div>
            </div>
          </details>
        </div>
      </section>

      <section id="sec-widgets" class="stack overviewSupport structuralSupportV24" data-dashboard-support="STRUCTURAL_SUPPORT_V24">
        <div class="v24CommandPanel panel">
          <div class="v24SectionHead">
            <div><span class="v24Eyebrow">QUICK COMMANDS</span><h2>القرارات السريعة</h2><p>أكثر الإجراءات استخداماً بدون فتح شاشات إضافية.</p></div>
          </div>
          <div class="quickDecisionGrid v24QuickActions">
            <button class="btn primary" id="quickAddCompanyBtn" data-create-tenant hidden style="display:none"><span class="actionIcon">+</span><span class="actionLabel"><b>إضافة شركة</b><small>إنشاء Workspace جديد</small></span></button>
            <button class="btn" id="quickCreateTenantBtn"><span class="actionIcon">▦</span><span class="actionLabel"><b>الشركات</b><small>فتح قائمة الشركات</small></span></button>
            <button class="btn" id="quickAuditBtn"><span class="actionIcon">◷</span><span class="actionLabel"><b>سجل التدقيق</b><small>مراجعة الأحداث الحساسة</small></span></button>
            <button class="btn" id="quickSourceBtn" hidden style="display:none"><span class="actionIcon">⇩</span><span class="actionLabel"><b>تحميل السورس</b><small>من إعدادات المنصة</small></span></button>
            <button class="btn" id="quickUsageReportBtn"><span class="actionIcon">↻</span><span class="actionLabel"><b>تحديث الاستخدام</b><small>تحديث مؤشرات الخطط</small></span></button>
            <button class="btn" id="quickNotifyBtn"><span class="actionIcon">⚑</span><span class="actionLabel"><b>التنبيهات</b><small>عرض التنبيهات الحالية</small></span></button>
          </div>
        </div>

        <div class="v24SupportGrid">
          <section class="panel v24SupportCard v24AttentionCard">
            <div class="v24SectionHead compact">
              <div><span class="v24Eyebrow">ATTENTION</span><h2>يحتاج متابعة</h2><p>أولوية التنفيذ والمخاطر الحالية.</p></div>
              <button class="btn" id="refreshAlertsBtn">تحديث</button>
            </div>
            <div id="commandFilters" class="filterChips"></div>
            <div id="commandAlerts" class="quickList v24List"></div>
            <div id="superAlerts" class="quickList v24List v24SecondaryList"></div>
          </section>

          <section class="panel v24SupportCard v24SearchCard searchCard">
            <div class="v24SectionHead compact">
              <div><span class="v24Eyebrow">GLOBAL SEARCH</span><h2>البحث الشامل</h2><p>شركة، فاتورة أو نشاط.</p></div>
            </div>
            <div class="v24SearchBar">
              <input id="globalSearchBox" placeholder="بحث باسم شركة / فاتورة / نشاط" />
              <button class="btn primary" id="globalSearchBtn">بحث</button>
            </div>
            <div id="globalSearchResults" class="quickList v24List"><div class="empty">اكتب كلمتين على الأقل للبحث.</div></div>
          </section>

          <section class="panel v24SupportCard v24UsageCard">
            <div class="v24SectionHead compact">
              <div><span class="v24Eyebrow">USAGE</span><h2>تحليلات الاستخدام</h2><p>استهلاك الشركات مقابل حدود الباقات.</p></div>
              <button class="btn" id="refreshUsageBtn">تحديث</button>
            </div>
            <div id="usageOverview" class="quickList v24List"></div>
          </section>

          <section class="panel v24SupportCard v24SecurityCard" id="securityPanel">
            <div class="v24SectionHead compact">
              <div><span class="v24Eyebrow">SECURITY</span><h2>مراجعة الأمان</h2><p>آخر الدخول والإجراءات الحساسة.</p></div>
              <button class="btn danger" id="loadSecurityBtn">تحديث</button>
            </div>
            <div id="securityReview" class="quickList v24List"></div>
          </section>
        </div>
      </section>

'''

CSS = r'''
    /* SUPER_ADMIN_PHASE2_4_STRUCTURAL_DASHBOARD_REBUILD_V1 */
    /* Structural dashboard rebuild. Existing IDs/data handlers remain unchanged. */
    #appShell.platformPageMode .mainContent{width:min(100%,1280px)!important;max-width:1280px!important;padding:14px 16px 28px!important}

    #appShell.platformPageMode .structuralDashboardV24,
    #appShell.platformPageMode .structuralSupportV24{--v24-ink:#172033;--v24-muted:#68778c;--v24-line:#dde4ec;--v24-soft:#f7f9fc;--v24-primary:#3157d5;--v24-surface:#fff}

    #appShell.platformPageMode .structuralDashboardV24{display:grid!important;gap:10px!important;min-width:0!important}
    #appShell.platformPageMode .v24OverviewHeader{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:2px 2px 4px}
    #appShell.platformPageMode .v24OverviewTitle h2{margin:2px 0 3px;font-size:22px;line-height:1.25;color:var(--v24-ink);letter-spacing:-.02em}
    #appShell.platformPageMode .v24OverviewTitle p{margin:0;font-size:11px;color:var(--v24-muted);line-height:1.45}
    #appShell.platformPageMode .v24Eyebrow{font-size:8px;font-weight:850;letter-spacing:.12em;color:#8a98aa}
    #appShell.platformPageMode .v24OverviewMeta{display:flex;align-items:center;gap:7px;white-space:nowrap;padding:7px 10px;border:1px solid var(--v24-line);border-radius:999px;background:#fff;color:var(--v24-muted);font-size:9px}
    #appShell.platformPageMode .v24LiveDot{width:7px;height:7px;border-radius:50%;background:#16a27a;box-shadow:0 0 0 3px rgba(22,162,122,.10)}

    #appShell.platformPageMode #smartInsights.v24KpiGrid{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:8px!important}
    #appShell.platformPageMode #smartInsights.v24KpiGrid>*{min-width:0!important;min-height:92px!important;padding:13px!important;background:#fff!important;border:1px solid var(--v24-line)!important;border-radius:13px!important;box-shadow:0 4px 14px rgba(22,32,51,.035)!important;overflow:visible!important}
    #appShell.platformPageMode #smartInsights.v24KpiGrid>*:before,#appShell.platformPageMode #smartInsights.v24KpiGrid>*:after{display:none!important;content:none!important}
    #appShell.platformPageMode #smartInsights.v24KpiGrid b,#appShell.platformPageMode #smartInsights.v24KpiGrid strong{color:var(--v24-ink)!important;font-size:20px!important;line-height:1.1!important}
    #appShell.platformPageMode #smartInsights.v24KpiGrid small,#appShell.platformPageMode #smartInsights.v24KpiGrid .muted{font-size:9px!important;color:var(--v24-muted)!important;line-height:1.35!important}

    #appShell.platformPageMode .v24ExecutiveRow{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(300px,.75fr);gap:8px;align-items:start}
    #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:8px!important}
    #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon>*{min-height:72px!important;padding:11px!important;background:#fff!important;border:1px solid var(--v24-line)!important;border-radius:12px!important;box-shadow:none!important;overflow:visible!important}
    #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon>*:before,#appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon>*:after{display:none!important;content:none!important}
    #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon b,#appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon strong{font-size:13px!important;color:var(--v24-ink)!important}
    #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon small,#appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon .muted{font-size:8.5px!important;color:var(--v24-muted)!important}

    #appShell.platformPageMode .v24KpiDetails{margin:0!important;border:1px solid var(--v24-line)!important;border-radius:12px!important;background:#fff!important;box-shadow:none!important;overflow:hidden!important}
    #appShell.platformPageMode .v24KpiDetails>summary{min-height:46px!important;padding:9px 11px!important;background:#fff!important;border:0!important}
    #appShell.platformPageMode .v24KpiDetails>summary b{font-size:11px!important;color:var(--v24-ink)!important}
    #appShell.platformPageMode .v24KpiDetails>summary small{font-size:8px!important;color:var(--v24-muted)!important}
    #appShell.platformPageMode .v24KpiDetails .commandDetailsBody{padding:9px!important;border-top:1px solid var(--v24-line)!important}
    #appShell.platformPageMode .v24KpiDetails #metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:6px!important}
    #appShell.platformPageMode .v24KpiDetails #metrics>*{min-height:62px!important;padding:8px!important;border-radius:9px!important;box-shadow:none!important}

    #appShell.platformPageMode .structuralSupportV24{display:grid!important;gap:10px!important}
    #appShell.platformPageMode .v24CommandPanel,#appShell.platformPageMode .v24SupportCard{margin:0!important;padding:13px!important;background:#fff!important;border:1px solid var(--v24-line)!important;border-radius:13px!important;box-shadow:0 4px 14px rgba(22,32,51,.03)!important;min-width:0!important}
    #appShell.platformPageMode .v24SectionHead{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:0 0 10px;padding:0 0 9px;border-bottom:1px solid var(--v24-line)}
    #appShell.platformPageMode .v24SectionHead.compact{margin-bottom:8px;padding-bottom:8px}
    #appShell.platformPageMode .v24SectionHead h2{margin:2px 0 1px;font-size:14px;line-height:1.25;color:var(--v24-ink)}
    #appShell.platformPageMode .v24SectionHead p{margin:0;font-size:8.5px;line-height:1.4;color:var(--v24-muted)}

    #appShell.platformPageMode .v24QuickActions{display:grid!important;grid-template-columns:repeat(6,minmax(0,1fr))!important;gap:7px!important}
    #appShell.platformPageMode .v24QuickActions .btn{min-height:54px!important;height:auto!important;padding:8px 9px!important;border-radius:10px!important;justify-content:flex-start!important;gap:8px!important;background:#f8fafc!important;border:1px solid var(--v24-line)!important;color:var(--v24-ink)!important;box-shadow:none!important;white-space:normal!important}
    #appShell.platformPageMode .v24QuickActions .btn.primary{background:var(--v24-primary)!important;color:#fff!important;border-color:var(--v24-primary)!important}
    #appShell.platformPageMode .v24QuickActions .actionIcon{width:26px!important;height:26px!important;flex:0 0 26px!important;border-radius:8px!important;display:grid!important;place-items:center!important;background:#fff!important;border:1px solid #e7ebf1!important;font-size:11px!important}
    #appShell.platformPageMode .v24QuickActions .btn.primary .actionIcon{background:rgba(255,255,255,.14)!important;border-color:rgba(255,255,255,.18)!important;color:#fff!important}
    #appShell.platformPageMode .v24QuickActions .actionLabel{min-width:0!important;text-align:start!important}
    #appShell.platformPageMode .v24QuickActions .actionLabel b{display:block;font-size:9.5px!important;line-height:1.3!important}
    #appShell.platformPageMode .v24QuickActions .actionLabel small{display:block;font-size:7.8px!important;line-height:1.35!important;opacity:.72!important}

    #appShell.platformPageMode .v24SupportGrid{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:10px;align-items:start}
    #appShell.platformPageMode .v24AttentionCard{grid-column:span 7}
    #appShell.platformPageMode .v24SearchCard{grid-column:span 5}
    #appShell.platformPageMode .v24UsageCard{grid-column:span 6}
    #appShell.platformPageMode .v24SecurityCard{grid-column:span 6}

    #appShell.platformPageMode .v24SearchBar{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:7px;padding:6px;background:#f8fafc;border:1px solid var(--v24-line);border-radius:10px}
    #appShell.platformPageMode .v24SearchBar input{min-width:0;height:34px;min-height:34px;border-radius:8px;font-size:10px}
    #appShell.platformPageMode .v24SearchBar .btn{height:34px!important;min-height:34px!important;padding:6px 12px!important;font-size:9.5px!important}

    #appShell.platformPageMode .v24List{min-width:0!important;max-height:230px!important;overflow-y:auto!important;overflow-x:hidden!important;scrollbar-width:thin!important}
    #appShell.platformPageMode .v24SecondaryList{margin-top:7px!important;padding-top:7px!important;border-top:1px dashed var(--v24-line)!important}
    #appShell.platformPageMode .v24List>.quickItem,#appShell.platformPageMode .v24List>.searchResult,#appShell.platformPageMode .v24List>.securityItem,#appShell.platformPageMode .v24List>div:not(.empty){min-height:44px!important;padding:7px 8px!important;margin:0 0 5px!important;border:1px solid #edf1f5!important;border-radius:8px!important;background:#fbfcfd!important;box-shadow:none!important;overflow:visible!important}
    #appShell.platformPageMode .v24List b,#appShell.platformPageMode .v24List strong{font-size:9.5px!important;color:var(--v24-ink)!important}
    #appShell.platformPageMode .v24List small,#appShell.platformPageMode .v24List .muted{font-size:8px!important;color:var(--v24-muted)!important}

    #appShell.platformPageMode .structuralSupportV24 .filterChips{gap:5px!important;margin-bottom:7px!important}
    #appShell.platformPageMode .structuralSupportV24 .filterChips>*{min-height:24px!important;padding:3px 7px!important;font-size:8px!important;border-radius:999px!important}

    html[data-theme="dark"] #appShell.platformPageMode .structuralDashboardV24,html[data-theme="dark"] #appShell.platformPageMode .structuralSupportV24{--v24-ink:#eef4fb;--v24-muted:#9aa9bd;--v24-line:#2b3b50;--v24-soft:#142237;--v24-surface:#111d2d}
    html[data-theme="dark"] #appShell.platformPageMode .v24OverviewMeta,html[data-theme="dark"] #appShell.platformPageMode #smartInsights.v24KpiGrid>*,html[data-theme="dark"] #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon>*,html[data-theme="dark"] #appShell.platformPageMode .v24KpiDetails,html[data-theme="dark"] #appShell.platformPageMode .v24CommandPanel,html[data-theme="dark"] #appShell.platformPageMode .v24SupportCard{background:var(--v24-surface)!important;border-color:var(--v24-line)!important;color:var(--v24-ink)!important}
    html[data-theme="dark"] #appShell.platformPageMode .v24SearchBar,html[data-theme="dark"] #appShell.platformPageMode .v24List>.quickItem,html[data-theme="dark"] #appShell.platformPageMode .v24List>.searchResult,html[data-theme="dark"] #appShell.platformPageMode .v24List>.securityItem,html[data-theme="dark"] #appShell.platformPageMode .v24List>div:not(.empty){background:#142237!important;border-color:#2b3b50!important;color:var(--v24-ink)!important}

    @media(max-width:1180px){
      #appShell.platformPageMode #smartInsights.v24KpiGrid{grid-template-columns:repeat(2,minmax(0,1fr))!important}
      #appShell.platformPageMode .v24ExecutiveRow{grid-template-columns:1fr!important}
      #appShell.platformPageMode .v24QuickActions{grid-template-columns:repeat(3,minmax(0,1fr))!important}
    }
    @media(max-width:900px){
      #appShell.platformPageMode .v24SupportGrid{grid-template-columns:1fr!important}
      #appShell.platformPageMode .v24SupportCard{grid-column:1!important}
      #appShell.platformPageMode #executiveRibbon.v24ExecutiveRibbon{grid-template-columns:1fr!important}
    }
    @media(max-width:640px){
      #appShell.platformPageMode .v24OverviewHeader{align-items:flex-start;flex-direction:column}
      #appShell.platformPageMode #smartInsights.v24KpiGrid,#appShell.platformPageMode .v24QuickActions{grid-template-columns:1fr!important}
      #appShell.platformPageMode .mainContent{padding:10px 8px 22px!important}
    }
    /* END SUPER_ADMIN_PHASE2_4_STRUCTURAL_DASHBOARD_REBUILD_V1 */
'''

REQUIRED_IDS = [
    'smartInsights','executiveRibbon','commandDetails','operationsPulse','metrics',
    'quickAddCompanyBtn','quickCreateTenantBtn','quickAuditBtn','quickSourceBtn',
    'quickUsageReportBtn','quickNotifyBtn','commandFilters','commandAlerts',
    'globalSearchBox','globalSearchBtn','globalSearchResults','refreshAlertsBtn',
    'superAlerts','refreshUsageBtn','usageOverview','securityPanel','loadSecurityBtn','securityReview'
]


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def main() -> int:
    if not TARGET.exists():
        print(f'ERROR: target not found: {TARGET}', file=sys.stderr)
        return 2
    text = TARGET.read_text(encoding='utf-8')
    if START in text or 'STRUCTURAL_DASHBOARD_V24' in text:
        print('Phase 2.4 marker already present; nothing to do.')
        return 0
    for marker in REQUIRED:
        if marker not in text:
            print(f'ERROR: required baseline marker missing: {marker}', file=sys.stderr)
            return 3
    if STYLE_ANCHOR not in text:
        print('ERROR: safe Super Admin style anchor not found.', file=sys.stderr)
        return 4

    match = BLOCK_RE.search(text)
    if not match:
        print('ERROR: Overview/Widgets structural block not found.', file=sys.stderr)
        return 5
    old_block = match.group(0)
    for item_id in REQUIRED_IDS:
        count = len(re.findall(rf'id="{re.escape(item_id)}"', old_block))
        if count != 1:
            print(f'ERROR: expected exactly one #{item_id} in old dashboard block, found {count}.', file=sys.stderr)
            return 6
        if HTML.count(f'id="{item_id}"') != 1:
            print(f'ERROR: replacement HTML does not preserve exactly one #{item_id}.', file=sys.stderr)
            return 7

    before = sha256(text)
    text = text[:match.start()] + HTML + text[match.end():]
    text = text.replace(STYLE_ANCHOR, CSS + '\n' + STYLE_ANCHOR, 1)

    if START not in text or END not in text or 'STRUCTURAL_DASHBOARD_V24' not in text:
        print('ERROR: final Phase 2.4 verification failed.', file=sys.stderr)
        return 8
    for item_id in REQUIRED_IDS:
        if len(re.findall(rf'id="{re.escape(item_id)}"', text)) != 1:
            print(f'ERROR: duplicate or missing preserved ID after patch: {item_id}', file=sys.stderr)
            return 9

    TARGET.write_text(text, encoding='utf-8')
    print(f'Applied Phase 2.4 structural dashboard rebuild to {TARGET}')
    print(f'before_sha256={before}')
    print(f'after_sha256={sha256(text)}')
    print('Scope: Overview/Support HTML structure + scoped presentation CSS. Existing IDs and data handlers preserved.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
