# options_chain_engine.py

# =========================
# OPTIONS CHAIN MEMORY
# =========================

options_chain_data = {}

# =========================
# UPDATE OI
# =========================

def update_options_chain(

    strike,
    call_oi,
    put_oi

):

    options_chain_data[strike] = {

        "call_oi": call_oi,

        "put_oi": put_oi

    }

# =========================
# PCR
# =========================

def calculate_pcr():

    total_call = 0
    total_put = 0

    for strike, data in options_chain_data.items():

        total_call += data["call_oi"]
        total_put += data["put_oi"]

    if total_call == 0:

        return 0

    return round(

        total_put / total_call,

        2

    )