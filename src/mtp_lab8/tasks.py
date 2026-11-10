"""Модель с property и функция подсчёта выполненных задач."""

from collections.abc import Iterable


class Task:
    def __init__(self, task_id: int, title: str) -> None:
        self._id = task_id
        self.title = title
        self.completed = False

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        clean = value.strip()
        if not clean:
            raise ValueError("Название не может быть пустым")
        self._title = clean


def count_completed(tasks: Iterable[Task]) -> int:
    """Подсчитать только завершённые задачи, включая пустой источник."""
    return sum(1 for task in tasks if task.completed)
