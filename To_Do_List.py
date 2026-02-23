# To-Do List Manager with File Saving

# Function to save tasks to file
def save_tasks(tasks):
    file = open("tasks.txt", "w")
    
    for task in tasks:
        file.write(task["name"] + "|" + str(task["done"]) + "\n")
    
    file.close()

# Function to load tasks from file
def load_tasks():
    tasks = []
    
    try:
        file = open("tasks.txt", "r")
        for line in file:
            name, done = line.strip().split("|")
            task = {
                "name": name,
                "done": done == "True"
            }
            tasks.append(task)
        file.close()
    except FileNotFoundError:
        pass
    
    return tasks

# Load tasks at start
tasks = load_tasks()

# Main loop
while True:

    print("\n---- TO DO LIST MANAGER ----")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # View tasks
    if choice == "1":
        if not tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(tasks, start=1):     
                if task["done"]:
                    status = "Complete"
                else:
                    status = "Not Complete"
                
                print(f"{i}. {task['name']} - {status}")

    # Add task
    elif choice == "2":
        task_name = input("Enter task name: ")
        task = {
            "name": task_name,
            "done": False
        }
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully")

    # Mark complete
    elif choice == "3":
        if not tasks:
            print("No tasks available")
        else:
            task_number = int(input("Enter task number: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["done"] = True
                save_tasks(tasks)
                print("Task marked complete")
            else:
                print("Invalid task number")

    # Delete task
    elif choice == "4":
        if not tasks:
            print("No tasks available")
        else:
            task_number = int(input("Enter task number: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                save_tasks(tasks)
                print("Task deleted successfully")
            else:
                print("Invalid task number")

    # Exit
    elif choice == "5":
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Invalid choice, Try again!")