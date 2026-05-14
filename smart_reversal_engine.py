# smart_reversal_engine.py

from reversal_engine import (
    detect_reversal
)

from rsi_engine import (
    calculate_rsi
)

# =========================
# SMART REVERSAL
# =========================

def detect_smart_reversal(

    symbol

):

    reversal = (

        detect_reversal(

            symbol

        )

    )

    rsi = (

        calculate_rsi(

            symbol

        )

    )

    signal = reversal["signal"]

    if (

        signal ==

        "BULLISH REVERSAL"

        and

        rsi < 40

    ):

        return "HIGH BULLISH REVERSAL"

    if (

        signal ==

        "BEARISH REVERSAL"

        and

        rsi > 60

    ):

        return "HIGH BEARISH REVERSAL"

    return "NO REVERSAL"