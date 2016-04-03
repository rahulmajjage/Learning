#Exercise 2.4
base_price= int (input ("Please Enter the base price of the car: "))
tax= float (base_price*8.25/100)
license_cost= float (base_price*10/100)
dealer_prep= 1000
dest_crg=1000
Act_price=base_price+tax+license_cost+dealer_prep+dest_crg
print ("Tax is: ", tax)
print ("License cost is: ", license_cost)
print ("Dealer Prep is: ", dealer_prep)
print ("Dest Charge is: ", dest_crg)
print ("Actual Price of car is:  ", Act_price)
input ("Press Enter to Exit")
