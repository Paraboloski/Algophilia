import httpx
import logging
from src.config.env import get_env

logger = logging.getLogger(__name__)

_TOKEN = get_env("TELEGRAM_BOT_TOKEN").unwrap_or("")
_CHAT_ID = get_env("TELEGRAM_CHAT_ID").unwrap_or("")
_BASE_URL = f"https://api.telegram.org/bot{_TOKEN}/sendMessage"


async def notify(message: str, level: str = "error") -> None:
    if not _TOKEN or not _CHAT_ID:
        logger.warning("Telegram non configurato, notifica saltata")
        return

    icons = {"info": "ℹ️", "warning": "⚠️", "error": "🚨", "critical": "🔥"}
    icon = icons.get(level, "🔔")

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.post(
                _BASE_URL,
                json={
                    "chat_id": _CHAT_ID,
                    "text": f"{icon} *{level.upper()}*\n\n{message}",
                    "parse_mode": "Markdown",
                },
            )
            response.raise_for_status()
    except httpx.HTTPError as e:
        logger.error("Errore invio notifica Telegram: %s", e)