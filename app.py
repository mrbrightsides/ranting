import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RANTAI Inggris",
    page_icon="🍀",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **RANTING (RANTAI Inggris)** is not just another English learning app.  
    It is a playful yet structured journey to master English – designed to feel like a game, but built on serious educational principles.
    
    With RANTING, you can:
    - Start from zero and reach fluency step by step.
    - Learn grammar, vocabulary, and conversation in a fun way.
    - Practice through real-life scenarios and mini challenges.
    - Collect badges, streaks, and achievements as you grow.

    We believe that learning English should feel less like homework 📚 and more like an adventure 🎮.  
    That’s why RANTING mixes **education, gamification, and community spirit**.
    
    ---
    #### 🔮 Vision Statement
    
    RANTING (RANTAI Inggris) is born from a simple belief:  
    **language is a bridge, and English is a key to global collaboration.**
    
    Our vision is to:
    1. Make English learning **accessible, fun, and motivating** for everyone.
    2. Transform the way people see language learning – from memorization to meaningful use.
    3. Connect learners into a larger **ecosystem of innovation (RANTAI)**, where knowledge, technology, and action meet.
    4. Grow with the community – from individuals improving their skills to a network of changemakers.
    
    ## 💡 Why RANTING?
    - Because we are part of **RANTAI** – Research, Action, Network, Technology, Application, Innovation.
    - Because every branch (*ranting* in Bahasa Indonesia 🌱) grows from a strong root, and English is one branch that empowers us to connect globally.
    - Because learning should be a **journey of growth**, not just a task.

    ---
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/ranting)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

iframe_url = "https://ranting.elpeef.com/"

embed_iframe(iframe_url, hide_top_px=40, hide_bottom_px = -145, height=800)
