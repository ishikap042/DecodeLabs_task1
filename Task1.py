# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

            try:
                task_no = int(input("Enter task number to mark as completed: "))
                tasks[task_no - 1]["completed"] = True
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number!")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                task_no = int(input("Enter task number to delete: "))
                deleted = tasks.pop(task_no - 1)
                print(f"Deleted task: {deleted['task']}")
            except (ValueError, IndexError):
                print("Invalid task number!")

    elif choice == "5":
        print("Thank you for using the To-Do List Application.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")