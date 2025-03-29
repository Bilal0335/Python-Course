# ! Love Calculator

# Taking User Input
name1 = input("What is Your Name: ").strip()
name2 = input("What is his/her Name: ").strip()

# Combine and Convert to Lowercase
combine_str = name1 + name2
lower_case_str = combine_str.lower()

# Counting Letters for "TRUE"
t = lower_case_str.count('t')
r = lower_case_str.count('r')
u = lower_case_str.count('u')
e = lower_case_str.count('e')

true = t + r + u + e  

# Counting Letters for "LOVE"
l = lower_case_str.count('l')
o = lower_case_str.count('o')
v = lower_case_str.count('v')
e = lower_case_str.count('e')

love = l + o + v + e  

# Correct Love Score Calculation
love_score = int(str(true) + str(love))

# Conditions
if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, and you go together like coffee and mentos ☕🍬")
elif 40 <= love_score <= 50:
    print(f"Your love score is {love_score}, and you are a perfect match! ❤️")
else:
    print(f"Your love score is {love_score}")
