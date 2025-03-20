# Create a program that asks for the distance traveled and calculates the fare based on predefined rates. 

distance = int(input("Enter distance traveled in km: ")) 

if distance < 0: 
    print("Distance cannot be negative!") 
    fare=0 
elif distance <= 5: 
    fare = 10 
elif distance <= 15:
    fare = 25 
else: 
    fare = 40 

print("Your fare is:", fare) 