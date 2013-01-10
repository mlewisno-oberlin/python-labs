# patternD.py
# generates pattern D
#
# Tyler Robertson
# January 6, 2013

def main() :
    n = eval(input("Enter an index: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            for k in range(1, j+1):
                print(j,end='')
        print()
   
main()
