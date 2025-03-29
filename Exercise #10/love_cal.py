
# ! Love calculator

name1 = input("What is Your Name: ")
name2 = input("What is his/her name: ")
combine_str = name1 + name2
lower_case_str = combine_str.lower()

t = lower_case_str.count('t')
r = lower_case_str.count('r')
u = lower_case_str.count('u')
e = lower_case_str.count('e')

true = t + r + u + e 

l = lower_case_str.count('l')
o = lower_case_str.count('o')
v = lower_case_str.count('v')
e = lower_case_str.count('e')

love = l + o + v + e

love_score = int(str(love)) + int(str(true))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, and you go together like coffe and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, and you are a perfect match!")
else:
    print(f"Your love score is {love_score}")