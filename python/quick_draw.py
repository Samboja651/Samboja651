# how fast a you
import random, time

print("Welcome to our fastest finger game.")

#  use input() to wait for the user to press Enter
input("When the screen says DRAW, please press Enter to start the game")
# wait a random number of seconds, then print "DRAW!"
delay = random.randint(1,10)
time.sleep(delay)
print("DRAW!")

# Time how long it takes for the user to press Enter. Get the current time with time.time()
start = time.time()

#  use input() to wait for the user to press Enter
input()

#  Use time.time() again to get the time after the user pressed Enter
stop = time.time()
#  Print how long it took
elapsed_time = stop - start

# Print different results, based on how long it took
print(f"The elapsed time is: {elapsed_time}")

if elapsed_time > 0.3:
  print("Too slow! Try again next time.")
elif elapsed_time < 0.1:
  print("You pressed Enter too soon, didn't you?")
elif elapsed_time > 0.1:
  print("You're the fastest draw in the west, congratulations!")
else:
  print("Try again!")
