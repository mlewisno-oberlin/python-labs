# patternN.py
# January 12th, 2013
#
# Mischa Lewis-Norelle

def main():
    endNum = eval(input("What level of the pattern would you like me to show you? "))
    
    # Print the top of the N
    print("*", end = '', sep = '')
    for i in range(1, endNum + 1):
        print(" ", sep = '', end = '')
    print("*", end = '', sep = '')
    print("")
    
    # Print the middle of the N
    for i in range(1, endNum + 1):
        # Print the first star of each line
        print("*", end = '', sep = '')
        # Print the middle part of the line
        for j in range(1, i):
            print(" ", end = '', sep = '')
        
        print("*", end = '', sep = '')
        
        for j in range(1, endNum - i + 1):
            print(" ", end = '', sep = '')
        # Print the last star of each line
        print("*", end = '', sep = '')
        print("")
    

    # Print the top of the N
    print("*", end = '', sep = '')
    for i in range(1, endNum + 1):
        print(" ", sep = '', end = '')
    print("*", end = '', sep = '')
    print("")
    
main()