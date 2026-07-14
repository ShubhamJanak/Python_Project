Principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than 0.")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate cannot be less than 0.")
    else:
        break

while True:
    time = float(input("Enter the time period: "))
    if time < 0:
        print("Time cannot be less than 0.")
    else:
        break
Total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} year is: ${Total:.2f}")