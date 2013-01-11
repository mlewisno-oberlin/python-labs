# Allison Gross
# monte.py
# 01-08-13

import random
import math

def simpleDistance(x,y):
    return math.sqrt(x*x + y*y)

def main():
    
    print("This program calculates the value of Pi by \nsimulating the throwing of darts onto a round \ntarget on a square background")
    
    darts = eval(input("How many darts to throw? "))
    hits = 0
    for i in range(0,darts):
        randX = random.uniform(-1.0, 1.0)
        randY = random.uniform(-1.0, 1.0)
        if simpleDistance(randX, randY) <= 1 :
            hits = hits + 1
    
    p = 4*hits/darts
    print("The value of Pi after", darts, "iterations is", p)
    

main()
    