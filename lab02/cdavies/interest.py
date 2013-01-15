# interest.py
# Calculates interest
# 
# Connor Davies
# 1/8/13


def main():
    print("Welcome to the Interest Calculator!")
    print()
    IS = eval(input("Enter your initial savings:")) #Get initial savings from user.
    IR = eval(input("Enter your monthly interest rate:")) #Get interest rate from user.
    MC = eval(input("Enter your monthly contribution:")) #Get monthly contribution from user.
    n = eval(input("How many months would you like computed:")) #Get number of months from user.
    total=IS
    print()
    print("Initially you put in", IS)
    for i in range(0,n): #loop and calculate interest
        total=total+total*(IR)+20
        total=((total*100)//1)/100
        print("After ", i+1, " month, you would have $", total, sep='')
    
    
main()