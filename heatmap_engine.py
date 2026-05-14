# heatmap_engine.py

from sector_trend_engine import (
    get_sector_trend
)

# =========================
# HEATMAP
# =========================

def get_heatmap():

    sectors = (

        get_sector_trend()

    )

    heatmap = []

    for sector in sectors:

        strength = sector["strength"]

        color = "GREEN"

        if strength < 0:

            color = "RED"

        heatmap.append({

            "sector":

            sector["sector"],

            "strength":

            strength,

            "color":

            color

        })

    return heatmap