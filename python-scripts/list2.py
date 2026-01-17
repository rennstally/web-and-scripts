tasks = []

def show_menu():
    print("\n------- TO-DO LIST -------")
    print("1. Add task")
    print("2. Wiew task")
    print("4. Quit the program")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        

    elif choice == "2":
        for i, tasks in enumerate(task, start=1):
            print(i, "-", task)
                 
    elif choice == "3":
       elif choice == "3":
    if not tasks:
        print("No tasks to remove!")
        continue 

    num = int(input("Enter task number to remove: "))

    if 1 <= num <= len(tasks):
        removed_task = tasks.pop(num - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number!")

        
    elif choice == "4":
        break

    else:
        print("Invalid choice")

shit place