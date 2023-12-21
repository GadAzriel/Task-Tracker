#This project is a simple task tracker
#Gad Azriel

#Help structure for the task
class Add_task:
    def __init__(self, num, title, description, due_date,is_complete):
        self.num = num
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_complete = False

#Func that print all the tasks
def print_all(tasks):
      for task in tasks:
        print("\nTask number: " + str(task.num))
        print("Title: " + task.title)
        print("Description: " + task.description)
        print("Date: " + task.due_date)
        print("Complete: " + str(task.is_complete) + "\n")

def main():
    print("Hello, welcome to creating your task tracker.")
    tasks = []
    i = 1
    num = 1
    while num > 0:
        print("\nTask Tracker Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            tasks.append(Add_task(i, title, description, due_date,False))
            i = i + 1
        elif choice == '2':
            print_all(tasks)
        elif choice == '3':
            num = int(input("What is the task number you would like to delete: "))
            if 1 <= num <= len(tasks):
                del tasks[num - 1]
            else:
                print("Invalid task number.")
        elif choice == '4':
            num = int(input("What is the task number that you would like to mark as complete: "))
            if 1 <= num <= len(tasks):
                tasks[num-1].is_complete = True
            else:
                print("Invalid task number.")
        elif choice == '5':
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
main()

