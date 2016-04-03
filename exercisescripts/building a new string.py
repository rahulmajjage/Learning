#No Vowels Program
#Demonstrate buildina a new string

message = input("Please enter the message: ")
new_message = ""
VOWEL = "aeiou"

for letter in message:
    if letter.lower() not in VOWEL:
        new_message += letter
        print ("New string created is: ", new_message)
print ("New message without Vowels is: ", new_message)
input("Press enter to exit")
