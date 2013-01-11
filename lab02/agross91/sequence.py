# Allison Gross
# sequence.py
# Prints a sequence of square numbers
# 01-08-13

def main():
    start = eval(input("Enter a starting integer: "))
    for i in range(start, 1, -1):
        print(i*i, ", ", sep='', end='')
    print("1")

main()