# Create a program that simulates an ATM cash withdrawal. The user enters an amount, and the program checks if they have sufficient balance before allowing the withdrawal.

balance = 5000 
withdraw = int(input("Enter amount to withdraw: ")) 

if withdraw < 0: 
    print("Invalid amount! Enter a positive number.") 
elif withdraw > balance: 
    print("Insufficient balance!") 
else: 
    balance -= withdraw 

print("Withdrawal successful. Remaining balance:", balance) 