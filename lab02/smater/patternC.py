#Samantha Mater
#patternC.py
#6 January 2013

def main():
    print("We are going to make a pattern out of ASCII characters!")
    num = eval(input("Please enter a positive integer: "))
    
    for i in range(1, num+1):
        for z in range(i, num+1):
            print(z, " ", sep='', end='')
        print()
main()