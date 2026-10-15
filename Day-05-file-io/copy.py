#8. Write a program to make a copy of a text file “this.txt”.
with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/poem.txt")as a:
    file=a.read()
with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/po.txt","w")as a:
    a.write(file)
