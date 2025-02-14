tasks=[]
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}'added.")

def view_tasks():
    if tasks:
        print("Your tasks:")
        for idx,task in enumerate(tasks,1):
            print(f"{idx}.{task}")

    else:
        print("No tasks to show.")
def remove_task(task_number):
    if 0< task_number <= len(tasks):
        removed_task=tasks.pop(task_number-1)
        print(f"Task'{removed_task}'removed.")
    else:
        print("Invalid task number.")
def main():
    while True:
        print("\nOptions: 1. Add Task 2.View Tasks 3.Remove Task 4.Exit")
        choice=input("enter yoour choice:")

        if choice=='1.':
            task=input("Enter task: ")
            add_task(task)
        elif choice=='2.':
            view_tasks()
        elif choice == '3.':
            task_number=int(input("Enter task number to remove: "))
            remove_task(task_number)
        elif choice =='4.' :
            print("Exiting..")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
                  main()
