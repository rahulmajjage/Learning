# Inventory program
# Demontrate Tuples
inventory = ()
if not inventory:
    print ("The inventory is empty")
input ("Press enter to continue")
inventory = ("Element",
             "One",
             "Two",
             "Three")
print ("\n The invetory list now is:\n", inventory)
for item in inventory:
    print (item)
input ("Press Enter to exit")
