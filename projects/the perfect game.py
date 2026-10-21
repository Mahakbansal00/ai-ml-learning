#Write a Python program that generates a random number and asks the user to guess it. If the guess is too high, print "Lower number please". If the guess is too low, print "Higher number please". When the user guesses correctly, display the correct number and the number of guesses taken to find it.
import random
choices = random.randint(1,100)
class computer():   
    def guess(self):
        count=0
        while True:
           user = int(input("Guess the number: "))
           if user > choices :
             print("Lower number please")
             count=count+1
           elif user < choices:
             print("Higher number please")
             count=count+1
           else:
             print("Your guess is correct")
             count=count+1
             break 
 
    
player1=computer()
player1.guess()