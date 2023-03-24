# See Instructions tab
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, " is a multiple of 3 and 5")
    elif num % 5 == 0:
        print(num, " is a multiple of 5")
    elif num % 3 == 0:
        print(num, " is a multiple of 3")
    else:
        print(num)
#initially line 7 ,5 were starting respectively then line 3 came last and the output is that it prints only multiples of 3 alone and 5 alone when I interchanged  it works / it was tricky

# Print numbers 1 to 100
# For multiples of 3, print "X is a multiple of 3"
# For multiples of 5, print "X is a multiple of 5"
