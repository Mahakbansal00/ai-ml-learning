f=open('/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/a.txt','a')
f.write("\n I am good ")# to append or add text using "a" and for writting in a file using "w"
f.close()
#using with is the best way to open files.
with open('/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/a.txt','r')as f:
 a= f.read()
 print(a)