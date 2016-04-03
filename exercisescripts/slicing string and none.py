#Pizza slice Program
#Demonstrate slicing a string and none 

word = "pizza"
print ("Please enter the beginning and ending values of the pizza slice")
print ("Press enter at begin: to exit")
begin = None
while begin != "":
    begin = input ("Begin: ")
    if begin:
        begin = int(begin)
        end = int (input ("End: "))
        print ("Word [", begin, ":", end,"]\t\t", word[begin:end])

input("Press enter to exit")
