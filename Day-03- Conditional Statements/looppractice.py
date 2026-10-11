#1. Write a program to print multiplication table of a given number using for loop.
user=int(input("enter a number"))
for i in range (1,11):
    print(user,"*",i,"=",i*user)
#2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
#l = ["Harry", "Soham", "Sachin", "Rahul"]
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
 if(i.lower().startswith("s")):
  print("good morning!",i)
#3. Attempt problem 1 using while loop.
user=int(input("enter a number : "))
i=1
while(i<=9):
 print(user,"*",i,"=",i*user)
 i=i+1
#Write a program to find whether a given number is prime or not.
number=int(input("enter a number"))
for i in range(2,number):
 if number % i == 0:
  print(" not a prime number")
  break
else:
  print("prime number")
#5. Write a program to find the sum of first n natural numbers using while loop.

a=int(input("enter a number"))
i=1
sum=0
while(i<=a):
 print(i)
 sum=sum+i
 i=i+1
print("natural number sum : ",sum)
#6. Write a program to calculate the factorial of a given number using for loop.
a=int(input("input a number"))
fac=1
for i in range(1,a+1):
  fac=fac*i
print(fac)
#7. Write a program to print the following star pattern.
"""
*
***
***** for n = 3
"""
n=3
for i in range(1,n+1):
 print()
 for j in range(1,2*i):
   print("*",end=" ")
#8. Write a program to print the following star pattern:
"""
*
**
*** for n = 3
"""
n=3
for i in range (1,n+1):
  print()
  for j in range(1,i+1):
   print("*",end=" ")
#9. Write a program to print the following star pattern.
"""
* * *
*   * for n = 3
* * * """
n=3
for i in range(1,n+1):
  if i==2:
    print("*  *")
  else:
    print("***")
#10. Write a program to print multiplication table of n using for loops in reversed order.
#11 print 1,22,333,4444,55555
n= int(input("enter a number"))
for i in range(0,n):
  i=i+1
  print(i)
  for j in range(1,i):
    print(i)