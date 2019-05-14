# ---
# Title: creating a simple handling script
# Dev: DTorres
# Date: May 12,2019
# ChangeLog: (Who, When, What)
#   DTorres, 5/12/2019, created handling script
# ---
import pickle  # here I importted pickle

dicRow = {}  # I created a dictionary, but you can use any object
ObjFile = open("dict.pickle", "wb")  # here I create/open a file in the pickled fomart (write its)
pickle.dump(dicRow, ObjFile)  # here we dumped our data to the pickled file
ObjFile.close

while True:  # while true do not end the script
    try:
        # if you enter a number the script will accept and the code will end since the condition is not false
        x = int(input("Please enter a number: "))
        dicRow = {"ID": x}
        break
    except Exception as e:  # if any letters or numbers with decimals it will keep asking for a whole number
        print(e)
