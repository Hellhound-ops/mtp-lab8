"""Демонстрация пакета из командной строки."""

import asyncio

from .report import build_report
from .repository import InMemoryTaskRepository
from .tasks import Task, count_completed


def main() -> None:
    repository = InMemoryTaskRepository()
    for task_id, title in enumerate(("Описать проект", "  Проверить код  ", "Сдать работу"), 1):
        repository.add(Task(task_id, title))

    repository.get(2).title = "Проверить работу тестами"
    repository.get(1).completed = True
    repository.get(2).completed = True

    print("МТП · ЛР №8 · Вариант 3")
    print(f"Выполнено задач: {count_completed(repository.all())}")
    for line in asyncio.run(build_report(repository)):
        print(line)


if __name__ == "__main__":
    main()
