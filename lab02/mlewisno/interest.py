# interest.py
# January 10th, 2013
#
# Mischa Lewis-Norelle

def main():
    print("This program calculates interest! You'll be rich in no time!")
    print("You will need to give me an initial deposit, monthly interest rate, monthly deposit, and number of months")
    INI_DEPOSIT = eval(input("Please enter an inital deposit: "))
    MON_RATE = eval(input("Please give me a monthly interest rate: "))
    MON_DEPOSIT = eval(input("Please enter a monthly deposit: "))
    NUM_MONTHS = eval(input("Please enter the number of months you'd like to calculate interest for: "))
    
    print("Initially you put in $", INI_DEPOSIT, sep='')
    TOTAL = INI_DEPOSIT
    for i in range(1, NUM_MONTHS + 1):
        TOTAL = TOTAL + TOTAL*MON_RATE
        TOTAL = TOTAL + MON_DEPOSIT
        TOTAL = TOTAL*100
        TOTAL = int(TOTAL)
        TOTAL = TOTAL / 100
        print("After month ", i, " you would have $", TOTAL, sep='')
    
    
main()