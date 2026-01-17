import datetime

tasks = []

def show_tasks():
    print("\nYour tasks:")
    if not tasks:
        print("(no tasks)")
        return

    for i, t in enumerate(tasks, start=1):
        status = "(done)" if t["done"] else "(not done)"
        print(f"{i}. {t['description']} {status} | Due: {t['due']}")

while True:
    show_tasks()
    action = input("\nChoose: add / remove / done / sort / search / edit / quit: ").strip().lower()

    if action == "quit":
        break

    elif action == "add":
        description = input("Enter task: ").strip().lower()
        due = input("Enter due date (YYYY-MM-DD): ").strip()

        try:
            datetime.datetime.strptime(due, "%Y-%m-%d")   
        except ValueError:
            print("Invalid date format!")
            continue

        tasks.append({"description": description, "done": False, "due": due})
        print("Task added!")

    elif action == "remove":
        num = int(input("Task number to remove: "))
        index = num - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task removed!")
        else:
            print("Invalid task number!")

    elif action == "done":
        num = int(input("Task number to mark as done: "))
        index = num - 1

        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")
   
    elif action == "sort":
        print("Sort by: description / due / status")
        how = input("Choose sorting method: ").strip().lower()

        if how == "description":
            tasks.sort(key=lambda t: t["description"])
        elif how == "due":
            tasks.sort(key=lambda t: t["due"])
        elif how == "status":
            tasks.sort(key=lambda t: t["done"])
        else:
            print("Invalid sort choice!")

    elif action == "search":
        keyword = input("Enter keyword to search: ").strip().lower()
        print("\nSearch results:")

        found = False
        for i, t in enumerate(tasks, start=1):
            if keyword in t["description"]:
                status = "(done)" if t["done"] else "(not done)"
                print(f"{i}. {t['description']} {status} | Due: {t['due']}")
                found = True
        
        if not found:
            print("No matching tasks found.")

    elif action == "edit":
        num = int(input("Enter task number to edit: "))
        index = num - 1

        if 0 <= index < len(tasks):
            new_desc = input("New description (leave blank to keep): ").strip().lower()
            if new_desc:
                tasks[index]["description"] = new_desc

            new_due = input("New due date YYYY-MM-DD (leave blank to keep): ").strip()
            if new_due:
                try:
                    datetime.datetime.strptime(new_due, "%Y-%m-%d")
                    tasks[index]["due"] = new_due
                except ValueError:
                    print("Invalid date format! Due date not changed.")
            
            print("Task updated!")
        else:
            print("Invalid task number!")

    else:
        print("Invalid action!")
