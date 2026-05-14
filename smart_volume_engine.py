# smart_volume_engine.py

from volume_engine import (
    calculate_relative_volume
)

# =========================
# SMART VOLUME
# =========================

def get_smart_volume_signal(

    symbol

):

    rel_volume = (

        calculate_relative_volume(

            symbol

        )

    )

    if rel_volume >= 3:

        return "ULTRA VOLUME"

    if rel_volume >= 2:

        return "HIGH VOLUME"

    if rel_volume >= 1.2:

        return "GOOD VOLUME"

    return "LOW VOLUME"