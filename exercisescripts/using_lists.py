#Inventory Program
#Demonstrate creating lists and displaying elements using for loop
#Demonstrate len fn, in operator, index, slice and concatination

inventory = ["sword", "armor", "shield", "healing position"]
#Print the elements of list

print ("Elements of list are:")
for item in inventory:
    print (item)
input ("\nPress Enter to continue")

#Using the len () to get the length of list

print ("The inventory has", len (inventory), "items in possession\n\n")

#using the in operator to check membership

if "healing position" in inventory:
    print ("You will live to fight another day\n\n")

#display one item through index

index = int (input ("Enter the index number for an element in the inventory: "))
print ("Element at index", index, "is", inventory [index] )

#displaying a slice

begin = int (input ("Enter index to begin slice: "))
end = int (input ("Enter index to end slice: "))
print ("Inventory [", begin, ":", end, "]\t\t", inventory[begin:end])
input ("\nPress Enter to continue")

#Concatinating two lists

chest = ["gold", "gems"]
print ("New invetory chest has: ", chest)
print ("Adding chest to the inventory\n\n")
inventory += chest
print ("The new inventory now contains: ", inventory)
input ("\nPress Enter to continue")



