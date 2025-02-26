# Coding Exercises for Beginners in Python | Exercise #2 | Program to swap two numbers

# Initialize two variables with different values
num_1 = int(input("Enter a first number: "))
num_2 = int(input("Enter a second number: "))

# Print before swapping values
print("\nBefore swapping, the values are: ")
print("First number:", num_1)
print("Second number:", num_2)

# Swap the numbers
temp = num_1
num_1 = num_2
num_2 = temp

# Print after swapping values
print("\nAfter swapping, the values are: ")
print("First number:", num_1)
print("Second number:", num_2)

'''
Short Tricl Swapping

a , b = b,a


# Swap the numbers
temp = a
a = b
b = temp

# Print after swapping values
print("\nAfter swapping, the values are: ")
print("First number:", a)
print("Second number:", b)
'''