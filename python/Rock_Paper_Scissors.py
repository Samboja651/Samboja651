# Write your solution below the starter code
# Follow the instructions in the tab to the right
# from random import seed
# from random import randint

# seed(6)
# #import random
# x = 1
# # Welcome the user to the game
# print("Welcome to rock, paper, scissors. Good luck!")
# while x < 4:

#   a = int(input("\nEnter your choice: 1 for Rock, \n 2 for Sccissors and 3 for Paper: "))

#   b = int(input("\nEnter your choice: 1 for Rock, \n 2 for Sccissors and 3 for Paper: "))

#   if a == b:
#     print("It's a draw")
#   elif (a == 1 or b == 1) and (a == 2 or b == 2):
#     print("Rock wins!")
#   elif (a == 1 and b == 3) or (a == 3 and b == 1):
#     print("Paper wins!")
#   elif (a == 2 and b == 3) or (a == 3 and b == 2):
#     print("Scissors wins!")
#   x += 1
# Make a choice for the computer player
# Get a choice from the user
# Compare the user and computer choice
# Print the right message, based on the choices

import random

choice = (["Rock", "Paper", "Scissors"])
length = 1
guess = random.choice(["Rock", "Paper", "Scissors"])

print("Welcome to rock, paper, scissors. Good luck!")
user = str(input("Rock,Paper or Scissors: "))
if guess == user:
    print("The computer chooses ", guess)
    print(guess, "and", user, ". Its a draw")
elif guess == "Rock" and user == "Paper":
    print("The computer chooses ", guess)
    print(user, " covers ", guess, ". You won!")
elif guess == "Rock" and user == "Scissors":
    print("The computer chooses ", guess)
    print(guess, " smashes ", user, ". You lose!")
elif guess == "Paper" and user == "Rock":
    print("The computer chooses ", guess)
    print(guess, " covers ", user, ". You won!")
elif guess == "Scissors" and user == "Rock":
    print("The computer chooses ", guess)
    print(user, " smashes ", guess, ". You won!")
else:
    print("You have to enter Rock, Paper or Scissors")
