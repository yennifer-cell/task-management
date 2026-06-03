from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):
    if not (validate_task_title(title) and
            validate_task_description(description) and
            validate_due_date(due_date)):
        return

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int):
        print("Error: Task index must be a number.")
        return

    if index < 1 or index > len(tasks):
        print("Error: Task index is out of range.")
        return

    task = tasks[index - 1]
    if task["completed"]:
        print("This task is already marked as complete.")
        return

    task["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")
    for idx, task in enumerate(pending, start=1):
        print(f"{idx}. {task['title']} - Due: {task['due_date']}")
        print(f"   Description: {task['description']}")
        print(f"   Completed: {task['completed']}")


def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0

    completed_count = sum(1 for task in tasks if task["completed"])
    return (completed_count / len(tasks)) * 100
