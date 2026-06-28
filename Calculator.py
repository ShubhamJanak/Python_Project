num1 = float(input("Enter First Number: "))
op = input("Enter a operator: ")
num2 = float(input("Enter second Number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
