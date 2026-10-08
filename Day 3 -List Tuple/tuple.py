t=(1,2,3,4,5,6,7,8,9)
print(t(2))
#we cant modifiy or change tuple elements 
#
c=()
print(c)
c=(1)#wrong way to declare a tuple always ends with comma if its one
print(c)
c=(1,)
print(c)
#methods************************************
#1 count method
a=(1,2,3,3,4,5,6,3,73,3)
print(a.count(3))
#2 index value of first accurance
print(a.index(6))
