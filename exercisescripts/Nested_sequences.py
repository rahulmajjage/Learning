# High scores 2.0
# Demonstrate Nested Sequences

scores= []
choice = None

#Print game

while choice !="0":
    print (\
        """
\t High scores keeper
0: Quit
1: List scores
2: Add a score
""")
    choice = input ("Choice: ")

#Exit
    if choice == "0":
        print ("\nEnd game")

# Displaying the scores
    elif choice == "1":
        print ("\nName\tScores")
        if scores:
            for entry in scores:
                score, name = entry
                print (name, "\t", score)
        else:
            print ("No entries yet")

#Adding the new scores by appending nested sequences
    elif choice == "2":
        name = input ("\nEnter the name of the player: ")
        score = int (input ("\nHow much did the player score: "))
        entry = (score,name)
        scores.append (entry)
        scores.sort ()
        scores.reverse ()

#invalid choice
    else:
        print ("\nInvalid choice")

input ("Press enter to exit")
        
        
    
