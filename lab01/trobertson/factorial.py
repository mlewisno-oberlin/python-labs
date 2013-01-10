# factorial.py
# Finds the factorial of the user inputted integer
#
# Tyler Robertson
# January 4, 2013

def main() :
    n = eval(input("Find factorial of: "))
    product = 1
    for i in range(1,n+1):
       product = product * i
    print("The factorial of", i, "is", product)

main()
