# sequence.py
# January 9th, 2013
#
# Mischa Lewis-Norelle

def main():
    NUM_SQUARES = eval(input("How many squares would you like calculated? "))
    print("These are all the squares from", NUM_SQUARES*NUM_SQUARES, "to 1")
    for i in range(NUM_SQUARES, 1, -1):
        print(i*i, ", ", sep='', end='')
    
    print(1)
    
main()