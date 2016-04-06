#Exercise 4.2

print ("\t\tReversing an user entered message!!!\n\n")

word = input ("Enter a message: ")
high = len (word)-1

new_word = ""
for letter in word:
    new_word += word[high]
    high-=1
print ("Reversed message is: ", new_word)
input ("Press enter to exit")
