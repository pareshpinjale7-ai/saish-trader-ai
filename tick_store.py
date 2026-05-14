# tick_store.py

tick_data = {}

def add_tick(symbol, data):

    if symbol not in tick_data:

        tick_data[symbol] = []

    tick_data[symbol].append(data)

    # KEEP LAST 500 TICKS

    tick_data[symbol] = tick_data[symbol][-500:]