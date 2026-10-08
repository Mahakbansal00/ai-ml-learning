#question
#Write a Python program to display a user entered name fallowed by Good Afternoon using input function
a=input("enter your name")
print("Goodafternoon "+a)
#write a program to fill in a letter template given beow with name and date.letter = '' Dear <I NAMEI>,You are selected! <I DATEI>"!
a=input("enter name")
b= input ("enter date")
print("dear",a,"you are selected",b)
letter=''' Dear NAME,You are selected! DATE '''
name=input("enter Name")
date = input ("enter Date")
letter =letter.replace("NAME",name)
letter =letter.replace("DATE",date)
print(letter)
#Write a program to detect double spaces in a string
a="mahak  Bansal"
doublespace=a.find("  ")
print(doublespace)
s="mahak  Bansal"
print(s.find("  "))
#replace double space to single space
s="mahak  Bansal"
print (s.replace("  "," "))
#write a formal letter "dear mam,this python is very easy.thanks.
q="""dear mam \n \t this python is very easy \nthanks"""
print(q)