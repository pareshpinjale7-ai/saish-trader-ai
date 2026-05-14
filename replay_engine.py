# replay_engine.py

# =========================
# REPLAY MEMORY
# =========================

market_replay = []

# =========================
# SAVE SNAPSHOT
# =========================

def save_market_snapshot(

    snapshot

):

    market_replay.append(snapshot)

# =========================
# GET SNAPSHOTS
# =========================

def get_market_replay():

    return market_replay