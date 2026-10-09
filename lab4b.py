# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Colin Spagnuolo
# Date: October 9th
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here
list=[1,2,3,4,5,6,7,8]
def even_numbers(mylist):
    evens=[]
    for i in mylist:
        if i%2==0:
            evens.append(i)
    return evens
print(even_numbers(list))

# TO DO 2: Create the function.

# TO DO 3: Call the function.
