# opening_range_engine.py

from opening_memory import (
    opening_memory
)

# =========================
# OPENING RANGE
# =========================

def get_opening_range(

    symbol

):

    if symbol not in opening_memory:

        return {}

    data = opening_memory[symbol]

    return {

        "opening_high":

        data["opening_high"],

        "opening_low":

        data["opening_low"],

        "opening_vwap":

        data["opening_vwap"]

    }