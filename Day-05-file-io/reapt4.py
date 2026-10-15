#5. Repeat program 4 for a list of such words to be censored.
with open ("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/donkey.txt")as a:
    list=a.read()
    words=["dog","rat","eating"]
    for word in words:
     list=list.replace(word,"donkey")
    with open ("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/donkey.txt","w")as a:
       a.write(list)   


