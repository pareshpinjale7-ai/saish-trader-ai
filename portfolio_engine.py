# portfolio_engine.py

# =========================
# POSITION SIZE
# =========================

def calculate_position_size(

    capital,
    risk_percent,
    stoploss_percent

):

    risk_amount = (

        capital * risk_percent

    ) / 100

    if stoploss_percent == 0:

        return 0

    size = (

        risk_amount / stoploss_percent

    )

    return round(size, 2)