# interest.py
# Calculates interest if you receive interest compounded monthly
#
# Tyler Robertson
# January 6, 2013

def main() :
    print("Welcome to the Interest Calculator!\n")
    principle = eval(input("Enter your initial savings: "))
    rate = eval(input("Enter the monthly interest rate: "))
    contribution = eval(input("Enter your monthly contribution: "))
    months = eval(input("How many months would you like computed: "))
    print("\nInitially you put in $",principle,sep='')
    for i in range(1,months+1):
        principle = principle + (principle * rate) + contribution
        principle = (int(principle * 100))/100
        print("After month ",i," you would have $",principle,sep='')
    
main()
