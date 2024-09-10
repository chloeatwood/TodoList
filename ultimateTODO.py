# <Chloe Atwood>             <4/5/2024>
# <Assignment 5>
# <Description> : Creating to todo list program that takes in items to make a list of items need to be done
                    #You can move these items, delete them, and save them to a list


import sys
import pickle

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("The Ultimate TODO List!")
    print()

    print("By: <Chloe Atwood>")
    print("[COM S 127 <A>]")
    print()

def initList():
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def checkIfListEmpty(todoList):
    """This function checks if there are any entries in the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean: If there is at least one item in the data structure, return False - it is not empty. Otherwise return True.
    """
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True

def saveList(todoList):
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    itemFound = False
    keyName = ""
    index = -1
    # TODO: Iterate through all the keys in the dictionary and check each list of each key to  
    # see if an item is present. If it is, set itemFound to be 'True.' Then, set the keyName variable  
    # to the key where the item was found, and the index in the list where the item was found. 
    # If the item is not found in any of the lists in the dictionary, keep the default values above. 
    # Return the itemFound boolean, the keyName string, and the index integer (1 pt.)
    for key, lst in todoList.items():
        if item in lst:
            itemFound = True
            keyName = key
            index = lst.index(item)
            break
    
    return itemFound, keyName, index

def addItem(item, toList, todoList):
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary
    # of lists. If the item is not in the Dictionary of Lists, add it to the list specified by the 'toList'
    # variable. If the item is already in the Dictionary of Lists, print an error message specifying:
    # - the name of the item
    # - the keyName of the list where the item is found
    # - the index of the item in the list
    # Return the todoList data structure after it has been modified (or not) (1 pt.)

    itemFound, keyName, index = checkItem(item, todoList)

    if not itemFound:
        todoList[toList].append(item)
        print("Item {} added to the list {}" .format(item, toList))
    else:
        print("ERROR: Item {} already exists in the list {} at the index {}" .format(item, keyName, index))

    return todoList

def deleteItem(item, todoList):
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """
    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary
    # of lists. If the item is already in the Dictionary of Lists, delete that item. If the item is not
    # in the Dictionary of Lists, print an error message specifying:
    # - the name of the item
    # Return the itemFound boolean and the todoList data structure after it has been modified (or not) (1 pt.)
    itemFound, keyName, index = checkItem(item, todoList)
    
    if itemFound:
        todoList[keyName].remove(item)
        print("The item {} has been deleted from the list {}" .format(item, keyName))
    else:
        print("Item {} was not found in any list" .format(item))



    return itemFound, todoList

def moveItem(item, toList, todoList):
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    # TODO: Use the deleteItem function to search for/ delete the specified item. Use the itemFound boolean
    # it returns to determine if the item was found. If it was, use the addItem function to add the item to  
    # the specified toList key.
    # Return the todoList data structure after it has been modified (or not) (1 pt.)
    itemFound, todoList = deleteItem(item, todoList)
    if itemFound:
        addItem(item, toList, todoList)
        print("Item moved")

    
    return todoList

def printTODOList(todoList):
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """
    # TODO: Iterate through all the keys in the dictionary and print both the key and the list the dictionary
    # holds for that key on a single line on the screen.
    # ex: todo: ['laundry', 'dishes']
    # Return None (1 pt.)
    for key, value in todoList.items():
        print(key, ": ", value)

    return None

def runApplication(todoList):
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            # TODO: Prompt the user to enter an item, and take in that input as a string. Call the addItem function
            # to add the item to the 'backlog' key's corresponding list. Finally, use the printTODOList function
            # to print the todoList data structure. (1 pt.)
            item = str(input("Please enter an Item:"))
            addItem(item, 'backlog', todoList)
            printTODOList(todoList)
            pass
        elif choice == "m":
            # TODO: Use the provided checkIfListEmpty() function to check to see if any of the lists in the data 
            # structure have items in them. 
            x = checkIfListEmpty(todoList)
            # If checkIfListEmpty() returns False, meaning that at least one of the lists in the dictionary has 
            # an item in it, do the following:
            # - Prompt the user to enter an item, and take in that input as a string.
            # - Use the checkItem function to confirm if that item is in the data structure.
            # - While the item is not in the data structure, print an error message stating the item does not exist
            #   and then prompt the user to enter a different item. Use the checkItem function again to confirm if 
            #   the new item is inside the data structure.
            # - Prompt the user to enter a dictionary key for the list to move the item to, and take in that input 
            #   as a string.
            # - While the dictionary key the user specifies is not a key that is in the dictionary, print an error
            #   message stating that the key does not exist. Then, prompt the user to enter a new dictionary key.
            # - Call the moveItem function, passing the item, dictionary key, and todoList as arguments.
            if x == False:
                item = str(input("Please enter an item:"))
                itemFound, keyName, index = checkItem(item, todoList)
                if itemFound == False:
                    while True:
                        print('ERROR: Item not found!!!')
                        item = str(input("Please enter a new item:"))
                        itemFound, keyName, index = checkItem(item, todoList)
                        if itemFound == True:
                            break


                location = str(input("Please enter the key you would like to move the object too:"))
                i = 0
                y = False
                while i < len(todoList): 
                    for key in todoList:
                        if location == key:
                            print("HI")
                            print(location)
                            moveItem(item, location, todoList)
                            y = True
                        i = i + 1
                            
                if y == False:
                    while True:
                        print("ERROR: THAT LOCATION DOES NOT EXIST!!!!!")
                        location = str(input("Please eneter the desired location of your item:"))
                        i = 0
                        while i < len(todoList):
                            for key in todoList:
                                if location == key:
                                    print(location)
                                    moveItem(item, location, todoList)
                                    x = True
                                i = i + 1
                            if x == True:
                                break
                            break
                        break
                    
                    

                    
                    
            else:
                print("ERROR: NO ITEMS TO MOVE!!!!!")

            printTODOList(todoList)

        
            # If all of the lists in the dictionary are empty, print an error message that states 'No items to move!' 
            # or something similar.
            #
            # Finally, whether or not the data structure is totally empty or not, call the printTODOList function
            # and print out the data structure. (1 pt.)
            pass
        elif choice == "d":
            # TODO: Use the provided checkIfListEmpty() function to check to see if any of the lists in the data 
            # structure have items in them. 
            x = checkIfListEmpty(todoList)
            # If checkIfListEmpty() returns False, meaning that at least one of the lists in the dictionary has 
            # an item in it, do the following:
            if x == False:
            # - Prompt the user to enter an item, and take in that input as a string. 
                while True:
                    item = str(input("Please enter an item:"))
            # - Call the deleteItem function to remove the item from the data structure if it is present. 
                    itemFound, keyName, index = checkItem(item, todoList)
                    if itemFound == True:
                        itemFound, todoList = deleteItem(item, todoList)
                        break
            else:
                print("No item to delete \n")

            # If all of the lists in the dictionary are empty, print an error message that states 'No items to move!' 
            # or something similar.
            #
            # Finally, whether or not the data structure is totally empty or not, call the printTODOList function
            # and print out the data structure. (1 pt.)
            printTODOList(todoList)
            #
            # HINT: the deleteItem function returns two (2) values - do you actually need to do things with both of them?
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False

    printTitleMaterial()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()