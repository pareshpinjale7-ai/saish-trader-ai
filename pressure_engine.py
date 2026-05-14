# pressure_engine.py

# =========================
# BUY SELL PRESSURE
# =========================

def calculate_pressure(

    bid_qty,
    ask_qty

):

    if ask_qty == 0:

        return 0

    pressure = (

        bid_qty / ask_qty

    )

    return round(

        pressure,

        2

    )