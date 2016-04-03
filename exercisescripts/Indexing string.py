#Random Access Program
#Demonstrate indexing strings

import random
word = "index"
high = len(word)
low = -len(word)
for i in range (10):
    position=random.randrange(low, high)
    print ("word [", position, "]\t", word[position])

input("Press enter to exit")
