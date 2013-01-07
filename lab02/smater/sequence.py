#Samantha Mater
#sequence.py

def main():
    print("This program lists the squares of all integers from some start down to one.")
    print()
    
    start = input("Enter a number to begin: ")
    print("Squares from", start, "down to 1: ")
    for i in range(6,1,-1):
        print(i*i, ", ", sep='', end='')
    print("1")
main()