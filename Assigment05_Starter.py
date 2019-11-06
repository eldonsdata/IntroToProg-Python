# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PShoup,11.6.2019,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
open(objFile, "a")
objFile = open(objFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0], "Priority": strData[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Current Task List: \n", dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("What task would you like to add?: ")
        if strTask not in dicRow:
            strPriority = input("What's the task priority level?: (low, medium, high)")
            dicRow[strTask] = strPriority
            print('\n', strTask, "has been added.")
        else:
            print("\nThat task already exists, try adding a new task or deleting an existing task")
        continue
    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        print("Current Task List: ", dicRow)
        strDelete = input("What task do you want to delete?: ")
        if strDelete in dicRow:
            del dicRow[strDelete]
            print("Updated Task List:", dicRow)
        else:
            print("\nThe task", strDelete, "doesn't exist in the dictionary.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        objFile.write(str(dicRow))
        objFile.close()
        print("Data saved to file.")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting program")
        break  # and Exit the program
