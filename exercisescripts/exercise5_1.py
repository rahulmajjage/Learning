#Exercise 5.1
# Print all the words in list randomly without repeating
import random
WORDS = ["one", "two", "three", "four", "five", "six"]
word = random.choice (WORDS)
count = len (WORDS)
print ("\n", count, "\n")
while (word in WORDS):
    print (word)
    WORDS.remove(word)
    count -= 1
#    print ("\n\nNew count", count)
    if count != 0:
        word = random.choice (WORDS)
input ("Press Enter to exit")
