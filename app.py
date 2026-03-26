# =============================================================================
# app.py — Main entry point
# CodeX Beverage Price Range Predictor
#
# Run with: streamlit run app.py
# =============================================================================

import streamlit as st

from ui import inject_css, render_hero, render_input_form, render_placeholder, render_result
from model_utils import predict

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CodeX | Price Predictor",
    page_icon="🧃",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Inject Styles ─────────────────────────────────────────────────────────────
inject_css()

# ── Hero Banner ───────────────────────────────────────────────────────────────
render_hero()

# ── Two Column Layout ─────────────────────────────────────────────────────────
left_col, right_col = st.columns([3, 2], gap="large")

with left_col:
    inputs, predict_clicked = render_input_form()

with right_col:
    label, confidence, prob, pred_class, demo_mode = predict(inputs)
    render_result(label, confidence, prob, pred_class, demo_mode)
