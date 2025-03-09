
#! Temperature Checker

try:
    temp = float(input("Enter Temperature in Celsius: "))
    
    if temp < 10:
        print("It's very cold! Wear a jacket. 🧥")
    elif temp < 25:
        print("The weather is pleasant. 🌤️")
    elif temp < 35:
        print("It's getting hot! Stay hydrated. 💧")
    else:
        print("It's too hot! Avoid going outside. ☀️")
except Exception as e:
    print("Invalid input! Please enter a number.")
