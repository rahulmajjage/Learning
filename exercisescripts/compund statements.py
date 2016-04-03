#Using Compound conditions
#Network Demo

print ("\t\tWelcome!!!! \n\n \t\tMemebers only")
Security = 0
username = ""
while not username:
    username = input ("Enter Username: ")
password = ""
while not password:
    password = input ("Enter Password: ")
if username == "a" and password == "abcd":
    print ("Hi a !!!")
    Security=2
elif username == "b" and password == "bcde":
    print ("Hi b !!!")
    Security=3
elif username == "c" and password == "cdef":
    print ("Hi c !!!")
    Security=5
elif username == "guest" and password == "guest":
    print ("Welcome guest !!!")
    Security=1
else:
    print ("Login failed, Not a member")
input ("Press enter to exit")
