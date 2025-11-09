from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
import json
from app import SessionLocal, models
from app.worker import deliver_notification

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notify/")
def create_notification(
    user_id: UUID,
    message: str,
    channels: list = ["email", "sms", "telegram"],
    db: Session = Depends(get_db)
):
    if not channels:
        raise HTTPException(status_code=400, detail="At least one channel required")

    db_notification = models.Notification(
        user_id=user_id,
        channels_order=json.dumps(channels)
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)

    deliver_notification.delay(str(db_notification.id), message)

    return {"notification_id": db_notification.id}
