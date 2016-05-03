# Hangman program
# Guess the word randomly chosen by computer. If you exceed maximum tries you will be hanged.

import random

# Constant

HANGMAN = (
    """
        ------
        |    |
        |    
        |  
        |  
        |  
        |  
        |  
        |
    ----------""",
    """
        ------
        |    |
        |    0
        |  
        |    
        |    
        |   
        |   
        |
    ----------""",
    """
        ------
        |    |
        |    0
        |   -+-
        |    
        |    
        |   
        |   
        |
    ----------""",
    """
        ------
        |    |
        |    0
        |  /-+-
        |    
        |    
        |   
        |   
        |
    ----------""",
    """
        ------
        |    |
        |    0
        |  /-+-/
        |    
        |    
        |   
        |   
        |
    ----------""",
    """
        ------
        |    |
        |    0
        |  /-+-/
        |    |
        |   
        |   
        |   
        |
    ----------""",
    """
        ------
        |    |
        |    0
        |  /-+-/
        |    |
        |    |
        |    |
        |    |
        |
    ----------""",
    """
        ------
        |    |
        |    0
        |  /-+-/
        |    |
        |    |
        |   |  |
        |   |  |
        |
    ----------""")

#Get maximum wrong tries number
#MAX_WRONG = len(HANGMAN)-1
MAX_WRONG = 7

# Create the words list to choose from
WORDS = ("ELEMENT","PYTHON","DIFFICULT","ANSWER","XYLOPHONE")

# CHOOSE THE RANDOM WORD
word = random.choice (WORDS)

# Create a variable so_far to hold the word so far result
so_far = "-"*len (word)# is filled with dashes

# Create variable wrong to hold the total number of wrong guesses
wrong=0

# Create a list to hold the letters used
used = []

print ("Welcome to the hangman Game\n\n")

while (wrong < MAX_WRONG) and (so_far != word):
    print ("\n", HANGMAN[wrong])
    print ("\n\nYou have already used the letters: ", used)
    print ("\n\n The word so far is: ", so_far)

#Start taking the guesses from the user.
    guess = input ("Guess the letter: ")
    guess = guess.upper()

#Check if the letter is already used
    while guess in used:
        print ("\nThe letter", guess, "is already used\n")
        guess = input ("Guess the letter: ")
        guess = guess.upper()
    used.append(guess)

# Check if the guess is present in word
    if guess in word:
        print ("\nYES!", guess, "is in word\n")
        new = ""
        for i in range (len(word)):
            if (guess == word[i]):
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print ("\nSORRY", guess,"is not in word")
        wrong+=1

# Ending the game
if wrong == MAX_WRONG:
    print ("\n",HANGMAN[wrong])
    print ("You are hanged!!")
else:
    print ("\nYou have guessed it!!!")
    print ("The correct word is: ", word)

input ("\n\nPress enter tot exit")
            
    
        
    




