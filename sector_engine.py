# sector_engine.py

from sector_map import SECTOR_MAP

def calculate_sector_strength(

    live_market_data

):

    sector_data = []

    for sector, stocks in SECTOR_MAP.items():

        live_stocks = []

        total_strength = 0

        total_count = 0

        for symbol in stocks:

            if symbol in live_market_data:

                stock = live_market_data[symbol]

                change = stock.get(

                    "change_percent",

                    0

                )

                total_strength += change

                total_count += 1

                live_stocks.append({

                    "symbol": symbol,

                    "ltp": stock.get(
                        "ltp",
                        0
                    ),

                    "change": round(
                        change,
                        2
                    ),

                    "volume": stock.get(
                        "volume",
                        0
                    ),

                    "oi": stock.get(
                        "oi",
                        0
                    )

                })

        if total_count > 0:

            strength = round(

                total_strength / total_count,

                2

            )

            sector_data.append({

                "sector": sector,

                "strength": strength,

                "stocks": live_stocks

            })

    sector_data.sort(

        key=lambda x: x["strength"],

        reverse=True

    )

    return sector_data