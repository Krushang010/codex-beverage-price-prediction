# =============================================================================
# model_utils.py — Model loading, feature engineering, prediction logic
# CodeX Beverage Price Range Predictor
# =============================================================================

import pickle
import os
import pandas as pd
import streamlit as st

from config import (
    AGE_GROUP_MAP, INCOME_MAP, HEALTH_MAP, FREQ_MAP,
    SIZE_MAP, AWARENESS_MAP, ZONE_SCORE_MAP, PRICE_LABELS
)


# ── Age Group Helper ──────────────────────────────────────────────────────────

def get_age_group(age: int) -> str:
    """Map a raw age integer to its age group bucket."""
    if age <= 25:   return '18-25'
    elif age <= 35: return '26-35'
    elif age <= 45: return '36-45'
    elif age <= 55: return '46-55'
    else:           return '56-70'


# ── Feature Engineering ───────────────────────────────────────────────────────

def engineer_features(inp: dict) -> dict:
    """
    Replicate the full feature engineering pipeline from training:
    - Age group binning
    - CF-AB score (consume frequency / awareness ratio)
    - ZAS score (zone × income)
    - BSI (brand switching indicator)
    """
    age_group   = get_age_group(inp['age'])
    freq_score  = FREQ_MAP[inp['consume_frequency']]
    aware_score = AWARENESS_MAP[inp['awareness']]
    cf_ab_score = round(freq_score / (freq_score + aware_score), 2)
    zas_score   = ZONE_SCORE_MAP[inp['zone']] * INCOME_MAP[inp['income']]
    bsi         = int(
        inp['current_brand'] != 'Established' and
        inp['reasons'] in ['Price', 'Quality']
    )
    return {
        'age_group':   age_group,
        'cf_ab_score': cf_ab_score,
        'zas_score':   zas_score,
        'bsi':         bsi
    }


# ── Input Vector Builder ──────────────────────────────────────────────────────

def build_input_vector(inp: dict) -> pd.DataFrame:
    """
    Convert raw user inputs into the encoded feature vector
    that matches the training pipeline exactly.
    """
    feats = engineer_features(inp)

    row = {
        # Label-encoded columns
        'age_group'                  : AGE_GROUP_MAP[feats['age_group']],
        'income_levels'              : INCOME_MAP[inp['income']],
        'consume_frequency(weekly)'  : FREQ_MAP[inp['consume_frequency']],
        'preferable_consumption_size': SIZE_MAP[inp['size']],
        'health_concerns'            : HEALTH_MAP[inp['health']],
        'cf_ab_score'                : feats['cf_ab_score'],
        'zas_score'                  : feats['zas_score'],
        'bsi'                        : feats['bsi'],

        # One-hot encoded columns
        'gender_M'                   : 1 if inp['gender'] == 'M' else 0,
        'zone_Metro'                 : 1 if inp['zone'] == 'Metro' else 0,
        'zone_Rural'                 : 1 if inp['zone'] == 'Rural' else 0,
        'zone_Semi-Urban'            : 1 if inp['zone'] == 'Semi-Urban' else 0,
        'zone_Urban'                 : 1 if inp['zone'] == 'Urban' else 0,
        'occupation_Entrepreneur'    : 1 if inp['occupation'] == 'Entrepreneur' else 0,
        'occupation_Retired'         : 1 if inp['occupation'] == 'Retired' else 0,
        'occupation_Student'         : 1 if inp['occupation'] == 'Student' else 0,
        'occupation_Working_Professional'             : 1 if inp['occupation'] == 'Working Professional' else 0,
        'current_brand_Newcomer'                      : 1 if inp['current_brand'] == 'Newcomer' else 0,
        'awareness_of_other_brands_2_to_4'            : 1 if inp['awareness'] == '2 to 4' else 0,
        'awareness_of_other_brands_above_4'           : 1 if inp['awareness'] == 'above 4' else 0,
        'reasons_for_choosing_brands_Availability'    : 1 if inp['reasons'] == 'Availability' else 0,
        'reasons_for_choosing_brands_Brand_Reputation': 1 if inp['reasons'] == 'Brand Reputation' else 0,
        'reasons_for_choosing_brands_Price'           : 1 if inp['reasons'] == 'Price' else 0,
        'reasons_for_choosing_brands_Quality'         : 1 if inp['reasons'] == 'Quality' else 0,
        'flavor_preference_Exotic'                    : 1 if inp['flavor'] == 'Exotic' else 0,
        'flavor_preference_Traditional'               : 1 if inp['flavor'] == 'Traditional' else 0,
        'purchase_channel_Retail_Store'               : 1 if inp['channel'] == 'Retail Store' else 0,
        'packaging_preference_Premium'                : 1 if inp['packaging'] == 'Premium' else 0,
        'packaging_preference_Simple'                 : 1 if inp['packaging'] == 'Simple' else 0,
        'typical_consumption_situations_Casual_(eg._At_home)': 1 if inp['situation'] == 'Casual (eg. At home)' else 0,
        'typical_consumption_situations_Social_(eg._Parties)': 1 if inp['situation'] == 'Social (eg. Parties)' else 0,
    }
    return pd.DataFrame([row])


# ── Model Loader ──────────────────────────────────────────────────────────────

@st.cache_resource
def load_model():
    """Load the trained LightGBM model from disk. Cached after first load."""
    from config import MODEL_PATH
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            return pickle.load(f)
    return None


# ── Prediction ────────────────────────────────────────────────────────────────

def predict(inp: dict) -> tuple:
    """
    Run the full prediction pipeline.
    Returns: (predicted_label, confidence_pct, prob_list, is_demo_mode)
    """
    model    = load_model()
    input_df = build_input_vector(inp)
    demo_mode = model is None

    if model is not None:
        # Align columns to exactly match training feature order
        model_cols = model.booster_.feature_name()
        for col in model_cols:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df   = input_df[model_cols]
        pred_class = int(model.predict(input_df)[0])
        prob       = list(model.predict_proba(input_df)[0])
    else:
        # Demo mode fallback — rule-based approximation
        feats      = engineer_features(inp)
        score      = feats['zas_score'] + FREQ_MAP[inp['consume_frequency']]
        pred_class = min(3, max(0, score // 5))
        base       = [0.08, 0.22, 0.35, 0.35]
        base[pred_class] += 0.25
        t    = sum(base)
        prob = [v / t for v in base]

    label      = PRICE_LABELS[pred_class]
    confidence = prob[pred_class] * 100

    return label, confidence, prob, pred_class, demo_mode
