#Samantha Mater
#fibonacci.py
#4 January 2013

def main():
    previous = 1
    current = 1
    print("My incredible Fibonacci number generator!")
    print()
    num = eval(input("Enter an integer: "))
    for i in range(3, num+1):
        temp = current
        current = current+previous
        previous = temp
    print("The ", num, "th number in the Fibonacci sequence is ", current, sep='')
    


main()