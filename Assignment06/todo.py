#-------------------------------------------------#
# Title: todo Script, with functions
# Dev: DTorres
# Date: May 5,2019
# ChangeLog: (Who, When, What)
#   DTorres, 5/5/2019, created script

#-------------------------------------------------#

strData = ""
dicRow = {}
lstTable = []


def showTodoList():
    print("******* The current items ToDo are: *******")
    for row in lstTable:
        print(row["Task"] + "(" + row["Priority"] + ")")
    print("*******************************************")


def addNewItem():
    strTask = str(input("What is the task? - ")).strip()
    strPriority = str(input("What is the priority? [high|low] - ")).strip()
    dicRow = {"Task": strTask, "Priority": strPriority}
    # print(dicRow, "hellooo")
    lstTable.append(dicRow)
    # print(lstTable, "herrrrrreeeeeee")
    print("Current Data in table:")
    for dicRow in lstTable:
        print(dicRow)

    # 4a Show the current items in the table
    print("******* The current items ToDo are: *******")
    for row in lstTable:
        print(row["Task"] + "(" + row["Priority"] + ")")
    print("*******************************************")


def deleteItem():
    # 5a-Allow user to indicate which row to delete
    strKeyToRemove = input("Which TASK would you like removed? - ")
    blnItemRemoved = False  # Creating a boolean Flag
    intRowNumber = 0
    while(intRowNumber < len(lstTable)):
        # the values function creates a list!
        if(strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):
            del lstTable[intRowNumber]
            blnItemRemoved = True
        # end if
        intRowNumber += 1
    # end for loop
    # 5b-Update user on the status
    if(blnItemRemoved == True):
        print("The task was removed.")
    else:
        print("I'm sorry, but I could not find that task.")

    # 5c Show the current items in the table
    print("******* The current items ToDo are: *******")
    for row in lstTable:
        print(row["Task"] + "(" + row["Priority"] + ")")
    print("*******************************************")


def saveData():
    print("******* The current items ToDo are: *******")
    for row in lstTable:
        print(row["Task"] + "(" + row["Priority"] + ")")
    print("*******************************************")
    # 5b Ask if they want save that data
    if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
        objFile = open("todo.txt", "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        input("Data saved to file! Press the [Enter] key to return to menu.")
    else:
        input(
            "New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")


# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
objFile = open("Todo.txt", "r")
for line in objFile:
    strData = line.split(",")  # readline() reads a line of the data into 2 elements
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# Step 2
# Display a menu of choices to the user
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3
    # Show the current items in the table
    if (strChoice.strip() == '1'):
        showTodoList()

    # Step 4
    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        addNewItem()

    # Step 5
    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        deleteItem()

    # Step 6
    # Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        saveData()

    elif (strChoice == '5'):
        break  # and Exit the program
