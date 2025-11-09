import json
from sqlalchemy.orm import Session
from .models import Notification, DeliveryStatus
from .channels import CHANNEL_REGISTRY

def attempt_delivery(db: Session, notification_id: str, message: str) -> bool:
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification or notification.status != DeliveryStatus.PENDING:
        return False

    channels = json.loads(notification.channels_order)
    current = notification.current_attempt

    if current >= len(channels):
        notification.status = DeliveryStatus.FAILED
        db.commit()
        return False

    channel_name = channels[current]
    channel_class = CHANNEL_REGISTRY.get(channel_name)
    if not channel_class:
        notification.current_attempt += 1
        db.commit()
        return attempt_delivery(db, notification_id, message)

    success = channel_class().send(str(notification.user_id), message)
    if success:
        notification.status = DeliveryStatus.DELIVERED
        db.commit()
        return True
    else:
        notification.current_attempt += 1
        notification.last_error = f"Failed on {channel_name}"
        db.commit()
        return attempt_delivery(db, notification_id, message)
    