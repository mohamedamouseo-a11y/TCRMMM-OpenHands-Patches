#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-/var/www/TCRMMT}"
OUT="$ROOT/client/public/tamiyouz-superadmin-logo.png"
mkdir -p "$(dirname "$OUT")"

# Prefer an existing approved local Tamiyouz logo if production already has one.
for local_candidate in \
  "$ROOT/client/public/logo.png" \
  "$ROOT/client/public/tamiyouz-logo.png" \
  "$ROOT/client/public/tamiyouz.png"
do
  if [ -s "$local_candidate" ]; then
    cp "$local_candidate" "$OUT"
    echo "LOGO_SOURCE=$local_candidate"
    echo "LOGO_FETCH=PASS"
    exit 0
  fi
done

# TCRM Main is public; try the canonical public asset locations without credentials.
urls=(
  "https://raw.githubusercontent.com/mohamedamouseo-a11y/TCRM-MAIN-Tamiyouz-CRM-/main/client/public/logo.png"
  "https://raw.githubusercontent.com/mohamedamouseo-a11y/TCRM-MAIN-Tamiyouz-CRM-/master/client/public/logo.png"
)
for url in "${urls[@]}"; do
  tmp="$(mktemp)"
  if curl -fL --connect-timeout 10 --max-time 30 "$url" -o "$tmp" 2>/dev/null && [ -s "$tmp" ]; then
    if file "$tmp" | grep -qiE 'PNG image|JPEG image|Web/P image'; then
      mv "$tmp" "$OUT"
      echo "LOGO_SOURCE=$url"
      echo "LOGO_FETCH=PASS"
      exit 0
    fi
  fi
  rm -f "$tmp"
done

echo "LOGO_FETCH=FAIL"
echo "FIRST_ERROR=approved_tamiyouz_logo_not_found"
exit 1
