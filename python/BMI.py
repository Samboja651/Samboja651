# find your body mass index
# know your health

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

#Calculate the BMI value based on the weight and height values
BMI = weight / (height**2)

# round the number to a 1 decimal point
BMI = round(BMI, 1)

print(f"The body mass index is: {BMI}")

print("\n------BMI Categories------")

print("<18.5        : Underweight")
print("18.5 – 24.9  : Normal weight")
print("25 - 29.9    : Overweight")
print(">=30         : Obese")
