# ! BMI Calculations

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = round(weight / (height ** 2),2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are Underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you are Normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are Overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are Obese.")
else:
    print(f"Your BMI is {bmi} and you are Clinically Obese.")
