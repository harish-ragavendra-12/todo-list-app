#to-do-list app

import json
import os


# Create file if it doesn't exist
if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as file:
        json.dump([], file)


# Load tasks from JSON
def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)


# Save tasks to JSON
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Add tasks
def add_tasks():

    try:
        count = int(input("How many tasks do you want to add? "))

        tasks = load_tasks()

        for i in range(count):

            user_task = input(
                f"Enter task {i+1}: "
            ).strip()

            if user_task:

                new_task = {
                    "task_id": len(tasks) + 1,
                    "task_name": user_task,
                    "status": "Pending"
                }

                tasks.append(new_task)

            else:
                print("Task cannot be empty")

        save_tasks(tasks)

        print("Tasks added successfully...")

    except ValueError:
        print("Enter numbers only")


# View tasks
def view_tasks():

    tasks = load_tasks()

    if not tasks:
        print("No tasks available")

    else:

        print("\nTasks:")
        print("----------------------")

        for index, item in enumerate(tasks, start=1):

            print(
                f"{index}. "
                f"{item['task_name']} "
                f"[{item['status']}]"
            )


# Delete task
def del_tasks():

    tasks = load_tasks()

    if not tasks:
        print("No tasks available")
        return

    view_tasks()

    try:

        choice = int(
            input(
                "Which task number do you want to delete? "
            )
        )

        if 0 < choice <= len(tasks):

            deleted_task = tasks.pop(choice - 1)

            save_tasks(tasks)

            print(
                "Deleted successfully:",
                deleted_task["task_name"]
            )

        else:
            print("Invalid task number")

    except ValueError:
        print("Enter numbers only")


# Edit task
def edit_tasks():

    tasks = load_tasks()

    if not tasks:
        print("No tasks available")
        return

    view_tasks()

    try:

        choice = int(
            input("Enter task number to edit: ")
        )

        if 0 < choice <= len(tasks):

            new_task = input(
                "Enter new task: "
            ).strip()

            old_task = tasks[choice - 1]["task_name"]

            tasks[choice - 1]["task_name"] = new_task

            save_tasks(tasks)

            print(
                f"{old_task} --> {new_task}"
            )

        else:
            print("Invalid task number")

    except ValueError:
        print("Enter numbers only")


# Mark complete
def mark_complete():

    tasks = load_tasks()

    if not tasks:
        print("No tasks available")
        return

    view_tasks()

    try:

        choice = int(
            input(
                "Enter completed task number: "
            )
        )

        if 0 < choice <= len(tasks):

            tasks[choice - 1]["status"] = "Done"

            save_tasks(tasks)

            print(
                "Task marked as completed"
            )

        else:
            print("Invalid task number")

    except ValueError:
        print("Enter numbers only")


# Menu
while True:

    print("\nMenu")
    print("----------------")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Edit Tasks")
    print("5. Mark Complete")
    print("6. Exit")

    choice = input(
        "Enter your choice: "
    )

    if choice == "1":
        add_tasks()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        del_tasks()

    elif choice == "4":
        edit_tasks()

    elif choice == "5":
        mark_complete()

    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")