tasks = []

def show_menu():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_done():
    view_tasks()
    choice = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= choice < len(tasks):
        tasks.pop(choice)
        print("Task marked as done!")
    else:
        print("Invalid choice.")

while True:
    show_menu()
    choice = input("Select an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
