import calclib
import math
print("=" * 25)
print("| Stephanie's Calc 2.0  |")
print("=" * 25)
while True:
    num1 = float(input("Input 1st number: "))
    op = input("What operator do you want to use (add, minus, divide, or multiply): ")
    if op.lower() == "exit":
        quit(0)
    elif op.lower() == "sqrt":
        print(math.sqrt(num1))
    if op.lower() == "add" or op == "+":
        num2 = float(input("Input 2nd number: "))
        print(calclib.add(num1, num2))
    elif op.lower() == "minus" or op.lower() == "subtract" or op == "-":
        num2 = float(input("\nInput 2nd number: "))
        print(calclib.minus(num1, num2))
    elif op.lower() == "divide" or op == "/":
        num2 = float(input("\nInput 2nd number: "))
        print(calclib.divide(num1, num2))
    elif op.lower() == "multiply" or op.lower() == "times" or op == "*" or op == "x":
        num2 = float(input("\nInput 2nd number: "))
        print(calclib.multiply(num1, num2))
    elif op.lower() == "power" or op.lower() == "^":
        num2 = float(input("\nInput 2nd number: "))
        print(calclib.power_of(num1, num2))
    elif op.lower() == "sqrt":
        pass
    else:
        print("Invalid Operator")
