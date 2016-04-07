#High Scores program
#Demonstrate List methods


#Create an empty list
scores = []
choice = None

#Print the options

while choice !="0":
    print (\
        """
\t High Scores Keeper
0: Exit
1: Show score
2: Add a score
3: Delete a score
4: Sort scores
""")
    choice= input ("Choice: ")
# Exit
    if (choice == "0"):
        print ("\nGood bye")

# Show scores
    elif (choice == "1"):
        print ("\nHigh Scores:")
        for score in scores:
            print (score)

# Adding a score
    elif (choice == "2"):
        score = int (input("\nEnter the score you wish to add: "))
        scores.append(score)

#Deleting a score
    elif (choice == "3"):
        score = int (input ("\nEnter the score you want to delete: "))
        if score in scores:
            scores.remove(score)
            print ("\nRemoved", score)
        else:
            print ("\n", score, "Entered is not one of the high scores.")

# Sorting the scores
    elif (choice == "4"):
        scores.sort()

# As scores are sorted in ascending order and program needs high scores first
#We will reverse the list after sorting
        scores.reverse()
        print ("\nScores after sorting are:\n", scores)
    else:
        print ("\nInvalid option entered")

input ("\nPress enter to exit")
        
    
