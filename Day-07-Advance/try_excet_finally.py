try:
    a=int(input("enter a value"))
    i=a/1
except Exception as e:
    print(e)
    exit()
finally :#use for cleanup.....
    print("we are done")
print("thanks for using program")