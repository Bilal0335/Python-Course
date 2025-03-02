# Age Calculator

curr_age = int(input("Enter Your Age: "))

year_left = 90 - curr_age
day_left = int(year_left * 365.25)  
week_left = year_left * 52
month_left = year_left * 12

print(f"You have {day_left} days, {week_left} weeks, and {month_left} months left.")

