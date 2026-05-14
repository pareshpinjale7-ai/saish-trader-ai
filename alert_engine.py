# alert_engine.py

# =========================
# ALERT ENGINE
# =========================

triggered_alerts = set()

# =========================
# ALERT
# =========================

def send_alert(

    symbol,
    signal,
    rfact

):

    key = f"{symbol}_{signal}"

    if key in triggered_alerts:

        return

    triggered_alerts.add(key)

    print(

        f"🚨 ALERT | {symbol} | {signal} | RF:{rfact}"

    )