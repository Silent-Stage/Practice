import os
import json
import random
import math
import requests
from fractions import Fraction
from bs4 import BeautifulSoup

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "Task Project.json")

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME2 = os.path.join(BASE_DIR, "DBDscrapelist.json")
 
if os.path.exists(FILENAME2):
    with open(FILENAME2, "r") as f:
        saved = json.load(f)
else:
    saved = {}

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
        print("\n1. Add task\n2. View task\n3. Mark task as completed\n4. Delete task\n5. Random task\n6. Exit")
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
        pos = ""
        pos2 = ""
        pos3 = ""
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
        print(
            f"\nAxis of symmetry: {axis}\nVertex: {axis}, {vert}\n{pos}\nFunction is {pos2} to the left of {axis} and {pos3} to the right of {axis}\nX-intercept(s): {xints}")
    elif type == 2:
        calculator()


def calculator():
    userint = int(input("\nMenu:\n1. Analyze Function\n2. Exit\n"))
    if userint == 1:
        analyzefunc()
    elif userint == 2:
        menu()
    else:
        print("Invalid option")


class Killerstats:
    def __init__(self, name, power, speed, terrorradius, height):
        self.name = name
        self.power = power
        self.speed = speed
        self.terrorradius = terrorradius
        self.height = height


def add_memory(saved):
    with open(FILENAME, "w") as f:
        json.dump(saved, f, indent=4)


def savekiller(killer):
    saved[killer.name] = (
        f"Power - {killer.power}\n"
        f"Speed - {killer.speed}\n"
        f"Terror Radius - {killer.terrorradius}\n"
        f"Height - {killer.height}"
    )
    add_memory(saved)


def scrape_page(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    # Get alias name (The Hillbilly) from <title>
    title_tag = soup.find("title")
    if title_tag:
        full_title = title_tag.get_text(strip=True)
        # Example: "Max Thompson Jr. — The Hillbilly - Official Dead by Daylight Wiki"
        if "—" in full_title:
            name = full_title.split("—")[1].split("-")[0].strip()
        else:
            name = full_title.split("-")[0].strip()
    else:
        name = "Unknown"

    # Defaults
    power = speed = terrorradius = height = "Unknown"

    # Loop over all tables
    tables = soup.find_all("table")
    for table in tables:
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) < 2:
                continue
            label = cells[0].get_text(" ", strip=True).lower()
            value = cells[1].get_text(" ", strip=True)

            # Other stats
            if "power" in label and "attack" not in label:
                power = value
            elif "movement speed" in label or "speed" in label:
                speed = value
            elif "terror radius" in label:
                terrorradius = value
            elif "height" in label:
                height = value
    return Killerstats(name, power, speed, terrorradius, height)


def printscrape():
    inp1 = input("1. Add Killer\n2. View Killer list\n")
    if inp1 == "1":
        url = input("Enter a Dead by Daylight wiki.gg killer URL: ")
        killer = scrape_page(url)
        print(f"\nName: {killer.name}")
        print(f"Power: {killer.power}")
        print(f"Speed: {killer.speed}")
        print(f"Terror Radius: {killer.terrorradius}")
        print(f"Height: {killer.height}\n")
        inp2 = input("Save Killer? (y/n)\n").strip().lower()
        if inp2 == "y":
            savekiller(killer)
            print(f"{killer.name} saved!\n")
        elif inp2 == "n":
            print("Not saved.\n")
    elif inp1 == "2":
        for name, stats in saved.items():
            print(f"\n{name}\n{stats}\n")


def menu():
    opt = int(
        input(archlogo + "\nMenu:\n1. Arch Task Manager\n2. Arch Calculator\n3. DBD Stats\n"))
    if opt == 1:
        taskmanager()
    elif opt == 2:
        calculator()
    elif opt == 3:
        printscrape()
    else:
        print("Pick 1-2 bro")


menu()
