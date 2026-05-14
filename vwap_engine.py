# vwap_engine.py

from timeframe_store import candles_1m

# =========================
# VWAP CALCULATOR
# =========================

def calculate_vwap(symbol):

    if symbol not in candles_1m:

        return None

    candles = list(

        candles_1m[symbol].values()

    )

    total_price_volume = 0
    total_volume = 0

    for candle in candles:

        high = candle["high"]
        low = candle["low"]
        close = candle["close"]
        volume = candle["volume"]

        typical_price = (

            high + low + close

        ) / 3

        total_price_volume += (

            typical_price * volume

        )

        total_volume += volume

    if total_volume == 0:

        return None

    vwap = (

        total_price_volume

        / total_volume

    )

    return round(vwap, 2)

# =========================
# VWAP STATUS
# =========================

def get_vwap_signal(

    symbol,

    ltp

):

    vwap = calculate_vwap(

        symbol

    )

    if not vwap:

        return {

            "vwap": None,

            "signal": "NO DATA"

        }

    signal = "ABOVE VWAP"

    if ltp < vwap:

        signal = "BELOW VWAP"

    return {

        "vwap": vwap,

        "signal": signal

    }