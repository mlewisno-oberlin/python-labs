# Allison Gross
# patternB.py
# prints pattern B
# 01-08-13

def main():
    n = eval(input("Enter an integer: "))
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i, end='')
        print()
    
main()