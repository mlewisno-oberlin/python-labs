# fibonacci.py
# finds the nth term in the Fibonacci sequence
#
# Tyler Robertson
# January 6, 2013

def main() :
    previous = 1
    current = 1
    print("My incredible Fibonacci number generator!\n")
    n = eval(input("Please enter an integer greater than 2: "))
    for i in range(2,n):
        current, previous = current + previous , current
    print("The ",n,"th number in the Fibonacci sequence is ",current,sep='')
    
main()
