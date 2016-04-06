# The Jumble word game
# The computer picks a random word and jumbles it.
# The player needs to guess the exact word

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
guess = input ("\nGuess the word: ")
guess = guess.lower ()
while (guess != correct) and (guess != ""):
    print ("I am sorry Wrong Guess, Try again\n\n")
    guess = input ("\nGuess the word: ")
    guess = guess.lower ()
if guess == correct:
    print ("Congrats!!! You have guessed it right.\n\n")
print ("Thanks for playing\n\n")
input ("Press Enter to exit")
