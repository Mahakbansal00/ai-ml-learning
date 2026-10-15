"""question  2. The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score."""
def game():
 return 6000
score=game()
with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/highscore.py")as a:
   highscore=a.read()
if highscore=="":
 with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/highscore.py","w")as a:
     a.write(str(score))
elif int(highscore)  < score:
   with open("/Users/mahak/Desktop/ai-ml-learning/Day-05-file-io/highscore.py","w")as a:
     a.write(str(score))