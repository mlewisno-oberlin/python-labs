# fibonacci.py
# Calculates the first n fibonacci numbers
# 
# Connor Davies
# 1/8/13


def main():
    print("My incredible Fibonacci number generator!")
    print()
    n = eval(input("Please enter an integer greater than 1: ")) #Get number from user.
    a=1
    b=1
    c=2
    for i in range(0,n-2): #loop and calculate each fibonacci number.
        temp=b+c
        a=b
        b=c
        c=temp
    print("Term", n, "in the fibonacci sequence is ", c)
    
main()