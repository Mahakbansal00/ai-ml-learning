#when same operator is allowed to have diffrnt mng accrdng to the context
#dunder function solve complex pb example a__add__b
#complex number i1+j3 i is real number j is imag addition
class complex():
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showno(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,c2):
      newreal=self.real +c2.real
      newimg=self.real+c2.img
      return complex(newreal,newimg)

c1=complex(1,3)  
c1.showno()
c2=complex(5,3)
c2.showno()
c3 = c1+c2
c3.showno()       
