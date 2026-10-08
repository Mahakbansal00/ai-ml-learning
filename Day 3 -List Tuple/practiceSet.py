#write a program to create a dictionary of Hindi words with values as their english translation.
#Provide user with an obtion to look it up!
dic={
    "key":"value",
    "kursi":"chair",
    "dabba":"box"
}
print("select only this",dic.keys())
a=input("enter a word")
print(dic.get(a))#get dont show error its show none
#Write a program to input eight numbers from the display all the unique numvers (orce)
user=[]
a=input("enter a number")
user.append(a)
a=input("enter a number")
user.append(a)
a=input("enter a number")
user.append(a)
a=input("enter a number")
user.append(a)
a=input("enter a number")
user.append(a)
a=input("enter a number")
user.append(a)
a=input("enter a number")
user.append(a)
a=input("enter a number")
user.append(a)
print(set(user))
#Can we have a set with 18 (int) and"18 (str) as a values in it?
sete={18,"18"}
print(sete)
"""What will be the length of following set 5:
5 = Set ()
5. add (20)
5: add (20.0)
5: add ("20") → length of 5 after these"""
s=set()
s.add (20)
s.add (20.0)
s.add ("20")
print(len(s))
#	what is the type of 5? 5={}
s={}
print(type(s))
#Create an empty dictionary. A use key as their names. Assumellow 4 friends to enter their favorite language as valu thatt he names are unique.
dic1={}
f=input("enter favourite language mahi \n")
dic1["mahi"]=f
f=input("enter favourite language anu \n")
dic1["anu"]=f
f=input("enter favourite language bhumi \n")
dic1["bhumi"]=f
f=input("enter favourite language mahak \n")
dic1["mahak"]=f
print(dic1)
#If the names of 2 friends are same; what will happen to the program in problem 6?
dic1={}
f=input("enter favourite language mahi \n")
dic1["mahi"]=f
f=input("enter favourite language anu \n")
dic1["anu"]=f
f=input("enter favourite language mahak \n")
dic1["mahak"]=f
f=input("enter favourite language mahak \n")
dic1["mahak"]=f
print(dic1)
#recent value print 
# If languages of two friends are same; what will happen to the program in problem 6?
#no changes same output