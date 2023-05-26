# alphabet pattern
print("The character pattern")
asciiValue = 65 # for A
for i in range(0,6):
    for j in range(0, i + 1):
        # convert ascii value to char
        alphabet = chr(asciiValue)
        print(alphabet, end = " ")
        asciiValue += 1
    print()
