#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path('/var/www/TCRMMT')
TARGET = ROOT / 'scripts/provisioning-schema-contract.mjs'
MANIFEST = ROOT / 'scripts/tenant-schema-manifest.json'

MARKER = 'TCRMMT_TENANT_SCHEMA_CONTRACT_V10_TABLECOUNT_199_F2'

OLD_VERSION = 'export const TENANT_SCHEMA_CURRENT_VERSION = 9;'
NEW_VERSION = """// TCRMMT_TENANT_SCHEMA_CONTRACT_V10_TABLECOUNT_199_F2
export const TENANT_SCHEMA_CURRENT_VERSION = 10;"""

OLD_TABLE_COUNT = 'export const TENANT_SCHEMA_FINAL_REQUIRED_TABLES = 198;'
NEW_TABLE_COUNT = 'export const TENANT_SCHEMA_FINAL_REQUIRED_TABLES = 199;'


def assert_manifest_contract():
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    checks = {
        'schemaVersion': 10,
        'minimumCompatibleSchemaVersion': 10,
        'requiredTableCount': 199,
    }
    for key, expected in checks.items():
        actual = manifest.get(key)
        if actual != expected:
            raise SystemExit(
                f'manifest {key} is {actual!r}; expected {expected!r}. STOP.'
            )


def main():
    assert_manifest_contract()
    text = TARGET.read_text(encoding='utf-8')

    if MARKER in text:
        required = [
            'export const TENANT_SCHEMA_CURRENT_VERSION = 10;',
            'export const TENANT_SCHEMA_FINAL_REQUIRED_TABLES = 199;',
        ]
        missing = [value for value in required if value not in text]
        if missing:
            raise SystemExit(
                'F2 marker exists but expected contract values are missing; STOP.'
            )
        print('TCRMMT tenant schema contract V10/table-count 199 F2 already applied; no changes made.')
        return

    anchors = [
        (OLD_VERSION, 'schema version 9'),
        (OLD_TABLE_COUNT, 'final required table count 198'),
    ]
    for old, label in anchors:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f'{label} anchor count is {count}; expected 1.')

    if 'export const TENANT_SCHEMA_CURRENT_VERSION = 10;' in text:
        raise SystemExit('schema contract already reports version 10 without F2 marker; STOP for review.')
    if 'export const TENANT_SCHEMA_FINAL_REQUIRED_TABLES = 199;' in text:
        raise SystemExit('schema contract already reports final table count 199 without F2 marker; STOP for review.')

    text = text.replace(OLD_VERSION, NEW_VERSION, 1)
    text = text.replace(OLD_TABLE_COUNT, NEW_TABLE_COUNT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied TCRMMT tenant schema contract V10/table-count 199 F2.')


if __name__ == '__main__':
    main()
