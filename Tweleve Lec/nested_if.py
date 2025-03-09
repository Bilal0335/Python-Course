# Nested If Else & elif Statements in Python

#! Example 1: Age Verification

# age:int = int(input("Enter Your age: "))

# if age >= 18:
#     print("You are an adult.")
#     if age>=60:
#         print("You are a senior citizen.")
#     else:
#         print("You are not a senior citizen.")
# else:
#     print("You are a minor.")

#! Example 2: Login System

# user_name = 'bilal123'
# password = 'BilalCode123'

# input_user_name = input("Enter User Name: ")

# if input_user_name == user_name:
#     user_password = input("Enter Password: ").lower()
    
#     if user_password == password:
#         print("Login Successful!")
        
#     else:
#         print("Incorrect password!")
# else:
#     print("User not found!")


# !🔹 Mini Project: ATM System (Using Nested if)
'''
✅ Features:

** User PIN enter karega.
** Agar PIN sahi hai, toh menu show hoga (Balance Check, Withdraw, Deposit).
** Agar PIN galat hai, toh access deny hoga.
** Nested if ka use hoga har step pe.
'''
# 🔹 Predefined PIN and Balance
correct_pin = "1234"
balance = 5000  

# 🔹 User enters PIN
user_pin = input("Enter your 4-digit PIN: ")

if user_pin == correct_pin:
    print("\n✅ PIN Verified! Welcome to Your ATM.")

    print("\n🏦 ATM Menu:")
    print("1️⃣ Check Balance")
    print("2️⃣ Withdraw Money")
    print("3️⃣ Deposit Money")
    
    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        print(f"\n💰 Your current balance is: Rs.{balance}")

    elif choice == "2":
        withdraw_amount = int(input("\nEnter amount to withdraw: "))
        
        if withdraw_amount > balance:
            print("\n❌ Insufficient balance!")
        else:
            balance -= withdraw_amount
            print(f"\n✅ Rs.{withdraw_amount} withdrawn successfully.")
            print(f"💰 Updated Balance: Rs.{balance}")

    elif choice == "3":
        deposit_amount = int(input("\nEnter amount to deposit: "))
        
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"\n✅ Rs.{deposit_amount} deposited successfully.")
            print(f"💰 Updated Balance: Rs.{balance}")
        else:
            print("\n❌ Invalid amount! Enter a positive number.")
    
    else:
        print("\n❌ Invalid choice! Please select 1, 2, or 3.")

else:
    print("\n❌ Incorrect PIN! Access Denied.")
