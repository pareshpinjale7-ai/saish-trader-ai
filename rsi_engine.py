# rsi_engine.py

from timeframe_store import candles_5m

# =========================
# RSI
# =========================

def calculate_rsi(

    symbol,

    period=14

):

    if symbol not in candles_5m:

        return 50

    candles = list(

        candles_5m[symbol].values()

    )

    if len(candles) < period + 1:

        return 50

    closes = [

        c["close"]

        for c in candles

    ]

    gains = []
    losses = []

    for i in range(

        1,

        len(closes)

    ):

        diff = (

            closes[i]

            - closes[i - 1]

        )

        if diff > 0:

            gains.append(diff)

        else:

            losses.append(abs(diff))

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:

        return 100

    rs = avg_gain / avg_loss

    rsi = (

        100

        - (

            100 / (1 + rs)

        )

    )

    return round(rsi, 2)