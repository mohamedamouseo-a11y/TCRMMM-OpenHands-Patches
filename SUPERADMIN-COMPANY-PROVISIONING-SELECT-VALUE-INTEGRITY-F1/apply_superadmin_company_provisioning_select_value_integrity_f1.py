#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/_core/index.ts')
MARKER = 'SUPER_ADMIN_COMPANY_PROVISIONING_SELECT_VALUE_INTEGRITY_F1'

REPLACES = [
    (
        '<div class="field"><label>الخطة</label><select id="newPlan"><option>starter</option><option>pro</option><option>enterprise</option></select></div>',
        '<div class="field"><label>الخطة</label><select id="newPlan"><option value="starter">starter</option><option value="pro">pro</option><option value="enterprise">enterprise</option></select></div>',
        'newPlan static options',
    ),
    (
        '<div class="field"><label>الحالة</label><select id="newStatus"><option>trialing</option><option>active</option></select></div>',
        '<div class="field"><label>الحالة</label><select id="newStatus"><option value="trialing">trialing</option><option value="active">active</option></select></div>',
        'newStatus static options',
    ),
    (
        "  function planOptions(selected){ const all = plans.length ? plans.map(function(p){return p.slug;}) : ['starter','pro','enterprise']; return all.map(function(p){return '<option '+(p===selected?'selected':'')+'>'+esc(p)+'</option>';}).join(''); }\n  function statusOptions(selected){ const all=['trialing','active','past_due','expired','cancelled']; return all.map(function(s){return '<option '+(s===selected?'selected':'')+'>'+esc(s)+'</option>';}).join(''); }",
        "  // SUPER_ADMIN_COMPANY_PROVISIONING_SELECT_VALUE_INTEGRITY_F1\n  // Keep machine values canonical even when the bilingual UI translates visible option text.\n  function planOptions(selected){ const all = plans.length ? plans.map(function(p){return p.slug;}) : ['starter','pro','enterprise']; return all.map(function(p){return '<option value=\\\"'+esc(p)+'\\\" '+(p===selected?'selected':'')+'>'+esc(p)+'</option>';}).join(''); }\n  function statusOptions(selected){ const all=['trialing','active','past_due','expired','cancelled']; return all.map(function(s){return '<option value=\\\"'+esc(s)+'\\\" '+(s===selected?'selected':'')+'>'+esc(s)+'</option>';}).join(''); }",
        'dynamic plan/status option builders',
    ),
]


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin company provisioning select-value integrity F1 already applied; no changes made.')
        return

    for old, _new, label in REPLACES:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f'{label} anchor count is {count}; expected 1.')

    for old, new, _label in REPLACES:
        text = text.replace(old, new, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin company provisioning select-value integrity F1.')


if __name__ == '__main__':
    main()
