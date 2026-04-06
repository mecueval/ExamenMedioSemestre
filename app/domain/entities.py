from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime
from app.domain.enums import TaskStatus, Priority

@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid4()))
    title: str
    description: str | None
    priority: Priority
    status: TaskStatus = TaskStatus.OPEN
    assignee_id: str | None
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("El título no puede estar vacío")
        if self.priority not in [Priority.LOW, Priority.MEDIUM, Priority.HIGH]:
            raise ValueError("Prioridad inválida")