# risk_engine.py

# =========================
# RISK SCORE
# =========================

def calculate_risk(

    volatility,
    probability

):

    risk = volatility * 2

    risk -= probability / 20

    return round(risk, 2)