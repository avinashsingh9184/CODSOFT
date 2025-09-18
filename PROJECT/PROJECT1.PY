tasks = []

def show_tasks():
    if not tasks:
        print("\n✅ Your to-do list is empty.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. {task['task']} [{status}]")

def add_task():
    task_name = input("\n➕ Enter a new task: ")
    if task_name.strip() == "":
        print("⚠️ Task cannot be empty!")
        return
    tasks.append({"task": task_name, "done": False})
    print("✅ Task added successfully!")

def mark_done():
    show_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("\n✔ Enter task number to mark as done: "))
        tasks[task_no - 1]["done"] = True
        print("🎉 Task marked as done!")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number!")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("\n🗑 Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"🗑 Deleted task: {removed['task']}")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number!")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("👉 Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()