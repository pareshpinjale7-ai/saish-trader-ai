# volume_engine.py

from timeframe_store import candles_1m

# =========================
# RELATIVE VOLUME
# =========================

def calculate_relative_volume(

    symbol

):

    if symbol not in candles_1m:

        return 0

    candles = list(

        candles_1m[symbol].values()

    )

    if len(candles) < 5:

        return 0

    latest = candles[-1]

    latest_volume = latest["volume"]

    avg_volume = sum(

        c["volume"]

        for c in candles[:-1]

    ) / max(

        len(candles[:-1]),

        1

    )

    if avg_volume == 0:

        return 0

    rel_volume = (

        latest_volume / avg_volume

    )

    return round(

        rel_volume,

        2

    )

# =========================
# VOLUME BURST
# =========================

def is_volume_burst(symbol):

    rv = calculate_relative_volume(

        symbol

    )

    return rv >= 2