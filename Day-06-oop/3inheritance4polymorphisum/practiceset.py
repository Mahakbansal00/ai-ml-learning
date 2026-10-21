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
#3. Create a class ‘Employee ʼand add salary and increment properties to it. Write a method ‘salaryAfterIncrement ʼmethod with a @property decorator with a setter which changes
#the value of increment based on the salary.
class employee():
  def __init__(self):
     self.salary=50000
     self.increment=1.5
  @property
  def salaryAfterIncrement(self):
     return self.salary*self.increment
  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self,sai):
       self.increment = sai/self.salary

a1=employee()
print(a1.salaryAfterIncrement)
#4. Write a class ‘Complex ʼto represent complex numbers, along with overloaded operators ‘+ ʼand ‘* ʼwhich adds and multiplies them.
class complex():
    def __init__(self,i,r):
        self.imag=i
        self.real=r
    
    def __add__(self,c):
        return complex(self.imag+c.imag,self.real+c.real)
    def __mul__(self,c):
     real=self.real*c.real-self.imag*c.imag
     imag=self.real*c.real+self.imag*c.imag
     return complex(real,imag)
    def __str__(self):
        return(f"{self.real}+{self.imag}i")
    
c1=complex(9,4)
c2=complex(7,9)
print(c1+c2)
print(c1*c2)
#5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class vector():
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1= " "
        index=0
        for i in  self.vec:
         str1 +=f"{i}a{index} +"
         index +=1
        return str1[:-1]#slicing 
    def __add__(self,vec2):
        newList=[]
        for i in range (len(self.vec)):
            newList.append(self.vec[i]+vec2.vec[i])
        return vector(newList)
    def __mul__(self,vec2):
        sum=0
        for i in range (len(self.vec)):
            sum+=self.vec[i]*vec2.vec[i]
        return sum

v1=vector([1,4,6])
v2=vector([2,3,7])
print(v1+v2)
print(v1*v2)
#6. Write __str__() method to print the vector as follows:7i + 8j + 10kAssume vector of dimension 3 for this problem  
class vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        return f"{self.vec[0]}i  +{self.vec[1]}j +{self.vec[2]}k "
v1=vector([7,8,10])
print(v1)
        
           
           
    