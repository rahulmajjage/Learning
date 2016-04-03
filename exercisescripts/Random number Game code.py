#Random number game code
import random
print ("\t\tWelcome!!!! \n\n \t\tLets Play the Random Game")
print ("Guess the Random number Chosen by computer")
c_num = random.randrange (100)+1
p_num = int (input ("Please guess the random number: "))
tries=1
while p_num != c_num:
    if p_num > c_num:
        print ("Your Guess is higher")
        p_num = int (input ("Please guess the lower random number again: "))
        tries+=1    
    else:
        print ("Your Guess is lower")
        p_num = int (input ("Please guess the higher random number again: "))
        tries+=1 
print ("Congrats !!!!, The right number was", p_num)
print ("You took", tries, "tries\n")
input ("Press enter to exit")
