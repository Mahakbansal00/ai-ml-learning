#A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating the same file.
with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/donkey.txt","r")as  f:
  q=f.read()
  q = q.replace("donkey", "dog")
  with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/donkey.txt","w") as f:
    f.write(q)
  

