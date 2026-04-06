# services/task_service.py
from app.domain.factories import TaskFactory
from app.api.dtos import TaskCreateRequest, TaskResponse

class TaskService:
    @staticmethod
    def create_task(request: TaskCreateRequest) -> TaskResponse:
        task = TaskFactory.create_task(
            priority=request.priority.value,
            title=request.title,
            description=request.description,
            assignee_id=request.assignee_id
        )
        
        return TaskResponse(
            id=task.id,
            title=task.title,
            priority=task.priority,
            status=task.status,
            created_at=task.created_at
        )