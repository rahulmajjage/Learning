#Exercise 5.3
#Daddy_Son_Program

# Daddy_Son Dictionary

daddy_son = { "Rahul" : "Shivalingappa",
              "Nikita" : "Ramesh",
              "Rohit" : "Rachappa" }


#To display the name of Father with Son's name

son = input  ("\n\nEnter the name of son to get the father name: ")

if son in daddy_son:
    print ("\nFather of", son , "is:\t", daddy_son[son])

else:
    print ("\nSon not in list\n")

print ("\n\n")
#Display menu
choice = None

while choice != 0:
    print ("""\
                 0: Quit
                 1: Add
                 2: Delete
                 3: Replace
                 4: List Sons
                 5: List Fathers
                 6: List daddy son pair""")
    choice = int (input ("\n\nEnter your choice: "))
    if choice == 0:
        print ("\n\n Good Bye")

#Adding new entry
        
    elif choice == 1:
        son_new = input ("\n\nEnter the name of the son to be added: ")
        if son_new not in daddy_son:
            daddy_new = input ("\n\nEnter the name of the father: ")
            daddy_son [son_new] = daddy_new
        else:
            print ("\n\nThe name of Son is already present")

# Deleting an entry

    elif choice == 2:
        son_new = input ("\n\nEnter the name of the son to be deleted: ")
        if son_new in daddy_son:
            del daddy_son [son_new]
        else:
            print ("\n\nThe name of Son is already present")

#Replacing an entry

    elif choice == 3:
        son_new = input ("\n\nEnter the name of the son whose father needs to be replaced: ")
        if son_new in daddy_son:
            daddy_new = input ("\n\nEnter the name of the new father: ")
            daddy_son [son_new] = daddy_new
        else:
            print ("\n\nThe name of Son is already present")

#Displaying only the list of Sons

    elif choice == 4:
        print ("\n\nThe name of all the sons are:", daddy_son.keys())
        
#Displaying only the list of Fathers

    elif choice == 5:
        print ("\n\nThe name of all the Fathers are:", daddy_son.values())

#Displaying only the list of Sons and father pair

    elif choice == 6:
        print ("\n\nThe name of all the sons are:", daddy_son.items())

#Invalid entry

    else:
        print ("\n\nYou have entered an invalid entry")

input ("\n\nPress Enter to exit")


