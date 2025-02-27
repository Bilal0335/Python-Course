# Type Checking, Type Error and Type Conversion | Type Casting in Python

print(len("bilal"))
print(len("123"))
# print(len(1234)) #TypeError: object of type 'int' has no len()


'''
Type Checking:
Checking if a variable is of a specific type.

Type Error:
An error that occurs when an operation or function is applied to an object of an inappropriate data type.

Type Conversion:
Converting one data type to another.

Type Casting:
Converting a value from one data type to another using built-in functions.

'''


'''
1️⃣ Type Checking:

Jab hum check karte hain ke koi variable kis data type ka hai.
Python mein type() aur isinstance() ka use hota hai.
'''
x = 10
print(type(x))  # Output: <class 'int'>

print(isinstance(x, int))  # Output: True

'''
2️⃣ Type Error:

Jab hum kisi function ya operation ko inappropriate type ke sath use karne ki koshish karte hain.
Example:
'''

# print("10" + 5)  # TypeError: can only concatenate str (not "int") to str

'''
Type Conversion (Implicit & Explicit):

Implicit Conversion (Automatic by Python):

Jab Python automatically ek type ko doosray compatible type mein convert kar deta hai.

'''

# num = 10      # int
# decimal = 2.5 # float
# result = num + decimal  # Python converts `num` to float automatically
# print(result)  # Output: 12.5
# print(type(result))  # Output: <class 'float'>


'''
Explicit Conversion (Manually by Developer - Type Casting):

Jab hum khud data type change karte hain using built-in functions like int(), float(), str() etc.
'''

# x = "100"
# y = int(x)  # Converting string to integer
# print(y, type(y))  # Output: 100 <class 'int'>
