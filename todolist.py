def add_task(todo_list, task):
    """
    Add a task to the to-do list.
    """
    todo_list[task] = False
    print(f"Task '{task}' added.")

def view_tasks(todo_list):
    """
    View all tasks in the to-do list.
    """
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, (task, completed) in enumerate(todo_list.items(), start=1):
            status = "✔" if completed else "❌"
            print(f"{index}. [{status}] {task}")

def complete_task(todo_list, task_index):
    """
    Mark a task as completed.
    """
    try:
        task = list(todo_list.keys())[task_index - 1]
        todo_list[task] = True
        print(f"Task '{task}' marked as completed.")
    except IndexError:
        print("Invalid task index.")

def delete_task(todo_list, task_index):
    """
    Delete a task from the to-do list.
    """
    try:
        task = list(todo_list.keys())[task_index - 1]
        del todo_list[task]
        print(f"Task '{task}' deleted.")
    except IndexError:
        print("Invalid task index.")

def main():
    todo_list = {}

    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            view_tasks(todo_list)
            task_index = int(input("Enter the index of the task to mark as completed: "))
            complete_task(todo_list, task_index)
        elif choice == '4':
            view_tasks(todo_list)
            task_index = int(input("Enter the index of the task to delete: "))
            delete_task(todo_list, task_index)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()