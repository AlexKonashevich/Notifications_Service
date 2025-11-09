from celery import Celery
from sqlalchemy.orm import Session
from . import SessionLocal
from .delivery import attempt_delivery
from config import BROKER_URL

celery_app = Celery("notifications", broker=BROKER_URL)

@celery_app.task
def deliver_notification(notification_id: str, message: str):
    db: Session = SessionLocal()
    try:
        attempt_delivery(db, notification_id, message)
    finally:
        db.close()
