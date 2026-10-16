#creatng own fuction for example avg(self)
class student():
    def __init__(self,name,marks):
      self.name=name
      self.marks=marks
    def avg(self):
     avg=sum(self.marks)
     print("avrg",avg/3)
   
        
s1=student("rakhi",[98,99,97])
print(s1.name,s1.marks)
s2=student("roky",[21,22,23])
print(s2.name,s2.marks)
s1.avg()
s2.avg()