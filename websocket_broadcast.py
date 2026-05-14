# websocket_broadcast.py

# =========================
# FRONTEND SOCKET DATA
# =========================

frontend_clients = []

# =========================
# REGISTER
# =========================

def register_client(client):

    frontend_clients.append(client)

# =========================
# BROADCAST
# =========================

def broadcast_data(data):

    for client in frontend_clients:

        try:

            client.send_json(data)

        except:

            pass