#!/usr/bin/env python3
from pathlib import Path
import hashlib
import re
import sys

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START = '/* SUPER_ADMIN_PHASE3_COMPANIES_USERS_WORKSPACE_V1 */'
END = '/* END SUPER_ADMIN_PHASE3_COMPANIES_USERS_WORKSPACE_V1 */'
STYLE_ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'
REQUIRED = [
    '/* SUPER_ADMIN_PHASE2_5_GRID_READABILITY_FINAL_FIX_V1 */',
    'data-dashboard-ui="STRUCTURAL_DASHBOARD_V24"',
]

BLOCK_RE = re.compile(r'      <section id="sec-tenants".*?(?=      <section id="sec-platform-admins")', re.S)

HTML = r'''      <section id="sec-tenants" class="stack orgWorkspaceV3" data-workspace-ui="ORGANIZATIONS_WORKSPACE_V3">
        <header class="v3PageHeader">
          <div class="v3PageTitle">
            <span class="v3Eyebrow">ORGANIZATIONS</span>
            <h2>الشركات</h2>
            <p id="tenantsCount">إدارة الشركات والباقات والحالة التشغيلية من مكان واحد.</p>
          </div>
          <div class="v3HeaderActions">
            <span id="currentTenantBadge" class="badge st-provisioning hidden"></span>
            <button class="btn primary" type="button" data-create-tenant>+ إضافة شركة</button>
          </div>
        </header>

        <div id="tenantViewSummary" class="tenantViewSummary v3SummaryGrid" aria-live="polite"></div>

        <section class="v3ControlCard" aria-label="فلاتر الشركات">
          <div class="v3ControlHead">
            <div><strong>البحث والفلاتر</strong><span>اعثر على الشركة المطلوبة بسرعة.</span></div>
            <div id="savedFilters" class="filterChips v3SavedViews"></div>
          </div>

          <div class="toolbar v3PrimaryFilters">
            <label class="v3Field v3SearchField"><span>بحث</span><input id="tenantSearch" placeholder="اسم الشركة، المسار أو البريد" /></label>
            <label class="v3Field"><span>الحالة</span><select id="tenantStatus" aria-label="الحالة">
              <option value="">كل الحالات</option>
              <option>active</option><option>trialing</option><option>provisioning</option>
              <option>suspended</option><option>past_due</option><option>expired</option><option>cancelled</option>
            </select></label>
            <label class="v3Field"><span>الخطة</span><select id="tenantPlan" aria-label="الخطة">
              <option value="">كل الخطط</option><option>starter</option><option>pro</option><option>enterprise</option>
            </select></label>
            <button class="btn primary v3ApplyBtn" id="applyFiltersBtn">تطبيق</button>
          </div>

          <div class="toolbarSecondary v3SecondaryFilters">
            <div class="v3DateGroup">
              <label class="v3Field"><span>من تاريخ</span><input id="createdFrom" type="date" title="من تاريخ الإنشاء" /></label>
              <label class="v3Field"><span>إلى تاريخ</span><input id="createdTo" type="date" title="إلى تاريخ الإنشاء" /></label>
              <label class="v3Field v3RowsField"><span>الصفوف</span><select id="tenantPageSize" aria-label="عدد الصفوف">
                <option>10</option><option selected>25</option><option>50</option><option>100</option>
              </select></label>
            </div>
            <div class="row v3SecondaryActions">
              <button class="btn" id="resetFiltersBtn">مسح الفلاتر</button>
              <button class="btn" id="saveCurrentViewBtn">حفظ العرض</button>
              <button class="btn" id="exportTenantsBtn">تصدير</button>
              <button class="btn" id="toggleDensityBtn" type="button"><span id="densityIcon">↕</span><span id="densityLabel">عرض مريح</span></button>
            </div>
          </div>
        </section>

        <section class="v3DataCard">
          <div class="v3TableIntro"><div><strong>قائمة الشركات</strong><span>الحالة، الخطة، الصحة والإجراءات.</span></div><span class="v3TableHint">يمكن التمرير أفقياً عند الحاجة</span></div>
          <div class="tableWrap v3TableWrap">
            <table class="v3ManagedTable v3CompaniesTable">
              <thead><tr><th>الشركة</th><th>المسار</th><th>الخطة</th><th>الصحة</th><th>الحالة</th><th>متبقي</th><th>الإجراءات</th></tr></thead>
              <tbody id="tenantsBody"></tbody>
            </table>
          </div>
          <div id="tenantPager" class="pager v3Pager"></div>
        </section>
      </section>

      <section id="sec-users" class="stack usersWorkspaceV3" data-workspace-ui="USERS_WORKSPACE_V3">
        <header class="v3PageHeader">
          <div class="v3PageTitle">
            <span class="v3Eyebrow">USERS & ACCESS</span>
            <h2>مستخدمو الشركات</h2>
            <p id="platformUsersCount">كل الحسابات المسجلة داخل جميع الشركات، بدون عرض كلمات المرور الحالية.</p>
          </div>
          <div class="v3HeaderActions"><span class="badge st-provisioning">Central Users</span></div>
        </header>

        <div id="platformUsersStats" class="userStatsGrid v3SummaryGrid" aria-live="polite"></div>

        <section class="v3ControlCard" aria-label="فلاتر المستخدمين">
          <div class="v3ControlHead"><div><strong>البحث والتصفية</strong><span>تصفية المستخدمين حسب الشركة والدور والحالة.</span></div></div>
          <div class="usersToolbar v3UsersFilters">
            <label class="v3Field v3SearchField"><span>بحث</span><input id="platformUserSearch" placeholder="الاسم، البريد أو الدور" /></label>
            <label class="v3Field"><span>الشركة</span><select id="platformUserTenant"><option value="">كل الشركات</option></select></label>
            <label class="v3Field"><span>الدور</span><select id="platformUserRole">
              <option value="">كل الأدوار</option>
              <option>Admin</option><option>SalesManager</option><option>SalesAgent</option><option>ServiceAdvisor</option><option>PartsAgent</option><option>CrmFollowUp</option><option>Viewer</option><option>MediaBuyer</option><option>AccountManager</option><option>AccountManagerLead</option>
            </select></label>
            <label class="v3Field"><span>الحالة</span><select id="platformUserStatus"><option value="">كل الحالات</option><option value="active">نشط</option><option value="inactive">موقوف</option><option value="deleted">محذوف</option></select></label>
            <button class="btn primary v3ApplyBtn" id="loadPlatformUsersBtn">عرض النتائج</button>
          </div>
        </section>

        <section class="v3DataCard">
          <div class="v3TableIntro"><div><strong>دليل المستخدمين</strong><span>الحساب، الشركة، الصلاحية والحالة.</span></div><span class="v3TableHint">إدارة موحدة لكل الشركات</span></div>
          <div class="tableWrap v3TableWrap">
            <table class="managedUsersTable v3ManagedTable v3UsersTable">
              <thead><tr><th>المستخدم</th><th>الشركة</th><th>الدور</th><th>الحالة</th><th>آخر دخول</th><th>بيانات الدخول</th><th>الإجراءات</th></tr></thead>
              <tbody id="platformUsersBody"><tr><td colspan="7"><div class="empty">جاري تحميل المستخدمين...</div></td></tr></tbody>
            </table>
          </div>
          <div id="platformUsersPager" class="pager v3Pager"></div>
        </section>
      </section>

'''

CSS = r'''
    /* SUPER_ADMIN_PHASE3_COMPANIES_USERS_WORKSPACE_V1 */
    /* Structural UX/UI redesign for Companies + Users. Existing IDs, APIs and handlers are preserved. */
    #appShell.platformPageMode .orgWorkspaceV3,
    #appShell.platformPageMode .usersWorkspaceV3{
      --v3-ink:#172033;
      --v3-muted:#68768a;
      --v3-line:#dce4ed;
      --v3-soft:#f7f9fc;
      --v3-surface:#ffffff;
      --v3-primary:#3157d5;
      --v3-radius:14px;
      display:grid!important;
      grid-template-columns:minmax(0,1fr)!important;
      gap:10px!important;
      min-width:0!important;
      padding:0!important;
      border:0!important;
      background:transparent!important;
      box-shadow:none!important;
      overflow:visible!important;
    }

    #appShell.platformPageMode .v3PageHeader{
      display:flex;align-items:flex-end;justify-content:space-between;gap:16px;
      padding:3px 2px 5px;border:0;background:transparent;
    }
    #appShell.platformPageMode .v3PageTitle{min-width:0}
    #appShell.platformPageMode .v3Eyebrow{display:block;margin-bottom:3px;font-size:9px;font-weight:850;letter-spacing:.11em;color:#8b98aa}
    #appShell.platformPageMode .v3PageTitle h2{margin:0 0 4px;font-size:24px;line-height:1.2;color:var(--v3-ink);letter-spacing:-.02em}
    #appShell.platformPageMode .v3PageTitle p{margin:0;max-width:780px;font-size:10.5px;line-height:1.5;color:var(--v3-muted)}
    #appShell.platformPageMode .v3HeaderActions{display:flex;align-items:center;gap:7px;flex-wrap:wrap;justify-content:flex-end}
    #appShell.platformPageMode .v3HeaderActions .btn{min-height:36px!important;height:36px!important;padding:6px 11px!important;border-radius:9px!important;font-size:10.5px!important}
    #appShell.platformPageMode .v3HeaderActions .badge{min-height:28px!important;padding:5px 9px!important;font-size:9px!important}

    /* Dynamic summary blocks become clean executive stat cards. */
    #appShell.platformPageMode .v3SummaryGrid{
      display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:8px!important;min-width:0!important;margin:0!important;
    }
    #appShell.platformPageMode .v3SummaryGrid>*{
      min-width:0!important;min-height:82px!important;padding:11px 12px!important;margin:0!important;
      border:1px solid var(--v3-line)!important;border-radius:12px!important;background:#fff!important;box-shadow:0 4px 14px rgba(22,32,51,.035)!important;
    }
    #appShell.platformPageMode .v3SummaryGrid b,
    #appShell.platformPageMode .v3SummaryGrid strong{font-size:18px!important;line-height:1.15!important;color:var(--v3-ink)!important}
    #appShell.platformPageMode .v3SummaryGrid small,
    #appShell.platformPageMode .v3SummaryGrid .muted{font-size:9px!important;line-height:1.4!important;color:var(--v3-muted)!important}

    #appShell.platformPageMode .v3ControlCard,
    #appShell.platformPageMode .v3DataCard{
      min-width:0!important;padding:13px!important;border:1px solid var(--v3-line)!important;border-radius:var(--v3-radius)!important;background:#fff!important;box-shadow:0 4px 14px rgba(22,32,51,.03)!important;
    }
    #appShell.platformPageMode .v3ControlHead,
    #appShell.platformPageMode .v3TableIntro{
      display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:10px;padding-bottom:9px;border-bottom:1px solid var(--v3-line);
    }
    #appShell.platformPageMode .v3ControlHead>div:first-child,
    #appShell.platformPageMode .v3TableIntro>div:first-child{display:grid;gap:2px;min-width:0}
    #appShell.platformPageMode .v3ControlHead strong,
    #appShell.platformPageMode .v3TableIntro strong{font-size:13.5px;color:var(--v3-ink)}
    #appShell.platformPageMode .v3ControlHead span,
    #appShell.platformPageMode .v3TableIntro span{font-size:9px;color:var(--v3-muted)}
    #appShell.platformPageMode .v3SavedViews{justify-content:flex-end!important;margin:0!important;max-width:55%}
    #appShell.platformPageMode .v3SavedViews>*{min-height:24px!important;padding:3px 7px!important;font-size:8px!important;border-radius:999px!important}

    #appShell.platformPageMode .v3PrimaryFilters,
    #appShell.platformPageMode .v3UsersFilters{
      display:grid!important;grid-template-columns:minmax(250px,1.7fr) minmax(145px,.75fr) minmax(145px,.75fr) auto!important;
      align-items:end!important;gap:8px!important;padding:0!important;margin:0!important;background:transparent!important;border:0!important;box-shadow:none!important;
    }
    #appShell.platformPageMode .v3UsersFilters{grid-template-columns:minmax(240px,1.55fr) minmax(150px,.8fr) minmax(170px,.9fr) minmax(135px,.7fr) auto!important}
    #appShell.platformPageMode .v3Field{display:grid;gap:5px;min-width:0}
    #appShell.platformPageMode .v3Field>span{font-size:8.5px;font-weight:750;color:#7a8799}
    #appShell.platformPageMode .v3Field input,
    #appShell.platformPageMode .v3Field select{
      width:100%!important;min-width:0!important;height:38px!important;min-height:38px!important;padding:7px 10px!important;
      border:1px solid var(--v3-line)!important;border-radius:9px!important;background:#fff!important;color:var(--v3-ink)!important;font-size:10.5px!important;box-shadow:none!important;
    }
    #appShell.platformPageMode .v3Field input:focus,
    #appShell.platformPageMode .v3Field select:focus{border-color:#9fb0ed!important;box-shadow:0 0 0 3px rgba(49,87,213,.08)!important;outline:none!important}
    #appShell.platformPageMode .v3ApplyBtn{height:38px!important;min-height:38px!important;padding:7px 14px!important;border-radius:9px!important;white-space:nowrap!important}

    #appShell.platformPageMode .v3SecondaryFilters{
      display:flex!important;align-items:end!important;justify-content:space-between!important;gap:12px!important;
      margin:10px 0 0!important;padding:10px 0 0!important;border-top:1px dashed var(--v3-line)!important;background:transparent!important;
    }
    #appShell.platformPageMode .v3DateGroup{display:grid;grid-template-columns:repeat(3,minmax(120px,1fr));gap:7px;min-width:min(100%,470px)}
    #appShell.platformPageMode .v3SecondaryActions{display:flex!important;align-items:center!important;justify-content:flex-end!important;gap:6px!important;flex-wrap:wrap!important}
    #appShell.platformPageMode .v3SecondaryActions .btn{height:34px!important;min-height:34px!important;padding:6px 9px!important;font-size:9.5px!important;border-radius:8px!important;box-shadow:none!important}

    #appShell.platformPageMode .v3TableHint{white-space:nowrap;padding:4px 7px;border-radius:999px;background:#f5f7fa;color:#8491a3!important;font-size:8px!important}
    #appShell.platformPageMode .v3TableWrap{
      min-width:0!important;width:100%!important;overflow:auto!important;border:1px solid var(--v3-line)!important;border-radius:11px!important;background:#fff!important;box-shadow:none!important;
      scrollbar-width:thin!important;
    }
    #appShell.platformPageMode .v3ManagedTable{width:100%!important;min-width:920px!important;border-collapse:separate!important;border-spacing:0!important;background:#fff!important}
    #appShell.platformPageMode .v3ManagedTable thead th{
      position:sticky!important;top:0!important;z-index:2!important;height:39px!important;padding:8px 10px!important;
      background:#f7f9fc!important;color:#6e7c90!important;border-bottom:1px solid var(--v3-line)!important;
      font-size:8.5px!important;font-weight:850!important;letter-spacing:.02em!important;white-space:nowrap!important;
    }
    #appShell.platformPageMode .v3ManagedTable tbody td{
      min-height:50px!important;padding:9px 10px!important;border-bottom:1px solid #edf1f5!important;color:#334155!important;font-size:10px!important;vertical-align:middle!important;
    }
    #appShell.platformPageMode .v3ManagedTable tbody tr:last-child td{border-bottom:0!important}
    #appShell.platformPageMode .v3ManagedTable tbody tr:hover td{background:#fbfcfe!important}
    #appShell.platformPageMode .v3ManagedTable .badge{font-size:8px!important;min-height:23px!important;padding:3px 7px!important;border-radius:999px!important}
    #appShell.platformPageMode .v3ManagedTable .btn{min-height:30px!important;height:30px!important;padding:5px 8px!important;font-size:8.8px!important;border-radius:7px!important;box-shadow:none!important}

    #appShell.platformPageMode .v3Pager{display:flex!important;align-items:center!important;justify-content:space-between!important;gap:8px!important;margin-top:9px!important;padding-top:9px!important;border-top:1px solid var(--v3-line)!important}
    #appShell.platformPageMode .v3Pager .btn{min-height:31px!important;height:31px!important;padding:5px 9px!important;font-size:9px!important;border-radius:8px!important}

    html[data-theme="dark"] #appShell.platformPageMode .orgWorkspaceV3,
    html[data-theme="dark"] #appShell.platformPageMode .usersWorkspaceV3{
      --v3-ink:#eef4fb;--v3-muted:#9cacc0;--v3-line:#2b3b50;--v3-soft:#142237;--v3-surface:#111d2d;
    }
    html[data-theme="dark"] #appShell.platformPageMode .v3SummaryGrid>*,
    html[data-theme="dark"] #appShell.platformPageMode .v3ControlCard,
    html[data-theme="dark"] #appShell.platformPageMode .v3DataCard,
    html[data-theme="dark"] #appShell.platformPageMode .v3TableWrap,
    html[data-theme="dark"] #appShell.platformPageMode .v3ManagedTable,
    html[data-theme="dark"] #appShell.platformPageMode .v3Field input,
    html[data-theme="dark"] #appShell.platformPageMode .v3Field select{background:var(--v3-surface)!important;border-color:var(--v3-line)!important;color:var(--v3-ink)!important}
    html[data-theme="dark"] #appShell.platformPageMode .v3ManagedTable thead th{background:#142237!important;color:#9eacc0!important;border-color:var(--v3-line)!important}
    html[data-theme="dark"] #appShell.platformPageMode .v3ManagedTable tbody td{color:#dbe5f2!important;border-color:#24354a!important}
    html[data-theme="dark"] #appShell.platformPageMode .v3ManagedTable tbody tr:hover td{background:#142237!important}

    @media(max-width:1180px){
      #appShell.platformPageMode .v3SummaryGrid{grid-template-columns:repeat(2,minmax(0,1fr))!important}
      #appShell.platformPageMode .v3PrimaryFilters{grid-template-columns:repeat(3,minmax(0,1fr))!important}
      #appShell.platformPageMode .v3PrimaryFilters .v3SearchField{grid-column:1/-1!important}
      #appShell.platformPageMode .v3UsersFilters{grid-template-columns:repeat(2,minmax(0,1fr))!important}
      #appShell.platformPageMode .v3UsersFilters .v3SearchField{grid-column:1/-1!important}
    }
    @media(max-width:820px){
      #appShell.platformPageMode .v3PageHeader{align-items:flex-start;flex-direction:column}
      #appShell.platformPageMode .v3HeaderActions{width:100%;justify-content:flex-start}
      #appShell.platformPageMode .v3PrimaryFilters,
      #appShell.platformPageMode .v3UsersFilters{grid-template-columns:1fr!important}
      #appShell.platformPageMode .v3PrimaryFilters .v3SearchField,
      #appShell.platformPageMode .v3UsersFilters .v3SearchField{grid-column:1!important}
      #appShell.platformPageMode .v3SecondaryFilters{align-items:stretch!important;flex-direction:column!important}
      #appShell.platformPageMode .v3DateGroup{grid-template-columns:1fr!important;min-width:0!important;width:100%!important}
      #appShell.platformPageMode .v3SecondaryActions{justify-content:flex-start!important}
      #appShell.platformPageMode .v3SavedViews{max-width:100%!important;justify-content:flex-start!important}
    }
    @media(max-width:560px){
      #appShell.platformPageMode .v3SummaryGrid{grid-template-columns:1fr!important}
      #appShell.platformPageMode .v3PageTitle h2{font-size:21px!important}
      #appShell.platformPageMode .v3ControlCard,#appShell.platformPageMode .v3DataCard{padding:10px!important}
    }
    /* END SUPER_ADMIN_PHASE3_COMPANIES_USERS_WORKSPACE_V1 */
'''

PRESERVED_IDS = [
    'tenantsCount','currentTenantBadge','tenantViewSummary','savedFilters','tenantSearch','tenantStatus','tenantPlan','applyFiltersBtn',
    'createdFrom','createdTo','tenantPageSize','resetFiltersBtn','saveCurrentViewBtn','exportTenantsBtn','toggleDensityBtn','densityIcon','densityLabel','tenantsBody','tenantPager',
    'platformUsersCount','platformUsersStats','platformUserSearch','platformUserTenant','platformUserRole','platformUserStatus','loadPlatformUsersBtn','platformUsersBody','platformUsersPager'
]


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def main() -> int:
    if not TARGET.exists():
        print(f'ERROR: target not found: {TARGET}', file=sys.stderr)
        return 2
    text = TARGET.read_text(encoding='utf-8')
    if START in text or 'ORGANIZATIONS_WORKSPACE_V3' in text:
        print('Phase 3 marker already present; nothing to do.')
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
        print('ERROR: Companies + Users block not found.', file=sys.stderr)
        return 5
    if len(BLOCK_RE.findall(text)) != 1:
        print('ERROR: Companies + Users block count is not exactly one.', file=sys.stderr)
        return 6

    old = match.group(0)
    for item_id in PRESERVED_IDS:
        if len(re.findall(rf'id="{re.escape(item_id)}"', old)) != 1:
            print(f'ERROR: expected exactly one #{item_id} in current Companies/Users block.', file=sys.stderr)
            return 7
        if HTML.count(f'id="{item_id}"') != 1:
            print(f'ERROR: replacement HTML does not preserve exactly one #{item_id}.', file=sys.stderr)
            return 8

    before = sha256(text)
    text = text[:match.start()] + HTML + text[match.end():]
    text = text.replace(STYLE_ANCHOR, CSS + '\n' + STYLE_ANCHOR, 1)

    if START not in text or END not in text or 'ORGANIZATIONS_WORKSPACE_V3' not in text or 'USERS_WORKSPACE_V3' not in text:
        print('ERROR: Phase 3 marker verification failed.', file=sys.stderr)
        return 9
    for item_id in PRESERVED_IDS:
        if len(re.findall(rf'id="{re.escape(item_id)}"', text)) != 1:
            print(f'ERROR: duplicate or missing preserved ID after patch: {item_id}', file=sys.stderr)
            return 10

    TARGET.write_text(text, encoding='utf-8')
    print(f'Applied Phase 3 Companies & Users workspace redesign to {TARGET}')
    print(f'before_sha256={before}')
    print(f'after_sha256={sha256(text)}')
    print('Scope: Companies/Users HTML structure + scoped presentation CSS. Existing IDs/data handlers preserved.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
