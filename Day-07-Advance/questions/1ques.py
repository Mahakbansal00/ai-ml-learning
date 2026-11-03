def readfile(filename):
 try:
    with open(filename,"r")as f:
        print(f.read())
 except FileNotFoundError:
    print(f"file not found{filename}")
readfile("/Users/mahak/Desktop/ai-ml-learning/Day-07-Advance/questions/1.txt")
readfile("/Users/mahak/Desktop/ai-ml-learning/Day-07-Advance/questions/2.txt")
readfile("/Users/mahak/Desktop/ai-ml-learning/Day-07-Advance/questions/3.txt")
