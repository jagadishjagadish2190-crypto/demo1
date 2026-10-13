# todo_list.py

from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.txt")


def load_tasks():
    """Load tasks from the text file."""
    tasks = []
    if TASKS_FILE.exists():
        for line in TASKS_FILE.read_text(encoding="utf-8").splitlines():
            parts = line.split("|", 1)
            if len(parts) == 2:
                completed, task = parts
                tasks.append({"task": task, "completed": completed == "1"})
    return tasks


def save_tasks(tasks):
    """Save tasks to the text file."""
    lines = [
        f"{'1' if item['completed'] else '0'}|{item['task']}"
        for item in tasks
    ]
    TASKS_FILE.write_text("\n".join(lines), encoding="utf-8")


def display_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\nTo-Do List:")
    for index, item in enumerate(tasks, start=1):
        status = "✓" if item["completed"] else " "
        print(f"{index}. [{status}] {item['task']}")


def get_task_number(tasks, prompt):
    try:
        number = int(input(prompt))
        if 1 <= number <= len(tasks):
            return number - 1
    except ValueError:
        pass

    print("Please enter a valid task number.")
    return None


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append({"task": task, "completed": False})
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                index = get_task_number(tasks, "Task number to complete: ")
                if index is not None:
                    tasks[index]["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as completed.")

        elif choice == "4":
            display_tasks(tasks)
            if tasks:
                index = get_task_number(tasks, "Task number to remove: ")
                if index is not None:
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Removed: {removed['task']}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
