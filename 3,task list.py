class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_name):
        self.tasks.append(task_name)
        print(f"Task '{task_name}' created successfully!")

    def read_tasks(self):
        print("Current tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def update_task(self, task_index, new_task_name):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task_name
            print(f"Task updated successfully!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Create task")
        print("2. Read tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_manager.create_task(task_name)
        elif choice == "2":
            task_manager.read_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to update: "))
            new_task_name = input("Enter new task name: ")
            task_manager.update_task(task_index, new_task_name)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            task_manager.delete_task(task_index)
        elif choice == "5":
            print("Exiting the task manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
