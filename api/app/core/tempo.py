from datetime import datetime, timezone

# Utilitario de data e hora, guardamos no banco de dados em utc, sem timezone
def agora() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)