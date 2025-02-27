# Program to add digits of a number


number = input("Enter a two-digit number: ")  
digit_1 = int(number[0]) 
digit_2 = int(number[1]) 

print("Sum of digits:", digit_1 + digit_2)

# Second Method to add digits of a number
number = int(input("Enter a two-digit number: "))  
digit_1 = number // 10  
digit_2 = number % 10   

print("Sum of digits:", digit_1 + digit_2)
