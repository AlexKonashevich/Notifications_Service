from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, user_id: str, message: str) -> bool:
        pass
    