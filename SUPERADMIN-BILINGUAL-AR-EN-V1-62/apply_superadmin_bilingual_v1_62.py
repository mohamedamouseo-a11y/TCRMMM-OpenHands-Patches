#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_62_COMPANY_PROFILE_USERS_AR_LAYOUT_CLOSURE'
V161_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_61_COMMERCIAL_MONETIZATION_FORMS_HARD_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V161";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_62_COMPANY_PROFILE_USERS_AR_LAYOUT_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V162";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V161';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V162';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v161.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v162.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V161';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V162';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v161', '?v=superadmin-bilingual-v162', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v161"', 'data-sa-bilingual-runtime="v162"', 'runtime asset marker', 1),
]

GLOBAL_ANCHOR = """  root.dataset.saUiVersion=VERSION;
  const themeKey='tcrm-super-admin-theme';"""

GLOBAL_REPLACEMENT = r"""  root.dataset.saUiVersion=VERSION;

  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_62_COMPANY_PROFILE_USERS_AR_LAYOUT_CLOSURE
  // Scope: Company Profile drawer on /super-admin only. Canonicalizes ordinary UI
  // copy in both directions and repairs wrapping/isolation without changing company,
  // user, email, path, plan, date, health percentage or other runtime data values.
  const applyCompanyProfileV162=()=>{
    if(typeof location==='undefined' || (location.pathname!=='/super-admin' && location.pathname!=='/super-admin/'))return;
    const ar=String(root.getAttribute('lang')||'').toLowerCase().startsWith('ar') || root.getAttribute('dir')==='rtl';
    const norm=(value)=>String(value||'').replace(/\s+/g,' ').trim();
    const titleValues=new Set(['Company Profile','ملف الشركة']);
    const titleEl=Array.from(document.querySelectorAll('h1,h2,h3,h4,strong,b,span,div')).find((el)=>{
      const text=norm(el.textContent);
      if(!titleValues.has(text))return false;
      return el.children.length===0 || /^H[1-4]$/.test(el.tagName);
    });
    if(!(titleEl instanceof HTMLElement))return;

    let profile=null;
    let cursor=titleEl.parentElement;
    for(let depth=0;cursor && depth<10;depth+=1,cursor=cursor.parentElement){
      const text=norm(cursor.innerText);
      const hasTabs=text.includes('Billing & Payments') || text.includes('الفواتير والمدفوعات');
      const hasSignin=text.includes('Sign in as Company Admin') || text.includes('الدخول كمسؤول الشركة');
      if(hasTabs && hasSignin){profile=cursor;break;}
    }
    if(!(profile instanceof HTMLElement))return;

    if(profile.dataset.saCompanyProfileV162!=='1')profile.dataset.saCompanyProfileV162='1';
    if(profile.getAttribute('dir')!==(ar?'rtl':'ltr'))profile.setAttribute('dir',ar?'rtl':'ltr');
    profile.style.setProperty('text-align',ar?'right':'left','important');
    profile.style.setProperty('overflow-x','hidden','important');

    const pairs=[
      ['Company Profile','ملف الشركة'],
      ['Smart view of company, subscription, and billing data.','عرض شامل لبيانات الشركة والاشتراك والفواتير.'],
      ['Trialing','فترة تجريبية'],
      ['Sign in as Company Admin','الدخول كمسؤول الشركة'],
      ['Overview','نظرة عامة'],
      ['Users','المستخدمون'],
      ['Subscription','الاشتراك'],
      ['Billing & Payments','الفواتير والمدفوعات'],
      ['Company Log','سجل الشركة'],
      ['Company Accounts','حسابات الشركة'],
      ['Company accounts','حسابات الشركة'],
      ['Current passwords are not shown. You can only create a new password.','لا يتم عرض كلمات المرور الحالية. يمكنك إنشاء كلمة مرور جديدة فقط.'],
      ['Current passwords are not displayed. You can only create a new password.','لا يتم عرض كلمات المرور الحالية. يمكنك إنشاء كلمة مرور جديدة فقط.'],
      ['Refresh','تحديث'],
      ['Admin','مسؤول'],
      ['Active','نشط'],
      ['Last Login','آخر تسجيل دخول'],
      ['Save role','حفظ الدور'],
      ['Save Role','حفظ الدور'],
      ['New password','كلمة مرور جديدة'],
      ['New Password','كلمة مرور جديدة'],
      ['Suspend','إيقاف الحساب'],
      ['Close','إغلاق']
    ];
    const byEn=new Map();
    const byAr=new Map();
    for(const pair of pairs){byEn.set(pair[0],pair[1]);byAr.set(pair[1],pair[0]);}

    const walker=document.createTreeWalker(profile,NodeFilter.SHOW_TEXT);
    let node=walker.nextNode();
    while(node){
      const parent=node.parentElement;
      if(parent && !/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(parent.tagName)){
        const raw=node.nodeValue||'';
        const trimmed=norm(raw);
        let next=trimmed;
        if(trimmed){
          if(ar){
            if(byEn.has(trimmed))next=byEn.get(trimmed);
            else{
              next=next.replace(/\bHealth\s+(\d{1,3}%)\b/g,'صحة الحساب $1');
              next=next.replace(/\bLast Login\b/g,'آخر تسجيل دخول');
              next=next.replace(/آخر\s+Login/g,'آخر تسجيل دخول');
              if(/كلمات المرور الحالية/.test(next) && /(كلمة جديدة|كلمة مرور جديدة)/.test(next)){
                next='لا يتم عرض كلمات المرور الحالية. يمكنك إنشاء كلمة مرور جديدة فقط.';
              }
            }
          }else{
            if(byAr.has(trimmed))next=byAr.get(trimmed);
            else{
              next=next.replace(/صحة الحساب\s+(\d{1,3}%)/g,'Health $1');
              next=next.replace(/آخر تسجيل دخول/g,'Last Login');
              if(/كلمات المرور الحالية/.test(next) && /(كلمة جديدة|كلمة مرور جديدة)/.test(next)){
                next='Current passwords are not shown. You can only create a new password.';
              }
            }
          }
          if(next!==trimmed){
            const lead=(raw.match(/^\s*/)||[''])[0];
            const trail=(raw.match(/\s*$/)||[''])[0];
            node.nodeValue=lead+next+trail;
          }
        }
      }
      node=walker.nextNode();
    }

    profile.querySelectorAll('[placeholder],[title],[aria-label]').forEach((el)=>{
      ['placeholder','title','aria-label'].forEach((name)=>{
        if(!el.hasAttribute(name))return;
        const raw=norm(el.getAttribute(name));
        if(!raw)return;
        const next=ar?(byEn.get(raw)||raw):(byAr.get(raw)||raw);
        if(next!==raw)el.setAttribute(name,next);
      });
    });

    profile.querySelectorAll('*').forEach((el)=>{
      if(!(el instanceof HTMLElement))return;
      el.style.setProperty('min-width','0','important');
      el.style.setProperty('box-sizing','border-box','important');
      const display=getComputedStyle(el).display;
      const text=norm(el.innerText);
      const hasEmail=/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(text);
      const hasActions=/(New password|كلمة مرور جديدة|Suspend|إيقاف الحساب|Save role|Save Role|حفظ الدور)/.test(text);
      if(display==='flex' && (hasEmail || hasActions)){
        el.style.setProperty('flex-wrap','wrap','important');
        el.style.setProperty('row-gap','8px','important');
        el.style.setProperty('column-gap','8px','important');
        el.style.setProperty('align-items','center','important');
      }
      if(display==='grid' && (hasEmail || hasActions)){
        el.style.setProperty('grid-template-columns','minmax(0,1fr)','important');
        el.style.setProperty('gap','8px','important');
        el.style.setProperty('align-items','start','important');
      }
    });

    Array.from(profile.querySelectorAll('a,span,p,small,strong,b,div')).forEach((el)=>{
      if(!(el instanceof HTMLElement) || el.children.length>0)return;
      const text=norm(el.textContent);
      if(!/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(text))return;
      el.style.setProperty('direction','ltr','important');
      el.style.setProperty('unicode-bidi','isolate','important');
      el.style.setProperty('overflow-wrap','anywhere','important');
      el.style.setProperty('word-break','break-word','important');
      el.style.setProperty('max-width','100%','important');
    });

    const buttons=Array.from(profile.querySelectorAll('button'));
    buttons.forEach((button)=>{
      if(!(button instanceof HTMLElement))return;
      button.style.setProperty('white-space','nowrap','important');
      const text=norm(button.textContent);
      if(/^(Overview|نظرة عامة|Users|المستخدمون|Subscription|الاشتراك|Billing & Payments|الفواتير والمدفوعات|Company Log|سجل الشركة)$/.test(text)){
        const parent=button.parentElement;
        if(parent instanceof HTMLElement){
          parent.style.setProperty('display','flex','important');
          parent.style.setProperty('flex-wrap','wrap','important');
          parent.style.setProperty('gap','8px','important');
        }
      }
      if(/^(Save role|Save Role|حفظ الدور|New password|New Password|كلمة مرور جديدة|Suspend|إيقاف الحساب)$/.test(text)){
        const parent=button.parentElement;
        if(parent instanceof HTMLElement){
          parent.style.setProperty('display','flex','important');
          parent.style.setProperty('flex-wrap','wrap','important');
          parent.style.setProperty('gap','8px','important');
          parent.style.setProperty('align-items','center','important');
        }
      }
    });
  };

  let companyProfileV162Pending=false;
  const scheduleCompanyProfileV162=()=>{
    if(companyProfileV162Pending)return;
    companyProfileV162Pending=true;
    requestAnimationFrame(()=>{
      companyProfileV162Pending=false;
      applyCompanyProfileV162();
    });
  };
  const companyProfileV162Observer=new MutationObserver(scheduleCompanyProfileV162);
  companyProfileV162Observer.observe(root,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:['lang','dir']});
  scheduleCompanyProfileV162();

  const themeKey='tcrm-super-admin-theme';"""


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.62 Company Profile Users Arabic/layout closure already applied; no changes made.')
        return
    if V161_MARKER not in text:
        raise SystemExit('Bilingual V1.61 Commercial monetization forms hard closure marker not found; apply V1.61 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    anchor_count = text.count(GLOBAL_ANCHOR)
    if anchor_count != 1:
        raise SystemExit(f'global UI anchor count is {anchor_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(GLOBAL_ANCHOR, GLOBAL_REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.62 Company Profile Users Arabic/layout closure.')


if __name__ == '__main__':
    main()
