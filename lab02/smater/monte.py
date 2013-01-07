#Samantha Mater
#monte.py
import random
import math

def simpleDistance(x, y):
    return math.sqrt(x*x + y*y)

def main():
    print("We are going to compute an approximation of pi using the Monte Carlo method")
    num = eval(input("How many trials would you like to run? "))
    hits = 0
    
    for i in range(1, num+1):
        randX = random.uniform(-1.0, 1.0)  # randX is between -1.0 and 1.0
        randY = random.uniform(-1.0, 1.0)  # randY is between -1.0 and 1.0
        if simpleDistance( randX, randY ) <= 1:
            hits = hits + 1
    
    pi = (hits/num) * 4
    print(pi)
    
main()