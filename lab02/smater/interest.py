#Samantha Mater
#interest.py
#4 January 2013

def main():
    print("Welcome to the Interest Calculator!")
    print()
    init = eval(input("Enter your intial savings: "))
    ir = eval(input("Enter your monthly interest rate: "))
    contrib = eval(input("Enter your monthly contribution: "))
    months = eval(input("How many months would you like computed? "))
    print()
    print("Initially you put in $", init, sep='')
    for i in range(1, months+1):
        init = (init*ir) + contrib + init
        init = init*100
        init = int(init)
        init = init/100
        print("After month ", i, " you would have $", init, sep='')
    
main()