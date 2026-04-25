import html
import threading
import urllib.parse
import urllib.request
from app.config.logger import Log, Level

class TelegramNotifier:
    def __init__(self, token: str, id: str, buffer_time: float = 10.0):
        self._chat_id = id
        self._token = token
        self._buffer: list[Log] = []
        self._lock = threading.Lock()
        self._buffer_time = buffer_time
        self._timer: threading.Timer | None = None

    def on_log(self, log: Log) -> None:
        if log.level not in (Level.ERROR, Level.WARNING) or not self._token or not self._chat_id:
            return

        with self._lock:
            self._buffer.append(log)
            if not self._timer:
                self._timer = threading.Timer(self._buffer_time, self._flush)
                self._timer.start()

    def _flush(self) -> None:
        with self._lock: logs, self._buffer, self._timer = self._buffer, [], None
        
        if not logs:
            return
        
        content = []
        for level, emoji, title in [(Level.ERROR, "🚨", "ERROR"), (Level.WARNING, "⚠️", "WARNING")]:
            message = [l for l in logs if l.level == level]
            if not message:
                continue

            content.append(f"<b>{emoji} {title}</b> ({len(message)} logs)\n\n" + "\n".join([f"• <code>[{l.timestamp:%H:%M:%S}]</code> {html.escape(l.message)}" for l in message]))

        text = "\n\n".join(content)
        if len(text) > 4000:
            text = text[:3990] + "\n\n... (truncated)"

        try:
            url = f"https://api.telegram.org/bot{self._token}/sendMessage"
            payload = {"id": self._chat_id, "text": text, "parse_mode": "HTML"}
            data = urllib.parse.urlencode(payload).encode()
            urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=10)
        except Exception:
            pass