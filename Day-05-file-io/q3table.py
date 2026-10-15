""" Write a program to generate multiplication tables from 2 to 20 and write it to the different
files. Place these files in a folder for a 13-year-old"""
for i in range(1,21):
 with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/tables"+str(i),"w")as q:
  for j in range(1,11):
   q.write(f"{i}*{j} = {i*j} \n")