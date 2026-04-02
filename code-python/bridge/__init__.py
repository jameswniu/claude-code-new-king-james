"""Bridge/REPL system — remote session management via WebSocket."""
TRANSPORT_TYPES = ["websocket", "polling"]
BRIDGE_KICK_COMMANDS = ["close", "poll", "register", "reconnect-session", "heartbeat", "reconnect", "status"]
