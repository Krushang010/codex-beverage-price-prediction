# =============================================================================
# ui.py — All UI rendering functions
# CodeX Beverage Price Range Predictor
# =============================================================================

import streamlit as st
from config import PRICE_LABELS


# ── CSS ───────────────────────────────────────────────────────────────────────

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background-color: #f0f2f8; }

    .hero-banner {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 16px; padding: 2.2rem 2.5rem;
        margin-bottom: 1.5rem; color: white;
    }
    .hero-banner h1 { font-size: 2rem; font-weight: 700; margin: 0; letter-spacing: -0.5px; }
    .hero-banner p  { font-size: 0.92rem; opacity: 0.65; margin: 0.35rem 0 0; }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 20px; padding: 3px 12px;
        font-size: 0.68rem; font-weight: 600;
        margin-bottom: 0.75rem; letter-spacing: 1.5px; text-transform: uppercase;
    }
    .section-header {
        font-size: 0.67rem; font-weight: 700; letter-spacing: 1.8px;
        text-transform: uppercase; color: #7c8db5;
        padding: 0.5rem 0; margin-bottom: 0.25rem;
        border-bottom: 1px solid #e4e8f4;
    }
    .result-box {
        background: linear-gradient(135deg, #0f3460 0%, #1a73e8 100%);
        border-radius: 16px; padding: 2.2rem 1.5rem;
        text-align: center; color: white; margin-bottom: 1rem;
    }
    .result-label { font-size: 0.72rem; opacity: 0.7; text-transform: uppercase; letter-spacing: 1.2px; }
    .result-price { font-size: 3.4rem; font-weight: 700; margin: 0.35rem 0; letter-spacing: -1px; }
    .result-conf  { font-size: 0.88rem; opacity: 0.8; }
    .conf-row { display: flex; align-items: center; gap: 10px; margin-bottom: 9px; }
    .conf-label { font-size: 0.8rem; font-weight: 500; color: #333; min-width: 82px; }
    .conf-bar-bg { flex: 1; background: #e8ecf8; border-radius: 99px; height: 7px; }
    .conf-bar { height: 7px; border-radius: 99px; background: linear-gradient(90deg, #0f3460, #1a73e8); }
    .conf-pct { font-size: 0.77rem; font-weight: 600; color: #0f3460; min-width: 40px; text-align: right; }
    .placeholder-box {
        text-align: center; padding: 4rem 1rem;
        background: #f8f9fc; border-radius: 14px;
        border: 1.5px dashed #d0d8ee;
    }
    </style>
    """, unsafe_allow_html=True)


# ── Hero Banner ───────────────────────────────────────────────────────────────

def render_hero():
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">🧃 CodeX Beverage Intelligence</div>
        <h1>Price Range Predictor</h1>
        <p>ML-powered consumer price segmentation</p>
    </div>
    """, unsafe_allow_html=True)


# ── Input Form ────────────────────────────────────────────────────────────────

def render_input_form():
    """Renders the full input form. Returns a dict of all user inputs."""
    from config import (
        GENDER_OPTIONS, ZONE_OPTIONS, OCCUPATION_OPTIONS,
        INCOME_OPTIONS, FREQ_OPTIONS, BRAND_OPTIONS, SIZE_OPTIONS,
        AWARENESS_OPTIONS, REASONS_OPTIONS, FLAVOR_OPTIONS,
        CHANNEL_OPTIONS, PACKAGING_OPTIONS, HEALTH_OPTIONS, SITUATION_OPTIONS
    )

    st.markdown('<div class="section-header">👤 Demographics</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    age        = c1.number_input("Age", 18, 70, 28, 1)
    gender     = c2.selectbox("Gender", GENDER_OPTIONS)
    zone       = c3.selectbox("Zone", ZONE_OPTIONS)
    occupation = c4.selectbox("Occupation", OCCUPATION_OPTIONS)

    st.markdown('<div class="section-header" style="margin-top:1.2rem;">💰 Financial Profile</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    income            = c1.selectbox("Income Level (In L)", INCOME_OPTIONS)
    consume_frequency = c2.selectbox("Consume Frequency (Weekly)", FREQ_OPTIONS)

    st.markdown('<div class="section-header" style="margin-top:1.2rem;">🏷️ Brand & Product Preferences</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    current_brand = c1.selectbox("Current Brand",  BRAND_OPTIONS)
    size          = c2.selectbox("Preferable Size", SIZE_OPTIONS)
    awareness     = c3.selectbox("Brand Awareness", AWARENESS_OPTIONS)
    c1, c2, c3 = st.columns(3)
    reasons = c1.selectbox("Reason for Choosing", REASONS_OPTIONS)
    flavor  = c2.selectbox("Flavor Preference",   FLAVOR_OPTIONS)
    channel = c3.selectbox("Purchase Channel",    CHANNEL_OPTIONS)

    st.markdown('<div class="section-header" style="margin-top:1.2rem;">🌿 Lifestyle & Health</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    packaging = c1.selectbox("Packaging",            PACKAGING_OPTIONS)
    health    = c2.selectbox("Health Concerns",      HEALTH_OPTIONS)
    situation = c3.selectbox("Consumption Situation", SITUATION_OPTIONS)

    st.markdown("<br>", unsafe_allow_html=True)
    predict_clicked = st.button(
        "🔮  Predict Price Range",
        use_container_width=True,
        type="primary"
    )

    return dict(
        age=age, gender=gender, zone=zone, occupation=occupation,
        income=income, consume_frequency=consume_frequency,
        current_brand=current_brand, size=size, awareness=awareness,
        reasons=reasons, flavor=flavor, channel=channel,
        packaging=packaging, health=health, situation=situation
    ), predict_clicked


# ── Result Panel ──────────────────────────────────────────────────────────────

def render_placeholder():
    st.markdown('<div class="section-header">📊 Prediction Result</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="placeholder-box">
        <div style="font-size:2.8rem;">🔮</div>
        <div style="font-size:0.95rem; font-weight:500; color:#555; margin-top:0.75rem;">
            Fill in the consumer profile<br>and click <strong>Predict Price Range</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_result(label: str, confidence: float, prob: list,
                  pred_class: int, demo_mode: bool):
    st.markdown('<div class="section-header">📊 Prediction Result</div>', unsafe_allow_html=True)

    if demo_mode:
        st.caption("⚠️ Demo mode — lgbm_model.pkl not found")

    # Main result box
    st.markdown(f"""
    <div class="result-box">
        <div class="result-label">Predicted Price Range</div>
        <div class="result-price">{label}</div>
        <div class="result-conf">Confidence: {confidence:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

    # Confidence bars
    bars_html = '<div style="margin: 0.25rem 0 0.5rem;">'
    for i, (lbl, p) in enumerate(zip(PRICE_LABELS.values(), prob)):
        pct   = p * 100
        style = "font-weight:700; color:#0f3460;" if i == pred_class else "color:#666;"
        bars_html += f"""
        <div class="conf-row">
            <div class="conf-label" style="{style}">{lbl}</div>
            <div class="conf-bar-bg">
                <div class="conf-bar" style="width:{pct:.1f}%"></div>
            </div>
            <div class="conf-pct">{pct:.1f}%</div>
        </div>"""
    bars_html += '</div>'
    st.markdown(bars_html, unsafe_allow_html=True)
