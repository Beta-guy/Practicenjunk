import calclib
print("=" * 20)
print("| Stephanie's Calc |")
print("=" * 20)
while True:
    num1 = float(input("\nInput 1st number: "))
    op = input("\nWhat operator do you want to use (add, minus, divide, or multiply): ")
    if op.lower() == "exit":
        quit(0)
    num2 = float(input("\nInput 2nd number: "))
    if op.lower() == "add" or op == "+":
        print(calclib.add(num1, num2))
    elif op.lower() == "minus" or op.lower() == "subtract" or op == "-":
        print(calclib.minus(num1, num2))
    elif op.lower() == "divide" or op == "/":
        print(calclib.divide(num1, num2))
    elif op.lower() == "multiply" or op.lower() == "times" or op == "*" or op == "x":
        print(calclib.multiply(num1, num2))
    elif op.lower() == "power" or op.lower() == "^":
        print(calclib.power_of(num1, num2))
    else:
        print("Invalid Operator")
