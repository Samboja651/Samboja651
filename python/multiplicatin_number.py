# multiplication number in column
rows = int(input("Enter the number of rows: "))
for i in range(1, rows):
    for j in range(1, i + 1):
        # print multiplication
        print(i * j, end = " ")
    print()
