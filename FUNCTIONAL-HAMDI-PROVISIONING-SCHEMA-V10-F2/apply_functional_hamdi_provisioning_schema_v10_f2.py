#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

OLD = "export const TENANT_SCHEMA_CURRENT_VERSION = 9;"
NEW = "export const TENANT_SCHEMA_CURRENT_VERSION = 10;"
TARGET = Path("scripts/provisioning-schema-contract.mjs")

APPLIED = "Applied F2 tenant provisioning schema contract v10 fix."
NOOP = "F2 tenant provisioning schema contract v10 fix already applied; no changes made."


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply the TCRMMT F2 tenant provisioning schema contract v10 fix."
    )
    parser.add_argument(
        "project_root",
        nargs="?",
        default=".",
        help="TCRMMT project root (default: current directory)",
    )
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    target = root / TARGET

    if not target.is_file():
        raise SystemExit(f"STOP: target file not found: {target}")

    text = target.read_text(encoding="utf-8")
    old_count = text.count(OLD)
    new_count = text.count(NEW)

    if old_count == 0 and new_count == 1:
        print(NOOP)
        return 0

    if old_count == 1 and new_count == 0:
        target.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")
        print(APPLIED)
        return 0

    raise SystemExit(
        "STOP: provisioning schema contract precondition failed "
        f"(old_count={old_count}, new_count={new_count}). "
        "Expected exactly one old v9 line and no v10 line, or exactly one v10 line and no v9 line."
    )


if __name__ == "__main__":
    raise SystemExit(main())
