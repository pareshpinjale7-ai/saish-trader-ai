# live_cache.py

# =========================
# LIVE MARKET CACHE
# =========================

live_market_data = {}

# =========================
# UPDATE CACHE
# =========================

def update_live_data(

    symbol,

    ltp,

    volume,

    change_percent=0,

    oi=0,

    bid_qty=0,

    ask_qty=0

):

    live_market_data[symbol] = {

        "ltp": ltp,

        "volume": volume,

        "change_percent": change_percent,

        "oi": oi,

        "bid_qty": bid_qty,

        "ask_qty": ask_qty

    }