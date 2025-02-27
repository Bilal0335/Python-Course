# ! Operators in Python | Arithmetic Operators 

'''

### **Operators in Python**  

#### **1. Arithmetic Operators**  
- `+`, `-`, `*`, `/`, `%`, `**`, `//`  

#### **2. Assignment Operators**  
- `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`  

#### **3. Comparison Operators**  
- `==`, `!=`, `>`, `<`, `>=`, `<=`  

#### **4. Logical Operators**  
- `and`, `or`, `not`  

#### **5. Bitwise Operators**  
- `&`, `|`, `^`, `~`, `<<`, `>>`  

#### **6. Membership Operators**  
- `in`, `not in`  

#### **7. Identity Operators**  
- `is`, `is not`  

#### **8. Ternary Operator**  
- `x if condition else y`  

'''

#  BODMAS Rule (Bracket, Order, Division, Multiplication, Addition, Subtraction)

'''
1. Arithmetic Operators**  
 - `+`, `-`, `*`, `/`, `%`, `**`, `//`
'''  

# print(2 + 3)
# print(2 * 3)
# print(2 - 3)
# print(2 / 3)
# print(2 % 3)
# print(2 // 3)
# print(2 ** 3)

# Assignments BMI Calculator
w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))

bmi = w / (h ** 2)

print("Your BMI is:", round(bmi, 2))
