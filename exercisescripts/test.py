#Using intentional infine loops
#break and continue statements demo

count=0
while True:
    count+=1
    if count > 10:
        break
#    print (count)
    if count == 5:
        continue
    print (count)
input ("Press enter to exit")
