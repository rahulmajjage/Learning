#Demonstarte Positional Parameters and keywork Arguments and default values.

# Function for Positional Parameteres

def birthday1 (name,age):
    print ("\nHi", name, "you are now ", age, "years old\n\n")


# Function for Default values

def birthday2 (name = "Jackson", age = 1):
    print ("\nHi", name, "you are now ", age, "years old\n\n")

#Main program

# Postional Arguements and positional parameteres

birthday1 ("Jackson",1)
birthday1 (1,"Jackson")

# Positional Parameters and Keyword Arguements

birthday1 (name = "Jackson", age = 1)
birthday1 (age = 1, name = "Jackson")

# Default Values

birthday2 ()

# Default values and Keyword Arguements

birthday2 (name = "Rahul")
birthday2 (age = 29)
birthday2 (name = "Rahul", age = 29)

# Third call also be done by: 

birthday2 ("Rahul",12)

input ("Press Enter to exit")
