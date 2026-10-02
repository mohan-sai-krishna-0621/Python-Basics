tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task():
    view_tasks()

    if len(tasks) > 0:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number.")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")