# institutional_engine.py

from volume_engine import (
    calculate_relative_volume
)

from momentum_engine import (
    calculate_momentum
)

from market_trend_engine import (
    get_market_trend
)

# =========================
# INSTITUTIONAL ACTIVITY
# =========================

def detect_institutional_activity(

    symbol

):

    rel_volume = (

        calculate_relative_volume(

            symbol

        )

    )

    momentum = (

        calculate_momentum(

            symbol

        )

    )

    market = (

        get_market_trend()

    )

    market_trend = market.get(

        "trend",

        "SIDEWAYS"

    )

    score = 0

    # =====================
    # VOLUME
    # =====================

    if rel_volume >= 2:

        score += 4

    elif rel_volume >= 1.5:

        score += 2

    # =====================
    # MOMENTUM
    # =====================

    if momentum >= 1:

        score += 3

    elif momentum <= -1:

        score -= 3

    # =====================
    # MARKET
    # =====================

    if market_trend == "BULLISH":

        score += 2

    elif market_trend == "BEARISH":

        score -= 2

    signal = "NEUTRAL"

    if score >= 5:

        signal = "INSTITUTIONAL BUYING"

    elif score <= -5:

        signal = "INSTITUTIONAL SELLING"

    return {

        "score": score,

        "signal": signal

    }