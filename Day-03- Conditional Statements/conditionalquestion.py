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
# Write a program to calculat escheme: the grade of a stutdent from his marks from the following 90 – 100 => Ex 80 – 90 => A 7 0 – 80 => B 60 – 7 0 => C 50 – 60 => D <50 => F    
a=int(input("input a number"))
if 90<=a and a<=100:
   print("ex") 
elif 80<=a <90:
   print("a")
elif 70<=a <80:
   print("b")
elif 60<=a <70:
   print("c")
elif 50<=a<60:
   print("d")
elif a< 50:
   print("f")
else:
  print("invalid number ")
phara="""Parts of the Indian capital, Delhi, have been turned into a fortress, with tens of thousands of security forces deployed, as the influential Gen Z-led "cockroach" movement has called for a major protest on Saturday.
The protesters are seeking electoral reforms and the resignation of Chief Election Commissioner (CEC) Gyanesh Kumar over allegations of manipulating voters' lists.
The Election Commission has denied this and Kumar is yet to comment on calls for his resignation.
The protest comes just months after the movement brought thousands of young people onto Delhi's streets in July, in demonstrations that saw violent clashes with police and forced India's education minister to resign.
Police say they have denied permission for the gathering and all roads leading to Jantar Mantar, the main protest venue, have been closed with huge metal barricades.
The restrictions have caused major disruption across central Delhi, with traffic diverted from several key roads. A journey that would normally take 15 minutes took more than an hour this morning.
At Jantar Mantar, metal barricades and ropes have been erected around the protest site, preventing people from entering. Some protesters who arrived early were stopped and questioned by police and paramilitary personnel deployed in the area.
At a nearby roundabout, loudspeakers repeatedly broadcast appeals for people to cooperate with the police.
ADVERTISEMENT

ADVERTISEMENT

In a late night post on X, Delhi Police on Friday defen"""
a=input("enter a string")
if phara.lower().find(a.lower()) != -1 and a!= "":
  print("yes")
else:
  print("no")