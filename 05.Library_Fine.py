# Create a program that calculates a library fine based on the number of late days. The fine should increase with more delayed days.

due_days = int(input("Enter number of days late: ")) 

if due_days < 0: 
    print("Days late cannot be negative!") 
    fine = 0  # Assign a default value to avoid NameError
elif due_days <= 5: 
    fine = due_days * 2 
elif due_days <= 10: 
    fine = due_days * 5 
else: 
    fine = due_days * 10 

print("Total fine is:", fine)