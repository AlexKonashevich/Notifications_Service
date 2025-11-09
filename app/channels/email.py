import requests
from config import EMAIL_API_KEY
from .base import NotificationChannel

class EmailChannel(NotificationChannel):
    def send(self, user_id: str, message: str) -> bool:
        try:
            response = requests.post(
                "https://api.sendgrid.com/v3/mail/send",
                headers={"Authorization": f"Bearer {EMAIL_API_KEY}"},
                json={
                    "personalizations": [{"to": [{"email": f"user_{user_id}@example.com"}]}],
                    "from": {"email": "notify@example.com"},
                    "subject": "Notification",
                    "content": [{"type": "text/plain", "value": message}],
                },
                timeout=10,
            )
            return response.status_code == 202
        except Exception:
            return False
        