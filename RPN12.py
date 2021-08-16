#!/bin/python
import math
from collections import deque
#Create stack
stack = deque()
#Error handler for checking the number of items in a stack
def error_Numitems(value):
    if len(stack) < value:
        print("ERROR: Insufficient items in stack")
        return True
    else:
        return False
#Error handler for check if the input value is numeric
def error_Numonly(value):
    if value.isnumeric() == True:
        return False
    else:
        return True
#Ensures that the right operation happens based on the operator
def parse_Operator(value):
    if value == "q":
        exit()
    elif value == "add":
        if error_Numitems(2) == False:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = add(num1, num2)
            stack.append(num3)
            print(int_morph(num3))
    elif value == "sub":
        if error_Numitems(2) == False:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = sub(num1, num2)
            stack.append(num3)
            print(int_morph(num3))
    elif value == "mul":
        if error_Numitems(2) == False:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = mul(num1, num2)
            stack.append(num3)
            print(int_morph(num3))
    elif value == "div":
        if error_Numitems(2) == False:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = div(num1, num2)
            stack.append(num3)
            print(int_morph(num3))
    elif value == "sqrt":
        if error_Numitems(1) == False:
            num1 = stack.pop()
            num2 = sqrt(num1)
            stack.append(num2)
            print(int_morph(num2))
    else:
        return False
    return True
#If value is equal to value.0 it spits out a integer
def int_morph(value):
    value1 = float(value)
    value2 = int(value)
    if float(value) == int(value):
        return value2
    else:
        return value1
#Additions
def add(val1, val2):
    val3 = float(val2) + float(val1)
    return val3
#Subtraction
def sub(val1, val2):
    val3 = float(val2) - float(val1)
    return val3
#Multiplication
def mul(val1, val2):
    val3 = float(val2) * float(val1)
    return val3
#Division
def div(val1, val2):
    val3 = float(val2) / float(val1)
    return val3
#square root
def sqrt(val1):
    return math.sqrt(int(val1))
#grabs number/operator from user and with some error mitigation add it to the stack
def acquire_Next():
    user_Input = input("Enter value: ").lower()
    if error_Numonly(user_Input) == False or user_Input.find("-") != -1 and user_Input != "-" or user_Input.find(".") != -1 and user_Input != ".":
        stack.append(user_Input)
    elif error_Numonly(user_Input) == True and user_Input != 'add' and user_Input != 'sub' and user_Input != 'mul' and user_Input != 'div' and user_Input != 'sqrt' and user_Input != 'q':
        print("ERROR:Only numbers are allowed in stack")
    elif parse_Operator(user_Input) == False:
        print("Error:  Input must be numeric or a valid operator [add,sub,mul,div,or q]")
#the start
print("*********************")
print("* Kilroy's RPN Calc *")
print("*********************")
while True:
    acquire_Next()
else:
	exit()
