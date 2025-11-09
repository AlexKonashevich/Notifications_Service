from .base import NotificationChannel
from .email import EmailChannel
from .sms import SmsChannel
from .telegram import TelegramChannel

CHANNEL_REGISTRY = {
    "email": EmailChannel,
    "sms": SmsChannel,
    "telegram": TelegramChannel,
}
