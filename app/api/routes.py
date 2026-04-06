from fastapi import APIRouter
from app.api.dtos import TaskResponse, TaskCreateRequest
from app.services.task_service import TaskService

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
def create_task(request: TaskCreateRequest) -> TaskResponse:
    # Solo valida DTO y llama al servicio
    return TaskService.create_task(request)