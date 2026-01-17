tasks = []

while True:
    action = input("\nChoose: add / remove / done / quit: ").strip().lower()

    if action == "quit":
        break

    elif action == "add":
        description = input("Enter task to add: ").strip().lower()

        
        if any(t["description"] == description for t in tasks):
            print("Task already exists!")
        else:
            tasks.append({"description": description, "done": False})
            print("Task added!")

    elif action == "remove":
        description = input("Enter task to remove: ").strip().lower()

        for t in tasks:
            if t["description"] == description:
                tasks.remove(t)
                print("Task removed!")
                break
        else:
            print("Task not found!")

    elif action == "done":
        description = input("Enter task to mark as done: ").strip().lower()

        for t in tasks:
            if t["description"] == description:
                t["done"] = True
                print("Task marked as done!")
                break
        else:
            print("Task not found!")
    
    else:
        print("Invalid action!")


print("\nYour tasks:")
for t in tasks:
    status = "(done)" if t["done"] else "(not done)"
    print("-", t["description"], status)
