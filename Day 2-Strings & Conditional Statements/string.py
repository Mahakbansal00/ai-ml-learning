"""String basic operators"""
#concatenation it means where we add two strings together example
a="Hello"
b="World"
print(a+b)
#length of string len
str = a+b
print (len(str))
#indexing M   A   H   A   K
        #[0] [1] [2] [3] [4] 
a="MAHAK"
print(a[3]) #A
#slicing
a="MAHAK"
print(a[1:4]) #AHA
#function 
#endswith() it checks whether the string ends with a particular character or not
a="MAHAK"
print(a.endswith("a")) #false
print(a.endswith("K")) #true
#cpaitalize() it converts the first character of the string to uppercase
print(a.capitalize()) #Mahak
#replace,find,count etc
print(a.replace("A","a")) #Mahak
print(a.find("m")) #-1
print(a.count("A")) #2