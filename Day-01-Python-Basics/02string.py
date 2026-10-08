"""String basic operators"""
#concatenation it means where we add two strings together example
#string is a datatype in python and it is sequance of char. enclosed in quotes.
a="Hello"
b=" World"
print(a+b)
#length of string len***************************************
str = a+b
print (len(str))
#indexing M   A   H   A   K
        #[0] [1] [2] [3] [4] 
a="MAHAK"
print(a[3]) #A
# String slicing *********************************************
a="MAHAK"
print(a[1:4]) #AHA
#String function*********************************************
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
# slicing with skip value
#  012345678910
a="punjabifood"
print(a[0:11:2]) #2means one skip value
print(a.count("o"))
print(a.capitalize())
print(a.replace("punjabifood","northfood"))
print(a.find("a"))
print("hello\n my name is \t mahak \' i am \\ v bad \" kyc")