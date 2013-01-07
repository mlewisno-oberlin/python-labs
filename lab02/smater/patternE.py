#Samantha Mater
#patternE.py
#6 January 2013

def main():
    print("We are going to make a pattern out of ASCII characters!")
    num = eval(input("Please enter a positive integer: "))
    
    print("**", sep='', end='')
    for i in range(1, num+1):
        print("*", sep='', end='')
    print()
    for a in range(1, num+1):
        print("*")
    print("*", sep='', end='')
    for j in range(1, num+1):
        print("*", sep='', end='')
    print()
    for b in range(1, num+1):
        print("*")
    print("**", sep='', end='')
    for k in range(1, num+1):
        print("*", sep='', end='')
    print()
    
main()