import httpx
import logging
from result import Result
from src.config import ok, err, AppError, IOError_, get_env, get_env_bool, attempt_async

logger = logging.getLogger(__name__)

_TOKEN = get_env("TELEGRAM_BOT_TOKEN").unwrap_or("")
_CHAT_ID = get_env("TELEGRAM_CHAT_ID").unwrap_or("")
_BASE_URL = f"https://api.telegram.org/bot{_TOKEN}/sendMessage"


async def notify(message: str, level: str = "error") -> Result[None, AppError]:
    if not _TOKEN or not _CHAT_ID:
        logger.warning("Telegram non configurato, notifica saltata")
        return ok(None)

    icons = {"info": "ℹ️", "warning": "⚠️", "error": "🚨", "critical": "🔥"}
    icon = icons.get(level, "🔔")

    async def _send():
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
            return None

    res = await attempt_async(
        _send(),
        lambda e: IOError_(message="Failed to send Telegram notification", target=str(e))
    )
    
    if res.is_err():
        logger.error("Errore invio notifica Telegram: %s", res.unwrap_err())
    
    return res