# 1. Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b and a > c and a > d:
    print(a)
elif b > a and b > c and b > d:
    print(b)
elif c > a and c > b and c > d:
    print(c)
else:
    print(d)


# 2. Write a program to find out whether a student has passed or failed.
# Required: 40% overall and at least 33% in each subject.

it = int(input("Enter IT marks: "))
math = int(input("Enter Maths marks: "))
english = int(input("Enter English marks: "))

if it >= 33:
    print("You are pass in IT:", it, "marks")

if math >= 33:
    print("You are pass in Maths:", math, "marks")

if english >= 33:
    print("You are pass in English:", english, "marks")

subjects = (it + math + english) / 300 * 100

if it >= 33 and math >= 33 and english >= 33 and subjects >= 40:
    print(subjects, "% You are pass")
else:
    print("Overall fail")


# 3. A spam comment contains these keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this".

a = input("Enter a string: ")

s = {
    "Make a lot of money": "spam",
    "buy now": "spam",
    "subscribe this": "spam",
    "click this": "spam"
}

if ("Make a lot of money" in a or
    "buy now" in a or
    "subscribe this" in a or
    "click this" in a):
    print("Spam")
else:
    print("Not spam")


# 4. Write a program to find whether a username contains less than 10 characters.

a = input("Enter a name: ")

if len(a) < 10:
    print("Yes, less than 10 characters:", a)
else:
    print("No, 10 or more characters:", a)


# 5. Write a program to check whether a given name is present in a list or not.

a = input("Enter a name: ")

names = ["gita", "sita", "rita", "bita", "chita"]

if a in names:
    print("Yes, given name is present:", a)
else:
    print("Not present")