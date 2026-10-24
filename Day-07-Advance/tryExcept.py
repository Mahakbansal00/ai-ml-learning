while (True):
    print("press q to quit")
    a=input("enter a number")
    if a == "q":
         break
    try:
       a=int(a)
       if a>9:
          print("your enter number greater than 9")
    except Exception as e:
          print(e)
          print("thanks for playing game")
    