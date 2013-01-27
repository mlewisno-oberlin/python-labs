# monte.py
# computes an approximation of pi using the monte carlo method
#
# Tyler Robertson
# January 12, 2013

import random
import math

def main() :
    print("This program calculates the value of Pi by")
    print("simulating the throwing of darts onto a round")
    print("target on a square background.\n")
    try:
        n = input("How many darts to throw: ")
        n = eval(n)
        hits = 0
        for i in range(0,n):
            if simpleDistance(random.uniform(-1.0, 1.0),random.uniform(-1.0, 1.0)) <= 1 :
                hits = hits + 1
        pi = 4 * hits/n
        print("The value of Pi after",n,"iterations is",pi)
        error = abs(pi - math.pi)/math.pi * 100
        print("which is off by ",round(error,3),"%",sep='')
    except ZeroDivisionError:
        print("Divide by zero error, enter a value greater than zero next time.")
    except NameError:
        print("\"",n,"\""," is not an acceptable number of darts",sep='')
    

def simpleDistance(x,y) :
    return math.sqrt(x*x + y*y)

main()
