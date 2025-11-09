import requests
from config import SMS_API_KEY
from .base import NotificationChannel

class SmsChannel(NotificationChannel):
    def send(self, user_id: str, message: str) -> bool:
        try:
            response = requests.post(
                "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Messages.json",
                auth=("ACxxx", SMS_API_KEY),
                data={
                    "To": f"+1000000000{user_id[-4:]}",
                    "From": "+15555555555",
                    "Body": message,
                },
                timeout=10,
            )
            return response.status_code == 201
        except Exception:
            return False
        