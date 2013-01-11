# Allison Gross
# patternD.py
# prints pattern D
# 01-08-13

def main():
    n = eval(input("Enter an integer: "))
    for i in range(1,n+1):
        for j in range(1, i+1):
            for c in range(1, j+1):
                print(j, end='')
        print()

main()