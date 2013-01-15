# patternE.py
# January 12th, 2013
#
# Mischa Lewis-Norelle

def main():
    endNum = eval(input("What level of the pattern would you like me to show you? "))
    # Prints the top row of the "E"
    for i in range(1, endNum + 3):
        print("*", sep='', end='')
    print("")
    # Prints the first part of the E's spine
    for i in range(1, endNum + 1):
        print("*")
    # Prints the middle row of the "E"
    for i in range(1, endNum + 3):
        print("*", sep='', end='')
    print("")
    # Prints the second part of the E's spine
    for i in range(1, endNum + 1):
        print("*")
    # Prints the last row of the "E"
    for i in range(1, endNum + 3):
        print("*", sep='', end='')
    
    print("")

main()