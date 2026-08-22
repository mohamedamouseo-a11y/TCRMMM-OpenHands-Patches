#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_PHASE5_OPERATIONS_INTEGRATIONS_V1'

CSS = r'''
    /* SUPER_ADMIN_PHASE5_OPERATIONS_INTEGRATIONS_V1 */
    #appShell.platformPageMode .opsV5Card{
      border:1px solid #dce4ed!important;
      border-radius:14px!important;
      background:#fff!important;
      padding:14px!important;
      box-shadow:0 4px 14px rgba(22,32,51,.03)!important;
    }
    #appShell.platformPageMode .opsV5Grid{
      display:grid!important;
      grid-template-columns:repeat(2,minmax(0,1fr))!important;
      gap:10px!important;
    }
    #appShell.platformPageMode .opsV5Header{
      display:flex;justify-content:space-between;align-items:center;
      margin-bottom:10px;padding-bottom:9px;border-bottom:1px solid #dce4ed;
    }
    #appShell.platformPageMode .opsV5Title{font-size:16px;font-weight:800;color:#172033}
    #appShell.platformPageMode .opsV5Meta{font-size:10px;color:#68768a}
    #appShell.platformPageMode .opsV5Table{
      overflow:auto!important;border:1px solid #edf1f5!important;border-radius:10px!important;
    }
    #appShell.platformPageMode .opsV5Table table{min-width:760px!important;width:100%!important}
    #appShell.platformPageMode .opsV5Table th{
      background:#f7f9fc!important;font-size:9px!important;position:sticky;top:0;
    }
    #appShell.platformPageMode .opsV5Table td{
      font-size:10px!important;padding:9px!important;
    }
    @media(max-width:900px){
      #appShell.platformPageMode .opsV5Grid{grid-template-columns:1fr!important}
    }
    /* END SUPER_ADMIN_PHASE5_OPERATIONS_INTEGRATIONS_V1 */
'''

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        return
    anchor = '/* END SUPER_ADMIN_PHASE4'
    text = text.replace(anchor, CSS + '\n' + anchor, 1)
    TARGET.write_text(text, encoding='utf-8')

if __name__ == '__main__':
    main()
