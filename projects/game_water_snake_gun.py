import random
def game():
    choices = ["snake", "water", "gun"]
    computer = random.choice(choices)
    a="snake"
    b="water"
    c="gun"
    player1=input("player one trun choice one? snake water gun\n ").lower()
    print("computer choice",computer)
    if player1 == a and computer == b:
     print("player1 win ")
    elif player1 == a and computer == c:
     print("computer win ")
    elif player1 == b and computer == a:
     print("computer win ")
    elif player1 == b and computer == c:
     print("player1 win ")  
    elif player1 == c and computer == a:
     print("player1 win ")
    elif player1 == c and computer == b:
     print("computer win ")
    elif player1 == computer:
     print("tie")
    else:
     print("invalid choice")
game()
