import os

BROKER_URL = os.getenv("BROKER_URL", "pyamqp://guest@localhost//")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/notifications")
EMAIL_API_KEY = os.getenv("EMAIL_API_KEY", "")
SMS_API_KEY = os.getenv("SMS_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
