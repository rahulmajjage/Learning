#Demonstrate Global variables

# Reading a global variable inside a function

def function1():
    print ("\nThe value in function 1 is", value)

# Shadowing a global variable inside a function

def function2():
    value = -10
    print ("\nThe value in function 2 is", value)

# Changing a global variable inside a function

def function3():
    global value
    value = -20
    print ("\nThe value in function 3 is", value)

# Main Program

value = 10

print ("\n\nThe value in main program is", value)

function1 ()

print ("\n\nThe value after function 1 is", value)

function2 ()

print ("\n\nThe value after function 2 is", value)

function3 ()

print ("\n\nThe value after function 3 is", value)

input ("\nPress Enter to exit")
