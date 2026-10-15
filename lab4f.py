# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Colin Francesco Spagnuolo
# Date: October 14th 2026
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py
def get_initials(*args):
    initials=[]
    for name in args:
        initials.append(name[0])
    return initials
def main():
    print(get_initials("Alex","Sandra","Billy"))
if __name__=="__main__":
    main()
# Follow the instructions from readme.md.
