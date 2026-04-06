from abc import ABC, abstractmethod

from app.domain.enums import EventType

class NotificationPolicy(ABC):
    @abstractmethod
    def should_notify(self, event: EventType) -> bool: 
        raise NotImplementedError("El método should_notify() debe ser implementado por las subclases")

class AlwaysNotify(NotificationPolicy):
    def should_notify(self, event: EventType) -> bool:
        if event in [EventType.TASK_CREATED, EventType.STATUS_CHANGED, EventType.TASK_DONE]:
            return True
        return False
class NotifyOnDoneOnly(NotificationPolicy):
    def should_notify(self, event: EventType) -> bool:
        if event == EventType.TASK_DONE:
            return True
        return False
