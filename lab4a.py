# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Colin Spagnuolo
# Date: October 9th, 2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
list=[1,2,3,4,5,6]
list_2=[1,3,5,7,9,11]
def is_even(mylist):
    result=False
    for i in mylist:
        if i%2==0:
            result=True
    return result
    
print(is_even(list))
print(is_even(list_2))

# @param: write parameters here
# @return: write return value here 

# TO DO 2: define the function with name `is_even`.

# TO DO 3: Call the function `is_even`.
