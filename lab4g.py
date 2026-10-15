# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Colin Spagnuolo
# Date: October 14th 2026
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py
numbers= list(range(2,11))
numbers_R = list(map(lambda x: x**2, numbers))
print(f"The numbers squared are: {numbers_R}")

numbers_D = list(filter(lambda x: x % 2 ==0, numbers))
print(f"The numbers divisible by 2 are: {numbers_D}")
# Follow the instructions from readme.md.
