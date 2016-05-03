# The Jumble word game
# The computer picks a random word and jumbles it.
# The player needs to guess the exact word

import random

WORDS = ("element","python","difficult","answer","xylophone")
#Picks one word randomly from the sequence
word = random.choice(WORDS)

# Take input from user
print ("Hello Player!!!\n\n")
print (\
      """
          Welcome to the Random word game!!

        Guess the word picked randomly by computer
    (Press the enter key at the prompt to quit)
    """)

if word == WORDS[0]:
    print ("It is a", len(word), "letter word\n\n")

elif word == WORDS[1]:
    print ("It is a", len(word), "letter word\n\n")

elif word == WORDS[2]:
    print ("It is a", len(word), "letter word\n\n")

elif word == WORDS[3]:
    print ("It is a", len(word), "letter word\n\n")

else:
    print ("It is a", len(word), "letter word\n\n")

# Ask the player to check if a letter is there in the word 5 times
print ("You have 5 chances to check if a particular letter is present in the word\n\n")
for i in range (5):
    letter = input ("Enter the letter to check: ")
    letter = letter.lower()
    if letter in word:
        print ("\nYes the letter is present in word\n\n")
    else:
        print ("\nNo the letter is not present in word\n\n")

# Tell the player to start guessing now

guess = input ("\nGuess the word: ")
guess = guess.lower ()
while (guess != word) or (guess == ""):
    print ("I am sorry Wrong Guess, Try again\n\n")
    guess = input ("\nGuess the word: ")
    guess = guess.lower ()
# Conratualte the player for the correct guess

if guess == word:
    print ("Congrats!!! You have guessed it right.\n\n")
    print ("The right word is: ", guess)
print ("Thanks for playing\n\n")
input ("Press Enter to exit")
