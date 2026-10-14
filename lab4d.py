# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Colin Spagnuolo
# Date: October 14th
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.
def compute(num1,num2, operation='+'):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == '/':
        return num1 / num2
    else:
        return "Not an operation"
def main():
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    operation = input("Enter an operation(+,-,*,/): ")
    result = compute(num1, num2, operation)
    print(f"Result: {result}")

if __name__== "__main__":
    main()
