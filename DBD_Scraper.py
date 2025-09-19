import requests
import os
import json
from bs4 import BeautifulSoup

FILENAME = "DBDscrapelist.json"
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        saved = json.load(f)
else:
        saved = {}

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
    opt1 = input("1. Add Killer\n2. View Killer list\n")
    if opt1 == "1":
        url = input("Enter a Dead by Daylight wiki.gg killer URL: ")
        killer = scrape_page(url)
        print(f"\nName: {killer.name}")
        print(f"Power: {killer.power}")
        print(f"Speed: {killer.speed}")
        print(f"Terror Radius: {killer.terrorradius}")
        print(f"Height: {killer.height}\n")
        opt2 = input("Save Killer? (y/n)\n").strip().lower()
        if opt2 == "y":
            savekiller(killer) 
            print(f"{killer.name} saved!\n")
        elif opt2 == "n":
            print("Not saved.\n")
    elif opt1 == "2":
        for name, stats in saved.items():
            print(f"\n{name}\n{stats}\n")
printscrape()
