import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task_manager.task_utils import add_task, mark_task_as_complete, calculate_progress, tasks


def test_add_and_complete_task():
    tasks.clear()

    add_task("Test Task", "A simple task", "2026-12-31")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"
    assert tasks[0]["completed"] is False

    mark_task_as_complete(1)
    assert tasks[0]["completed"] is True
    assert calculate_progress() == 100.0


if __name__ == "__main__":
    test_add_and_complete_task()
    print("test_task_manager.py passed")
