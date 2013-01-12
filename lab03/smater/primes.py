# Samantha Mater
# 6 January 2013
# This finds a number of primes and lists how many twin primes are among them.
# primes.py

def isPrime(num):
    for i in range (2, num):
        if num%i == 0:
            return False
    if num <= 0:
        return False
    return True

def main():
    print("We are going to generate some prime numbers!")
    num = eval(input("How many numbers would you like to generate? "))
    primes = 0
    twinprimes = 0
    start = 2 
    while primes < num:
        if isPrime(start):
            primes = primes + 1
            print(start, " ", sep ='', end='')
            if isPrime(start-2):
                twinprimes = twinprimes + 1
        start = start + 1
    print()
    print("There are", twinprimes-1, "twin primes.") #the -1 accounts for 1 and 3, which
    #are two apart but are not twin primes

main()