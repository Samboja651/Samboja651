# diamond shaped pyramid
rows = int(input("Enter number of rows: "))
k = 2 * rows - 2
# outer loop to print number of rows
for i in range(0, rows):
    # inner loop is used to print number of space
    for j in range(0, k):
        print(end = " ")
    # decrement k after each iteration
    k = k - 1
    # this inner loop is used to print stars
    for j in range(0, i + 1):
        print("*", end = " ")
    print(" ")

# downward triangle pyramid
# used to print the space
k = rows - 2
# output for downward triangle pyramid
for i in range(rows, -1,-1):
    # inner loop will print the spaces
    for j in range(k, 0, -1):
        print(end = " ")
    # increment k
    k = k + 1
    # print number of stars
    for j in range(0, i + 1):
        print("*", end = " ")
    print(" ")
