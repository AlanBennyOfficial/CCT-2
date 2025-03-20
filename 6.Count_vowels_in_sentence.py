# Write a program that asks for a sentence and counts the number of vowels (a, e, i, o, u) present in it.

sentence = input("Enter a sentence: ") 
vowels = "aeiouAEIOU" 
count = 0 

for char in sentence: 
    if char in vowels: 
        count += 1 
print("Number of vowels:", count)