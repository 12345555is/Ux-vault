import streamlit as st
import pandas as pd
import datetime

# --- CONFIGURATION & UX STYLE ---
st.set_page_config(page_title="UX Strategy Engine", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background: linear-gradient(180deg, #111111 0%, #1a1a1a 100%); color: #ffffff; }
    .stMetric { background: #262626; padding: 15px; border-radius: 12px; border: 1px solid #3e3e3e; }
    div.stButton > button {
        background: linear-gradient(90deg, #00C6FF 0%, #0072FF 100%);
        color: white; border: none; padding: 12px 30px; border-radius: 8px;
        font-weight: bold; width: 100%; transition: 0.3s;
    }
    div.stButton > button:hover { transform: scale(1.02); box-shadow: 0px 4px 15px rgba(0, 114, 255, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- BACKEND LOGIC ---
def get_strategic_score(impact, alignment, effort):
    # נוסחת ROI קלאסית מעולם ה-Product Management
    # $Score = \frac{Impact \times Alignment}{Effort}$
    score = (impact * alignment) / (effort if effort > 0 else 1)
    return round(score, 2)

# --- UI LAYOUT ---
st.title("💎 UX Strategic Decision Engine")
st.markdown("---")

col_input, col_display = st.columns([1, 2])

with col_input:
    st.subheader("⚙️ הפרמטרים")
    with st.container():
        title = st.text_input("שם ההחלטה האסטרטגית", "למשל: אינטגרציית AI לממשק")
        category = st.selectbox("קטגוריה", ["UI Design", "Research", "System Architecture", "Business Strategy"])
        
        st.write("ציונים אסטרטגיים (1-10):")
        impact = st.select_slider("אימפקט על המשתמש (Impact)", options=range(1, 11), value=5)
        align = st.select_slider("הלימה ליעדי החברה (Alignment)", options=range(1, 11), value=5)
        effort = st.select_slider("מורכבות פיתוח וזמן (Effort)", options=range(1, 11), value=3)
        
        pre_mortem = st.text_area("⚠️ ניתוח סיכונים (Pre-Mortem)", "מה יגרום לזה להיכשל?")
        
        submit = st.button("בצע אנליזה ושמור")

with col_display:
    st.subheader("📊 ניתוח החלטה בזמן אמת")
    score = get_strategic_score(impact, align, effort)
    
    # הצגת המדד המרכזי
    c1, c2, c3 = st.columns(3)
    c1.metric("Strategic Score", f"{score}/100")
    
    status = "🚀 High Priority" if score > 15 else "⏳ Backlog" if score < 5 else "✅ Consider"
    c2.metric("מצב המשימה", status)
    
    priority_color = "#00FF00" if score > 15 else "#FF4B4B" if score < 5 else "#FFA500"
    
    if submit:
        st.success(f"ההחלטה '{title}' נשמרה בהצלחה!")
        st.balloons()
        
        # הדמיית דאשבורד יוקרתי
        df = pd.DataFrame({
            "Metric": ["Impact", "Alignment", "Effort"],
            "Value": [impact, align, effort]
        })
        st.bar_chart(df.set_index("Metric"))
        
        st.markdown(f"""
        > **סיכום אדריכלי:** ההחלטה מסוג **{category}** קיבלה ציון של **{score}**. 
        > ניתוח הסיכונים מציין ש: *{pre_mortem}*.
        """)

st.markdown("---")
st.caption("Developed with ❤️ for Mom | Version 2.0 (Ultra-Professional)")
