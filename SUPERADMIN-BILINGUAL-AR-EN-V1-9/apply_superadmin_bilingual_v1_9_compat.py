#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
import tempfile

ORIGINAL = Path(__file__).with_name("apply_superadmin_bilingual_v1_9.py")
OLD = 'MAP_ANCHOR="  const enToAr=new Map(pairs),arToEn=new Map(pairs.map((p)=>[p[1],p[0]]));"'
NEW = 'MAP_ANCHOR="  const enToAr=new Map(pairs);\\n  const arToEn=new Map(pairs.map((p)=>[p[1],p[0]]));"'


def main():
    if not ORIGINAL.exists():
        raise SystemExit(f"Missing sibling patch: {ORIGINAL}")
    source = ORIGINAL.read_text(encoding="utf-8")
    count = source.count(OLD)
    if count != 1:
        raise SystemExit(f"V1.9 compatibility anchor count is {count}; refusing unknown patch source.")
    fixed = source.replace(OLD, NEW, 1)
    with tempfile.TemporaryDirectory(prefix="tcrmmt-v19-compat-") as tmp:
        patched = Path(tmp) / "apply_superadmin_bilingual_v1_9_compat_generated.py"
        patched.write_text(fixed, encoding="utf-8")
        result = subprocess.run([sys.executable, str(patched)], check=False)
        if result.returncode != 0:
            raise SystemExit(result.returncode)
    print("V1.9 compatibility runner completed successfully.")


if __name__ == "__main__":
    main()
