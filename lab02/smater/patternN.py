#Samantha Mater
#patternN.py
#6 January 2013

def main():
    print("We are going to make a pattern out of ASCII characters!")
    num = eval(input("Please enter a positive integer: "))
    
    print("*", end='')
    for i in range(1, num+1):
        print(" ", end='')
    print("*")
    for n in range(1, num+1):
        print("*", end='')
        for o in range(1, n):
            print(" ", end='')
        print("*", end ='')
        for p in range(n, num):
            print(" ", end='')
        print("*")
    print("*", end='')
    for m in range(1, num+1):
        print(" ", end='')
    print("*")
    
main()