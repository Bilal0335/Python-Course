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




#### **2. Assignment Operators**  
# `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=` 


# a = 5  # correct
# 5 = a # incorrect
# c = 5
# c += 1
# c -= 1
# c *= 1
# c /= 1
# c //= 1
# c %= 1
# print(c)


#### **3. Comparison Operators**  
#** `==`, `!=`, `>`, `<`, `>=`, `<=`  
# print( 5 > 4)
# print( 5 < 4)
# print( 5 == 4)
# print( 5 <= 4) 
# print( 5 >= 4)
# print( 5 != 4)

#### **4. Logical Operators**  
### ** `and`, `or`, `not`  

# a, b = 5 ,4

# print(a > 4 and b > 4) # 5 > 4 and 4 > 4 # F
# print(a > 4 and b < 3)  # 5 > 4 and 4 < 3 # F

# x = 10
# y = 5
# z = 20
# a = True
# b = False

# print(x > 5 and y < 10)    # T and T = T
# print(x > 5 and y > 10)    # T and F = F
# print(x > 5 or y < 10)     # T or T = T
# print(x < 5 or y > 10)     # F or F = F
# print(not (x > 5))         # F
# print(not (x < 5))         # T
# print(x > 5 and (y < 10 or z < 15))  # T and (T or F) = T
# print(not (x > 5 and y < 10))  #  T and T = F
# print(a and b)  # F
# print(num := 8, num % 2 == 0 and num > 0)  #

# ! := is the walrus operator, which assigns a value to a variable as part of an expression.

# print(x := 5)   # Walrus Operator]

# while (num := int(input("Enter a number: "))) > 0:
#     print("You entered:", num)


# if (length := len("Python")) > 5:
#     print("Length is:", length)

'''
The code uses the print function to output text to the console.

The f before the string indicates an f-string, which allows embedding expressions inside curly braces {}.

Inside the f-string, the expression (value := 50) is used.

:= is the walrus operator, which assigns a value to a variable as part of an expression.

value is assigned the value 50 and then embedded in the string.

The first print statement outputs: "The number is 50".

The second print statement outputs the value of value, which is 50.


'''

# print(f"The number is {(value := 50)}")
# print(value)


#### **5. Bitwise Operators**  
#** `&`, `|`, `^`, `~`, `<<`, `>>`  



#### **6. Membership Operators**  
## ** `in`, `not in`  



#### **7. Identity Operators**  
# ** `is`, `is not`  

'''
Identity operators in Python are used to compare the memory locations of two objects. These operators check whether two variables reference the same object in memory, not just if they have the same value.

Operators:
is → Returns True if both variables refer to the same object.
is not → Returns True if both variables refer to different objects.

caching range (-5 to 256)
'''

# a = 5
# print(id(a))
# b = 5
# print(id(b))

# print(a is b)  # Output: True


# a = 5

# b = a 

# print(a is b)  


# x = [1,2,3]
# print(id(x))

# y = [1,2,3 ]  # Different objects with the same values
# print(id(y))


# print(x is y)
# print(x is not y)


# x = int(5000)
# y = int(5000)

# print(id(x), id(y))  # Check memory locations True
# print(x is y)        # Check identity True

# a = 5
# b = '5'
# print(id(a),"\n",id(b)) # Check memory locations
# print(a is b)



#### **6. Membership Operators**  
## ** `in`, `not in`  


'''
Python provides two membership operators, in and not in, which are used to check whether a value exists in a sequence such as a list, tuple, string, or dictionary.

in
not in
'''

str_name = "Bilal"
print('b' in str_name) #false
print('B' in str_name) #True
print('B' not in str_name) # F
print('Y' not in str_name) # F