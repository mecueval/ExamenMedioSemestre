from app.domain.entities import Task

from app.domain.enums import Priority


class TaskFactory:
    @staticmethod
    def create_task(title: str, priority: str, description: str | None = None,
                   assignee_id: str | None = None) -> Task:
        if not title:
            raise ValueError("Título no puede estar vacío")
        
        try:
            priority_enum = Priority(priority.upper())
        except ValueError:
            raise ValueError("Prioridad inválida")
        
        return Task(
            title=title,
            description=description,
            priority=priority_enum,
            assignee_id=assignee_id
        )