objFile = open("Customers.txt", "r+")  # see page 193
print("Here is the current data:")
print(objFile.read())

print("Type in a Customer Id and Name you want to add to the file")
print("(Enter 'Exit' to quit!)")

while(True):
    Id = input("Enter the Id: ")
    Name = input("Enter name: ")
    strUserInput = Id + ", " + Name

    SaveData = input("Would you like to exit? (yes/no): ")
    if(SaveData.lower() == "yes"):
        objFile.write(strUserInput + "\n")
        break
    # elif(Name.lower() == "exit"):
    #     break
    else:
        objFile.write(strUserInput + "\n")

print("Here is this data was saved:")
objFile.seek(0)
print(objFile.read())
objFile.close()
