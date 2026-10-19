#inheritance 
#single inheritance
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