# Add comments before you do anything else
#!/usr/bin/env python3
# Author: Colin Spagnuolo
# Date: October 
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.

def sum(num1,num2):
    suma= num1 + num2
    return suma

def main():
     value1=input("Enter a Number: ")
     value2=input("Enter a second Number")
     result= value1 + value2
     print(f"The value of your 2 numbers is: {result}")

if __name__ == __main__:
    main()

