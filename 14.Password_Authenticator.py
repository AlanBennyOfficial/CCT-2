#  Write a program that asks for a username and password, then checks if they match stored values to allow login.

stored_user = "admin" 
stored_pass = "password123" 
user = input("Enter username: ") 
password = input("Enter password: ") 

if user == stored_user and password == stored_pass: 
    print("Login successful") 
else: 
    print("Login failed")