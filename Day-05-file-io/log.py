with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/log.txt")as a:
    log=a.read()
    if "python logged" in log.lower():
        print("python")