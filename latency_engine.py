# latency_engine.py

import time

# =========================
# LATENCY CHECK
# =========================

def calculate_latency(

    tick_time

):

    now = time.time()

    latency = now - tick_time

    return round(

        latency,

        3

    )