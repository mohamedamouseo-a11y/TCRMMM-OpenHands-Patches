# TCRMMT — Super Admin Bilingual AR/EN V1.5 Verification

## Purpose
V1.5 is a final-gate post-render localization sweep built from the confirmed V1.4 live audit findings. It does not change DB, APIs, auth, routes, permissions, billing/subscription/business logic, or navigation handlers.

## Patch
- Target: `/var/www/TCRMMT/server/superAdminUiPolish.ts`
- Marker: `SUPER_ADMIN_BILINGUAL_AR_EN_V1_5`
- Requires markers V1 through V1.4.
- Apply once only.

## Technical validation
Run in `/var/www/TCRMMT`:

```bash
git status --short
python3 /tmp/apply_superadmin_bilingual_v1_5.py
git diff --check
npm run check
npm run build
```

If all pass, restart only:

```bash
pm2 restart tamiyouz-crm
```

Do not commit or push.

## Why V1.5 is different
Previous passes used the source-aware translation pipeline. V1.4 evidence showed late-rendered dynamic labels and attributes could still reappear in the wrong language. V1.5 adds a post-render sweep after the existing pipeline and reuses all prior dictionaries against the actual rendered DOM, then applies explicit critical overrides.

## Required QA
Use real Playwright browser contexts. Test both languages and persistence.

### English gate
Scan visible text nodes plus `placeholder`, `title`, `aria-label` on:
- Login / recovery
- Overview
- Companies
- Tenant Details
- Users
- Platform Admins
- Activity
- Audit Log
- GitHub Sync
- Evolution API
- Tara APIs
- Plans Catalog / Editor / Company Overrides
- Commercial / Billing / Subscriptions
- Settings / Source Code

Any ordinary Arabic static UI is FAIL. Exclude only real data or technical identifiers: company/user names, emails, IDs, URLs, slugs, tokens, repository/branch/commit values, product names, plan IDs, raw technical identifiers.

### Arabic gate
Scan the same surfaces. Any ordinary English static UI is FAIL, with the same technical/data exclusions.

Pay special attention to:
- Arabic Login brand copy
- `ATTENTION`
- Plans: `Back to Command Center`, `Refresh Data`, `View details`
- Commercial: mixed enforcement heading, `Kill Switch`, `Canary %`, `Grace Days`, `Feature Overrides JSON`, `Limit Overrides JSON`
- language toggle title/aria-label

### Dynamic re-render test
For English, visit and wait for network/data rendering on:
- Overview
- GitHub Sync
- Evolution API
- Plans Catalog
- Commercial
Then wait 2 seconds after the final DOM mutation and scan again. The final scan, not the initial scan, determines PASS.

### Navigation
From Overview:
- `#githubSyncNav` must activate `#sec-github`
- `#evolutionApiNav` must activate `#sec-evolution-api`
Test Evolution at 1440 and 768.

### Responsive
Both languages:
- 1440×900
- 1024×768
- 768×900
- 390×844

Required:
- EN: `lang=en`, `dir=ltr`
- AR: `lang=ar`, `dir=rtl`
- page horizontal overflow = 0px
- no clipping / overlap
- language survives refresh

## Evidence screenshots
At minimum:
1. login-en-1440.png
2. login-ar-1440.png
3. overview-en-1440.png
4. overview-ar-1440.png
5. companies-en-1024.png
6. users-en-1024.png
7. tenant-details-en-1024.png
8. activity-en-1440.png
9. audit-en-1440.png
10. settings-en-390.png
11. settings-ar-390.png
12. github-sync-en-1440.png
13. evolution-api-en-1440.png
14. plans-catalog-en-1440.png
15. plans-catalog-ar-1440.png
16. commercial-en-1440.png
17. commercial-ar-1440.png

## Final report gate
The report must include exactly this heading:

`UNTRANSLATED STATIC UI`

Final acceptance is allowed only when the result under it is:

`NONE FOUND`

If even one legitimate untranslated static UI item remains, do not fix it manually. Record language, surface, exact text, selector/attribute, screenshot, and stop.
