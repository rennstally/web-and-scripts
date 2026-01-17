import datetime

tasks = []

while True:
    action = input("\nChoose: add / remove / done / sort / quit: ").strip().lower()

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

    else:
        print("Invalid action!")

    print("\nYour tasks:")
    if not tasks:
        print("(no tasks)")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "(done)" if t["done"] else "(not done)"
            print(f"{i}. {t['description']} {status} | Due: {t['due']}")
