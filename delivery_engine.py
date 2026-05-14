# delivery_engine.py

# =========================
# DELIVERY BREAKOUT
# =========================

def detect_delivery_breakout(

    delivery_percent,
    volume

):

    if (

        delivery_percent >= 60

        and

        volume >= 1000000

    ):

        return "HIGH DELIVERY"

    return "NORMAL"