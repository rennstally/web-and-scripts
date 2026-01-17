tasks = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for t in tasks:
            line = f"{t['description']}|{t['done']}\n"
            file.write(line)
    print("Tasks saved to tasks.txt!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks.clear()
            for line in file:
                description, done_str = line.strip().split("|")
                done = True if done_str == "True" else False
                tasks.append({"description": description, "done": done})
        print("Tasks loaded!")
    except FileNotFoundError:
        print("No saved file found.")

def show_tasks():
    print("\nCurrent tasks:")
    if not tasks:
        print("(no tasks)")
        return
    for i, t in enumerate(tasks, start=1):
        status = "(done)" if t["done"] else "(not done)"
        print(f"{i}. {t['description']} {status}")

while True:
    show_tasks()
    action = input("\nChoose: add / remove / done / save / load / quit: ").strip().lower()

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

    elif action == "save":
        save_tasks()

    elif action == "load":
        load_tasks()

    else:
        print("Invalid action!")

print("\nGoodbye!")
