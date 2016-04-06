# Demontrate Tuples concatination, indexing, slicing and using len () and in operator.
inventory = ("Element",
             "One",
             "Two",
             "Three")
print ("\n The invetory list is:\n", inventory)

# demonstarte using len ()
print ("\n\nThe inventory has", len(inventory), "elemnts\n")
# Demonstrate indexing
index = int (input ("\n\nEnter the index number of the elemnt to print in inventory: "))
print ("\nThe elemnt at index", index, "is: ", inventory[index])

#demonstrate Slicing
begin = int (input ("\nEnter the Begin position of slice: "))
end = int (input ("\nEnter the End position of slice: "))
print ("\nThe Inventory [", begin, ":", end, "]is: ",inventory[begin:end])

# Demonstarte in operator
ele = input ("Enter the element to check: ")
if ele in inventory:
    print ("\n\nThe element is present in Inventory\n")
else:
    print ("\n\nThe Element is not present\n")

#Demonstrate Concatination of tuples
inventory2 = ("Four", "Five")
print ("\nThe new Inventroy is: ", inventory2)
inventory += inventory2
print ("\n\nThe new concatinated inventory tuple is:\n", inventory)
print ("\nThe inventory has", len(inventory), "elemnts now")
input ("\nPress Enter to exit")
