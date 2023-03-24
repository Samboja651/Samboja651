numbers = int(input("How many numbers will you enter? "))
i = 0
minimum = float('inf')

for i in range(numbers):
  x = int(input("Enter a number: "))
  # check whether x is smaller than minimum, and reassign minimum to it if so
  if x < minimum:
    minimum = x

print("The smallest number is:", minimum)