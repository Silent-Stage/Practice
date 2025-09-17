import os, json, random, math
from fractions import Fraction

FILENAME = "Task Project.json"

# if file doesn't exist, create it with an empty list
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        json.dump([], f)

# now load it
with open(FILENAME, "r") as f:
    tasks = json.load(f)

    # The file where tasks will be saved

FILENAME = "Task Project.json"

# Load tasks from file if it exists

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

archlogo = r"""
      /\
     /  \  
    /    \
   /  ||  \ 
  /   ,,   \ 
 /   |  |   \
/_-''    ''-_\
    -ARCH-
    """


def taskmanager():
    # this function adds the changes made by the user to the JSON file to save it
    def add_memory(tasks):
        with open(FILENAME, "w") as f:
            json.dump(tasks, f, indent=4)

    # this function prints the list of tasks

    def see_list(plc):
        for i, task1 in enumerate(plc, start=1):
            print(f"\nTask {i}:\n{task1}\n")

    def add_task():
        task = input(
            "(Use comma to add multiple, enter 0 to go back)\nAdd task: ")
        if task == "0":
            tasklist()
        else:
            date = input("When is it due: ")
            task_list = task.split(",")
            date_list = date.split(",")
            for t, d in zip(task_list, date_list):
                tasks.append(t.strip() + " (Due: " + d.strip() + ")")

    # this function removes the task of the index the user input

    def rem_task(plc):
        rem = input("(Enter 0 to go back)\nRemove task: ").strip()
        if rem == "0":
            tasklist()
        else:
            for delete in sorted(rem.split(","), reverse=True, key=lambda x:
                                 int(x.strip())):
                plc_del = int(delete.strip()) - 1
                if 0 <= plc_del < len(plc):
                    del plc[(plc_del)]

    # this function adds -DONE to the task of the users choosing, if input is outside of the index of the list, it tells the user, if it returns a ValueError, it tells the user to try again

    def done_task(plc):
        while True:
            try:
                don = input("(Enter 0 to go back)\nCompleted task: ")
                if don == "0":
                    tasklist()
                else:
                    if 1 <= int(don) <= len(plc):
                        plc[int(don) - 1] += " -DONE"
                        break
                    else:
                        print("Task number out of range")
            except ValueError:
                print("Enter a number bronado")

    def tasklist():
        print(f"{archlogo}\n1. Add task\n2. View task\n3. Mark task as completed\n4. Delete task\n5. Random task\n6. Exit")
        try:
            choice = int(input())
        except ValueError:
            print("\n\nPick 1-6 brotato\n")
        if choice == 1:
            add_task()
            add_memory(tasks)
            tasklist()
        elif choice == 2:
            see_list(tasks)
            tasklist()
        elif choice == 3:
            see_list(tasks)
            done_task(tasks)
            add_memory(tasks)
            tasklist()
        elif choice == 4:
            see_list(tasks)
            rem_task(tasks)
            add_memory(tasks)
            tasklist()
        elif choice == 5:
            rand = random.choice(tasks)
            print("\nTo do:", rand, "\n")
            tasklist()
        elif choice == 6:
            print(" ")
            menu()
        else:
            print("\n\nPick 1-6 brotato\n")

    tasklist()


def analyzefunc():
    type = int(input("\n1. Quadratic Equation\n2. Exit\n"))
    if type == 1:
        variables = input("a(x)^2 + b(x) + c\na, b, c = ")
        var = variables.split(",")
        a, b, c = [Fraction(v.strip())
                   for v in var]
        axis = (-1 * b) / (2 * a)
        vert = (a * (axis ** 2)) + (b * axis) + c
        if a > 0:
            pos = f"Minimum: ({vert}, ∞)"
            pos2 = "decreasing"
            pos3 = "increasing"
        elif a < 0:
            pos = f"Maximum: (-∞, {vert})"
            pos2 = "increasing"
            pos3 = "decreasing"
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            xints = f"{x1}, {x2}"
        elif discriminant == 0:
            xints = f"{-b / (2*a)}"
        else:
            xints = "No real x-intercepts"
        print(f"\nAxis of symmetry: {axis}\nVertex: {axis}, {vert}\n{pos}\nFunction is {pos2} to the left of {axis} and {pos3} to the right of {axis}\nX-intercept(s): {xints}")
    elif type == 2:
        calculator()


def calculator():
    userint = int(input(f"{archlogo}\nMenu:\n1. Analyze Function\n2. Exit\n"))
    if userint == 1:
        analyzefunc()
    elif userint == 2:
        menu()
    else:
        print("Invalid option")


def menu():
    opt = int(input("\nMenu:\n1. Arch Task Manager\n2. Arch Calculator\n"))
    if opt == 1:
        taskmanager()
    elif opt == 2:
        calculator()
    else:
        print("Pick 1-2 bro")


menu()
