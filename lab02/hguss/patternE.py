# patternE.py
# creates a pattern of stars resembling an E
#
# Henry Lionni Guss
# 1/5/12

def main():
    n = eval(input("Enter a positive integer: "))
    for i in range(0, n + 2):
        print("*", end = '')
    print()
    for i in range(0, n):
        print("*")
    for i in range(0, n + 1):
        print("*", end = '')
    print()
    for i in range(0, n):
        print("*")
    for i in range(0, n + 2):
        print("*", end = '')
    print()
main()