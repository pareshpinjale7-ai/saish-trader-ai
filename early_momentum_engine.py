# early_momentum_engine.py

from opening_memory import (
    opening_memory
)

# =========================
# EARLY MOMENTUM
# =========================

def detect_early_momentum(

    symbol,
    ltp

):

    if symbol not in opening_memory:

        return 0

    opening_low = opening_memory[
        symbol
    ]["opening_low"]

    if opening_low == 0:

        return 0

    momentum = (

        (ltp - opening_low)

        / opening_low

    ) * 100

    return round(momentum, 2)