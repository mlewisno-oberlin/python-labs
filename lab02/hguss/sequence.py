# sequence.py
# list squares of integers from input number down to 1.
#
# Henry Lionni Guss
# 1/5/12

def main():
    start = eval(input("Give me a whole number:"))
    print("Perfect squares from", start * start, "down to 1")
    for i in range(start, 0, -1):
        print(i**2, end=' ')
    print()
    
main()