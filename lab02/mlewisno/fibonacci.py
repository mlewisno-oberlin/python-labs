# fibonacci.py
# January 10th, 2013
#
# Mischa Lewis-Norelle

def main():
    print("My incredible Fibonacci number generator!")
    print()
    FIB_NUM = eval(input("Please tell me which fibonacci number you'd like me to calculate: "))
    current = 1
    previous = 1
    for i in range(3, FIB_NUM + 1):
        temp = current
        current = current + previous
        previous = temp
    
    print("The ", FIB_NUM, "th Fibonacci number is ", current,  sep='')

main()