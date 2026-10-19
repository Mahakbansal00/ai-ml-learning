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
print(c1.x,c1.y,c1.z)

