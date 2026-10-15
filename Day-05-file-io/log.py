#6. Write a program to mine a log file and find out whether it contains ‘pythonʼ.̓
with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/log.txt")as a:
    log=a.read()
    if "python logged" in log.lower():
        print("python")
#7. Write a program to find out the line number where python is present from ques 6.
with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/log.txt")as a:
  log=a.read()
  count=1
for line in log.splitlines():
   if "python logged" in line.lower():
      print(count) 
   count=count+1

    