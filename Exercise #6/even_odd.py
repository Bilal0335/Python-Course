
#! Even or Odd Number Checker

# num:int = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#! Grade Calculator

# marks:float = float(input("Number of marks: "))
# grade = ''
# if marks < 0 or marks > 100:
#     print("Invalid input! Marks should be between 0 and 100.")
# else:
#     if marks >= 90:
#         grade = 'A'
#     elif marks >= 80:
#         grade = 'B'
#     elif marks >= 70:
#         grade = 'C'
#     elif marks >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#     print(f"Your grade is {grade}.")    


#! Age Verifier (Voting Eligibility)

# use_age:int = int(input("Enter Your Age:"));
# if use_age > 18:
#     if use_age == 18:
#         print("You are eligible to vote but it is your first time.")
#     else:
#         print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

#! Positive, Negative, or Zero Checker

# try:
#     num:int = int(input("Enter a number: "))
#     if num > 0:
#         print("This is a positive number.")
#     elif num < 0:
#         print('this is a negative number.')
#     else:
#         print('This is zero.')
# except ValueError:
#     print("Invalid input! Please enter a number.")


# ! Largest of Three Numbers

# try:
#     a:int = int(input("Enter first number: "))
#     b:int = int(input("Enter second number: "))
#     c:int = int(input("Enter third number: "))

#     if a == b == c:
#         print("All numbers are equal.")
#     elif a >= b and a >= c:
#         print(f"{a} is the largest number.")
#     elif b >= c and b >= a:
#         print(f"{b} is the largest number.")
#     else:
#         print(f"{c} is the largest number.")
# except ValueError:
#     print("Invalid input! Please enter numbers only.")

#! 🛠 Mini Project: Number Guessing Game
import random

# Random number generate karna (1 se 100 tak)
# secret_number = random.randint(1, 100)


# print("🎯 Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 100.")

# while True:
#     try:
#         guess = int(input("Enter your guess: "))
        
#         if guess < 1 or guess > 100:
#             print("❌ Please enter a number between 1 and 100.")
#         elif guess < secret_number:
#             print("📉 Too low! Try again. Increase your number.")  
#         elif guess > secret_number:
#             print("📈 Too high! Try again. Decrease your number.") 
#         else:
#             print(f"🎉 Congratulations! You guessed the correct number: {secret_number}")
#             break 
            
#     except ValueError:
#         print("⚠️ Invalid input! Please enter a numeric value.")

while True:
    num = int(input("Enter a number: "))
    
    if num == 50:
        print("🎉 Correct! You found the number.")
        break  # ✅ Loop ends here
    else:
        print("❌ Wrong! Try again.")
