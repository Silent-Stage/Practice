# Enter python practice.py into the terminal to see the output of the code
import random
import os
import json
character = "Joseph"
age = 12
myage = 15
if age > myage:
    print("date")
else:
    print("not date")
# elements is each letter in a string or the entire number assigned to a variable
# len() returns the amount of elements in a variable
print("1", len(character))
# brackets with a number returns the element in the index of your choosing
print("2", character[1])
# brackets with a colon return any part of a variable, depending on the amount and which index you use
print("3", character[0:3])
print("4", character[:4])
print("5", character[:])
# adding \n adds a line break, placing the remainder of the string on the next line down
char1 = "Python \nProgramming"
print("6 ", char1)
# an f string is a function in which calling it runs any variables in the {}, instead of using + or something
first = "Joseph"
last = "Richmond"
full = f"{first} {last}"
print(full)
# .title makes the first letter uppercase
print("7", character.title())
# .strip removes all white strips, .lstrip removes all white strips at the beginning, .rstrip removes all white strips at the end
print("8", character.strip())
# .find finds the index of the first letter that you input in the function
print("9", character.find("my"))
# .replace, replaces all of the letters of the first string with that of the second in the function
print("10", character.replace("m", "j"))
# the in function looks for those letters or whatever in the variable that you call after th in function
print("11", "mj" in character)
# not in is the reverse value of in
print("12", "jo" not in character)
# .index() finds the index of an element inside of a list or string
print("13", character.index("p"))
# 1 / is normal division, // rounds the number down
print(10/3)
print(10//3)
# 2 * is to the power of
print(10**3)

# for...in assigns a value to the variable you put after "for", and the value is each element variable after "in", and it updates each time, going in order through each element in the variable after "in"

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# cypher_amt = 4
# password = input("Password:")
# encrypted = ""
# for char in password.lower():
#     if char in alphabet:
#         index = alphabet.find(char)
#         new_index = (index + cypher_amt) % len(alphabet)
#         new_char = alphabet[new_index]
#         encrypted += new_char
#     else:
#         encrypted += char
# print("Original Password:", password)
# print("Encrypted Password:", encrypted)

# += shortens adding a number to a variable, round() rounds a number, abs() returns the absolute value of a number

# x = float(input("x = :"))
# operator = input("Operator: ")
# y = float(input("y = :"))
# if operator == "+":
#     result = x + y
# elif operator == "-":
#     result = x - y
# elif operator == "*":
#     result = x * y
# elif operator == "/":
#     if y != 0:
#         result = x / y
#     else:
#         result = "Error"
# else:
#     result = "Error"
# print("Answer:", result)

# the range() function runs whatever loop for every integer within that range

# my_age = int(input("How old are you? "))
# their_age = int(input("How old are they? "))

# if my_age in range(0, 17):
#     if their_age in range(0, 17):
#         print("Can date")
#     elif their_age in range(18, 116):
#         print("Cannot date, it is illegal")
# elif my_age in range(18, 116):
#     if their_age in range(18, 116):
#         print("Can date")
#     elif their_age in range(0, 17):
#         print("Cannot date, it is illegal")

# the function .append(), adds whatever is inside the parenthesis to whatever variable that is before .append

num = []
num.append(4)
print(num)

num1 = ""
num1 += str(4)
print(num1)

# number = int(input())
# even_amt = 0
# odd_amt = 0
# even_list = []
# odd_list = []
# string = ""
# for i in range(1, number + 1):
#     string += str(i)
#     if i % 2 == 0:
#         even_amt += 1
#         even_list.append(i)
#     else:
#         odd_amt += 1
#         odd_list.append(i)
# print(f"There are {even_amt} even numbers and {odd_amt} odd numbers")
# print(f"Even Numbers: {even_list}\nOdd Numbers: {odd_list}")

# row_amt = int(input())
# def triangle(shift):
#     for row in range(1, row_amt + 1):
#         spaces = " " * (row_amt - row + shift)
#         numbers = "*" * (2 * row - 1)
#         spaces_2 = (" " * (shift + row_amt - row)) + (" " * ((row_amt - row)))
#         print(f"{spaces}{numbers}{spaces_2}{numbers}")


# triangle(5)
# triangle(10)
# triangle(15)
# triangle(20)
# triangle(25)


# The file where tasks will be saved
FILENAME = "Task Project.json"
# Load tasks from file if it exists
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        tasks = json.load(f)
else:
    tasks = []
# this function adds the changes made by the user to the JSON file to save it


def add_memory(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)
# this function prints the list of tasks


def see_list(plc):
    for i, task1 in enumerate(plc, start=1):
        print(f"\nTask {i}:\n{task1}\n")
# this function removes the task of the index the user input


def rem_task(plc):
    rem = int(input("Remove task: "))
    del plc[int(rem) - 1]
# this function adds -DONE to the task of the users choosing, if input is outside of the index of the list, it tells the user, if it returns a ValueError, it tells the user to try again


def done_task(plc):
    while True:
        try:
            don = int(input("Completed task: "))
            if 1 <= don <= len(plc):
                plc[don - 1] += " -DONE"
                break
            else:
                print("Task number out of range")
        except ValueError:
            print("Enter a number bronado")


# while True: continually prints the menu
while True:
    print("\n\nMENU:\n1. Add task\n2. View tasks\n3. Mark task as done\n4. Delete task\n5. Random task\n6. Exit")
    try:
        choice = int(input())
    except ValueError:
        print("\n\nPick 1-6 brotato\n")
        continue
    if choice == 1:
        task = input("Add task: ")
        tasks.append(task)
        add_memory(tasks)
    elif choice == 2:
        see_list(tasks)
    elif choice == 3:
        see_list(tasks)
        done_task(tasks)
        add_memory(tasks)
    elif choice == 4:
        see_list(tasks)
        rem_task(tasks)
        add_memory(tasks)
    elif choice == 5:
        rand = random.choice(tasks)
        print("\n", rand, "\n")
        input("\nDo it brochacho\n")
    elif choice == 6:
        print("\n\nSee ya brotein\n")
        break
    else:
        print("\n\nPick 1-6 brotato\n")
