# Allison Gross
# patternC.py
# prints pattern C
# 01-08-13

def main():
    n = eval(input("Enter an integer: "))
    for i in range(1, n+1):
        p = i
        for j in range(i, n+1):
            print(p, end='')
            p = p+1
        print()

main()