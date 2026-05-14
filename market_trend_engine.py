# market_trend_engine.py

from live_cache import (
    live_market_data
)

# =========================
# MARKET TREND
# =========================

def get_market_trend():

    bullish = 0
    bearish = 0

    for symbol, data in live_market_data.items():

        chg = data.get(

            "change_percent",

            0

        )

        if chg > 0:

            bullish += 1

        elif chg < 0:

            bearish += 1

    total = bullish + bearish

    if total == 0:

        return {

            "trend":

            "SIDEWAYS"

        }

    bullish_ratio = (

        bullish / total

    ) * 100

    if bullish_ratio > 60:

        trend = "BULLISH"

    elif bullish_ratio < 40:

        trend = "BEARISH"

    else:

        trend = "SIDEWAYS"

    return {

        "trend": trend,

        "bullish": bullish,

        "bearish": bearish

    }