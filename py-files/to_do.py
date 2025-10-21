class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print("The task was added successfully!")
    
    def delete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            deleted = self.tasks.pop(index)
            print(f"The task '{deleted}' was deleted successfully!")
        else:
            print("Invalid task number!")
    
    def list_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks in the list!")
        else:
            print("\n--- Your Tasks ---")
            for i in range(len(self.tasks)):
                print(f"{i + 1}. {self.tasks[i]}")
            print("------------------\n")


my_list = TodoList()

while True:
    print("\n=== TODO LIST MENU ===")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. List Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        task_name = input("Enter the task name: ")
        my_list.add_task(task_name)
    
    elif choice == "2":
        my_list.list_tasks()
        if len(my_list.tasks) > 0:
            task_number = int(input("Enter the task number to be deleted: "))
            my_list.delete_task(task_number - 1)
    
    elif choice == "3":
        my_list.list_tasks()
    
    elif choice == "4":
        print("Exiting from the program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")