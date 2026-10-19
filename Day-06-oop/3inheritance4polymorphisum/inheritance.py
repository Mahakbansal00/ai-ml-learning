#inheritance 
#1.single inheritance
class car():#parents class
    color="black"
    feature="fast"
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stop.....")
class toyata(car):#child class
    def __init__(self,name):
     self.name=name

car1=toyata("prius")
car2=toyata("fortuner")
car.start()
car.stop()
print(car1.color)
print(car2.feature)

#3 type of inheritance
"""
1.single
2.multi-level
3.multiple
"""
#2.multi-level
class car():#parents class
    color="black"
    feature="fast"
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stop.....")
class toyata(car):#child class
    def __init__(self,name):
     self.name=name
class fortuner(toyata):
   def __init__(self,type):
      self.type=type
      print(self.type)
car1=fortuner("diesel")
print(type(car1))
#multiple
class a:
   vara=("hello :a")
class b:
   varb=("hello :b")
class c(a,b):
   varc=("hello :c")
c1=c()
print(c1.varc,c1.vara,c1.varb)
#super method()
class car():#parents class
   def __init__(self,type):
     self.type=type
   @staticmethod
   def start():
        print("car started...")
   @staticmethod
   def stop():
        print("car stop.....")
class toyata(car):#child class
    def __init__(self,name,type):
     self.name=name
     super(). __init__(type)
   
car1=toyata("prius","diesel")
print(car1.type)