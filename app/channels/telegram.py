import requests
from config import TELEGRAM_BOT_TOKEN
from .base import NotificationChannel

class TelegramChannel(NotificationChannel):
    def send(self, user_id: str, message: str) -> bool:
        try:
            response = requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                json={"chat_id": f"tg_{user_id}", "text": message},
                timeout=10,
            )
            return response.status_code == 200
        except Exception:
            return False
        