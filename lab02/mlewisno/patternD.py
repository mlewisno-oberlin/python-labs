# patternD.py
# January 12th, 2013
#
# Mischa Lewis-Norelle

def main():
    endNum = eval(input("What level of the pattern would you like me to show you? "))
    for i in range(1, endNum + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                print(j, " ", end='', sep='')
        print()

main()