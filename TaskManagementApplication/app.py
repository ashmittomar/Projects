def task():
    tasks = []
    print("--- WELCOME TO THE TASK MANAGEMENT APP ---")

    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks: {tasks}")

    while True:
        print("\nPlease choose an option:")
        print("1 - Add Task")
        print("2 - Update Task")
        print("3 - Delete Task")
        print("4 - View All Tasks")
        print("5 - Exit")

        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1-5.")
            continue

        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' has been updated to '{up}'.")
            else:
                print(f"Task '{updated_val}' not found!")

        elif operation == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print(f"Task '{del_val}' not found!")

        elif operation == 4:
            if tasks:
                print(f"Current tasks: {tasks}")
            else:
                print("No tasks available.")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input! Please enter a number between 1-5.")


task()
