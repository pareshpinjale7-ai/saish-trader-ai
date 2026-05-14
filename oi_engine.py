# oi_engine.py

# =========================
# OI BUILDUP ENGINE
# =========================

oi_store = {}

def update_oi(

    symbol,

    oi

):

    if symbol not in oi_store:

        oi_store[symbol] = []

    oi_store[symbol].append(oi)

    oi_store[symbol] = oi_store[symbol][-50:]

# =========================
# OI TREND
# =========================

def detect_oi_build(

    symbol

):

    if symbol not in oi_store:

        return "NO DATA"

    data = oi_store[symbol]

    if len(data) < 5:

        return "NO DATA"

    if data[-1] > data[0]:

        return "LONG BUILDUP"

    if data[-1] < data[0]:

        return "SHORT COVERING"

    return "SIDEWAYS"