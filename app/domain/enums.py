from enum import Enum

class TaskStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class EventType(str, Enum):
    TASK_CREATED = "TASK_CREATED"
    STATUS_CHANGED = "STATUS_CHANGED"  
    TASK_DONE = "TASK_DONE"            