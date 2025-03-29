
# List
# num = [4,5,6,7,1,2,3,-1,8,9,10,11,12,13,14,15]
# print("Number: ",num) 
# print(num[0:5:1])
# num.sort()
# print("Number Sort: ",num)
# num.reverse()
# print("Number Reverse: ",num)
# print("Number Max: ",max(num))
# print("Number Min: ",min(num))


# mix_list = [1,2,3,'bilal',True]

# print("Mix list: ",mix_list)

# print(mix_list[3]) #out : bilal



num = []
num.append(1)
num.append(2)
num.append(True)
num.append("Bilal")
num.extend(['h','e','l','l','o',1,4,5])
num.insert(78,'h3llo') # Inserts an element at a specific index
num.insert(1,66) # 1
print("Number: {}".format(num))

# Removes the specified element from the list
num.remove(66)
num.remove('h')
num.remove('e')
num.remove('l')
num.remove('l')
num.remove('o')
num.remove('h3llo')
print("Number: {}".format(num))

# 🔹 Removes and returns the last element (or a specific index)
num.pop()
num.pop()
# num.pop(1)  # Removes element at index 1
num.pop(2)
print("Number: {}".format(num))

# Returns the index of a given element

print("Number: {}".format(num.index(1)))
print("Number: {}".format(num.index('Bilal')))
print(f"----------------------------------------------------------------")
# Counts occurrences of a specific element
num = [1, 2, 2, 3, 4, 2]
print("Number Count: {}".format(num.count(2)))
print(f"----------------------------------------------------------------")

num.sort(reverse=True)
print("Sort",num)  # [9, 4, 2, 1]


print(f"----------------------------------------------------------------")

# Creates a copy of the list (original list remains unchanged)
new_list = num.copy()
print("Copy: ",new_list)

print(f"----------------------------------------------------------------")
num.clear()

print("Clear: ",num)  # []

num = [12,13,14]
print("Sum ",sum(num))
print("Length ",len(num))

print(f"----------------------------------------------------------------")

# Concatenates two lists

list1 = [1,4,2,3]
list2 = [4,5,6]
print("Concatenated List: ",list1 + list2)

# Returns a sorted copy of the list (original list remains unchanged)

print("Sorted Copy: ", sorted(list1))
print("origional List1",list1)

print(f"----------------------------------------------------------------")

# Reverses the list (original list is modified)

print(f"----------------------------------------------------------------")
words = ["Hello", "World"]
print(" ".join(words))  # "Hello World"


# 🔹 Converts any iterable into a list
string = "Python"
print(list(string))  # ['P', 'y', 't', 'h', 'o', 'n']

