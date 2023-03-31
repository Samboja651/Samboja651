
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
    
#Ask the user to guess
#Check to see if the guess is <, >, or = secret number
# Print the right message
