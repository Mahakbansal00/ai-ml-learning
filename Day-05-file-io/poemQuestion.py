"""question 1. Write a program to read the text from a given file ‘poem.txtʼ and find out whether it
contains the word ‘twinkleʼ.̓"""
with open('/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/poem.txt','r')as f:
    a=f.read()
    print(a)
    s=a.lower().find("twinkle")
    if s != -1:
      print(s,"twinkle is present")
    else:
       print(s,"twinkle is not present")