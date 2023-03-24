import random, time

# TODO 1: Print a welcome message. Include "press Enter to start".

print("Welcome to our fastest finger game.")

# TODO 2: use input() to wait for the user to press Enter
input("When the screen says DRAW, please press Enter to start the game")
# TODO 3: wait a random number of seconds, then print "DRAW!"
delay = random.randint(1,10)
time.sleep(delay)
print("DRAW!")

# TODO 4: Time how long it takes for the user to press Enter. Get the current time with time.time()
start = time.time()

# TODO 5: use input() to wait for the user to press Enter
input()

# TODO 6: Use time.time() again to get the time after the user pressed Enter
stop = time.time()
# TODO 7: Print how long it took
elapsed_time = stop - start

# TODO 8: Print different results, based on how long it took
print(f"The elapsed time is: {elapsed_time}")

if elapsed_time > 0.3:
  print("Too slow! Try again next time.")
elif elapsed_time < 0.1:
  print("You pressed Enter too soon, didn't you?")
elif elapsed_time > 0.1:
  print("You're the fastest draw in the west, congratulations!")
else:
  print("Try again!")