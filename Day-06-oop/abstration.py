#4 oop concept 
#1abstraction 2encapsulation 3inheritance 4polymorphisum
#1abstraction which means hide all unnecessary things visible ness.exmple
class car():
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clu=False
    def start(self):
         self.acc=True
         self.clu=True
         print("car start......")
car1=car()
car1.start()
