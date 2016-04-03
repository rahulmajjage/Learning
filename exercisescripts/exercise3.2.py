#Exercise 3.2
import random
print ("\t\tWelcome!!!! \n\n \t\tLet's calculate Heads and tails today")
flips = int (input ("Enter the number of flips, between 1-100: "))
heads = 0
tails = 0
num=1
while num <= flips:
    c_num = random.randrange(2)+1
    if c_num == 1:
        heads+=1
        num+=1
    else:
        tails+=1
        num+=1
print ("Total Heads: ", heads)
print ("Total Tails: ", tails)
input ("Press enter to exit")
