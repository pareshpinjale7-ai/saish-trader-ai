# learning_engine.py

# =========================
# LEARNING MEMORY
# =========================

learning_memory = []

# =========================
# SAVE RESULT
# =========================

def save_learning(

    signal,
    outcome

):

    learning_memory.append({

        "signal": signal,

        "outcome": outcome

    })

# =========================
# WIN RATE
# =========================

def get_learning_accuracy():

    if len(learning_memory) == 0:

        return 0

    wins = 0

    for item in learning_memory:

        if item["outcome"] == "WIN":

            wins += 1

    accuracy = (

        wins / len(learning_memory)

    ) * 100

    return round(

        accuracy,

        2

    )