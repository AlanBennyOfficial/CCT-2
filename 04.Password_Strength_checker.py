# Develop a program that asks the user for a password and checks if it is strong based on length and character variety (uppercase, numbers, special characters). 

password = input("Enter a password: ") 
if len(password) < 8: 
    print("Weak password: Too short!") 
elif password.isalpha() or password.isdigit(): 
    print("Weak password: Use a mix of letters and numbers!") 
else: 
    print("Strong password!")