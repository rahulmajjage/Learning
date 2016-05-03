#Demonstrate Argument passing and return values

#Function Receiveing value through Parameters
def display (message):
    print (message)


#Function Returning value
def give_me_five ():
    five = 5
    return five

#Function Receiveing value and returning as well
def ask_yes_no (question):
    Response = None
    while Response not in ("y", "n"):
        Response = input (question).lower ()
    return Response

#Main Program

display ("\n\nHere's a message for you.\n")

number = give_me_five ()
print ("\n\nThe give_me_five() function gave me: ", number)

answer = ask_yes_no ("\n\nPlease enter 'y' or 'n': ")
print ("\n\nThanks for entering: ", answer)

input ("\n\nPress enter to exit")



