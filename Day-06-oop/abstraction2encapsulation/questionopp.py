#1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer():
    def __init__(self,name,product):
     self.name=name
     self.product=product
    
    def information(self):
      print(f"The name of programmer is {self.name} The product is {self.product} ")

p1=Programmer("reena","github")
p2=Programmer("meena","python")
p3=Programmer("alien","java")
p1.information()#print name
p2.information()
p3.information()


    
  