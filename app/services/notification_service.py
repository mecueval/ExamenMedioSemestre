from app.domain.enums import EventType
from app.domain.strategies import NotificationPolicy


class NotificationService:
    def __init__(self, service: NotificationPolicy):
        self.policy = service
    def notify(self, event: EventType):  # ← Cambiar str a EventType
        if self.policy.should_notify(event):
            print(f"Enviando notificación para el evento: {event.value}")
