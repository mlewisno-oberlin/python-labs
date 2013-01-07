#Samantha Mater
#patternB.py

def main():
    print("We are going to make a pattern out of ASCII characters!")
    num = eval(input("Please enter a positive integer: "))
    
    for i in range(1, num+1):
        for z in range(1, num+1):
            print(i, " ", sep='', end='')
        print()
main()