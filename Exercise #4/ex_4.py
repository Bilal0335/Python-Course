# Assignments BMI Calculator
w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))

bmi = w / (h ** 2)

print("Your BMI is:", round(bmi, 2))