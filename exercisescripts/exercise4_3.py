# The Jumble word game
# The computer picks a random word and jumbles it.
# The player needs to guess the exact word
#Exercise 4.3

import random

WORDS = ("element","python","difficult","answer","xylophone")
#Picks one word randomly from the sequence
word = random.choice(WORDS)
# To check if the plaer's word is right.
correct = word

# To jumble a randomly chosen word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble+=word[position]
    word = word[:position]+word[(position+1):]
# Take input from user
print ("Hello Player!!!\n\n")
print (\
      """
          Welcome to the Jumble word game!!

        Unscramble the letters to make the word
    (Press the enter key at the prompt to quit)
    """)
print ("The Jumbled word is: ", jumble)
guess = input ("\nGuess the word: or press enter for hint: ")
guess = guess.lower()
count = 0
while (guess == ""):
    if correct == WORDS[0]:
        print ("It is used in Physics")
        guess = input ("\nGuess the word: ")
        guess = guess.lower ()
        count+=1
    elif correct == WORDS[1]:
        print ("It is scripting language")
        guess = input ("\nGuess the word: ")
        guess = guess.lower ()
        count+=1
    elif correct == WORDS[2]:
        print ("It is opposite of easy")
        guess = input ("\nGuess the word: ")
        guess = guess.lower ()
        count+=1
    elif correct == WORDS[3]:
        print ("you use it when asked a question")
        guess = input ("\nGuess the word: ")
        guess = guess.lower ()
        count+=1
    else:
        print ("It is a musical instrument")
        guess = input ("\nGuess the word: ")
        guess = guess.lower ()
        count+=1
guess = guess.lower ()       
while (guess != correct):
    print ("I am sorry Wrong Guess, Try again\n\n")
    guess = input ("\nGuess the word: ")
    guess = guess.lower ()
if guess == correct and count ==0:
    print ("Congrats bonus points!!! You have guessed it right without a hint.\n\n")
else:
    print ("Congrats!!! You have guessed it right after using the hint. No bonus points\n\n")
print ("Thanks for playing\n\n")
input ("Press Enter to exit")
