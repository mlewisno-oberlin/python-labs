# interest.py
# Generates interest on an initial deposit using monthyl deposits and monthly interest rates
#
# Henry Lionni Guss
# 1/5/12

def main():
    deposit = eval(input("Enter an inital deposit: "))
    interest = eval(input("Enter a monthly interest rate: "))
    mDeposit = eval(input("Enter a monthly deposit: "))
    numMonths = eval(input("Enter a number of months: "))
    print("Initially you put in $", deposit, sep='')
    for i in range(numMonths):
        deposit = round(deposit * (1 + interest) + mDeposit, 2)
        print("After month ", i + 1, " you would have ", "$", deposit, sep='')
main()