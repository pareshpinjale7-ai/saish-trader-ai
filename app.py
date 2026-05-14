# app.py

from flask import Flask, jsonify
from flask_cors import CORS

import threading

# =========================
# SCANNER
# =========================

from scanner_manager import (

    get_breakout_data,
    get_intraday_boost

)

# =========================
# MARKET / SECTOR
# =========================

from market_trend_engine import (
    get_market_trend
)

from sector_trend_engine import (
    get_sector_trend
)

from heatmap_engine import (
    get_heatmap
)

from top_movers_engine import (
    get_top_movers
)

from scanner_health_engine import (
    get_scanner_health
)

from sector_strength_engine import (

    calculate_sector_strength,
    get_sector_strength,
    get_top_sector,
    get_weak_sector

)

# =========================
# SOCKET
# =========================

from dhan_socket import (
    start_socket
)

# =========================
# FLASK
# =========================

app = Flask(__name__)

CORS(app)

# =========================
# START DHAN SOCKET
# =========================

socket_thread = threading.Thread(

    target=start_socket

)

socket_thread.daemon = True

socket_thread.start()

# =========================
# ROOT
# =========================

@app.route("/")

def home():

    return jsonify({

        "status": "RUNNING",

        "project":

        "DHAN INSTITUTIONAL SCANNER",

        "socket": "CONNECTED"

    })

# =========================
# BREAKOUT BEACON
# =========================

@app.route("/breakout-beacon")

def breakout_beacon():

    return jsonify(

        get_breakout_data()

    )

# =========================
# INTRADAY BOOST
# =========================

@app.route("/intraday-boost")

def intraday_boost():

    return jsonify(

        get_intraday_boost()

    )

# =========================
# LIVE SECTOR
# =========================

@app.route("/live-sector")

def live_sector():

    return jsonify(

        get_sector_trend()

    )

# =========================
# MARKET TREND
# =========================

@app.route("/market-trend")

def market_trend():

    return jsonify(

        get_market_trend()

    )

# =========================
# HEATMAP
# =========================

@app.route("/heatmap")

def heatmap():

    return jsonify(

        get_heatmap()

    )

# =========================
# TOP MOVERS
# =========================

@app.route("/top-movers")

def top_movers():

    return jsonify(

        get_top_movers()

    )

# =========================
# HEALTH
# =========================

@app.route("/scanner-health")

def scanner_health():

    return jsonify(

        get_scanner_health()

    )

# =========================
# SECTOR STRENGTH
# =========================

@app.route("/sector-strength")

def sector_strength():

    calculate_sector_strength()

    return jsonify(

        get_sector_strength()

    )

# =========================
# TOP SECTOR
# =========================

@app.route("/top-sector")

def top_sector():

    calculate_sector_strength()

    sector = get_top_sector()

    return jsonify(

        sector

    )

# =========================
# WEAK SECTOR
# =========================

@app.route("/weak-sector")

def weak_sector():

    calculate_sector_strength()

    sector = get_weak_sector()

    return jsonify(

        sector

    )

# =========================
# RUN
# =========================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False,

        threaded=True

    )