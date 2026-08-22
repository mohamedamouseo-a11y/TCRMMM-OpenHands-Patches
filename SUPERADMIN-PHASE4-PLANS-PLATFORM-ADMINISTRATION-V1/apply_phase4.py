#!/usr/bin/env python3
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path('/var/www/TCRMMT')
INDEX = ROOT / 'server/_core/index.ts'
PLANS = ROOT / 'server/superAdminPlansPage.ts'

INDEX_START = '/* SUPER_ADMIN_PHASE4_PLATFORM_ADMINISTRATION_V1 */'
INDEX_END = '/* END SUPER_ADMIN_PHASE4_PLATFORM_ADMINISTRATION_V1 */'
PLANS_START = '/* SUPER_ADMIN_PHASE4_PLANS_WORKSPACE_V1 */'
PLANS_END = '/* END SUPER_ADMIN_PHASE4_PLANS_WORKSPACE_V1 */'
INDEX_STYLE_ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'
PLANS_STYLE_ANCHOR = '  </style>\n</head>\n<body>'

ADMIN_BLOCK_RE = re.compile(r'      <section id="sec-platform-admins".*?(?=      <section id="sec-activity")', re.S)

ADMIN_HTML = r'''      <section id="sec-platform-admins" class="stack platformAdminsWorkspaceV4" data-owner-only data-workspace-ui="PLATFORM_ADMINS_WORKSPACE_V4" hidden style="display:none">
        <header class="v4AdminHeader">
          <div class="v4AdminTitle">
            <span class="v4Eyebrow">PLATFORM ADMINISTRATION</span>
            <h2>مسؤولو المنصة</h2>
            <p id="platformAdminsCount">إدارة مسؤولي المنصة وربط كل مسؤول بالشركات التابعة له.</p>
          </div>
          <div class="v4AdminActions">
            <span class="v4OwnerBadge">Owner Only</span>
            <button class="btn primary" id="openPlatformAdminCreateBtn">+ إضافة مسؤول</button>
          </div>
        </header>

        <div id="platformAdminStats" class="platformAdminStats v4AdminStats" aria-live="polite"></div>

        <section class="v4AdminDataCard">
          <div class="v4AdminTableHead">
            <div><strong>دليل مسؤولي المنصة</strong><span>الحسابات، الشركات المسندة، آخر دخول والحالة.</span></div>
            <span class="v4TableHint">صلاحيات مركزية</span>
          </div>
          <div class="tableWrap v4AdminTableWrap">
            <table class="platformAdminsTable v4AdminTable">
              <thead><tr><th>المسؤول</th><th>الحالة</th><th>أنشأه</th><th>الشركات التابعة</th><th>آخر دخول</th><th>الإجراءات</th></tr></thead>
              <tbody id="platformAdminsBody"><tr><td colspan="6"><div class="empty">جاري تحميل مسؤولي المنصة...</div></td></tr></tbody>
            </table>
          </div>
        </section>
      </section>

'''

INDEX_CSS = r'''
    /* SUPER_ADMIN_PHASE4_PLATFORM_ADMINISTRATION_V1 */
    #appShell.platformPageMode .platformAdminsWorkspaceV4{
      --v4-ink:#172033;--v4-muted:#68778a;--v4-line:#dce4ed;--v4-soft:#f7f9fc;--v4-surface:#fff;--v4-primary:#3157d5;
      display:grid!important;grid-template-columns:minmax(0,1fr)!important;gap:10px!important;min-width:0!important;
      padding:0!important;border:0!important;background:transparent!important;box-shadow:none!important;overflow:visible!important;
    }
    #appShell.platformPageMode .v4AdminHeader{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;padding:3px 2px 5px}
    #appShell.platformPageMode .v4AdminTitle{min-width:0}
    #appShell.platformPageMode .v4Eyebrow{display:block;margin-bottom:3px;font-size:9px;font-weight:850;letter-spacing:.11em;color:#8b98aa}
    #appShell.platformPageMode .v4AdminTitle h2{margin:0 0 4px;font-size:24px;line-height:1.2;color:var(--v4-ink);letter-spacing:-.02em}
    #appShell.platformPageMode .v4AdminTitle p{margin:0;max-width:760px;font-size:10.5px;line-height:1.5;color:var(--v4-muted)}
    #appShell.platformPageMode .v4AdminActions{display:flex;align-items:center;gap:7px;flex-wrap:wrap;justify-content:flex-end}
    #appShell.platformPageMode .v4AdminActions .btn{height:36px!important;min-height:36px!important;padding:6px 11px!important;border-radius:9px!important;font-size:10.5px!important}
    #appShell.platformPageMode .v4OwnerBadge{display:inline-flex;align-items:center;min-height:28px;padding:5px 9px;border:1px solid #dddafb;border-radius:999px;background:#f3f2ff;color:#6352c8;font-size:8.5px;font-weight:850}
    #appShell.platformPageMode .v4AdminStats{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:8px!important;margin:0!important}
    #appShell.platformPageMode .v4AdminStats>*{min-width:0!important;min-height:82px!important;padding:11px 12px!important;margin:0!important;border:1px solid var(--v4-line)!important;border-radius:12px!important;background:#fff!important;box-shadow:0 4px 14px rgba(22,32,51,.035)!important}
    #appShell.platformPageMode .v4AdminStats b,#appShell.platformPageMode .v4AdminStats strong{font-size:18px!important;line-height:1.15!important;color:var(--v4-ink)!important}
    #appShell.platformPageMode .v4AdminStats small,#appShell.platformPageMode .v4AdminStats .muted{font-size:9px!important;line-height:1.4!important;color:var(--v4-muted)!important}
    #appShell.platformPageMode .v4AdminDataCard{min-width:0;padding:13px;border:1px solid var(--v4-line);border-radius:14px;background:#fff;box-shadow:0 4px 14px rgba(22,32,51,.03)}
    #appShell.platformPageMode .v4AdminTableHead{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:10px;padding-bottom:9px;border-bottom:1px solid var(--v4-line)}
    #appShell.platformPageMode .v4AdminTableHead>div{display:grid;gap:2px;min-width:0}
    #appShell.platformPageMode .v4AdminTableHead strong{font-size:13.5px;color:var(--v4-ink)}
    #appShell.platformPageMode .v4AdminTableHead span{font-size:9px;color:var(--v4-muted)}
    #appShell.platformPageMode .v4TableHint{white-space:nowrap;padding:4px 7px;border-radius:999px;background:#f5f7fa;color:#8491a3!important;font-size:8px!important}
    #appShell.platformPageMode .v4AdminTableWrap{width:100%!important;min-width:0!important;overflow:auto!important;border:1px solid var(--v4-line)!important;border-radius:11px!important;background:#fff!important;box-shadow:none!important;scrollbar-width:thin!important}
    #appShell.platformPageMode .v4AdminTable{width:100%!important;min-width:880px!important;border-collapse:separate!important;border-spacing:0!important;background:#fff!important}
    #appShell.platformPageMode .v4AdminTable thead th{position:sticky!important;top:0!important;z-index:2!important;height:39px!important;padding:8px 10px!important;background:#f7f9fc!important;color:#6e7c90!important;border-bottom:1px solid var(--v4-line)!important;font-size:8.5px!important;font-weight:850!important;white-space:nowrap!important}
    #appShell.platformPageMode .v4AdminTable tbody td{min-height:50px!important;padding:9px 10px!important;border-bottom:1px solid #edf1f5!important;color:#334155!important;font-size:10px!important;vertical-align:middle!important}
    #appShell.platformPageMode .v4AdminTable tbody tr:hover td{background:#fbfcfe!important}
    #appShell.platformPageMode .v4AdminTable .badge{font-size:8px!important;min-height:23px!important;padding:3px 7px!important;border-radius:999px!important}
    #appShell.platformPageMode .v4AdminTable .btn{height:30px!important;min-height:30px!important;padding:5px 8px!important;font-size:8.8px!important;border-radius:7px!important;box-shadow:none!important}
    #appShell.platformPageMode #platformAdminDrawer .drawerInner{max-width:560px!important}
    #appShell.platformPageMode #platformAdminDrawer .drawerHead{padding-bottom:12px!important;border-bottom:1px solid var(--v4-line)!important}
    #appShell.platformPageMode #platformAdminDrawer .field{gap:5px!important}
    #appShell.platformPageMode #platformAdminDrawer .field label{font-size:9px!important;color:var(--v4-muted)!important}
    #appShell.platformPageMode #platformAdminDrawer input,#appShell.platformPageMode #platformAdminDrawer select{min-height:39px!important;border-radius:9px!important}
    html[data-theme="dark"] #appShell.platformPageMode .platformAdminsWorkspaceV4{--v4-ink:#eef4fb;--v4-muted:#9cacc0;--v4-line:#2b3b50;--v4-soft:#142237;--v4-surface:#111d2d}
    html[data-theme="dark"] #appShell.platformPageMode .v4AdminStats>*,html[data-theme="dark"] #appShell.platformPageMode .v4AdminDataCard,html[data-theme="dark"] #appShell.platformPageMode .v4AdminTableWrap,html[data-theme="dark"] #appShell.platformPageMode .v4AdminTable{background:var(--v4-surface)!important;border-color:var(--v4-line)!important;color:var(--v4-ink)!important}
    html[data-theme="dark"] #appShell.platformPageMode .v4AdminTable thead th{background:#142237!important;color:#9eacc0!important;border-color:var(--v4-line)!important}
    html[data-theme="dark"] #appShell.platformPageMode .v4AdminTable tbody td{color:#dbe5f2!important;border-color:#24354a!important}
    @media(max-width:980px){#appShell.platformPageMode .v4AdminStats{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
    @media(max-width:700px){#appShell.platformPageMode .v4AdminHeader{align-items:flex-start;flex-direction:column}#appShell.platformPageMode .v4AdminActions{width:100%;justify-content:flex-start}#appShell.platformPageMode .v4AdminStats{grid-template-columns:1fr!important}}
    /* END SUPER_ADMIN_PHASE4_PLATFORM_ADMINISTRATION_V1 */
'''

PLANS_CSS = r'''
    /* SUPER_ADMIN_PHASE4_PLANS_WORKSPACE_V1 */
    /* Final enterprise visual layer for the standalone Plans & Commercial workspace. */
    body{background:#f4f6f9!important;color:#172033!important;font-size:13px!important}
    .shell{max-width:1500px!important;padding:16px!important}
    .top{position:sticky!important;top:0!important;z-index:40!important;min-height:60px!important;margin:-16px -16px 12px!important;padding:8px 16px!important;grid-template-columns:minmax(260px,1fr) auto!important;background:rgba(255,255,255,.96)!important;border-bottom:1px solid #dce4ed!important;box-shadow:0 4px 16px rgba(22,32,51,.045)!important;backdrop-filter:blur(14px)!important}
    .identity{gap:10px!important}.mark{width:36px!important;height:36px!important;border-radius:10px!important;background:#3157d5!important;box-shadow:none!important}.identity:after{min-height:23px!important;padding:3px 8px!important;font-size:8px!important;background:#f3f4ff!important;border-color:#dedffc!important;color:#5d59c7!important}
    h1{font-size:19px!important;line-height:1.2!important}.sub{font-size:9px!important;color:#6d7a8d!important;margin-top:2px!important}.actions{gap:6px!important}.actions .btn{min-height:34px!important;height:34px!important;padding:6px 10px!important;border-radius:8px!important;font-size:9.5px!important;box-shadow:none!important}
    .safetyNotice{margin-bottom:10px!important;border-radius:11px!important;box-shadow:none!important}.safetyNotice summary{min-height:44px!important;padding:8px 11px!important;grid-template-columns:26px minmax(0,1fr) auto!important}.noticeIcon{width:25px!important;height:25px!important;border-radius:8px!important}.noticeSummary strong{font-size:10.5px!important}.noticeSummary small{font-size:8.5px!important}.status{min-height:36px!important;padding:7px 34px 7px 11px!important;border-radius:9px!important;font-size:9.5px!important;margin-bottom:10px!important}
    .tabs{position:sticky!important;top:61px!important;z-index:32!important;display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:6px!important;margin:0 0 12px!important;padding:6px!important;border:1px solid #dce4ed!important;border-radius:12px!important;background:rgba(255,255,255,.96)!important;box-shadow:0 4px 14px rgba(22,32,51,.035)!important;backdrop-filter:blur(12px)!important}
    .tab{min-height:48px!important;padding:6px 9px!important;grid-template-columns:30px minmax(0,1fr)!important;gap:8px!important;border-radius:9px!important;box-shadow:none!important}.tabIcon{width:30px!important;height:30px!important;border-radius:8px!important;font-size:12px!important}.tabText b{font-size:10.5px!important}.tabText small{font-size:7.8px!important}.tab.active{background:#eef2ff!important;border-color:#d8e0ff!important;box-shadow:none!important}.tab.active .tabIcon{background:#3157d5!important;box-shadow:none!important}
    .viewIntro{min-height:76px!important;margin:0 0 10px!important;padding:12px 14px!important;grid-template-columns:38px minmax(0,1fr) auto!important;gap:10px!important;border-radius:12px!important;background:#fff!important;border:1px solid #dce4ed!important;box-shadow:0 4px 14px rgba(22,32,51,.03)!important}.viewIntro:after{display:none!important}.viewIntroIcon{width:38px!important;height:38px!important;border-radius:10px!important;background:#3157d5!important;box-shadow:none!important;font-size:15px!important}.viewEyebrow{font-size:8px!important}.viewIntro h2{font-size:17px!important}.viewIntro p{font-size:9px!important;line-height:1.5!important}.viewIntroBadge{min-height:25px!important;padding:4px 8px!important;font-size:8px!important}
    .card{padding:13px!important;border:1px solid #dce4ed!important;border-radius:13px!important;background:#fff!important;box-shadow:0 4px 14px rgba(22,32,51,.03)!important}.cardHead{margin-bottom:10px!important;padding-bottom:8px!important;border-bottom:1px solid #edf1f5!important}.cardHead h2{font-size:14px!important}.cardHead p{font-size:8.5px!important;margin-top:3px!important}
    .grid,.commercialGrid{grid-template-columns:minmax(280px,330px) minmax(0,1fr)!important;gap:12px!important}.grid>aside.card,.commercialGrid>aside.card{top:122px!important;box-shadow:none!important}.grid>section.card.editor,.commercialGrid>section.card.editor{box-shadow:none!important}
    .list{gap:6px!important}.listItem{min-height:62px!important;padding:9px 10px!important;border-radius:9px!important;background:#fafbfc!important;box-shadow:none!important}.listItem b{font-size:10.5px!important}.listItem.active{background:#eef2ff!important;border-color:#ccd6ff!important;box-shadow:none!important}.listItem.active:after{width:20px!important;height:20px!important;border-radius:6px!important;font-size:8px!important;background:#3157d5!important}
    .field{gap:4px!important}.field label{font-size:8.5px!important}.input,.select{min-height:37px!important;height:auto!important;padding:7px 9px!important;border-radius:8px!important;background:#fff!important;border-color:#dce4ed!important;font-size:10px!important}.input:focus,.select:focus{border-color:#9eb0ee!important;box-shadow:0 0 0 3px rgba(49,87,213,.08)!important}
    .sectionBox{padding:11px!important;border-radius:10px!important;background:#f9fafc!important;border-color:#e2e8f0!important;box-shadow:none!important}.sectionTitle{margin-bottom:8px!important}.sectionTitle b{font-size:12px!important}.sectionTitle small{font-size:8px!important}.featureGrid,.limitGrid{gap:7px!important}.featureRow,.limitRow,.miniItem,.previewBox,.summaryCard,.whatsappUsageCard,.checkField{border-radius:9px!important;box-shadow:none!important}.featureRow,.limitRow{padding:8px!important}.featureRow p{font-size:8.5px!important}.toggle{width:17px!important;height:17px!important}
    .summaryGrid{gap:7px!important}.summaryCard{min-height:76px!important;padding:10px!important;background:#fafbfc!important}.summaryCard:after{display:none!important}.summaryCard span{font-size:8.5px!important}.summaryCard b{font-size:17px!important;margin-top:4px!important}.settingsGrid{gap:7px!important}.checkField{min-height:46px!important;padding:8px 9px!important;font-size:9px!important}.three,.split{gap:7px!important}
    .footerBar{position:sticky!important;bottom:8px!important;padding:8px!important;border-radius:10px!important;box-shadow:0 8px 24px rgba(22,32,51,.09)!important}.footerBar .btn{min-width:105px!important;min-height:34px!important;height:34px!important;padding:6px 9px!important;font-size:9px!important;border-radius:8px!important}
    .tableList,.codeList{padding:7px!important;border-radius:9px!important;box-shadow:none!important}.miniItem{padding:8px 9px!important}.commercialToolbar{gap:6px!important}.commercialToolbar .btn{min-height:34px!important;height:34px!important;padding:6px 9px!important;font-size:9px!important;border-radius:8px!important}
    @media(max-width:1050px){.grid,.commercialGrid{grid-template-columns:1fr!important}.grid>aside.card,.commercialGrid>aside.card{position:relative!important;top:auto!important}.tabs{top:61px!important}}
    @media(max-width:760px){.shell{padding:10px!important}.top{margin:-10px -10px 10px!important;padding:8px 10px!important;grid-template-columns:1fr!important}.tabs{position:relative!important;top:auto!important;grid-template-columns:1fr!important}.viewIntro{grid-template-columns:34px minmax(0,1fr)!important}.viewIntroBadge{display:none!important}.summaryGrid,.settingsGrid{grid-template-columns:1fr!important}.footerBar{position:relative!important;bottom:auto!important}}
    /* END SUPER_ADMIN_PHASE4_PLANS_WORKSPACE_V1 */
'''

ADMIN_IDS = ['platformAdminsCount','openPlatformAdminCreateBtn','platformAdminStats','platformAdminsBody']


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def patch_index(text: str) -> str:
    if INDEX_START in text or 'PLATFORM_ADMINS_WORKSPACE_V4' in text:
        return text
    if '/* SUPER_ADMIN_PHASE3_COMPANIES_USERS_WORKSPACE_V1 */' not in text:
        raise RuntimeError('Phase 3 baseline marker missing in index.ts')
    if INDEX_STYLE_ANCHOR not in text:
        raise RuntimeError('Super Admin style anchor missing in index.ts')
    match = ADMIN_BLOCK_RE.search(text)
    if not match or len(ADMIN_BLOCK_RE.findall(text)) != 1:
        raise RuntimeError('Platform Admin section not found exactly once')
    old = match.group(0)
    for item_id in ADMIN_IDS:
        if len(re.findall(rf'id="{re.escape(item_id)}"', old)) != 1:
            raise RuntimeError(f'Expected exactly one #{item_id} in current Platform Admin section')
        if ADMIN_HTML.count(f'id="{item_id}"') != 1:
            raise RuntimeError(f'Replacement does not preserve exactly one #{item_id}')
    text = text[:match.start()] + ADMIN_HTML + text[match.end():]
    text = text.replace(INDEX_STYLE_ANCHOR, INDEX_CSS + '\n' + INDEX_STYLE_ANCHOR, 1)
    text = text.replace('<span class="navLabel">مزود المنصة</span>', '<span class="navLabel">مسؤولو المنصة</span>', 1)
    for item_id in ADMIN_IDS:
        if len(re.findall(rf'id="{re.escape(item_id)}"', text)) != 1:
            raise RuntimeError(f'Duplicate or missing #{item_id} after patch')
    return text


def patch_plans(text: str) -> str:
    if PLANS_START in text:
        return text
    if 'PLANS_CATALOG_PROFESSIONAL_UX_UI_V1' not in text:
        raise RuntimeError('Plans catalog baseline marker missing')
    if text.count(PLANS_STYLE_ANCHOR) != 1:
        raise RuntimeError('Plans style anchor not found exactly once')
    return text.replace(PLANS_STYLE_ANCHOR, PLANS_CSS + '\n' + PLANS_STYLE_ANCHOR, 1)


def main() -> int:
    if not INDEX.exists() or not PLANS.exists():
        print('ERROR: target files missing', file=sys.stderr)
        return 2
    index_before = INDEX.read_text(encoding='utf-8')
    plans_before = PLANS.read_text(encoding='utf-8')
    try:
        index_after = patch_index(index_before)
        plans_after = patch_plans(plans_before)
    except RuntimeError as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 3
    if index_after == index_before and plans_after == plans_before:
        print('Phase 4 already present; nothing to do.')
        return 0
    if INDEX_START not in index_after or INDEX_END not in index_after:
        print('ERROR: index Phase 4 markers missing after patch', file=sys.stderr)
        return 4
    if PLANS_START not in plans_after or PLANS_END not in plans_after:
        print('ERROR: plans Phase 4 markers missing after patch', file=sys.stderr)
        return 5
    INDEX.write_text(index_after, encoding='utf-8')
    PLANS.write_text(plans_after, encoding='utf-8')
    print('Applied Phase 4 Plans & Platform Administration UX/UI patch.')
    print(f'index_before_sha256={sha256(index_before)}')
    print(f'index_after_sha256={sha256(index_after)}')
    print(f'plans_before_sha256={sha256(plans_before)}')
    print(f'plans_after_sha256={sha256(plans_after)}')
    print('Scope: Platform Admin structural UI + Plans standalone visual layer. No DB/API/Auth/Business Logic changes.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
