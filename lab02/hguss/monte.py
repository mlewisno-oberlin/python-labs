# monte.py
# generates an approximation of pi using a dart throwing system.
#
# Henry Lionni Guss
# 1/5/12

import random
import math

def main():
    print("This program calculates the value of Pi by simulating the throwing of darts onto a round target on a square background.")
    darts = eval(input("Enter a number of darts to throw: "))
    hits = 0
    for i in range(darts):
        randX = random.uniform(-1.0,1.0)
        randY = random.uniform(-1.0,1.0)
        distance = simpleDistance(randX,randY)
        if distance <= 1:
            hits = hits + 1
    valueOfPi = hits / darts * 4
    print("The Value of Pi after", darts, "iterations is", valueOfPi)
def simpleDistance(x, y):
    return math.sqrt(x*x + y*y)

main()