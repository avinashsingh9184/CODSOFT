# To-Do List Application (Command Line)

tasks = []

def show_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✔ Done" if task['done'] else "Not Done"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task name: ")
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added successfully!")

def mark_done():
    show_tasks()
    try:
        task_no = int(input("\nEnter task number to mark as done: "))
        tasks[task_no - 1]['done'] = True
        print(" Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def update_task():
    show_tasks()
    try:
        task_no = int(input("\nEnter task number to update: "))
        new_title = input("Enter new task title: ")
        tasks[task_no - 1]['title'] = new_title
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f" Task '{removed['title']}' deleted!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def menu():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print(" Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()