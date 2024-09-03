# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

shopping_list=[]

def add_item(shopping_list):
    item = input("Enter an item to add: ")
    shopping_list.append(item)
    print(f"{item} added to shopping list")

def remove_item(shopping_list):
    item = input("Enter an item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from shopping list")
    else:
        print(f"{item} does not exist in shopping list")

def print_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(item)

while True:
    print("Enter \"1\" To Add An Item")
    print("Enter \"2\" To Remove An Item")
    print("Enter \"3\" To Display Full Shopping List")
    print("Enter \"4\" To Exit")
    action = int(input())
    if action==1:
        add_item(shopping_list)
    elif action==2:
        remove_item(shopping_list)
    elif action==3:
        print_list(shopping_list)
    elif action==4:
        print("Exiting")
        break
    else:
        print("Not a valid choice.")