# Write a program that takes the total bill amount and the tip percentage from the user, then calculates the tip and final bill amount. 

bill = float(input("Enter bill amount: ")) 
tip_percent = float(input("Enter tip percentage:")) 

if bill < 0 or tip_percent < 0: 
    print("Bill and tip percentage must be positive.") 
else: 
    tip = (tip_percent / 100) * bill
 
print("Tip amount:", tip) 
print("Total bill:", bill + tip)  