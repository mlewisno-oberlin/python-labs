# monte.py
# Calculates pi
# 
# Connor Davies
# 1/9/13

import random
import math

def main():
    print("This program calculates the value of Pi by simulating the throwing of darts onto a round target on a square background.")
    try:
        n = eval(input("How many darts to throw: "))
        hits = 0
        for i in range(0, n):
            randX = random.uniform(-1.0, 1.0)  # randX is between -1.0 and 1.0
            randY = random.uniform(-1.0, 1.0)  # randY is between -1.0 and 1.0
            if simpleDistance(randX,randY) <= 1 :
                hits=hits+1
        print("The value of Pi after ", n, " iterations is ", (4*hits/n)*100//1/100, " which is off by ", (math.pi/(4*hits/n))*100//1/100, "%", sep='')
    except ZeroDivisionError:
        print("\nPlease enter something other than 0.")
    except NameError:
        print("\nPlease enter a number.")
    except:
        print("\nSomething unexpected went wrong. Sorry!")
    
def simpleDistance(x, y):
    return math.sqrt(x*x + y*y)

main()