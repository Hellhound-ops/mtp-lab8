"""Проверки функции, свойства и работы с репозиторием."""

import asyncio

import pytest

from mtp_lab8 import report
from mtp_lab8.repository import InMemoryTaskRepository
from mtp_lab8.tasks import Task, count_completed


def test_count_completed_accepts_an_iterable():
    first = Task(1, "Первая")
    first.completed = True
    assert count_completed(iter((first, Task(2, "Вторая")))) == 1
    assert count_completed(iter(())) == 0


def test_title_property_preserves_value_on_invalid_assignment():
    task = Task(1, "  Первая  ")
    assert task.title == "Первая"
    task.title = "  Другая  "
    with pytest.raises(ValueError):
        task.title = " "
    assert task.title == "Другая"


def test_repository_keeps_record_when_id_is_duplicated():
    repository = InMemoryTaskRepository()
    original = Task(1, "Первая")
    repository.add(original)
    with pytest.raises(ValueError):
        repository.add(Task(1, "Дубликат"))
    assert repository.get(1) is original
    assert repository.all() == (original,)


def test_report_starts_all_coroutines_before_waiting_for_results(monkeypatch):
    repository = InMemoryTaskRepository()
    repository.add(Task(1, "Первая"))
    repository.add(Task(2, "Вторая"))

    async def verify():
        second_started = asyncio.Event()

        async def fake_line(task):
            if task.id == 1:
                await second_started.wait()
            else:
                second_started.set()
            return task.title

        monkeypatch.setattr(report, "report_line", fake_line)
        return await asyncio.wait_for(report.build_report(repository), timeout=2)

    assert asyncio.run(verify()) == ["Первая", "Вторая"]
