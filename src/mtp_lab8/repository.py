"""Шаблон Repository: интерфейс и реализация в памяти."""

from typing import Protocol

from .tasks import Task


class TaskRepository(Protocol):
    def add(self, task: Task) -> None: ...
    def get(self, task_id: int) -> Task: ...
    def all(self) -> tuple[Task, ...]: ...


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}

    def add(self, task: Task) -> None:
        if task.id in self._tasks:
            raise ValueError(f"Задача №{task.id} уже есть")
        self._tasks[task.id] = task

    def get(self, task_id: int) -> Task:
        return self._tasks[task_id]

    def all(self) -> tuple[Task, ...]:
        return tuple(self._tasks.values())
