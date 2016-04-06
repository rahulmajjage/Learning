#Exercise 4.1

print ("\t\tCounting numbers!!!\n\n")

begin = int (input ("Enter the starting point: "))
end = int (input ("Enter the ending point: "))
count = int (input ("Enter the Amount by which to count: "))
for i in range (begin,end,count):
    print(i)
input ("Press enter to exit")
