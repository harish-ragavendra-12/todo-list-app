#to do list app

#global variable
pending_task = []

#add user tasks
def add_tasks():

    try:
        count = int(input("How many tasks do you want to add ? "))

        #stores tasks in a list
        for i in range(count):
            user_task = input(f'Enter task {i + 1}: ').strip()
            if user_task:

                pending_task.append({
                    'task': user_task,
                    'status': 'Pending'
                })
            else:
                print("Task cannot be empty")

        print("Tasks added successfully...")

    except ValueError:
        print("Enter numbers only")


#view tasks
def view_tasks():

    if not pending_task:
        print("No tasks available")
    else:
        print('\nTasks to be completed:')

        for index, item in enumerate(pending_task, start=1):
            print(
                f"{index}. {item['task']} "
                f"[{item['status']}]"
            )


#delete tasks
def del_tasks():

    if not pending_task:
        print('No tasks available')
        return

    view_tasks()

    try:
        choice = int(input('Which task number do you want to delete ? '))

        if 0 < choice <= len(pending_task):
            delete_task = pending_task.pop(choice-1)
            print('Deleted successfully:',delete_task['task'])
        else:
            print('Invalid task number')

    except ValueError:
        print("Please enter numbers only")

def edit_tasks():

    if not pending_task:
        print('No tasks available')
    else:
        view_tasks()

        try:
            choice = int(input('Enter task number to edit: '))

            if 0 < choice <= len(pending_task):
                new_task = input('Enter new task: ')

                old_task = pending_task[choice-1]['task']

                pending_task[choice-1]['task'] = new_task

                print(f"Task updated:")
                print(f"{old_task} --> {new_task}")

            else:
                print("Invalid task number")

        except ValueError:
            print("Please enter numbers only")

def mark_complete():

    if not pending_task:
        print('No tasks available')
    else:
        view_tasks()

        try:
            choice = int(input('Enter completed task number: '))

            if 0 < choice <= len(pending_task):
                pending_task[choice - 1]["status"] = "Done"

                print("Task marked as completed")
            else:
                print("Invalid task number")

        except ValueError:
            print("Enter numbers only")

while True:

    print("\nMenu")
    print("-----------------")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Edit Tasks")
    print("5. Mark Complete")
    print("6. Exit")

    choice = input("Enter your choice: ")

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
