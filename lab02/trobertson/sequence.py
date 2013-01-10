# sequence.py
# Computes a list of squares starting from user's input to 1
#
# Tyler Robertson
# January 6, 2013

def main() :
    start = eval(input("Please input a start value for the sequence: "))
    print("Squares from",start**2,"down to 1:")
    print(start**2,sep='',end='')
    for i in range(start-1, 0, -1):
        print(", ",i**2,sep='',end='')
    print()
    
main()
