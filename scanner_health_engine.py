# scanner_health_engine.py

from live_cache import (
    live_market_data
)

# =========================
# HEALTH CHECK
# =========================

def get_scanner_health():

    total = len(

        live_market_data

    )

    active = 0

    for symbol, data in live_market_data.items():

        if data.get(

            "ltp",

            0

        ) > 0:

            active += 1

    return {

        "total_symbols": total,

        "active_symbols": active,

        "status": "RUNNING"

    }