from pydantic import BaseModel
from datetime import datetime
from app.domain.enums import Priority, TaskStatus

class TaskCreateRequest(BaseModel):
    title: str
    description: str|None
    priority: Priority
    assignee_id: str|None

class TaskResponse(BaseModel):
    id: str
    title: str
    priority: Priority
    status: TaskStatus
    created_at: datetime