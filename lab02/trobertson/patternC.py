# patternC.py
# generates pattern C
#
# Tyler Robertson
# January 6, 2013

def main() :
    n = eval(input("Enter an index: "))
    for i in range(1,n+1):
        for j in range(i,n+1):
            print(j,end='')
        print()
   
main()
