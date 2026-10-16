# class and object
class Student():#student is object
    name="hari"
s1=Student()
print(s1.name)
s2=Student()
print(s2.name)
#constructor def__int__(self)
class Student():
    name="hari"
    def __init__(self):
     print("STUDENTS NAME")

s1=Student()
#*******************
class Student():
    def __init__(self,Fullname):
     self.name=Fullname
s1=Student("kaean")
print(s1.name)
#***************parameterized constructor
class student():
    def __init__(self,name,marks):
      self.name=name
      self.marks=marks
      def avg(self):
         for add in self.marks:
            add=+sum
            print("avrg",add/3)
s1=student("rakhi",22)
print(s1.name,s1.marks)
s2=student("roky",21)
print(s2.name,s2.marks)
