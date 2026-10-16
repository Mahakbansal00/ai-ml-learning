#10. Write a program to wipe out the content of a file using python.
with open ("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/po.txt","r")as f:
   wipe= f.read()
with open ("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/po.txt","w")as f:
   wipe1=f.write("")
