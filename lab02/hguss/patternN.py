# patternN.py
# creates a pattern of stars resembling an N
#
# Henry Lionni Guss
# 1/5/12

def main():
    n = eval(input("Enter a positive integer: "))
    print("*", end = '')
    for i in range(0, n):
        print(" ", end = '')
    print("*")
    for i in range(0, n):
        print("*", end = '')
        for j in range(0, i):
            print(" ", end = '')
        print("*", end = '')
        for j in range(0, n - i - 1):
            print(" ", end = '')
        print("*")
    print("*", end = '')
    for i in range(0, n):
        print(" ", end = '')
    print("*")
main()