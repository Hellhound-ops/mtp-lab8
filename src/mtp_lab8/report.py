"""Формирование строк отчёта с asyncio."""

import asyncio

from .repository import TaskRepository
from .tasks import Task


async def report_line(task: Task) -> str:
    """Сымитировать ожидание ввода-вывода для одной строки отчёта."""
    await asyncio.sleep(0.1)
    status = "готово" if task.completed else "в работе"
    return f"{task.id}. {task.title}: {status}"


async def build_report(repository: TaskRepository) -> list[str]:
    """Запустить обработку всех задач одновременно и сохранить порядок строк."""
    return await asyncio.gather(*(report_line(task) for task in repository.all()))
