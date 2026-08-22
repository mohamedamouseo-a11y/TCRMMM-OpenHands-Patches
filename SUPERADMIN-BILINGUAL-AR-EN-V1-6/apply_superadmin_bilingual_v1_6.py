#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_6'
V15_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_5'
JS_ANCHOR = '  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_5\n'
DOC_ANCHOR = "    applyV12CriticalOverrides();\n    applyV13CriticalOverrides();\n    applyV14CriticalOverrides();\n    applyV15PostSweep();\n    syncLanguageControls();"
SYNC_TITLE_OLD = "      button.title=ar?'Switch to English':'التبديل إلى العربية';"
SYNC_TITLE_NEW = "      button.title=ar?'التبديل إلى الإنجليزية':'Switch to Arabic';"

JS = r'''
  // SUPER_ADMIN_BILINGUAL_AR_EN_V1_6
  // Lifecycle-first bilingual finalization. V1.6 repairs the language-control lifecycle,
  // fixes the old syncLanguageControls title semantics, and runs an exact post-render
  // canonicalizer after the legacy/source-aware translators. It only touches audited
  // static UI strings/attributes; tenant/user/business data is not pattern-translated.

  const V16_RULES=[
    // Arabic dashboard eyebrow/static items
    ['PLATFORM OVERVIEW','PLATFORM OVERVIEW','نظرة عامة على المنصة'],
    ['QUICK COMMANDS','QUICK COMMANDS','أوامر سريعة'],
    ['ATTENTION','ATTENTION','يحتاج متابعة'],
    ['USAGE','USAGE','الاستخدام'],
    ['GLOBAL SEARCH','GLOBAL SEARCH','البحث الشامل'],
    ['SECURITY','SECURITY','الأمان'],
    ['ORGANIZATIONS','ORGANIZATIONS','المؤسسات'],
    ['إنشاء Workspace جديد','Create a new Workspace','إنشاء مساحة عمل جديدة'],
    ['Create a new Workspace','Create a new Workspace','إنشاء مساحة عمل جديدة'],
    ['Provisioning Queue','Provisioning Queue','قائمة التجهيز'],
    ['Slug','Slug','المعرّف'],
    ['Email','Email','البريد الإلكتروني'],
    ['حفظ Admin وصلاحيات الشركات','Save Admin & Company Permissions','حفظ المسؤول وصلاحيات الشركات'],
    ['Save Admin & Company Permissions','Save Admin & Company Permissions','حفظ المسؤول وصلاحيات الشركات'],
    ['Owner Only','Owner Only','للمالك فقط'],
    ['OWNER ONLY','OWNER ONLY','للمالك فقط'],
    ['تحميل نسخة حقيقية من السورس الحالي للـ SaaS.','Download a real copy of the current SaaS source.','تحميل نسخة حقيقية من الكود المصدري الحالي للمنصة.'],
    ['تحميل نسخة حقيقية من السورس الحالي لـ SaaS.','Download a real copy of the current SaaS source.','تحميل نسخة حقيقية من الكود المصدري الحالي للمنصة.'],
    ['Download a real copy of the current SaaS source.','Download a real copy of the current SaaS source.','تحميل نسخة حقيقية من الكود المصدري الحالي للمنصة.'],

    // Login final-state copy
    ['Platform administration, simplified.','Platform administration, simplified.','إدارة المنصة، ببساطة.'],
    ['Platform administration. Simplified.','Platform administration, simplified.','إدارة المنصة، ببساطة.'],
    ['Secure, multi-tenant control for your entire TCRMMT ecosystem.','Secure, multi-tenant control for your entire TCRMMT ecosystem.','تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.'],

    // Plans / commercial Arabic final gate
    ['Back to Command Center','Back to Command Center','العودة إلى مركز القيادة'],
    ['Refresh Data','Refresh Data','تحديث البيانات'],
    ['View details','View details','عرض التفاصيل'],
    ['Kill Switch','Kill Switch','مفتاح الإيقاف الطارئ'],
    ['Canary %','Canary %','نسبة النشر التجريبي %'],
    ['Grace Days','Grace Days','أيام السماح'],
    ['Feature Overrides JSON','Feature Overrides JSON','تجاوزات الخصائص JSON'],
    ['Limit Overrides JSON','Limit Overrides JSON','تجاوزات الحدود JSON'],
    ['Controlled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout','Controlled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout','التحكم · التفعيل · الاستخدام · دورة الاشتراك · الفوترة · الخدمة الذاتية · التشغيل التدريجي'],
    ['تحكمled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout','Controlled Enforcement · Usage · Lifecycle · Billing · Self-Service · Rollout','التحكم · التفعيل · الاستخدام · دورة الاشتراك · الفوترة · الخدمة الذاتية · التشغيل التدريجي'],

    // English final-gate leftovers from V1.5 evidence
    ['متأخر / منتهي','Overdue / expired','متأخر / منتهي'],
    ['كل الحسابات','All accounts','كل الحسابات'],
    ['نشاط المنصة','Platform activity','نشاط المنصة'],
    ['الإيراد الشهري','Monthly revenue','الإيراد الشهري'],
    ['يتطلب متابعة','Needs attention','يتطلب متابعة'],
    ['بحث عام: شركة / فاتورة / نشاط','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط'],
    ['إدارة المستخدمين والصلاحيات عبر جميع الشركات','Manage users and permissions across all companies','إدارة المستخدمين والصلاحيات عبر جميع الشركات'],
    ['أحدث العمليات والتغييرات المسجلة على المنصة','Latest operations and changes recorded on the platform','أحدث العمليات والتغييرات المسجلة على المنصة'],
    ['Review sensitive events وتتبع العمليات الإدارية','Review sensitive events and track administrative operations','مراجعة الأحداث الحساسة وتتبع العمليات الإدارية'],
    ['الفرع النشط','Active branch','الفرع النشط'],
    ['موجودة','Present','موجودة'],
    ['إدارة اتصال WhatsApp المركزي واختبار الخدمة','Manage the central WhatsApp connection and test the service','إدارة اتصال WhatsApp المركزي واختبار الخدمة'],
    ['حفظ إعدادات الSecurity','Save Security Settings','حفظ إعدادات الأمان'],
    ['Save Security Settings','Save Security Settings','حفظ إعدادات الأمان'],
    ['Switch to English','Switch to English','التبديل إلى الإنجليزية'],
    ['Switch to Arabic','Switch to Arabic','التبديل إلى العربية']
  ];

  const V16_BY_SOURCE=new Map(V16_RULES.map(rule=>[rule[0],rule]));
  const V16_BY_EN=new Map(V16_RULES.map(rule=>[rule[1],rule]));
  const V16_BY_AR=new Map(V16_RULES.map(rule=>[rule[2],rule]));
  const v16Norm=value=>String(value==null?'':value).trim().replace(/\s+/g,' ');

  const v16Canonical=value=>{
    const raw=v16Norm(value);
    return V16_BY_SOURCE.get(raw)||V16_BY_EN.get(raw)||V16_BY_AR.get(raw)||null;
  };
  const v16Translate=value=>{
    const raw=v16Norm(value);
    if(!raw)return raw;
    const rule=v16Canonical(raw);
    if(!rule)return raw;
    return currentLanguage()==='ar'?rule[2]:rule[1];
  };

  const v16TranslateTextNode=node=>{
    const parent=node&&node.parentElement;
    if(!parent||/^(SCRIPT|STYLE|NOSCRIPT|CODE|PRE|TEXTAREA)$/.test(parent.tagName))return;
    const current=node.nodeValue||'';
    const trimmed=current.trim();
    if(!trimmed)return;
    const desired=v16Translate(trimmed);
    if(desired===trimmed)return;
    const leading=(current.match(/^\s*/)||[''])[0];
    const trailing=(current.match(/\s*$/)||[''])[0];
    node.nodeValue=leading+desired+trailing;
  };
  const v16TranslateAttrs=element=>{
    if(!(element instanceof Element))return;
    ['placeholder','title','aria-label'].forEach(name=>{
      if(!element.hasAttribute(name))return;
      const current=element.getAttribute(name)||'';
      const desired=v16Translate(current);
      if(desired!==v16Norm(current))element.setAttribute(name,desired);
    });
  };

  const v16BindLanguageButton=button=>{
    if(!(button instanceof HTMLButtonElement))return;
    if(!button.dataset.saLanguageV16Bound){
      button.dataset.saLanguageV16Bound='1';
      button.addEventListener('click',event=>{
        event.preventDefault();
        event.stopPropagation();
        toggleLanguage();
        queueMicrotask(applyV16FinalLocalizationCore);
        setTimeout(applyV16FinalLocalizationCore,80);
        setTimeout(applyV16FinalLocalizationCore,350);
      });
    }
    const ar=currentLanguage()==='ar';
    button.textContent=ar?'EN':'AR';
    const title=ar?'التبديل إلى الإنجليزية':'Switch to Arabic';
    button.title=title;
    button.setAttribute('aria-label',title);
  };

  const v16EnsureButton=(host,kind)=>{
    if(!(host instanceof HTMLElement))return null;
    const selector=kind==='dock'?'[data-sa-language-toggle]':'[data-sa-language-inline]';
    let button=host.querySelector(selector);
    if(!(button instanceof HTMLButtonElement)){
      button=document.createElement('button');
      button.type='button';
      button.className='sa-language-inline sa-language-v16';
      if(kind==='dock')button.dataset.saLanguageToggle='1';
      else button.dataset.saLanguageInline='1';
      if(kind==='dock'){
        const top=host.querySelector('[data-sa-top]');
        if(top)host.insertBefore(button,top); else host.appendChild(button);
      }else host.appendChild(button);
    }
    v16BindLanguageButton(button);
    return button;
  };

  const ensureV16LanguageControls=()=>{
    // Login: prefer the existing utility row. If a late Login render omits it, create a
    // dedicated visible host so language switching never disappears.
    let loginHost=document.querySelector('#loginView .tamiyouzLoginUtility');
    const loginView=document.querySelector('#loginView');
    if(!(loginHost instanceof HTMLElement)&&loginView instanceof HTMLElement){
      loginHost=loginView.querySelector('.sa-language-v16-login-host');
      if(!(loginHost instanceof HTMLElement)){
        loginHost=document.createElement('div');
        loginHost.className='sa-language-v16-login-host';
        Object.assign(loginHost.style,{position:'absolute',top:'18px',right:'22px',zIndex:'1000',display:'flex',gap:'8px',alignItems:'center'});
        loginView.appendChild(loginHost);
      }
    }
    if(loginHost instanceof HTMLElement)v16EnsureButton(loginHost,'inline');

    // Authenticated topbar.
    let topHost=document.querySelector('#appShell .topbarActions');
    if(!(topHost instanceof HTMLElement))topHost=document.querySelector('#appShell .topbar');
    if(topHost instanceof HTMLElement)v16EnsureButton(topHost,'inline');

    // Floating UI dock.
    const dock=document.querySelector('.sa-ui-dock');
    if(dock instanceof HTMLElement)v16EnsureButton(dock,'dock');

    document.querySelectorAll('[data-sa-language-toggle],[data-sa-language-inline]').forEach(v16BindLanguageButton);
  };

  const v16SetText=(selector,en,ar)=>{
    const el=document.querySelector(selector);
    if(!(el instanceof HTMLElement))return;
    const desired=currentLanguage()==='ar'?ar:en;
    if(v16Norm(el.textContent)!==desired)el.textContent=desired;
  };
  const v16SetAttr=(selector,name,en,ar)=>{
    const el=document.querySelector(selector);
    if(!(el instanceof Element))return;
    const desired=currentLanguage()==='ar'?ar:en;
    if(el.getAttribute(name)!==desired)el.setAttribute(name,desired);
  };

  const applyV16CriticalOverrides=()=>{
    // Login copy is rewritten by the auth/recovery view, so pin it after each render.
    v16SetText('#loginView .tamiyouzBrandContent h1','Platform administration, simplified.','إدارة المنصة، ببساطة.');
    v16SetText('#loginView .tamiyouzBrandContent p','Secure, multi-tenant control for your entire TCRMMT ecosystem.','تحكم آمن ومتعدد الشركات في منظومة TCRMMT بالكامل.');

    // High-churn attributes.
    v16SetAttr('#topGlobalSearch','placeholder','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط');
    v16SetAttr('#topGlobalSearch','aria-label','Global search: company / invoice / activity','بحث عام: شركة / فاتورة / نشاط');
    v16SetAttr('#globalSearchBox','placeholder','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');
    v16SetAttr('#globalSearchBox','aria-label','Search by company / invoice / activity','بحث باسم شركة / فاتورة / نشاط');
    v16SetAttr('#refreshBtn','aria-label','Refresh dashboard data','تحديث بيانات لوحة التحكم');
    v16SetAttr('#createTenantOpenBtn','aria-label','Add Company','إضافة شركة');
    v16SetAttr('#openPlatformAdminsTopBtn','aria-label','Open Platform Admins','فتح إدارة مسؤولي المنصة');
    v16SetAttr('#openSettingsBtn','aria-label','Open Download Source Center','فتح مركز تحميل السورس');

    ensureV16LanguageControls();
  };

  const applyV16FinalLocalizationCore=()=>{
    if(!document.body)return;
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    let node=walker.nextNode();
    while(node){v16TranslateTextNode(node);node=walker.nextNode()}
    document.querySelectorAll('[placeholder],[title],[aria-label]').forEach(v16TranslateAttrs);
    applyV16CriticalOverrides();
  };

  let v16BurstUntil=0;
  const applyV16FinalLocalization=()=>{
    applyV16FinalLocalizationCore();
    const now=Date.now();
    if(now<v16BurstUntil)return;
    v16BurstUntil=now+2400;
    [60,250,900,2200].forEach(delay=>setTimeout(applyV16FinalLocalizationCore,delay));
  };
  // END SUPER_ADMIN_BILINGUAL_AR_EN_V1_6
'''


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label} anchor count is {count}; refusing unknown baseline.')
    return text.replace(old, new, 1)


def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.6 already applied; no changes made.')
        return
    if V15_MARKER not in text:
        raise SystemExit('Bilingual V1.5 marker not found; apply V1 through V1.5 first.')

    for label, anchor in [
        ('V1.5 JS end', JS_ANCHOR),
        ('V1.5 translation document chain', DOC_ANCHOR),
        ('language-control title semantics', SYNC_TITLE_OLD),
    ]:
        if text.count(anchor) != 1:
            raise SystemExit(f'{label} anchor count is {text.count(anchor)}; refusing unknown baseline.')

    text = replace_once(text, JS_ANCHOR, JS_ANCHOR + JS + '\n', 'V1.6 JS')
    text = replace_once(text, SYNC_TITLE_OLD, SYNC_TITLE_NEW, 'language-control title semantics')
    text = replace_once(
        text,
        DOC_ANCHOR,
        "    applyV12CriticalOverrides();\n    applyV13CriticalOverrides();\n    applyV14CriticalOverrides();\n    applyV15PostSweep();\n    syncLanguageControls();\n    applyV16FinalLocalization();",
        'V1.6 final localization hook',
    )

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual Arabic / English V1.6 language-control lifecycle and final canonicalization patch.')


if __name__ == '__main__':
    main()
