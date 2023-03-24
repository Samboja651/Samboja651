# Write a program to find the minimum of numbers provided by the user
times = int(input("How many times will you enter? "))
small = []

for time in range(times):
    number = int(input("Enter a number:"))
    x = number
    small.append(x)
    minimum = small[0]
    for num in small:
        if num < minimum:
            minimum = num
print("The smallest number is: ",minimum)
# your starter code gave me a big challenge using it, I have wiped out the entire starter code and written on my thinking, the output matches