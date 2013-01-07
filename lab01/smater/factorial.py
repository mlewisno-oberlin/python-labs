# factorial.py
# Computes the sum of the first 4 positive integers
# Samantha Mater
   
def main():
    sum = 1
    num = eval(input("Enter a number greater than 1: "))
    for i in range(1,num+1):
        sum = sum * i
    print(i, "! is ", sum, sep='')

main()