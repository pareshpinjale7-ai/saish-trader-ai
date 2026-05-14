# sector_trend_engine.py

from sector_map import SECTOR_MAP

from live_cache import (
    live_market_data
)

# =========================
# SECTOR STRENGTH
# =========================

def get_sector_trend():

    result = []

    for sector, stocks in SECTOR_MAP.items():

        total = 0
        count = 0

        for symbol in stocks:

            if symbol in live_market_data:

                change = live_market_data[
                    symbol
                ].get(

                    "change_percent",

                    0

                )

                total += change

                count += 1

        if count == 0:

            continue

        avg = total / count

        result.append({

            "sector": sector,

            "strength": round(

                avg,

                2

            )

        })

    result.sort(

        key=lambda x:

        x["strength"],

        reverse=True

    )

    return result