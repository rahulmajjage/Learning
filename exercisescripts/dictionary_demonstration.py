#Demonstrate Dictionaries
words = {"python":"is a programming language",
         "element":"Is used in physics",
         "difficult":"Opposite of easy",
         "answer":"Is a response to a question",
         "xylophone":"It is a musical instrument"}
choice = None

# get () function testing
print ("Testing the get () function!!!\n\n")
element = input ("Enter a word to check if it is available in dictionary: ")
if element in words:
    print ("\nWord is present in dictionary")
else:
    print ("\n\t",words.get (element, "not an elemnt of dictionary"))
while (choice != "0"):
    print (\
        """
\t Demonstration of using dictionaries
0: Quit
1: Look up a word
2: Add a word
3: Redefine a word
4: Delete a word
5: Dislay the contents of dictionary
""")
    choice = input ("Choice: ")
    if (choice == "0"):
        print ("\nGood  bye")

# Getting a value
    elif (choice == "1"):
        word = input ("Enter the word you wan to look up: ")
        if word in words:
            print ("The definition of", word, "is: ",words[word])
        else:
            print ("Word not present in dictionary")

#Adding a key-value pair
    elif (choice == "2"):
        word = input ("Enter the word you want to add: ")
        if word not in words:
            definition = input ("Enter the definition of the new word: ")
            words [word] = definition
            print ("\n", word, "Added\n")
        else:
            print ("\n Word is already present in the dictionary")

#Redifine a word
    elif (choice == "3"):
        word = input ("Enter the word to be redifined: ")
        if word in words:
            definition = input ("Enter the new definition of the word: ")
            words [word] = definition
            print ("\n", word, "definition is modified")
        else:
            print ("\nWord is not present in the dictionary")

#Delete a key-value pair
    elif (choice == "4"):
        word = input ("Enter the word to be deleted: ")
        if word in words:
            del words [word]
            print ("\n", word, "Ha been deleted")
        else:
            print ("\nWord is not present in the dictionary")
#Display the contents of dictionary
    elif (choice == "5"):
        for item in words:
            print ("\n\n",item, "\t", words [item])

#Invalid option
    else:
        print ("Invalid option")

input ("Press enter to exit")
        
        
        
