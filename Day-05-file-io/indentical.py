#9. Write a program to find out whether a file is identical and matches the content of another file
file1="/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/poem.txt"
file2="/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/po.txt"
with open(file1)as f:
 f1= f.read()
with open(file2)as f:
  f2= f.read()
if f1==f2:
   print("Files are identical")
else:
    print("Files are not identical")




