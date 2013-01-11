# Allison Gross
# patternE.py
# prints pattern E
# 01-08-13

def main():
    n = eval(input("Enter an integer: "))
    for i in range(1, n+3):
        print("*", end='')
    print()
    for i in range(1, n+1):
        print("*")
    for i in range(1, n+2):
        print("*", end='')
    print()
    for i in range(1, n+1):
        print("*")
    for i in range(1, n+3):
        print("*", end='')
    print()

main()