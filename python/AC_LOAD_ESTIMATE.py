# AC Load Estimator 
print("Enter room dimensions.")
width=float(input("width: "))
height=float(input("height: "))
number_of_people=float(input("number of people: "))
horsepower=width * height * 0.1 + number_of_people * 0.06
print(f"horsepower used is: {horsepower:.2f}")
