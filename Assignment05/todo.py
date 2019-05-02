# ---
# Title: todo Script
# Dev: DTorres
# Date: April 28,2019
# ChangeLog: (Who, When, What)
#   DTorres, 4/28/2019, created script
# ---

fob = open('todo.txt', 'r')  # opens the file we are working with
list = {}  # this creates a dictonary where our info will go
for line in fob:  # here we created a for loop to get items into the dictonary
    item = line.split(',')
    list[item[0]] = item[1]
fob.close()
list_obj = [list]  # here we made the dictonary into a list, making easier to add and delete
menu_item = 0  # here we are creating a list of options the user can select
while menu_item <= 4:  # here were saying that that if any number is high than 4 none of the while loop will work
    print("Menu of Options")
    print("1. Show current data")
    print("2. Add a new item")
    print("3. Remove an existing item")
    print("4. Save Data to File")
    print("5. Exit Program")
    menu_item = int(input("pick an item from the menu:"))
    if menu_item == 1:  # here were displaying our current information
        current = 0
        if len(list_obj) > 0:
            while current < len(list_obj):
                print(list_obj[current])
                current = current + 1
    elif menu_item == 2:  # here we are addiing info to the dictonary but are not saving
        task = input("enter the name of the task:")
        priority = input("enter the priority of the task:")
        list[task] = priority + "\n"
        menu_item = 0
    elif menu_item == 3:  # this is where I had the most issue, whenever I tried to find the index of the item it kept saying item not found in list
        delete = input("which name would you like to remove:")
        if delete in list:
            item_number = list_obj.index(delete)
        else:
            print(delete, "was not found")
    elif menu_item == 4:  # here we saved the information to the text file
        fob = open('todo.txt', 'w')
        fob.write(str(list))
        print(" Data saved!")
        fob.close()
print("goodbye")
