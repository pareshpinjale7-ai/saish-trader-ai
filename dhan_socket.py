# dhan_socket.py

import json
import websocket
import struct

from config import (
    CLIENT_ID,
    ACCESS_TOKEN
)

from instrument_loader import (
    FILTERED_SECURITY_MAP
)

from market_memory_engine import (
    update_market_memory
)

# =========================
# LIVE CACHE
# =========================

from live_cache import (
    update_live_data
)

# =========================
# ENGINES
# =========================

from candle_engine import (
    process_tick
)

from opening_memory import (
    update_opening_memory
)

from oi_engine import (
    update_oi
)

from market_depth_engine import (
    analyze_market_depth
)

# =========================
# DHAN SOCKET URL
# =========================

SOCKET_URL = (

    f"wss://api-feed.dhan.co"
    f"?version=2"
    f"&token={ACCESS_TOKEN}"
    f"&clientId={CLIENT_ID}"
    f"&authType=2"

)

# =========================
# CREATE INSTRUMENT LIST
# =========================

instrument_list = []

for symbol, data in FILTERED_SECURITY_MAP.items():

    instrument_list.append({

        "ExchangeSegment": "NSE_EQ",

        "SecurityId": str(
            data["security_id"]
        )

    })

# =========================
# SECURITY ID MAP
# =========================

SECURITY_ID_MAP = {}

for symbol, data in FILTERED_SECURITY_MAP.items():

    SECURITY_ID_MAP[
        str(data["security_id"])
    ] = symbol

# =========================
# DECODE TICKER PACKET
# =========================

def decode_ticker_packet(packet):

    try:

        # =====================
        # PACKET TYPE
        # =====================

        packet_type = packet[0]

        if packet_type != 2:

            return

        # =====================
        # SECURITY ID
        # =====================

        security_id = str(

            int.from_bytes(

                packet[4:8],

                byteorder="little"

            )

        )

        # =====================
        # LTP FLOAT
        # =====================

        ltp = round(

            struct.unpack(

                '<f',

                packet[8:12]

            )[0],

            2

        )

        # =====================
        # SYMBOL
        # =====================

        symbol = SECURITY_ID_MAP.get(

            security_id

        )

        if not symbol:

            return

        # =====================
        # UPDATE CACHE
        # =====================

        update_live_data(

            symbol=symbol,

            ltp=ltp,

            volume=0,

            change_percent=0,

            oi=0,

            bid_qty=0,

            ask_qty=0

        )

        # =====================
        # PROCESS
        # =====================

        process_tick(

            symbol,

            ltp,

            0

        )

        update_opening_memory(

            symbol,

            ltp,

            0

        )

       # =====================
       # MARKET MEMORY
       # =====================

        update_market_memory(

            symbol,

            ltp

        )

        # =====================
        # LIVE LOG
        # =====================

        print(

            f"{symbol} | "

            f"LTP {ltp}"

        )

    except Exception as e:

        print(

            "DECODE ERROR:",

            e

        )

# =========================
# ON OPEN
# =========================

def on_open(ws):

    print("\nCONNECTED TO DHAN WEBSOCKET")

    print(

        f"TOTAL SUBSCRIPTIONS: "

        f"{len(instrument_list)}"

    )

    # =====================
    # SUBSCRIBE CHUNKS
    # =====================

    chunk_size = 100

    for i in range(

        0,
        len(instrument_list),
        chunk_size

    ):

        chunk = instrument_list[
            i:i + chunk_size
        ]

        payload = {

            "RequestCode": 15,

            "InstrumentCount": len(chunk),

            "InstrumentList": chunk

        }

        ws.send(

            json.dumps(payload)

        )

        print(

            f"SUBSCRIBED: "

            f"{i} to {i+len(chunk)}"

        )

    print("\nALL SUBSCRIPTIONS DONE")

# =========================
# ON MESSAGE
# =========================

def on_message(ws, message):

    try:

        # =====================
        # BINARY PACKET
        # =====================

        if isinstance(message, bytes):

            decode_ticker_packet(message)

            return

        # =====================
        # JSON LOG
        # =====================

        data = json.loads(message)

        print(data)

    except Exception as e:

        print(

            "MESSAGE ERROR:",

            e

        )

# =========================
# ON ERROR
# =========================

def on_error(ws, error):

    print(

        "SOCKET ERROR:",

        error

    )

# =========================
# ON CLOSE
# =========================

def on_close(

    ws,
    close_status_code,
    close_msg

):

    print(

        "\nSOCKET CLOSED"

    )

# =========================
# START SOCKET
# =========================

def start_socket():

    websocket.enableTrace(False)

    ws = websocket.WebSocketApp(

        SOCKET_URL,

        on_open=on_open,

        on_message=on_message,

        on_error=on_error,

        on_close=on_close

    )

    ws.run_forever()