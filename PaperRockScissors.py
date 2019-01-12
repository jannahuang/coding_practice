'''
The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors.
Instruct the computer to randomly select either Rock, Paper, or Scissors.
Compare the user's choice and the computer's choice.
Determine a winner (the user or the computer).
Inform the user who the winner is.
'''
from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie" : "Yawn it's a tie",
  "won" : "Yay you won!",
  "lost" : "Aww you lost!",
}

def decide_winner(user_choice, computer_choice):
  print "%s" % user_choice
  print "%s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]
    
def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ").upper()
  computer_choice = options[randint(0,3)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()
