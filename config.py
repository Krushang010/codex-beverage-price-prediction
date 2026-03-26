# =============================================================================
# config.py — All constants, encoding maps, and feature definitions
# CodeX Beverage Price Range Predictor
# =============================================================================

# ── Encoding Maps (must match training pipeline exactly) ──────────────────────

AGE_GROUP_MAP = {
    '18-25': 1,
    '26-35': 2,
    '36-45': 3,
    '46-55': 4,
    '56-70': 5,
    '70+':   6
}

INCOME_MAP = {
    'Not Reported': 0,
    '<10L':         1,
    '10L - 15L':    2,
    '16L - 25L':    3,
    '26L - 35L':    4,
    '> 35L':        5
}

HEALTH_MAP = {
    'Low (Not very concerned)':             1,
    'Medium (Moderately health-conscious)': 2,
    'High (Very health-conscious)':         3
}

FREQ_MAP = {
    '0-2 times': 1,
    '3-4 times': 2,
    '5-7 times': 3
}

SIZE_MAP = {
    'Small (250 ml)':  1,
    'Medium (500 ml)': 2,
    'Large (1 L)':     3
}

AWARENESS_MAP = {
    '0 to 1':  1,
    '2 to 4':  2,
    'above 4': 3
}

ZONE_SCORE_MAP = {
    'Rural':      1,
    'Semi-Urban': 2,
    'Urban':      3,
    'Metro':      4
}

# ── Target Label Map ──────────────────────────────────────────────────────────

PRICE_LABELS = {
    0: '₹50–100',
    1: '₹100–150',
    2: '₹150–200',
    3: '₹200–250'
}

# ── Dropdown Options ──────────────────────────────────────────────────────────

GENDER_OPTIONS     = ['M', 'F']
ZONE_OPTIONS       = ['Metro', 'Urban', 'Semi-Urban', 'Rural']
OCCUPATION_OPTIONS = ['Working Professional', 'Student', 'Entrepreneur', 'Retired']
INCOME_OPTIONS     = ['<10L', '10L - 15L', '16L - 25L', '26L - 35L', '> 35L', 'Not Reported']
FREQ_OPTIONS       = ['0-2 times', '3-4 times', '5-7 times']
BRAND_OPTIONS      = ['Newcomer', 'Established']
SIZE_OPTIONS       = ['Small (250 ml)', 'Medium (500 ml)', 'Large (1 L)']
AWARENESS_OPTIONS  = ['0 to 1', '2 to 4', 'above 4']
REASONS_OPTIONS    = ['Price', 'Quality', 'Availability', 'Brand Reputation']
FLAVOR_OPTIONS     = ['Traditional', 'Exotic']
CHANNEL_OPTIONS    = ['Online', 'Retail Store']
PACKAGING_OPTIONS  = ['Simple', 'Premium', 'Eco-Friendly']
HEALTH_OPTIONS     = [
    'Low (Not very concerned)',
    'Medium (Moderately health-conscious)',
    'High (Very health-conscious)'
]
SITUATION_OPTIONS  = [
    'Active (eg. Sports, gym)',
    'Social (eg. Parties)',
    'Casual (eg. At home)'
]

# ── Model File Path ───────────────────────────────────────────────────────────

MODEL_PATH = 'lgbm_model.pkl'
