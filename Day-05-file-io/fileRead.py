#use opn function to read the content  file of a 
f=open('/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/a.txt','r')
data=f.read()
data=f.read(5)#read only 5 char.
data=f.readline()#read one line 
print(data)
data=f.readline()#read secound line 
print(data)
f.close()
