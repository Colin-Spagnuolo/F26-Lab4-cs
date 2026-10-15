# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Colin Spagnuolo
# Date: October 14th
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

# Follow the instructions from readme.md.
def compute(num1=0,num2=0, operation='+'):
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
    nuM1 = int(input("Enter Number 1: "))
    nuM2 = int(input("Enter Number 2: "))
    operatioN = input("Enter an operation(+,-,*,/): ")
    result = compute(num1=nuM1, num2=nuM2, operation=operatioN)
    print(f"Result: {result}")

if __name__== "__main__":
    main()
