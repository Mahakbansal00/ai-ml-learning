#queston1. Write a program using functions to find greatest of three numbers.
def greatest(a,b,c):
 if a>b and a>c:
    print(a)
 elif b>a and b>c:
   print(b)
 else:
   print(c)
 return greatest
call = greatest(5,4,8)
print(call)
#question 2. Write a python program using function to convert Celsius to Fahrenheit.
def temp(c):
 f=c*(9/5)+32
 return f
call = temp(30)  
print(call)     
# f=c (f-32)*5/9
#3. How do you prevent a python print() function to print a new line at the end.
print("hello", end=" ")
print("cute", end=" ")
#4. Write a recursive function to calculate the sum of first n natural numbers.
def recursion(n):
  if n==0:
    return 1
  return n+recursion(n-1)
call=recursion(34)
print(call)
#question 5. Write a python function to print first n lines of the following pattern.
"""
*** 
** - for n = 3
*
"""
def fun(n=3):
  for i in range(3,0,-1):
   print()
   for j in range(1,i+1):
    print("*", end=" ")
fun()
#question 6. Write a python function which converts inches to cms.
def measure(inch):
    i = inch * 2.54
    return i

cm = measure(5)
print(cm)
#question 7. Write a python function to remove a given word from a list and strip it at the same time.
def mylist():
    a = ["hello  ", "kiko", "chiko  "]
    a = [word.strip() for word in a]
    a.remove("kiko")
    return a

print(mylist())
#8. Write a python function to print multiplication table of a given number.
def multi(n):
    for i in range(1, 11):
        a = i * n
        print(a)

multi(2)