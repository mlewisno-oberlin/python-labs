# monte.py
# January 10th 2013
#
# Mischa Lewis-Norelle
import random
import math

def main():
    # Prompt user for number of throws to use for approximation
    trials = eval(input("How many triels would you like me to use to calculate pi? "))
    suc_attempts = 0
    for i in range(1, trials + 1):
        # Start by throwing a dart on a two by two square
        randX = random.uniform(-1.0,1.0)
        randY = random.uniform(-1.0,1.0)
        if(simpleDistance(randX, randY) < 1):
            suc_attempts = suc_attempts + 1

    cal_pi = 4*suc_attempts/trials
    print("The value of Pi after", trials, "iterations is:", cal_pi)
    
def simpleDistance(x, y) :
    return math.sqrt( x*x + y*y )

main()