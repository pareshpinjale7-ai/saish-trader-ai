# candle_pattern_engine.py

from timeframe_store import candles_5m

# =========================
# CANDLE PATTERN
# =========================

def detect_candle_pattern(

    symbol

):

    if symbol not in candles_5m:

        return "NO DATA"

    candles = list(

        candles_5m[symbol].values()

    )

    if len(candles) < 1:

        return "NO DATA"

    candle = candles[-1]

    body = abs(

        candle["close"]

        - candle["open"]

    )

    full = abs(

        candle["high"]

        - candle["low"]

    )

    if full == 0:

        return "DOJI"

    body_percent = (

        body / full

    ) * 100

    if body_percent > 70:

        if candle["close"] > candle["open"]:

            return "BIG BULLISH"

        else:

            return "BIG BEARISH"

    if body_percent < 20:

        return "DOJI"

    return "NORMAL"