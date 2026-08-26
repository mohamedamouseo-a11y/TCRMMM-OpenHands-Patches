#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('/var/www/TCRMMT/server/superAdminUiPolish.ts')
MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_47_TARA_APIS_FULL_STATIC_CLOSURE'
V144_MARKER = 'SUPER_ADMIN_BILINGUAL_AR_EN_V1_44_EVOLUTION_API_EN_RUNTIME_STATUS_HINTS_CLOSURE'

REPLACES = [
    ('const UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V144";',
     '// SUPER_ADMIN_BILINGUAL_AR_EN_V1_47_TARA_APIS_FULL_STATIC_CLOSURE\nconst UI_VERSION = "SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V147";',
     'UI version', 1),
    ("  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V144';",
     "  const VERSION='SUPER_ADMIN_FULL_UI_POLISH_V2_BILINGUAL_V147';",
     'legacy UI runtime version', 1),
    ('const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v144.js";',
     'const BILINGUAL_RUNTIME_PATH = "/super-admin/bilingual-v147.js";',
     'runtime path', 1),
    ("  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V144';",
     "  const VERSION='SUPER_ADMIN_BILINGUAL_RUNTIME_V147';",
     'standalone runtime version', 1),
    ('?v=superadmin-bilingual-v144', '?v=superadmin-bilingual-v147', 'asset cache key', 3),
    ('data-sa-bilingual-runtime="v144"', 'data-sa-bilingual-runtime="v147"', 'runtime asset marker', 1),
]

ANCHOR = """    const v144ManagedCapability=document.querySelector('#evolutionManagedCapability');
    if(v144ManagedCapability){
      const key=(v144ManagedCapability.textContent||'').trim();
      const ar='الإعداد التلقائي متاح على السيرفر. سيتم تحديث ملف الخدمة وإعادة تشغيل Evolution API بأمان.';
      const en='Automatic setup is available on the server. The service file will be updated and Evolution API restarted safely.';
      if(key===ar||key===en)v144ManagedCapability.textContent=(root.lang==='ar'?ar:en);
    }
  }};"""

REPLACEMENT = """    const v144ManagedCapability=document.querySelector('#evolutionManagedCapability');
    if(v144ManagedCapability){
      const key=(v144ManagedCapability.textContent||'').trim();
      const ar='الإعداد التلقائي متاح على السيرفر. سيتم تحديث ملف الخدمة وإعادة تشغيل Evolution API بأمان.';
      const en='Automatic setup is available on the server. The service file will be updated and Evolution API restarted safely.';
      if(key===ar||key===en)v144ManagedCapability.textContent=(root.lang==='ar'?ar:en);
    }
  }

    // SUPER_ADMIN_BILINGUAL_AR_EN_V1_47_TARA_APIS_FULL_STATIC_CLOSURE
    // V1.46 Full Audit + source audit: Tara parity page is standalone and its ordinary UI is hardcoded Arabic.
    // Canonicalize the whole static surface while preserving tenant/provider/runtime/domain values.
    if(typeof location!=='undefined' && location.pathname==='/super-admin/tara-integrations'){
      const v147Pairs=[
        ['Tara Integrations','تكاملات تارا'],
        ['Manage the selected company integrations securely, with secrets encrypted and never shown after saving.','إدارة تكاملات الشركة المختارة بصورة آمنة، مع تشفير الأسرار وعدم عرضها بعد الحفظ.'],
        ['Back to Admin Console','العودة إلى لوحة الإدارة'],
        ['Bahgat Settings','إعدادات بهجت'],
        ['Add Integration','إضافة تكامل'],
        ['Company','الشركة'],
        ['Refresh Data','تحديث البيانات'],
        ['Available to the platform owner only. All save, test, and disable operations are recorded in the audit log.','متاح لمالك المنصة فقط. تُسجل جميع عمليات الحفظ والاختبار والتعطيل في سجل التدقيق.'],
        ['Total integrations','إجمالي التكاملات'],
        ['For this company','لهذه الشركة'],
        ['Enabled integrations','التكاملات المفعّلة'],
        ['Ready to use','جاهزة للاستخدام'],
        ['Complete connection data','بيانات الاتصال المكتملة'],
        ['Secrets stored securely','أسرار محفوظة بأمان'],
        ['Successful tests','اختبارات ناجحة'],
        ['Latest recorded status','آخر حالة مسجلة'],
        ['Integrations and APIs','التكاملات والواجهات البرمجية'],
        ['Each integration remains disabled by default until it is saved, tested, and then enabled.','يظل أي تكامل متوقفًا افتراضيًا حتى الحفظ والاختبار ثم التفعيل.'],
        ['Enter the required provider data. Keys and secrets will not be shown again after saving.','أدخل بيانات المزود المطلوبة. لن تظهر المفاتيح أو الأسرار مرة أخرى بعد الحفظ.'],
        ['Close','إغلاق'],
        ['Basic settings','الإعدادات الأساسية'],
        ['Provider','مزود الخدمة'],
        ['Integration status','حالة التكامل'],
        ['Disabled','متوقف'],
        ['Enabled','مفعّل'],
        ['Connection data','بيانات الاتصال'],
        ['Model','النموذج'],
        ['API key','مفتاح الواجهة البرمجية'],
        ['Voice ID','معرّف الصوت'],
        ['Transcription model','نموذج تحويل الصوت'],
        ['Output format','صيغة الإخراج'],
        ['Access token','رمز الوصول'],
        ['App secret','سر التطبيق'],
        ['Verify token','رمز التحقق'],
        ['Phone number ID','معرّف رقم الهاتف'],
        ['WhatsApp Business Account ID','معرّف حساب واتساب للأعمال'],
        ['API version','إصدار الواجهة البرمجية'],
        ['Account name','اسم الحساب'],
        ['Sensitive data is encrypted before storage.','يتم تشفير البيانات الحساسة قبل التخزين.'],
        ['Save securely','حفظ آمن'],
        ['No integrations for this company','لا توجد تكاملات لهذه الشركة'],
        ['Start by adding the first Tara provider, then test the connection before enabling it. All credentials remain encrypted and cannot be displayed after saving.','ابدأ بإضافة أول مزود لتارا، ثم اختبر الاتصال قبل تفعيله. تظل جميع بيانات الدخول مشفرة وغير قابلة للعرض بعد الحفظ.'],
        ['Add first integration','إضافة أول تكامل'],
        ['Default account','الحساب الافتراضي'],
        ['Complete and saved','مكتملة ومحفوظة'],
        ['Needs completion','تحتاج استكمالًا'],
        ['Last test','آخر اختبار'],
        ['Successful','ناجح'],
        ['Failed','فشل'],
        ['Not tested','لم يُختبر'],
        ['Last test time','وقت آخر اختبار'],
        ['Never','لم يتم'],
        ['Edit','تعديل'],
        ['Test connection','اختبار الاتصال'],
        ['Disable and delete secret','تعطيل وحذف السر'],
        ['Saving','جارٍ الحفظ'],
        ['Testing','جارٍ الاختبار'],
        ['Disabling','جارٍ التعطيل'],
        ['Integration saved and its data encrypted successfully','تم حفظ التكامل وتشفير بياناته بنجاح'],
        ['Connection tested successfully','تم اختبار الاتصال بنجاح'],
        ['Integration disabled and encrypted secret deleted','تم تعطيل التكامل ومسح السر المشفر'],
        ['Unauthorized','غير مصرح'],
        ['Request failed','فشل الطلب']
      ];
      const v147Map=new Map();
      for(const [en,ar] of v147Pairs)v147Map.set(root.lang==='ar'?en:ar,root.lang==='ar'?ar:en);
      const v147TranslateLeaf=(el)=>{
        if(!el || el.children.length)return;
        const key=(el.textContent||'').trim();
        const next=v147Map.get(key);
        if(next)el.textContent=next;
      };
      document.querySelectorAll('body *').forEach(v147TranslateLeaf);

      const v147SetDirectText=(selector,en,ar)=>{
        const el=document.querySelector(selector); if(!el)return;
        const next=(root.lang==='ar'?ar:en);
        for(const node of Array.from(el.childNodes)){
          if(node.nodeType===3 && String(node.nodeValue||'').trim()){node.nodeValue=next;return;}
        }
      };
      v147SetDirectText('.eyebrow','Platform Administration · Tara','إدارة المنصة · تارا');
      v147SetDirectText('label:has(#tenant)','Company','الشركة');
      v147SetDirectText('label:has(#provider)','Provider','مزود الخدمة');
      v147SetDirectText('label:has(#enabled)','Integration status','حالة التكامل');
      v147SetDirectText('label[data-field="model"]','Model','النموذج');
      v147SetDirectText('label[data-field="apiKey"]','API key','مفتاح الواجهة البرمجية');
      v147SetDirectText('label[data-field="voiceId"]','Voice ID','معرّف الصوت');
      v147SetDirectText('label[data-field="transcriptionModel"]','Transcription model','نموذج تحويل الصوت');
      v147SetDirectText('label[data-field="outputFormat"]','Output format','صيغة الإخراج');
      v147SetDirectText('label[data-field="accessToken"]','Access token','رمز الوصول');
      v147SetDirectText('label[data-field="appSecret"]','App secret','سر التطبيق');
      v147SetDirectText('label[data-field="verifyToken"]','Verify token','رمز التحقق');
      v147SetDirectText('label[data-field="phoneNumberId"]','Phone number ID','معرّف رقم الهاتف');
      v147SetDirectText('label[data-field="wabaId"]','WhatsApp Business Account ID','معرّف حساب واتساب للأعمال');
      v147SetDirectText('label[data-field="apiVersion"]','API version','إصدار الواجهة البرمجية');
      v147SetDirectText('label[data-field="displayName"]','Account name','اسم الحساب');

      const v147Subtitle=document.querySelector('#pageSubtitle');
      if(v147Subtitle){
        const raw=(v147Subtitle.textContent||'').trim();
        if(root.lang==='en'){
          const m=raw.match(/^إدارة تكاملات (.+) بصورة آمنة، مع تشفير الأسرار وعدم عرضها بعد الحفظ\.$/u);
          if(m)v147Subtitle.textContent='Manage '+m[1]+' integrations securely, with secrets encrypted and never shown after saving.';
        }else{
          const m=raw.match(/^Manage (.+) integrations securely, with secrets encrypted and never shown after saving\.$/u);
          if(m)v147Subtitle.textContent='إدارة تكاملات '+m[1]+' بصورة آمنة، مع تشفير الأسرار وعدم عرضها بعد الحفظ.';
        }
      }

      const v147ModalTitle=document.querySelector('#modalTitle');
      if(v147ModalTitle){
        const raw=(v147ModalTitle.textContent||'').trim();
        if(root.lang==='en'){
          const m=raw.match(/^تعديل\s+(.+)$/u); if(m)v147ModalTitle.textContent='Edit '+m[1];
        }else{
          const m=raw.match(/^Edit\s+(.+)$/u); if(m)v147ModalTitle.textContent='تعديل '+m[1];
        }
      }

      const v147Tenant=document.querySelector('#tenant');
      if(v147Tenant)v147Tenant.setAttribute('aria-label',root.lang==='ar'?'اختر الشركة':'Select company');
      const v147Control=document.querySelector('.controlBar');
      if(v147Control)v147Control.setAttribute('aria-label',root.lang==='ar'?'اختيار الشركة':'Company selection');
      const v147Stats=document.querySelector('.stats');
      if(v147Stats)v147Stats.setAttribute('aria-label',root.lang==='ar'?'ملخص التكاملات':'Integrations summary');
      const v147ApiKey=document.querySelector('#apiKey');
      if(v147ApiKey)v147ApiKey.setAttribute('placeholder',root.lang==='ar'?'اتركه فارغًا للاحتفاظ بالمحفوظ':'Leave blank to keep the saved value');
      document.title=(root.lang==='ar'?'تكاملات تارا · إدارة المنصة':'Tara Integrations · Platform Administration');
    }
  };"""

def main():
    text = TARGET.read_text(encoding='utf-8')
    if MARKER in text:
        print('Super Admin bilingual V1.47 Tara APIs full static closure already applied; no changes made.')
        return
    if V144_MARKER not in text:
        raise SystemExit('Bilingual V1.44 Evolution API runtime status/hints marker not found; apply V1.44 first.')

    for old, _new, label, expected in REPLACES:
        count = text.count(old)
        if count != expected:
            raise SystemExit(f'{label} anchor count is {count}; expected {expected}.')
    anchor_count = text.count(ANCHOR)
    if anchor_count != 1:
        raise SystemExit(f'V1.47 Tara finalizer anchor count is {anchor_count}; expected 1.')

    for old, new, _label, _expected in REPLACES:
        text = text.replace(old, new)
    text = text.replace(ANCHOR, REPLACEMENT, 1)

    TARGET.write_text(text, encoding='utf-8')
    print('Applied Super Admin Bilingual V1.47 Tara APIs full static closure runtime.')

if __name__ == '__main__':
    main()
