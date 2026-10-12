def add(marks):
 p=sum(marks)
 return p
 
a=[2,3,4,5]
a2=add(a)
print(a2)
#write a program to greet a user with "good day" using function
def user():
 greet="good day"
 return greet
a=input("enter your name :")
user1=user()
print(a,user1)
#2 way
def greet(name):
 print("good day",name)
 
greet("mahak")
#function argument 1 or more tha 2 values
def sum(num1,num2):
 return num1+num2
print(5,4)
#default argument
def greet(name="mahak"):
 s=("hello")+name
 return s

s1=greet()
print(s1)
#recurison
def recurison(n):
 if n==0 or n==1:
  return 1
 return n*recurison(n-1)
call = recurison(5)
print(call)
