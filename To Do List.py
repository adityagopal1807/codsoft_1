class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")

    def mark_task_completed(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]['completed'] = True
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        print("--------------------------------------") 
        
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
        print("-------------------------------------")     


if __name__ == "__main__":
    main()