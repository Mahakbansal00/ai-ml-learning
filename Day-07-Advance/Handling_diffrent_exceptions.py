try:
  a= int(input("enter a number"))
  c= 1/a
  print(c)

except ValueError as e:
      print("please enter a valid value :")
      print(e)
except ZeroDivisionError as e:
      print("make sure you are not divided by :")
      print(e)
    
except Exception as e:
      print("exception accured")

      print(e)
print("Thanks for using this code!")
