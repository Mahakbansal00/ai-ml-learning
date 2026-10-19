#1. create a class (2-D vector) and use it to create another class representing a 3-D vector.
class c2dvec():
    def __init__(self,x,y):
        self.x=x
        self.y=y
class c3dvec(c2dvec):
    def  __init__(self,x,y,z):
     super().__init__(x, y)
     self.z=z
    
c1=c3dvec(1,2,3)
print(f"x{c1.x},y{c1.y},z{c1.z}")
#2. Create a class ‘Pets ʼfrom a class ‘Animals ʼand further create a class ‘Dog ʼfrom ‘Pets.ʼAdd a method ‘bark ʼto class ‘Dog.ʼ
class animals():
   def feature(self,sleep,bath,eat,bark):
    self.sleep=sleep
    self.bath=bath
    self.eat=eat
    self.bark=bark
class pet(animals):
     def pets(self,dog,cat,hamster,rabbit):
        self.dog=dog
        self.cat=cat
        self.hamster=hamster
        self.rabbit=rabbit
class dog(pet):
         def bark(self):
           print("Dog is barking")
       
    
d1 =dog()
d1.bark()


           
           
    