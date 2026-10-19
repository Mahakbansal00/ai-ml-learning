#proprty method
class  score():
    def __init__(self,math,english,science):
        self.math=math
        self.english=english
        self.science=science
    @property
    def average(self):
     return (self.math+self.english+self.science)/3
m1=score(97,98,99)
print(m1.average)
m1.math=88
print(m1.average)
