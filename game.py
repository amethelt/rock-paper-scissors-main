@@ -0,0 +1,56 @@
# game.py
import random
import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("PLAYER_NAME"))

print("Rock, Paper, Scissors, Shoot!")

## USER INPUT 
print("---------")
user_choice = input("Choose 'Rock' or 'Paper' or 'Scissors': ")
print("You Chose: ")
print(user_choice)
options = ["Rock", "Paper", "Scissors"]


##VALIDATING USER INPUT
if user_choice not in ["Rock", "Paper", "Scissors"]:
    print("Please choose valid option: Rock, Paper, or Scissors (make sure to use caps)")
    exit()


##COMPUTER INPUT
computer_choice = random.choice(options)
print("The Computer Chose: ")
print(computer_choice)
print("----------")

## Determining the Winner 
if (user_choice == "Rock") and (computer_choice == "Paper") :
    print("SORRY! YOU LOST!")
elif (user_choice == "Rock") and (computer_choice == "Scissors") :
    print("WINNER! NICE JOB!")
elif (user_choice == "Paper") and (computer_choice == "Rock") :
    print("WINNER! NICE JOB!")
elif (user_choice == "Paper") and (computer_choice == "Scissors") :
    print("SORRY! YOU LOST!")
elif (user_choice == "Scissors") and (computer_choice == "Rock") :
    print("SORRY! YOU LOST!")
elif (user_choice == "Scissors") and (computer_choice == "Paper") :
    print("WINNER! NICE JOB!")
else: print("TIED! NO WINNER!")
##pulled the else function for a tie from Basil's Code on Slack









##breakpoint()

print("PLAY AGAIN!")
