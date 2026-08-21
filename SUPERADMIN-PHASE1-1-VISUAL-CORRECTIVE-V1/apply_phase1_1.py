#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
START = '/* SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */'
END = '/* END SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */'
ANCHOR = '    /* END SUPER_ADMIN_PHASE1_ENTERPRISE_SHELL_V1_ADAPTED */'

css = r'''
    /* SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */
    /* Visual-only corrective layer: compact shell, wider content, cleaner topbar, better RTL balance. */
    #appShell.platformPageMode{
      --sidebar-w:216px!important;
      grid-template-columns:var(--sidebar-w) minmax(0,1fr)!important;
      column-gap:0!important;
      background:#f5f7fb!important;
    }
    #appShell.platformPageMode .sidebar{
      width:var(--sidebar-w)!important;
      margin:10px 10px 10px 0!important;
      height:calc(100dvh - 20px)!important;
      max-height:calc(100dvh - 20px)!important;
      border-radius:18px!important;
      padding:12px 10px!important;
      box-shadow:0 12px 34px rgba(15,35,66,.12)!important;
    }
    #appShell.platformPageMode .sidebarBrand{
      min-height:58px!important;
      padding:9px 10px!important;
      border-radius:14px!important;
    }
    #appShell.platformPageMode .sidebarBrand .logoMark{width:36px!important;height:36px!important;border-radius:11px!important}
    #appShell.platformPageMode .sidebarBrand strong{font-size:14px!important;letter-spacing:0!important}
    #appShell.platformPageMode .sidebarBrand span{font-size:9px!important}
    #appShell.platformPageMode .sidebarBrand:after{display:none!important}
    #appShell.platformPageMode .sidebarNav{padding-inline:2px!important}
    #appShell.platformPageMode .navGroupTitle{margin:10px 8px 4px!important;font-size:9px!important;letter-spacing:.08em!important}
    #appShell.platformPageMode .navItem{min-height:38px!important;padding:7px 9px!important;border-radius:11px!important;font-size:11.5px!important;gap:8px!important}
    #appShell.platformPageMode .navIcon{width:26px!important;height:26px!important;border-radius:9px!important;font-size:12px!important}
    #appShell.platformPageMode .sidebarFooter{padding-top:8px!important}
    #appShell.platformPageMode .sidebarUser{padding:9px 10px!important;border-radius:13px!important;font-size:10.5px!important}

    #appShell.platformPageMode .mainArea{min-width:0!important;width:100%!important}
    #appShell.platformPageMode .topbar{
      min-height:68px!important;
      margin:10px 12px 0!important;
      padding:8px 12px!important;
      border-radius:16px!important;
      grid-template-columns:minmax(220px,.9fr) minmax(260px,1.15fr) auto!important;
      column-gap:10px!important;
      box-shadow:0 8px 24px rgba(24,48,83,.07)!important;
    }
    #appShell.platformPageMode .pageIdentity strong{font-size:17px!important}
    #appShell.platformPageMode .pageIdentity small{font-size:9.5px!important;line-height:1.35!important}
    #appShell.platformPageMode .titleShield{min-width:34px!important;height:30px!important;border-radius:10px!important;font-size:9px!important}
    #appShell.platformPageMode .topbarSearch{min-width:0!important}
    #appShell.platformPageMode .topbarSearch input{min-height:38px!important;height:38px!important;font-size:11px!important}
    #appShell.platformPageMode .topbarActions{gap:5px!important}
    #appShell.platformPageMode .topbarActions .btn,
    #appShell.platformPageMode .topbarActions .iconBtn{min-height:36px!important;height:36px!important;padding:7px 9px!important;border-radius:10px!important;font-size:11px!important}
    #appShell.platformPageMode .lastRefreshLabel{padding-inline-end:0!important;font-size:8px!important}

    #appShell.platformPageMode .mainContent{
      width:100%!important;
      max-width:none!important;
      margin:0!important;
      padding:16px 16px 34px!important;
      gap:14px!important;
      overflow:visible!important;
    }
    #appShell.platformPageMode .mainContent>section.platformPageActive{max-width:none!important;width:100%!important}
    #appShell.platformPageMode .panel,
    #appShell.platformPageMode .card{border-radius:16px!important;box-shadow:0 4px 16px rgba(28,52,88,.045)!important}
    #appShell.platformPageMode .panelHead{margin-bottom:12px!important;padding-bottom:11px!important}
    #appShell.platformPageMode .panelHead h2{font-size:18px!important}
    #appShell.platformPageMode .panelHead p{font-size:10px!important}

    #appShell.platformPageMode #sec-github{padding:14px!important}
    #appShell.platformPageMode #sec-github .githubV5Workspace{grid-template-columns:minmax(0,1.55fr) minmax(300px,.85fr)!important;gap:12px!important}
    #appShell.platformPageMode #sec-github .githubStatusGrid{grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:8px!important}
    #appShell.platformPageMode #sec-github .githubMetric{min-height:82px!important;padding:11px 12px!important;border-radius:13px!important}
    #appShell.platformPageMode #sec-github .githubCard{border-radius:14px!important;padding:14px!important}
    #appShell.platformPageMode #sec-github .githubV5Quickbar{gap:8px!important;margin-bottom:10px!important}

    #appShell.platformPageMode.sidebarCollapsed{--sidebar-w:72px!important}
    #appShell.platformPageMode.sidebarCollapsed .sidebar{padding-inline:8px!important}
    #appShell.platformPageMode.sidebarCollapsed .sidebarBrand{padding:8px!important;justify-content:center!important}
    #appShell.platformPageMode.sidebarCollapsed .sidebarBrand>div:not(.logoMark),
    #appShell.platformPageMode.sidebarCollapsed .navGroupTitle,
    #appShell.platformPageMode.sidebarCollapsed .navItem{font-size:0!important;justify-content:center!important}
    #appShell.platformPageMode.sidebarCollapsed .navItem{padding-inline:6px!important}
    #appShell.platformPageMode.sidebarCollapsed .navIcon{margin:0!important}

    @media(max-width:1180px){
      #appShell.platformPageMode{--sidebar-w:198px!important}
      #appShell.platformPageMode .topbar{grid-template-columns:minmax(200px,1fr) minmax(220px,.9fr) auto!important}
      #appShell.platformPageMode #sec-github .githubV5Workspace{grid-template-columns:1fr!important}
    }
    @media(max-width:980px){
      #appShell.platformPageMode{display:block!important}
      #appShell.platformPageMode .sidebar{margin:0!important;height:100dvh!important;max-height:100dvh!important;border-radius:0!important}
      #appShell.platformPageMode .topbar{margin:0!important;border-radius:0!important;grid-template-columns:minmax(0,1fr) auto!important;grid-template-areas:'identity actions' 'search search' 'refresh refresh'!important}
      #appShell.platformPageMode .mainContent{padding:14px 12px 28px!important}
    }
    @media(max-width:620px){
      #appShell.platformPageMode .topbar{padding:8px 10px!important}
      #appShell.platformPageMode .topbarActions .btnLabel{display:none!important}
      #appShell.platformPageMode .mainContent{padding:10px 8px 22px!important}
      #appShell.platformPageMode #sec-github .githubStatusGrid{grid-template-columns:repeat(2,minmax(0,1fr))!important}
    }
    /* END SUPER_ADMIN_PHASE1_1_VISUAL_CORRECTIVE_V1 */
'''.strip('\n')

if not TARGET.exists():
    raise SystemExit(f'Missing target: {TARGET}')
text = TARGET.read_text()
if START in text:
    print('Phase 1.1 already applied; no changes made.')
    raise SystemExit(0)
if ANCHOR not in text:
    raise SystemExit('Expected Phase 1 anchor not found; stop and adapt manually.')
text = text.replace(ANCHOR, css + '\n' + ANCHOR, 1)
TARGET.write_text(text)
print('Applied Phase 1.1 visual corrective to server/_core/index.ts')
