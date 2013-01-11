# Allison Gross
# interest.py
# Figures out money earned from interest
# 01-08-13

def main():
    print("Welcome to the Interest Calculator")
    print()
    
    init = float(input("Enter your initial savings: "))
    rate = eval(input("Enter the monthly interest rate: "))
    cont = eval(input("Enter your monthly contribution: "))
    num = eval(input("How many months would you like computed: "))
    print()
    
    print("Initially you put in $", init, sep='')
    for i in range(1,num+1):
        init = round((init + init*rate + cont)*100)/100.0
        print("After month ", i, " you would have $", init, sep='')

main()
                      