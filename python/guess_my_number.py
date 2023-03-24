# See the Instructions tab
import random
# Set secret number
secret = random.randint(1, 99)
print("I'm thinking of a number between 1 and 99")
# while condition
while True:
    guess = int(input("Enter the number: "))
  
    if guess < secret:
        print("Too low")
    elif guess == secret:
        print("Congrats! The number was ", secret)
        break
    else:
        print("Too high")
#hello sir I have heard difficulties with . isdecimal unable to implement it, hope to see you at office hours for help
# The condition while, why is it most time we use while True, True as the condition, is there another way in which we can enter something like an expression as the condition


      
#Ask the user to guess
#Check to see if the guess is <, >, or = secret number
# Print the right message
