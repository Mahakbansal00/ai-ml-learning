#create a list using print() function
a=[1 , 2,3 ,4,56]
print(a)
# acess using index using[0],[1]
print(a[0])
#value change using index
a[2]=80
print (a)
#we can create a list with diffrent items 
a=["ice",True,1,0.0,False]
print(a)
#slicing list 
print(a[1:4])
#list sort low to high
li=[1,2,9,3,5,4,6]
li.sort()
print(li)
#list reverse high to low
li.reverse()
print(li)
#list append its meand adds the end of the list 
li.append(333)
print(li)
#list insert
li.insert(1,44)
print(li)
#list pop means delete element at index and return its value
li.pop(2)
print (li)
#list remove delete element 
li.remove(333)
print(li)
