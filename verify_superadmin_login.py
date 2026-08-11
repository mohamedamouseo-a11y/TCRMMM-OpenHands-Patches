#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys

ROOT=Path('/var/www/TCRMMT')
INDEX=ROOT/'server/_core/index.ts'
LOGO=ROOT/'client/public/tamiyouz-superadmin-logo.png'

checks=[]
def check(name, ok):
    checks.append((name,bool(ok)))
    print(f'{name}=' + ('PASS' if ok else 'FAIL'))

text=INDEX.read_text(encoding='utf-8') if INDEX.exists() else ''
check('INDEX_EXISTS', INDEX.exists())
check('MARKER', 'TAMIYOUZ_SUPER_ADMIN_LOGIN_LIGHT_V1' in text)
check('LOGIN_EMAIL', 'id="loginEmail"' in text)
check('LOGIN_PASSWORD', 'id="loginPassword"' in text)
check('LOGIN_BUTTON', 'id="loginBtn"' in text)
check('LOGIN_API_PREFIX', "/api/super-admin" in text)
check('LOGIN_FUNCTION', "api('/login'" in text or 'api("/login"' in text)
check('LOGO_REFERENCE', '/tamiyouz-superadmin-logo.png' in text)
check('LOGO_EXISTS', LOGO.exists() and LOGO.stat().st_size > 0)
check('NO_AUTH_REPLACEMENT_MARKER', 'TAMIYOUZ_AUTH_REWRITE' not in text)

p=subprocess.run(['git','diff','--check'],cwd=ROOT,text=True,capture_output=True)
check('GIT_DIFF_CHECK',p.returncode==0)
if p.stdout.strip(): print(p.stdout.strip())
if p.stderr.strip(): print(p.stderr.strip())

failed=[name for name,ok in checks if not ok]
if failed:
    print('FIRST_ERROR='+failed[0])
    print('VERIFY=FAIL')
    sys.exit(1)
print('FIRST_ERROR=NONE')
print('VERIFY=PASS')
