# volatility_engine.py

from timeframe_store import candles_1m

# =========================
# VOLATILITY
# =========================

def calculate_volatility(

    symbol

):

    if symbol not in candles_1m:

        return 0

    candles = list(

        candles_1m[symbol].values()

    )

    if len(candles) < 10:

        return 0

    moves = []

    for candle in candles[-10:]:

        move = abs(

            candle["high"]

            - candle["low"]

        )

        moves.append(move)

    volatility = (

        sum(moves)

        / len(moves)

    )

    return round(

        volatility,

        2

    )