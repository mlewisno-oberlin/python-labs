# Allison Gross
# fibonacci.py
# Gets the nth number in Fibonacci sequence
# 01-08-13

def main():
    print("My incredible Fibonacci number generator")
    print()
    
    n = eval(input("Please enter an integer: "))
    fib1=1
    fib2=1
    for i in range(3,n+1):
        num = fib1+fib2
        fib1 = fib2
        fib2 = num
    print("The ", i, "th number in the Fibonacci sequence is ", num, sep='')

main()