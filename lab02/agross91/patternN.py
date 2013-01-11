# Allison Gross
# patternN.py
# prints pattern N
# 01-08-13

def main():
    n = eval(input("Enter an integer: "))
    print("*", end='')
    for i in range (1,n+1):
        print(" ", end='')
    print("*")
    
    for i in range(1,n+1):
        print("*", end='')
        for j in range(1, i):
            print(" ", end='')
        print("*", end='')
        for j in range(1, n-i+1):
            print(" ", end='')
        print("*")
    
    print("*", end='')
    for i in range (1,n+1):
        print(" ", end='')
    print("*")

main()