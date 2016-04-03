#Exercise 3.3
import random
print ("\t\tWelcome!!!! \n\n \t\tLets Play the Random Game")
print ("Guess the Random number between 1-100 Chosen by computer")
c_num = random.randrange (100)+1
tries=1
p_num = int (input ("Please guess the random number: "))
while p_num != c_num and tries<= 5:
    if p_num > 100:
        print ("You entered an invalid number")
        p_num = int (input ("Please guess the right random number: "))
        
    elif p_num > c_num:
        print ("Your Guess is higher")
        p_num = int (input ("Please guess the lower random number again: "))
        tries+=1
        if tries > 5:
            break
    else:
        print ("Your Guess is lower")
        p_num = int (input ("Please guess the higher random number again: "))
        tries+=1
        if tries > 5:
            break
if tries <= 5:
    print ("Congrats !!!!, The right number was", p_num)
    print ("You took", tries, "tries\n")   
else:
    print("You Lost!!! exceeded the total number of tries")
    print ("The right number was", c_num)
#   print ("Congrats !!!!, The right number was", p_num)
#   print ("You took", tries, "tries\n")
input ("Press enter to exit")
