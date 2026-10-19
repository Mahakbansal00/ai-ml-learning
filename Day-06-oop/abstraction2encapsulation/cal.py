#2. Write a class “Calculator” capable of finding square, cube and square root of a number.
import math
class Calculator():
     def __init__(self,num):
        self.number=num
      
     def square(self):
      print(self.number*self.number)
     def cube(self):
       print(self.number*self.number*self.number) 
     def sqroot(self):
      print(math.sqrt(self.number) )
      
c1=Calculator(2)
c1.square()
c1.cube()
c1.sqroot()
