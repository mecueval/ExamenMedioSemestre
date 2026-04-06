# Task Management API - Corrección de Examen

----------

## Implementación 
| Pregunta| Descripción |
| P1 - Docker Compose | Infraestructura con PostgreSQL, FastAPI (puerto 8000) y pgAdmin (puerto 5050), volumen persistente y depends_on |
| P2 - Domain + Factory | Entidad Task con validaciones (título no vacío, prioridad válida, estado inicial OPEN) y TaskFactory para crear tareas |
| P3 - Strategy | Políticas de notificación: AlwaysNotify y NotifyOnDoneOnly, con NotificationService que usa print()|
| P4A - API + DTOs| Endpoint POST /tasks con TaskCreateRequest y TaskResponse, sin lógica de negocio en el endpoint|
| P4B - Git + Docker | Comandos para control de versiones y gestión de contenedores|


## Comandos Git
```
# 1. Iniciar repositorio
git init

# 2. Crear rama feature/tasks
git checkout -b feature/tasks

# 3. Agregar archivos y hacer commit
git add .
git commit -m "feat: implement task management API with Docker, Factory and Strategy patterns"

# 4. Agregar repositorio remoto
git remote add origin https://github.com/usuario/task-management-api.git

# 5. Push de la rama
git push -u origin feature/tasks

```
## Comandos Docker
```
# Levantar los contenedores
docker-compose up -d

# Bajar los contenedores
docker-compose down

```