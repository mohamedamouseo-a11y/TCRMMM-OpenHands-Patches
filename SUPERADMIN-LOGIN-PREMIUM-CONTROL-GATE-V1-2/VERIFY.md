# Super Admin Login Premium Control Gate V1.2 — Verify

Scope: final visual-only micro-corrective pass on the Super Admin login.

Fixes only:
1. Remove clipped brand copy in the compact <=1100px brand header.
2. Keep `Forgot password?` visually integrated in dark mode.

## Apply

Target project: `/var/www/TCRMMT`

Run:

```bash
git status --short
python3 apply_login_premium_gate_v1_2.py
git diff --check
npm run check
npm run build
```

Restart only `tamiyouz-crm` if all checks pass.

## Prohibited

Do not change DB, API, Auth, Routes, Permissions, Business Logic, Login handlers, Password Recovery logic, or element IDs.
Do not Reset/Clean/Restore.
Do not Commit/Push.

## Visual acceptance

Use real Playwright viewport emulation.

### 1024x768 Light + Dark
- Compact navy brand header shows logo/TAMIYOUZ/TCRMMT cleanly.
- No clipped `Platform administration...` copy at the lower edge of the header.
- No text touches or crosses the navy/white boundary.
- Full login form and Sign In remain inside the first viewport.
- Page-level horizontal overflow = 0px.

### 390x844 Light + Dark
- Single login card surface remains unchanged and contained.
- Forgot password remains readable and does not become a white pill in dark mode.
- No clipping or overlap.
- Page-level horizontal overflow = 0px.

### Desktop regression
At 1440x900 preserve the existing full left branding panel and login composition.

### Functional spot checks
- Show/Hide password.
- Forgot Password opens recovery.
- Back to Sign In.
- Invalid login error remains visible.
- `#appShell` remains hidden while login is active.

## Required evidence

Send screenshots:
1. Light 1440x900
2. Light 1024x768
3. Dark 1024x768
4. Light 390x844
5. Dark 390x844

Also report `innerWidth`, `clientWidth`, `scrollWidth`, and page overflow for each viewport.
