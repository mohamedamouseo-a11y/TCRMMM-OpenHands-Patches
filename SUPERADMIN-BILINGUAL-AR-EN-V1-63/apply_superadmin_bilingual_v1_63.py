#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')

MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_63_COMPANY_PROFILE_UX_REBUILD'
V162_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_62_COMPANY_PROFILE_USERS_AR_LAYOUT_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V162";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_63_COMPANY_PROFILE_UX_REBUILD\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V163";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V162';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V163';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v162.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v163.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V162';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V163';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v162', '?v=superadmin-bilingual-v163', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v162"', 'data-sa-bilingual-runtime="v163"', 'runtime asset marker', 1),
]

ANCHOR = """  scheduleCompanyProfileV162();

  const themeKey='tcrm-super-admin-theme';"""

REPLACEMENT = r"""  scheduleCompanyProfileV162();

  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_63_COMPANY_PROFILE_UX_REBUILD
  // Full Company Profile drawer rebuild. V1.63 keeps all runtime values and existing
  // actions intact, but reflows the drawer into stable sections, hard-isolates emails,
  // normalizes user cards/actions, and canonicalizes bilingual copy without cloning
  // or replacing interactive controls.
  const ensureCompanyProfileV163Style=()=>{
    if(document.querySelector('style[data-sa-company-profile-v163-style="1"]'))return;
    const style=document.createElement('style');
    style.setAttribute('data-sa-company-profile-v163-style','1');
    style.textContent=[
      '[data-sa-company-profile-v163="1"]{width:min(720px,calc(100vw - 28px))!important;max-width:720px!important;height:min(860px,calc(100vh - 24px))!important;max-height:calc(100vh - 24px)!important;padding:22px!important;overflow-y:auto!important;overflow-x:hidden!important;box-sizing:border-box!important;}',
      '[data-sa-company-profile-v163="1"] *{box-sizing:border-box!important;min-width:0;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-header{display:flex!important;align-items:flex-start!important;justify-content:space-between!important;gap:16px!important;padding-bottom:14px!important;margin-bottom:14px!important;border-bottom:1px solid rgba(148,163,184,.35)!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-header h1,[data-sa-company-profile-v163="1"] .sa-v163-header h2,[data-sa-company-profile-v163="1"] .sa-v163-header h3{margin:0 0 4px!important;line-height:1.35!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-hero{display:grid!important;grid-template-columns:minmax(0,1fr) auto!important;gap:18px!important;align-items:center!important;padding:18px!important;margin:0 0 18px!important;border:1px solid rgba(148,163,184,.28)!important;border-radius:18px!important;background:rgba(248,250,252,.76)!important;}',
      '[data-sa-company-profile-v163="1"][dir="rtl"] .sa-v163-hero{grid-template-columns:auto minmax(0,1fr)!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-hero *{max-width:100%!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-tabs{display:flex!important;flex-wrap:wrap!important;gap:9px!important;align-items:stretch!important;margin:0 0 20px!important;padding:0!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-tabs button{flex:1 1 112px!important;min-height:40px!important;padding:9px 12px!important;white-space:normal!important;line-height:1.35!important;text-align:center!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-users-section{display:block!important;padding-top:6px!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-users-section>*,[data-sa-company-profile-v163="1"] .sa-v163-user-card>*{max-width:100%!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-users-toolbar{display:flex!important;flex-wrap:wrap!important;align-items:center!important;justify-content:space-between!important;gap:10px!important;margin:12px 0 14px!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-user-card{display:grid!important;grid-template-columns:minmax(0,1fr)!important;gap:12px!important;padding:16px!important;margin:0 0 14px!important;border:1px solid rgba(148,163,184,.34)!important;border-radius:16px!important;background:#fff!important;box-shadow:0 5px 18px rgba(15,23,42,.04)!important;position:relative!important;inset:auto!important;transform:none!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-user-card div,[data-sa-company-profile-v163="1"] .sa-v163-user-card p,[data-sa-company-profile-v163="1"] .sa-v163-user-card span,[data-sa-company-profile-v163="1"] .sa-v163-user-card small,[data-sa-company-profile-v163="1"] .sa-v163-user-card label,[data-sa-company-profile-v163="1"] .sa-v163-user-card strong,[data-sa-company-profile-v163="1"] .sa-v163-user-card a{position:relative!important;inset:auto!important;transform:none!important;float:none!important;max-width:100%!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-user-card select,[data-sa-company-profile-v163="1"] .sa-v163-user-card input{width:100%!important;max-width:100%!important;min-height:42px!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-actions{display:flex!important;flex-wrap:wrap!important;gap:9px!important;align-items:center!important;margin-top:2px!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-actions button{flex:0 1 auto!important;min-height:40px!important;white-space:normal!important;line-height:1.25!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-email{display:block!important;width:100%!important;direction:ltr!important;unicode-bidi:isolate!important;text-align:left!important;overflow-wrap:anywhere!important;word-break:break-word!important;line-height:1.55!important;margin:3px 0!important;font-weight:650!important;}',
      '[data-sa-company-profile-v163="1"] .sa-v163-meta{display:flex!important;flex-wrap:wrap!important;gap:8px 12px!important;align-items:center!important;line-height:1.55!important;}',
      '[data-sa-company-profile-v163="1"][dir="rtl"] .sa-v163-meta{text-align:right!important;}',
      '[data-sa-company-profile-v163="1"] button{position:relative!important;inset:auto!important;transform:none!important;}',
      '@media(max-width:760px){[data-sa-company-profile-v163="1"]{width:calc(100vw - 14px)!important;max-width:none!important;height:calc(100vh - 14px)!important;max-height:none!important;padding:16px!important;}[data-sa-company-profile-v163="1"] .sa-v163-hero,[data-sa-company-profile-v163="1"][dir="rtl"] .sa-v163-hero{grid-template-columns:minmax(0,1fr)!important;}[data-sa-company-profile-v163="1"] .sa-v163-tabs button{flex:1 1 calc(50% - 9px)!important;}}'
    ].join('');
    document.head.appendChild(style);
  };

  const applyCompanyProfileV163=()=>{
    if(typeof location==='undefined' || (location.pathname!=='/super-admin' && location.pathname!=='/super-admin/'))return;
    ensureCompanyProfileV163Style();
    const norm=(value)=>String(value||'').replace(/\s+/g,' ').trim();
    const all=Array.from(document.body.querySelectorAll('*')).filter((el)=>el instanceof HTMLElement);
    const candidates=all.filter((el)=>{
      const text=norm(el.innerText);
      if(text.length<40 || text.length>12000)return false;
      const hasTitle=text.includes('Company Profile') || text.includes('ملف الشركة');
      const hasUsers=text.includes('Users') || text.includes('المستخدمون') || text.includes('حسابات الشركة');
      const hasSignin=text.includes('Sign in as Company Admin') || text.includes('الدخول كمسؤول الشركة');
      return hasTitle && hasUsers && hasSignin;
    });
    if(!candidates.length)return;
    candidates.sort((a,b)=>{
      const ra=a.getBoundingClientRect(),rb=b.getBoundingClientRect();
      const areaA=Math.max(1,ra.width*ra.height),areaB=Math.max(1,rb.width*rb.height);
      return areaA-areaB;
    });
    const profile=candidates.find((el)=>{
      const r=el.getBoundingClientRect();
      return r.width>=300 && r.height>=300;
    })||candidates[0];
    if(!(profile instanceof HTMLElement))return;

    const declared=String(root.getAttribute('lang')||'').toLowerCase();
    const declaredDir=String(root.getAttribute('dir')||'').toLowerCase();
    const pressed=Array.from(document.querySelectorAll('[aria-pressed="true"],[aria-current="true"],.active')).map((el)=>norm(el.textContent)).join(' ');
    let ar=declared.startsWith('ar') || declaredDir==='rtl' || /العربية|عربي/.test(pressed);
    if(!declared.startsWith('ar') && !declared.startsWith('en') && declaredDir!=='rtl' && declaredDir!=='ltr'){
      const bodyText=norm(document.body.innerText);
      const arSignals=(bodyText.match(/[\u0600-\u06FF]/g)||[]).length;
      const enSignals=(bodyText.match(/[A-Za-z]/g)||[]).length;
      ar=arSignals>enSignals*.22;
    }

    profile.dataset.saCompanyProfileV163='1';
    profile.setAttribute('dir',ar?'rtl':'ltr');
    profile.style.setProperty('text-align',ar?'right':'left','important');

    const phrases=[
      ['Company Profile','ملف الشركة'],
      ['Smart view of company, subscription, and billing data.','عرض شامل لبيانات الشركة والاشتراك والفواتير.'],
      ['Sign in as Company Admin','الدخول كمسؤول الشركة'],
      ['Overview','نظرة عامة'],
      ['Users','المستخدمون'],
      ['Subscription','الاشتراك'],
      ['Billing & Payments','الفواتير والمدفوعات'],
      ['Company Log','سجل الشركة'],
      ['Company Accounts','حسابات الشركة'],
      ['Company accounts','حسابات الشركة'],
      ['Refresh','تحديث'],
      ['Admin','مسؤول'],
      ['Active','نشط'],
      ['Trialing','فترة تجريبية'],
      ['Save role','حفظ الدور'],
      ['Save Role','حفظ الدور'],
      ['New password','كلمة مرور جديدة'],
      ['New Password','كلمة مرور جديدة'],
      ['Suspend','إيقاف الحساب'],
      ['Last Login','آخر تسجيل دخول'],
      ['Current passwords are not shown. You can only create a new password.','لا يتم عرض كلمات المرور الحالية. يمكنك إنشاء كلمة مرور جديدة فقط.'],
      ['Current passwords are not displayed. You can only create a new password.','لا يتم عرض كلمات المرور الحالية. يمكنك إنشاء كلمة مرور جديدة فقط.']
    ];

    const translateText=(raw)=>{
      let value=String(raw||'');
      const compact=norm(value);
      if(!compact)return value;
      if(ar){
        for(const pair of phrases){
          if(compact===pair[0])return value.replace(compact,pair[1]);
        }
        value=value.replace(/\bHealth\s+(\d{1,3}%)/g,'صحة الحساب $1');
        value=value.replace(/\bLast\s+Login\b/g,'آخر تسجيل دخول');
        value=value.replace(/آخر\s+Login/g,'آخر تسجيل دخول');
        if(/كلمات المرور الحالية/.test(value) && /(كلمة جديدة|كلمة مرور جديدة)/.test(value)){
          const count=(value.match(/\b\d+\b/)||[])[0];
          return 'لا يتم عرض كلمات المرور الحالية. يمكنك إنشاء كلمة مرور جديدة فقط.'+(count?' عدد الحسابات: '+count:'');
        }
      }else{
        for(const pair of phrases){
          if(compact===pair[1])return value.replace(compact,pair[0]);
        }
        value=value.replace(/صحة الحساب\s+(\d{1,3}%)/g,'Health $1');
        value=value.replace(/آخر تسجيل دخول/g,'Last Login');
        if(/كلمات المرور الحالية/.test(value) && /(كلمة جديدة|كلمة مرور جديدة)/.test(value)){
          const count=(value.match(/\b\d+\b/)||[])[0];
          return 'Current passwords are not shown. You can only create a new password.'+(count?' Accounts: '+count:'');
        }
      }
      return value;
    };

    const walker=document.createTreeWalker(profile,NodeFilter.SHOW_TEXT);
    let node=walker.nextNode();
    while(node){
      const parent=node.parentElement;
      if(parent && !/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(parent.tagName)){
        const next=translateText(node.nodeValue||'');
        if(next!==node.nodeValue)node.nodeValue=next;
      }
      node=walker.nextNode();
    }

    profile.querySelectorAll('[placeholder],[title],[aria-label]').forEach((el)=>{
      ['placeholder','title','aria-label'].forEach((name)=>{
        if(!el.hasAttribute(name))return;
        const current=el.getAttribute(name)||'';
        const next=translateText(current);
        if(next!==current)el.setAttribute(name,next);
      });
    });

    const titleLeaf=Array.from(profile.querySelectorAll('h1,h2,h3,h4,strong,b,span,div')).find((el)=>{
      const text=norm(el.textContent);
      return (text==='Company Profile' || text==='ملف الشركة') && (el.children.length===0 || /^H[1-4]$/.test(el.tagName));
    });
    if(titleLeaf instanceof HTMLElement){
      let header=titleLeaf.parentElement;
      for(let i=0;header && i<3;i+=1){
        const t=norm(header.innerText);
        if(t.includes('Smart view of company') || t.includes('عرض شامل لبيانات الشركة'))break;
        header=header.parentElement;
      }
      if(header instanceof HTMLElement)header.classList.add('sa-v163-header');
    }

    const signButton=Array.from(profile.querySelectorAll('button,a')).find((el)=>/Sign in as Company Admin|الدخول كمسؤول الشركة/.test(norm(el.textContent)));
    if(signButton instanceof HTMLElement){
      let hero=signButton.parentElement;
      for(let i=0;hero && i<6;i+=1){
        const text=norm(hero.innerText);
        const hasEmail=/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(text);
        const hasPath=/\/t\/[a-z0-9_-]+/i.test(text);
        if(hasEmail && hasPath){hero.classList.add('sa-v163-hero');break;}
        hero=hero.parentElement;
      }
    }

    const tabNames=/^(Overview|نظرة عامة|Users|المستخدمون|Subscription|الاشتراك|Billing & Payments|الفواتير والمدفوعات|Company Log|سجل الشركة)$/;
    const tabButtons=Array.from(profile.querySelectorAll('button')).filter((el)=>tabNames.test(norm(el.textContent)));
    const tabParents=new Map();
    tabButtons.forEach((button)=>{
      const parent=button.parentElement;
      if(parent)tabParents.set(parent,(tabParents.get(parent)||0)+1);
    });
    let tabs=null,tabCount=0;
    for(const [parent,count] of tabParents){
      if(count>tabCount){tabs=parent;tabCount=count;}
    }
    if(tabs instanceof HTMLElement && tabCount>=3)tabs.classList.add('sa-v163-tabs');

    const accountsHeading=Array.from(profile.querySelectorAll('h1,h2,h3,h4,strong,b,div,span')).find((el)=>{
      const text=norm(el.textContent);
      return (text==='Company Accounts' || text==='Company accounts' || text==='حسابات الشركة') && (el.children.length===0 || /^H[1-4]$/.test(el.tagName));
    });
    let usersSection=null;
    if(accountsHeading instanceof HTMLElement){
      let section=accountsHeading.parentElement;
      for(let i=0;section && i<6;i+=1){
        const text=norm(section.innerText);
        const hasRefresh=/Refresh|تحديث/.test(text);
        const hasAction=/New password|New Password|كلمة مرور جديدة|Suspend|إيقاف الحساب/.test(text);
        if(hasRefresh && hasAction){usersSection=section;break;}
        section=section.parentElement;
      }
      if(usersSection instanceof HTMLElement)usersSection.classList.add('sa-v163-users-section');
    }

    if(usersSection instanceof HTMLElement){
      const refresh=Array.from(usersSection.querySelectorAll('button')).find((el)=>/^(Refresh|تحديث)$/.test(norm(el.textContent)));
      if(refresh instanceof HTMLElement && refresh.parentElement)refresh.parentElement.classList.add('sa-v163-users-toolbar');

      const actionButtons=Array.from(usersSection.querySelectorAll('button')).filter((el)=>/^(Save role|Save Role|حفظ الدور|New password|New Password|كلمة مرور جديدة|Suspend|إيقاف الحساب)$/.test(norm(el.textContent)));
      const cards=new Set();
      actionButtons.forEach((button)=>{
        let cursor=button.parentElement;
        let card=null;
        for(let i=0;cursor && i<7;i+=1){
          const text=norm(cursor.innerText);
          const emails=text.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/ig)||[];
          const actions=Array.from(cursor.querySelectorAll('button')).filter((el)=>/Save role|Save Role|حفظ الدور|New password|New Password|كلمة مرور جديدة|Suspend|إيقاف الحساب/.test(norm(el.textContent))).length;
          if(emails.length>=1 && actions>=2){card=cursor;break;}
          cursor=cursor.parentElement;
        }
        if(card instanceof HTMLElement)cards.add(card);
      });

      cards.forEach((card)=>{
        card.classList.add('sa-v163-user-card');
        Array.from(card.querySelectorAll('button')).forEach((button)=>{
          const text=norm(button.textContent);
          if(/Save role|Save Role|حفظ الدور|New password|New Password|كلمة مرور جديدة|Suspend|إيقاف الحساب/.test(text)){
            const parent=button.parentElement;
            if(parent instanceof HTMLElement)parent.classList.add('sa-v163-actions');
          }
        });
        Array.from(card.querySelectorAll('a,span,p,small,strong,b,div,label')).forEach((el)=>{
          if(!(el instanceof HTMLElement))return;
          const text=norm(el.textContent);
          if(el.children.length===0 && /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(text))el.classList.add('sa-v163-email');
          if(el.children.length===0 && /Last Login|آخر تسجيل دخول|Active|نشط|Admin|مسؤول/.test(text))el.classList.add('sa-v163-meta');
        });
      });
    }

    Array.from(profile.querySelectorAll('a,span,p,small,strong,b,div,label')).forEach((el)=>{
      if(!(el instanceof HTMLElement) || el.children.length>0)return;
      const text=norm(el.textContent);
      if(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(text))el.classList.add('sa-v163-email');
    });
  };

  let companyProfileV163Pending=false;
  const scheduleCompanyProfileV163=()=>{
    if(companyProfileV163Pending)return;
    companyProfileV163Pending=true;
    requestAnimationFrame(()=>{
      companyProfileV163Pending=false;
      applyCompanyProfileV163();
    });
  };
  const companyProfileV163Observer=new MutationObserver(scheduleCompanyProfileV163);
  companyProfileV163Observer.observe(root,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:['lang','dir','class','aria-selected','aria-pressed']});
  window.addEventListener('hashchange',scheduleCompanyProfileV163);
  scheduleCompanyProfileV163();

  const themeKey='tcrm-super-admin-theme';"""


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.63 Company Profile UX rebuild already applied; no changes made.')
        return
    if V162_MARKER not in text:
        raise SystemExit('Bilingual V1.62 Company Profile Users Arabic/layout closure marker not found; apply V1.62 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    anchor_count = text.count(ANCHOR)
    if anchor_count != 1:
        raise SystemExit(f'V1.63 insertion anchor count is {anchor_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)
    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.63 Company Profile UX rebuild.')


if __name__ == '__main__':
    main()
