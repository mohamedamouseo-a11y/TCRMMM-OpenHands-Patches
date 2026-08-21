#!/usr/bin/env python3
from pathlib import Path
import re, shutil, sys, datetime

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START = '/* SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1 */'
END = '/* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1 */'

if not TARGET.exists():
    sys.exit(f'ERROR: target not found: {TARGET}')

text = TARGET.read_text(encoding='utf-8')
if START in text:
    print('Phase 1 patch already present; no changes made.')
    sys.exit(0)

stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
backup = TARGET.with_name(TARGET.name + f'.pre-phase1-{stamp}.bak')
shutil.copy2(TARGET, backup)

old_nav_re = re.compile(r'<nav class="sidebarNav" aria-label="التنقل الرئيسي">.*?</nav>', re.S)
match = old_nav_re.search(text)
if not match:
    sys.exit('ERROR: sidebarNav block not found; aborting without write.')

new_nav = '''<nav class="sidebarNav" aria-label="التنقل الرئيسي" data-nav-system="enterprise-v1">
      <div class="navGroupTitle">Overview</div>
      <button class="navItem active" data-section="sec-overview"><span class="navIcon">⌂</span><span class="navLabel">مركز القيادة</span></button>

      <div class="navGroupTitle">Organizations</div>
      <button class="navItem" data-section="sec-tenants"><span class="navIcon">▦</span><span class="navLabel">الشركات</span></button>

      <div class="navGroupTitle">Users & Access</div>
      <button class="navItem" data-section="sec-users"><span class="navIcon">♙</span><span class="navLabel">المستخدمون</span></button>
      <button class="navItem" id="platformAdminsNav" data-section="sec-platform-admins" data-owner-only hidden style="display:none"><span class="navIcon">♛</span><span class="navLabel">مسؤولو المنصة</span></button>

      <div class="navGroupTitle">Plans & Commercial</div>
      <button class="navItem" id="plansManagementNav" data-owner-only hidden style="display:none"><span class="navIcon">◫</span><span class="navLabel">الباقات والحدود</span></button>

      <div class="navGroupTitle">Operations</div>
      <button class="navItem" data-section="sec-widgets"><span class="navIcon">⚡</span><span class="navLabel">الإجراءات والتحليلات</span></button>
      <button class="navItem" data-section="sec-activity"><span class="navIcon">↻</span><span class="navLabel">آخر الأنشطة</span></button>
      <button class="navItem" data-section="sec-audit"><span class="navIcon">◷</span><span class="navLabel">سجل التدقيق</span></button>

      <div class="navGroupTitle">Integrations</div>
      <button class="navItem" id="githubSyncNav" data-section="sec-github" data-owner-only hidden style="display:none"><span class="navIcon">⌘</span><span class="navLabel">GitHub Sync</span></button>
      <button class="navItem" id="evolutionApiNav" data-section="sec-evolution-api" data-owner-only hidden style="display:none"><span class="navIcon">◉</span><span class="navLabel">Evolution API</span></button>
      <button class="navItem" id="taraIntegrationsNav" data-owner-only hidden style="display:none"><span class="navIcon">✦</span><span class="navLabel">Tara APIs</span></button>

      <div class="navGroupTitle">Platform Administration</div>
      <button class="navItem" id="openSettingsBtnSide"><span class="navIcon">⚙</span><span class="navLabel">إعدادات النظام</span></button>
    </nav>'''
text = text[:match.start()] + new_nav + text[match.end():]

# Add a compact/collapse control in the existing brand without changing routes/auth.
brand_old = '<div class="sidebarBrand"><div class="logoMark">T</div><div><strong>TCRM</strong><span>Platform Admin</span></div></div>'
brand_new = '<div class="sidebarBrand"><div class="logoMark">T</div><div class="sidebarBrandCopy"><strong>TCRM</strong><span>Platform Admin</span></div><button type="button" id="sidebarCollapseBtn" class="sidebarCollapseBtn" aria-label="طي القائمة" aria-pressed="false">‹</button></div>'
if brand_old not in text:
    sys.exit('ERROR: sidebar brand signature not found; aborting without write.')
text = text.replace(brand_old, brand_new, 1)

css = r'''

    /* SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1 */
    #appShell{
      --sa-navy:#102744;
      --sa-navy-2:#17365d;
      --sa-gold:#c49a4a;
      --sa-gold-soft:#f7f1e6;
      --sa-canvas:#f6f8fb;
      --sa-surface:#ffffff;
      --sa-surface-soft:#f9fbfd;
      --sa-text:#18283e;
      --sa-muted:#718096;
      --sa-border:#e3e9f1;
      --sa-danger:#b84b5b;
      --sa-success:#1d8067;
      --sa-radius-sm:10px;
      --sa-radius-md:14px;
      --sa-radius-lg:18px;
      --sa-radius-xl:22px;
      --sa-shadow:0 10px 28px rgba(16,39,68,.07);
      --sidebar-w:244px;
      background:var(--sa-canvas)!important;
      color:var(--sa-text);
      font-family:Inter,"Segoe UI",Tahoma,Arial,sans-serif;
    }
    #appShell .sidebar{
      width:var(--sidebar-w)!important;
      padding:14px 12px!important;
      gap:10px!important;
      background:var(--sa-navy)!important;
      border-inline-end:1px solid rgba(255,255,255,.08);
      box-shadow:none!important;
      transition:width .2s ease,padding .2s ease;
    }
    #appShell .sidebarBrand{
      position:relative;display:grid!important;grid-template-columns:38px minmax(0,1fr) 28px;
      align-items:center;gap:10px;padding:6px 5px 15px!important;margin-bottom:2px;
      border-bottom:1px solid rgba(255,255,255,.10);
    }
    #appShell .sidebarBrand .logoMark{width:38px!important;height:38px!important;border-radius:12px!important;background:rgba(196,154,74,.14)!important;border:1px solid rgba(196,154,74,.44)!important;color:#e1bd74!important;box-shadow:none!important}
    #appShell .sidebarBrand strong{font-size:15px!important;letter-spacing:.08em;color:#fff}
    #appShell .sidebarBrand span{font-size:9px!important;color:#9fb1c8!important;letter-spacing:.04em}
    #appShell .sidebarCollapseBtn{width:28px;height:28px;border-radius:9px;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.05);color:#d7e0ec;cursor:pointer;font-size:18px;line-height:1;display:grid;place-items:center}
    #appShell .sidebarCollapseBtn:hover{background:rgba(255,255,255,.10);color:#fff}
    #appShell .sidebarNav{padding:2px 0 10px!important;gap:2px!important}
    #appShell .navGroupTitle{margin:13px 10px 5px!important;font-size:9px!important;line-height:1.2!important;letter-spacing:.11em!important;text-transform:uppercase;color:#728aa7!important;font-weight:800!important}
    #appShell .navItem{min-height:40px!important;padding:7px 9px!important;border-radius:11px!important;gap:9px!important;font-size:12px!important;font-weight:650!important;color:#c5d1df!important;border:1px solid transparent!important;background:transparent!important;box-shadow:none!important;transform:none!important}
    #appShell .navItem:hover{background:rgba(255,255,255,.055)!important;color:#fff!important;border-color:rgba(255,255,255,.06)!important;transform:none!important}
    #appShell .navItem.active{background:rgba(196,154,74,.13)!important;color:#fff!important;border-color:rgba(196,154,74,.25)!important;box-shadow:inset 3px 0 0 var(--sa-gold)!important}
    #appShell .navIcon{width:27px!important;height:27px!important;border-radius:8px!important;background:rgba(255,255,255,.055)!important;color:#9fb2c9!important;border:0!important;font-size:12px!important}
    #appShell .navItem.active .navIcon{background:rgba(196,154,74,.16)!important;color:#e3c27f!important}
    #appShell .sidebarFooter{border-top:1px solid rgba(255,255,255,.08);background:var(--sa-navy)!important;padding-top:10px!important}
    #appShell .sidebarUser{border:1px solid rgba(255,255,255,.08)!important;background:rgba(255,255,255,.04)!important;border-radius:12px!important;box-shadow:none!important;color:#dce5ef!important}

    #appShell .mainArea{background:var(--sa-canvas)!important}
    #appShell.platformPageMode .topbar{
      min-height:70px!important;padding:9px 20px!important;background:rgba(255,255,255,.96)!important;
      border-bottom:1px solid var(--sa-border)!important;box-shadow:none!important;backdrop-filter:blur(10px);
    }
    #appShell .pageIdentity strong{font-size:18px!important;color:var(--sa-text)!important;letter-spacing:-.02em}
    #appShell .pageIdentity small{font-size:10.5px!important;color:var(--sa-muted)!important}
    #appShell .titleShield{background:var(--sa-navy)!important;color:#fff!important;border:0!important;border-radius:10px!important;box-shadow:none!important}
    #appShell .topbarSearch{border:1px solid var(--sa-border)!important;background:var(--sa-surface-soft)!important;border-radius:12px!important;box-shadow:none!important}
    #appShell .topbarSearch:focus-within{border-color:rgba(196,154,74,.7)!important;box-shadow:0 0 0 3px rgba(196,154,74,.11)!important;background:#fff!important}
    #appShell .topbarSearch input{background:transparent!important;border:0!important;box-shadow:none!important}
    #appShell .topbarActions .btn,#appShell .topbarActions .iconBtn{min-height:38px!important;border-radius:10px!important;border-color:var(--sa-border)!important;background:#fff!important;color:#42546a!important;box-shadow:none!important}
    #appShell .topbarActions .btn.primary{background:var(--sa-navy)!important;color:#fff!important;border-color:var(--sa-navy)!important}
    #appShell .topbarActions .btn.danger{color:var(--sa-danger)!important;background:#fff!important}

    #appShell.platformPageMode .mainContent{max-width:1540px!important;padding:22px 24px 40px!important;gap:16px!important}
    #appShell .panel,#appShell .card,#appShell .commandHero,#appShell .kpiCard{border:1px solid var(--sa-border)!important;background:var(--sa-surface)!important;border-radius:var(--sa-radius-lg)!important;box-shadow:var(--sa-shadow)!important}
    #appShell .panelHead{border-bottom-color:var(--sa-border)!important}
    #appShell .panelHead h2,#appShell .panelHead h3{color:var(--sa-text)!important;letter-spacing:-.02em}
    #appShell .muted,#appShell .panelHead p{color:var(--sa-muted)!important}
    #appShell input,#appShell select,#appShell textarea{border:1px solid var(--sa-border)!important;background:#fff!important;border-radius:10px!important;color:var(--sa-text)!important;box-shadow:none!important}
    #appShell input:focus,#appShell select:focus,#appShell textarea:focus{border-color:rgba(196,154,74,.78)!important;box-shadow:0 0 0 3px rgba(196,154,74,.10)!important}
    #appShell .btn{border-radius:10px!important;box-shadow:none!important;transform:none!important}
    #appShell .btn:hover{transform:none!important}
    #appShell .btn.primary{background:var(--sa-navy)!important;border-color:var(--sa-navy)!important;box-shadow:none!important}
    #appShell .tableWrap{border:1px solid var(--sa-border)!important;border-radius:14px!important;background:#fff!important;box-shadow:none!important}
    #appShell th{background:#f6f8fb!important;color:#64758a!important;border-bottom:1px solid var(--sa-border)!important;font-size:10px!important;letter-spacing:.045em!important}
    #appShell td{color:#33465d!important;border-bottom-color:#edf1f5!important}
    #appShell tbody tr:hover{background:#fafbfd!important}
    #appShell .badge{padding:5px 8px!important;border-radius:999px!important;box-shadow:none!important}
    #appShell .empty{border:1px dashed #d9e0e9!important;background:#fafbfd!important;color:#77869a!important;border-radius:12px!important}
    #appShell :focus-visible{outline:2px solid var(--sa-gold)!important;outline-offset:2px!important}

    #appShell.sidebarCollapsed{--sidebar-w:76px}
    #appShell.sidebarCollapsed .sidebar{padding-inline:10px!important}
    #appShell.sidebarCollapsed .sidebarBrand{grid-template-columns:1fr;justify-items:center;padding-inline:0!important}
    #appShell.sidebarCollapsed .sidebarBrandCopy,#appShell.sidebarCollapsed .navLabel,#appShell.sidebarCollapsed .navGroupTitle,#appShell.sidebarCollapsed .sidebarUser{display:none!important}
    #appShell.sidebarCollapsed .sidebarCollapseBtn{position:absolute;right:-1px;bottom:-14px;background:var(--sa-navy)!important;transform:rotate(180deg)}
    #appShell.sidebarCollapsed .navItem{justify-content:center!important;padding-inline:6px!important}
    #appShell.sidebarCollapsed .navIcon{margin:0!important}
    #appShell.sidebarCollapsed .sidebarFooter #logoutBtnSide .navLabel{display:none!important}

    html[data-theme="dark"] #appShell{--sa-canvas:#0b1423;--sa-surface:#111e31;--sa-surface-soft:#15243a;--sa-text:#eef3fa;--sa-muted:#9baabd;--sa-border:#27384e;background:var(--sa-canvas)!important}
    html[data-theme="dark"] #appShell .mainArea{background:var(--sa-canvas)!important}
    html[data-theme="dark"] #appShell.platformPageMode .topbar{background:rgba(17,30,49,.96)!important;border-bottom-color:var(--sa-border)!important}
    html[data-theme="dark"] #appShell .panel,html[data-theme="dark"] #appShell .card,html[data-theme="dark"] #appShell .commandHero,html[data-theme="dark"] #appShell .kpiCard{background:var(--sa-surface)!important;border-color:var(--sa-border)!important}
    html[data-theme="dark"] #appShell input,html[data-theme="dark"] #appShell select,html[data-theme="dark"] #appShell textarea,html[data-theme="dark"] #appShell .topbarActions .btn,html[data-theme="dark"] #appShell .topbarActions .iconBtn{background:#14243a!important;border-color:var(--sa-border)!important;color:var(--sa-text)!important}
    html[data-theme="dark"] #appShell .tableWrap{background:#111e31!important;border-color:var(--sa-border)!important}
    html[data-theme="dark"] #appShell th{background:#15243a!important;color:#9fb0c5!important;border-bottom-color:var(--sa-border)!important}
    html[data-theme="dark"] #appShell td{color:#d8e1ed!important;border-bottom-color:#223248!important}
    html[data-theme="dark"] #appShell tbody tr:hover{background:#15243a!important}
    html[data-theme="dark"] #appShell .empty{background:#14243a!important;border-color:#334760!important;color:#9baabd!important}

    @media(max-width:980px){#appShell{--sidebar-w:220px}#appShell.platformPageMode .mainContent{padding:16px!important}.sidebarCollapseBtn{display:none!important}}
    @media(max-width:620px){#appShell.platformPageMode .mainContent{padding:12px!important}#appShell.platformPageMode .topbar{padding:9px 12px!important}}
    @media(prefers-reduced-motion:reduce){#appShell .sidebar{transition:none!important}}
    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1 */
'''

style_pos = text.rfind('</style>')
if style_pos < 0:
    sys.exit('ERROR: closing </style> not found; aborting without write.')
text = text[:style_pos] + css + text[style_pos:]

js = r'''
<script id="superAdminPhase1EnterpriseShellV1">
(function(){
  var shell=document.getElementById('appShell');
  var btn=document.getElementById('sidebarCollapseBtn');
  if(!shell||!btn)return;
  var key='tcrmmt-superadmin-sidebar-collapsed';
  try{if(localStorage.getItem(key)==='1'){shell.classList.add('sidebarCollapsed');btn.setAttribute('aria-pressed','true');}}catch(e){}
  btn.addEventListener('click',function(){
    var collapsed=shell.classList.toggle('sidebarCollapsed');
    btn.setAttribute('aria-pressed',collapsed?'true':'false');
    btn.setAttribute('aria-label',collapsed?'توسيع القائمة':'طي القائمة');
    try{localStorage.setItem(key,collapsed?'1':'0')}catch(e){}
  });
})();
</script>
'''
body_pos = text.rfind('</body>')
if body_pos < 0:
    sys.exit('ERROR: closing </body> not found; aborting without write.')
text = text[:body_pos] + js + text[body_pos:]

text = text.replace('data-ui-revision="1.1.0"', 'data-ui-revision="1.2.0"', 1)
TARGET.write_text(text, encoding='utf-8')
print(f'Applied Phase 1 patch to {TARGET}')
print(f'Backup: {backup}')
