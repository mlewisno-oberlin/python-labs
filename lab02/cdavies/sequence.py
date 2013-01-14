# sequence.py
# Calculates a sequence of squares
# 
# Connor Davies
# 1/9/13

import math

def main():
    print("This program calculates a list of squares equal or lower than your number squared")
    n = eval(input("Please enter a number to square: "))
    print("Squares from", n*n, "down to 1:")
    for i in range(0, n-1):
        print((n-i)*(n-i), ", ", end="")
    print("1.")
    

main()