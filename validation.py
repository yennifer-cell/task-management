from datetime import datetime


def validate_task_title(title):
    if title is None:
        print("Error: Title cannot be empty.")
        return False

    title = title.strip()
    if len(title) == 0:
        print("Error: Title cannot be empty.")
        return False
    if len(title) > 100:
        print("Error: Title must be 100 characters or fewer.")
        return False

    return True


def validate_task_description(description):
    if description is None:
        print("Error: Description cannot be empty.")
        return False

    description = description.strip()
    if len(description) == 0:
        print("Error: Description cannot be empty.")
        return False
    if len(description) > 250:
        print("Error: Description must be 250 characters or fewer.")
        return False

    return True


def validate_due_date(due_date):
    if due_date is None:
        print("Error: Due date cannot be empty.")
        return False

    due_date = due_date.strip()
    if len(due_date) == 0:
        print("Error: Due date cannot be empty.")
        return False

    try:
        datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
        return False

    return True
