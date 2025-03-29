
# ! Pizza Order Programm

size = input("What size pizza you want (S/L/M): ").strip()
bill = 0

if size == 's' or size == 'S':
    bill += 100
    print("Small Pizza price is $100")

elif size == 'm' or size == 'M':
    bill += 200
    print("Medium Pizza price is $200")
elif size == 'l' or size == 'L':
    bill += 300
    print("Large Pizza price is $300")
else:
    print("Invalid size! Please choose S/M/L.")
    exit()    
    
add_pepperoni = input("Do you want pepperoni (Y/N): ").strip()
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == "S" or size == "S":
        bill += 30
    else:
        bill += 40


extra_cheezes = input("Do you want extra cheezes (Y/N): ").strip()
if extra_cheezes == 'Y' or extra_cheezes == 'y':
        bill += 20
 
print(f"Your final bill is {bill}")  
 