# patternE.py
# generates pattern E
#
# Tyler Robertson
# January 6, 2013

def main() :
    n = eval(input("Enter an index: "))
    print("**",sep='',end='')
    for i in range(1,n+1):
        print("*",sep='',end='')
    print()
    for i in range(1,n+1):
        print("*")
    print("*",sep='',end='')
    for i in range(1,n+1):
        print("*",sep='',end='')
    print()
    for i in range(1,n+1):
        print("*")
    print("**",sep='',end='')
    for i in range(1,n+1):
        print("*",sep='',end='')
    print()
   
main()
