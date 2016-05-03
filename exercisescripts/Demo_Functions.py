#Demonstrate  Functions

#Function definition
def instructions ():
    """display game instructions"""
    print (\
        """
Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
This will be showdown between your human brains and silicon processor

You will make your move known by entering a number, 0 - 8. The number
will correspond to the board position as illustrated:

                            0 | 1 | 2
                           -----------
                            3 | 4 | 5
                           -----------
                            6 | 7 | 8

Prepare ypurseld, HUMAN. The ultimate battle is about to begin. \n """)


#Main

print ("Here are the instructions to the Tic-Tac-Toe game:")
instructions ()
print ("Here they are again")
instructions ()

input ("Press Enter to exit")
