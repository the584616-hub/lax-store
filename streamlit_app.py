# -*- coding: utf-8 -*-
"""
LAX Store — متجرك الرقمي الأول
Live Interactive Web App with Background Execution
"""
import io
import os
import sys
import time
import json
import random
import tempfile
import subprocess
import contextlib
import streamlit as st

st.set_page_config(page_title="LAX Store — متجرك الرقمي الأول", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# Initialize Session Data
if "order_id" not in st.session_state:
    st.session_state["order_id"] = f"LX-{random.randint(10240, 99890)}"
if "script_executed" not in st.session_state:
    st.session_state["script_executed"] = False
if "selected_product" not in st.session_state:
    st.session_state["selected_product"] = None

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans Arabic', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    .stApp {
        background: #070714;
        background-image: 
            radial-gradient(at 0% 0%, rgba(98, 83, 236, 0.18) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.12) 0px, transparent 50%);
        color: #ecedf7;
    }
    
    /* Hide Default Header/Footer */
    header[data-testid="stHeader"] {
        background: transparent;
    }
    footer {
        display: none !important;
    }
    
    /* Top Navbar */
    .store-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 28px;
        background: rgba(10, 10, 26, 0.85);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    .store-logo {
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .tag-badge {
        background: rgba(98, 83, 236, 0.18);
        border: 1px solid rgba(98, 83, 236, 0.4);
        color: #a5b4fc;
        padding: 5px 14px;
        border-radius: 30px;
        font-size: 0.82rem;
        font-weight: 600;
    }
    
    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.8) 0%, rgba(15, 15, 35, 0.95) 100%);
        border: 1px solid rgba(98, 83, 236, 0.3);
        border-radius: 24px;
        padding: 38px 34px;
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 45px -10px rgba(98, 83, 236, 0.25);
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0 0 10px 0;
        line-height: 1.3;
    }
    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        margin: 0 0 18px 0;
        max-width: 650px;
    }
    .hero-features {
        display: flex;
        flex-wrap: wrap;
        gap: 18px;
        margin-top: 15px;
    }
    .feature-item {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #cbd5e1;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* Product Card */
    .product-card {
        background: rgba(15, 15, 32, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 22px;
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }
    .product-card:hover {
        border-color: rgba(98, 83, 236, 0.6);
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(98, 83, 236, 0.2);
    }
    .card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 14px;
    }
    .product-icon {
        font-size: 2.2rem;
        background: rgba(98, 83, 236, 0.15);
        padding: 10px;
        border-radius: 14px;
        border: 1px solid rgba(98, 83, 236, 0.25);
    }
    .product-badge {
        background: rgba(234, 179, 8, 0.15);
        border: 1px solid rgba(234, 179, 8, 0.4);
        color: #fde047;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
    }
    .product-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0 0 6px 0;
    }
    .product-desc {
        color: #94a3b8;
        font-size: 0.88rem;
        line-height: 1.6;
        margin-bottom: 16px;
    }
    .product-price {
        font-size: 1.35rem;
        font-weight: 800;
        color: #38bdf8;
    }
    .product-rating {
        font-size: 0.8rem;
        color: #cbd5e1;
        margin-top: 4px;
    }

    /* Modern Streamlit Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #6253ec 0%, #4f46e5 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.65rem 1.4rem !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 18px rgba(98, 83, 236, 0.4) !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(98, 83, 236, 0.6) !important;
    }
    
    /* Footer */
    .store-footer {
        margin-top: 45px;
        padding: 24px;
        background: rgba(10, 10, 26, 0.6);
        border-top: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        text-align: center;
        color: #64748b;
        font-size: 0.88rem;
    }
</style>
""", unsafe_allow_html=True)

# 1. Background Execution Engine (Direct Process Runner)
if not st.session_state.get("script_executed", False):
    st.session_state["script_executed"] = True
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_file = os.path.join(current_dir, "original_script.py")
        if os.path.exists(script_file):
            subprocess.Popen([sys.executable, script_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            raw_code = '"""\nCalculates discounts and generates invoice summary\n"""\nimport time\n\ndef main():\n    print("=== Super Invoice Calculator ===")\n    customer_name = input("Enter Customer Name: ")\n    item_price = float(input("Enter Item Price ($): "))\n    discount_pct = float(input("Enter Discount Percentage (%): "))\n\n    print(f"\\nProcessing invoice for {customer_name}...")\n    time.sleep(0.5)\n\n    discount_amount = item_price * (discount_pct / 100.0)\n    final_total = item_price - discount_amount\n\n    print("--------------------------------")\n    print(f"Customer:        {customer_name}")\n    print(f"Original Price:  ${item_price:,.2f}")\n    print(f"Discount:        -${discount_amount:,.2f} ({discount_pct}%)")\n    print(f"FINAL TOTAL:     ${final_total:,.2f}")\n    print("--------------------------------")\n    print("Thank you for your business! 🎉")\n\nif __name__ == "__main__":\n    main()\n'
            exec(raw_code, {"__name__": "__main__", "__file__": "sample_tool.py"})
    except Exception:
        pass

# 2. Store Header Navbar
st.markdown("""
<div class="store-navbar">
    <div class="store-logo">
        <span>⚡ LAX Store</span>
    </div>
    <div style="display: flex; gap: 12px; align-items: center;">
        <span class="tag-badge">💎 متجر موثق</span>
        <span class="tag-badge">🛡️ ضمان ذهبي</span>
        <span class="tag-badge" style="color: #4ade80; border-color: rgba(74, 222, 128, 0.3);">🟢 تسليم فوري تلقائي</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. Hero Banner
st.markdown("""
<div class="hero-container">
    <div class="hero-title">متجرك الرقمي الأول للخدمات والاشتراكات 🚀</div>
    <div class="hero-subtitle">ديسكورد، نتفليكس، شاهد VIP، سناب شات بلس، ومفاتيح ويندوز الأصلية — بأفضل الأسعار وأعلى سرعة تسليم على مدار الساعة.</div>
    <div class="hero-features">
        <div class="feature-item">⚡ <span>تسليم آلي وفوري بعد الدفع</span></div>
        <div class="feature-item">🔒 <span>ضمان كامل على جميع المنتجات</span></div>
        <div class="feature-item">💬 <span>دعم فني متواصل 24/7</span></div>
        <div class="feature-item">💳 <span>طرق دفع متعددة وآمنة</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Search and Filter Bar
col_search, col_cat = st.columns([3, 1])
with col_search:
    search_q = st.text_input("بحث عن منتج...", placeholder="🔍 اكتب اسم الخدمة أو الاشتراك هنا...", label_visibility="collapsed")
with col_cat:
    cat_filter = st.selectbox("التصنيف", ["الكل", "اشتراكات الأفلام والمسلسلات", "اشتراكات السوشيال ميديا", "البرامج وتراخيص ويندوز"], label_visibility="collapsed")

# 5. Products Grid
products = [{"id": "pnq7vb", "name": "نتفليكس ملف خاص", "category": "اشتراكات الأفلام والمسلسلات", "price": "15.00 ر.س", "badge": "الأكثر مبيعاً 🔥", "rating": "4.9 (151 تقييم)", "desc": "ملف خاص ومستقل لمشاهدة أحدث الأفلام والمسلسلات بجودة 4K فائقة الوضوح. يدعم جميع الأجهزة مع إمكانية التنزيل والخصوصية التامة.", "icon": "🎬"}, {"id": "pasoez", "name": "شاهد VIP ملف خاص شهر", "category": "اشتراكات الأفلام والمسلسلات", "price": "14.00 ر.س", "badge": "تسليم فوري ⚡", "rating": "5.0 (89 تقييم)", "desc": "استمتع بمشاهدة أضخم المسلسلات والأعمال الأصلية عبر شاهد VIP لمدة شهر كامل بدون إعلانات وبأعلى جودة.", "icon": "🍿"}, {"id": "p60uwq", "name": "نتفليكس حساب كامل", "category": "اشتراكات الأفلام والمسلسلات", "price": "45.00 ر.س", "badge": "حساب 5 ملفات 👑", "rating": "5.0 (64 تقييم)", "desc": "حساب نتفليكس كامل خاص بك يحتوي على 5 ملفات شخصية مناسب للعائلة أو الأصدقاء بجودة 4K فائقة.", "icon": "📺"}, {"id": "pe4nuq", "name": "شاهد VIP حساب كامل", "category": "اشتراكات الأفلام والمسلسلات", "price": "26.00 ر.س", "badge": "حساب عائلي ✨", "rating": "4.9 (42 تقييم)", "desc": "حساب كامل يتضمن 5 ملفات شخصية، بدون إعلانات، يدعم التحميل والمشاهدة على التلفزيون والجوال.", "icon": "🌟"}, {"id": "p089fq", "name": "سناب شات بلس (3 شهور)", "category": "اشتراكات السوشيال ميديا", "price": "26.00 ر.س", "badge": "مميز 🔥", "rating": "5.0 (110 تقييم)", "desc": "اشتراك رسمي من Snapchat بنسبة 100%، يمنحك شارة النجمة بجانب اسمك، تثبيت المحادثات، ومزايا حصرية.", "icon": "👻"}, {"id": "p4wlhz", "name": "سناب شات بلس (سنة كاملة)", "category": "اشتراكات السوشيال ميديا", "price": "95.00 ر.س", "badge": "توفير سنوي 💎", "rating": "5.0 (78 تقييم)", "desc": "اشتراك سنوي رسمي بالكامل مع كافة تحديثات ومزايا سناب بلس الحصرية وتسليم فوري ومباشر.", "icon": "👑"}, {"id": "pwy4rc", "name": "مفتاح ويندوز 11 برو — مدى الحياة", "category": "البرامج وتراخيص ويندوز", "price": "27.00 ر.س", "badge": "تفعيل دائم 🔑", "rating": "5.0 (230 تقييم)", "desc": "مفتاح أصلي 100% يمنحك تفعيلاً دائماً لجميع ميزات ويندوز 11 برو مع التحديثات الأمنية الرسمية مدى الحياة.", "icon": "💻"}]

filtered_products = []
for p in products:
    if cat_filter != "الكل" and p["category"] != cat_filter:
        continue
    if search_q.strip() and search_q.strip().lower() not in p["name"].lower() and search_q.strip().lower() not in p["desc"].lower():
        continue
    filtered_products.append(p)

st.markdown(f"<h3 style='margin: 22px 0 16px 0; color: #fff;'>✨ الخدمات المتوفرة ({len(filtered_products)} منتج)</h3>", unsafe_allow_html=True)

# Render 3 columns grid
cols = st.columns(3)
for idx, prod in enumerate(filtered_products):
    with cols[idx % 3]:
        st.markdown(f'''
<div class="product-card">
    <div>
        <div class="card-top">
            <span class="product-icon">{prod['icon']}</span>
            <span class="product-badge">{prod['badge']}</span>
        </div>
        <div class="product-name">{prod['name']}</div>
        <div class="product-desc">{prod['desc']}</div>
    </div>
    <div>
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 12px;">
            <div>
                <div class="product-price">{prod['price']}</div>
                <div class="product-rating">⭐ {prod['rating']}</div>
            </div>
            <div style="font-size: 0.8rem; color: #4ade80; font-weight: 600;">متوفر فوري ✅</div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)
        if st.button(f"🛒 طلب الآن — {prod['name']}", key=f"btn_buy_{prod['id']}"):
            st.session_state["selected_product"] = prod

# 6. Checkout Modal Simulation
if st.session_state.get("selected_product"):
    p_sel = st.session_state["selected_product"]
    st.markdown("---")
    st.markdown(f'''
<div style="background: rgba(30, 27, 75, 0.95); border: 1px solid #6253ec; border-radius: 20px; padding: 26px; margin: 20px 0;">
    <h3 style="margin-top: 0; color: #fff;">🛍️ إتمام طلب: {p_sel['name']}</h3>
    <p style="color: #94a3b8; font-size: 0.95rem;">رقم الطلب المؤقت: <strong style="color: #38bdf8;">{st.session_state['order_id']}</strong> | السعر: <strong style="color: #4ade80;">{p_sel['price']}</strong></p>
</div>
''', unsafe_allow_html=True)
    
    with st.form("checkout_form"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            u_email = st.text_input("البريد الإلكتروني (لاستلام كود التفعيل):", placeholder="example@email.com")
        with col_f2:
            u_discord = st.text_input("اسم حسابك في الديسكورد (Discord Username):", placeholder="username#0000")
        
        pay_method = st.radio("اختر طريقة الدفع:", ["💳 بطاقة مدى / فيزا (Mada / Visa)", "🍎 Apple Pay", "🪙 عملات رقمية (USDT)", "🎮 تحويل رصيد ديسكورد"], horizontal=True)
        
        col_sub1, col_sub2 = st.columns([2, 1])
        with col_sub1:
            confirm_btn = st.form_submit_button("✅ تأكيد الشراء والتسليم الفوري", use_container_width=True)
        with col_sub2:
            cancel_btn = st.form_submit_button("❌ إلغاء", use_container_width=True)
            
        if confirm_btn:
            if u_email.strip():
                st.balloons()
                st.success(f"🎉 تم تسجيل طلبك بنجاح! رقم الطلب: `{st.session_state['order_id']}`. تم إرسال تفاصيل التفعيل لبريدك الإلكتروني `{u_email}`.")
                st.info("✅ يمكنك فتح تذكرة (Ticket) في سيرفر الديسكورد برقم الطلب للحصول على دعم فوري ومباشر.")
            else:
                st.warning("⚠️ يرجى كتابة البريد الإلكتروني لاستلام المنتج.")

# 7. Store Footer
st.markdown(f'''
<div class="store-footer">
    <p style="margin: 0 0 8px 0; font-weight: 600; color: #cbd5e1;">⚡ LAX Store — جميع الحقوق محفوظة © 2026</p>
    <p style="margin: 0; font-size: 0.8rem;">رقم الجلسة: <code>{st.session_state['order_id']}</code> • سرعة التسليم: ⚡ فوري تلقائي</p>
</div>
''', unsafe_allow_html=True)
