# instrument_loader.py

import requests
import csv
from io import StringIO

# =========================
# CSV URL
# =========================

CSV_URL = (
    "https://images.dhan.co/api-data/api-scrip-master.csv"
)

# =========================
# ALL STOCKS
# =========================

ALL_STOCKS = [

    "HDFCBANK",
    "ICICIBANK",
    "AXISBANK",
    "SBIN",
    "RELIANCE",
    "INFY",
    "TCS",
    "WIPRO",
    "TATAMOTORS",
    "TATASTEEL",
    "JSWSTEEL",
    "ITC",
    "LUPIN",
    "SUNPHARMA",
    "CIPLA",
    "BAJFINANCE",
    "BAJAJFINSV",
    "ADANIPOWER",
    "POWERGRID",
    "NTPC",
    "ONGC",
    "COALINDIA",
    "HINDALCO",
    "MARUTI",
    "M&M",
    "ULTRACEMCO",
    "DLF",
    "HAL",
    "BEL",
    "TRENT",
    "TITAN",
    "BHARTIARTL",
    "TECHM",
    "HCLTECH",
    "INDUSINDBK",
    "KOTAKBANK",
    "BANKBARODA",
    "PNB",
    "CANBK",
    "FEDERALBNK",
    "RBLBANK",
    "AUBANK",
    "YESBANK",
    "COFORGE",
    "MPHASIS",
    "PERSISTENT",
    "TATAELXSI",
    "KPITTECH",
    "ASHOKLEY",
    "TVSMOTOR",
    "EICHERMOT",
    "BHARATFORG",
    "DRREDDY",
    "DIVISLAB",
    "BIOCON",
    "AUROPHARMA",
    "TORNTPHARM",
    "ZYDUSLIFE",
    "LAURUSLABS",
    "VEDL",
    "NMDC",
    "GAIL",
    "IOC",
    "BPCL",
    "NHPC",
    "TATAPOWER",
    "JSWENERGY",
    "HINDUNILVR",
    "DABUR",
    "BRITANNIA",
    "MARICO",
    "GODREJCP",
    "OBEROIRLTY",
    "GODREJPROP",
    "PRESTIGE",
    "JIOFIN",
    "PFC",
    "RECLTD",
    "ABB",
    "SIEMENS",
    "CGPOWER",
    "POLYCAB",
    "HAVELLS",
    "KEI",
    "BDL",
    "COCHINSHIP",
    "MAZDOCK",
    "DMART",
    "VBL",
    "INDUSTOWER",
    "SRF",
    "UPL",
    "PIIND",
    "PAYTM",
    "POLICYBZR",
    "NYKAA",
    "SWIGGY",
    "ETERNAL",
    "BSE",
    "MCX",
    "IRCTC",
    "IRFC",
    "RVNL",
    "RAILTEL",
    "IREDA",
    "INOXWIND",
    "SUZLON",
    "LT",
    "NBCC"

]

# =========================
# DOWNLOAD CSV
# =========================

print("\nDOWNLOADING DHAN MASTER...")

response = requests.get(CSV_URL)

csv_text = response.text

print("CSV LOADED")

# =========================
# READ CSV
# =========================

csv_file = StringIO(csv_text)

reader = csv.DictReader(csv_file)

# =========================
# FINAL MAP
# =========================

FILTERED_SECURITY_MAP = {}

print("\nMAPPING NSE STOCKS...\n")

for row in reader:

    try:

        exchange = row.get(

            "SEM_EXM_EXCH_ID",

            ""

        )

        symbol = row.get(

            "SEM_TRADING_SYMBOL",

            ""

        ).upper().strip()

        security_id = row.get(

            "SEM_SMST_SECURITY_ID",

            ""

        )

        if (

            exchange == "NSE"

            and

            symbol in ALL_STOCKS

        ):

            FILTERED_SECURITY_MAP[symbol] = {

                "security_id": security_id,

                "exchange_segment": "NSE_EQ"

            }

            print(

                f"ADDED: {symbol}"

            )

    except:

        pass

# =========================
# FINAL OUTPUT
# =========================

print(

    f"\nTOTAL INSTRUMENTS: "

    f"{len(FILTERED_SECURITY_MAP)}"

)

print("\nLIVE STOCKS:\n")

print(

    list(

        FILTERED_SECURITY_MAP.keys()

    )[:200]

)