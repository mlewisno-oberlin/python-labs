# primes.py
# Gives the first n primes, and number of pairs of twin primes in such set
#
# Henry Lionni Guss
# 1/11/13

def main():
    x = eval(input("Enter a number: "))
    primes = 0
    twins = 0
    i = 2
    print ("The first", x, "primes are:")
    while primes < x:
        if isPrime(i) == True:
            primes = primes + 1
            print (i, end = ' ')
            if primes < x:
                if isPrime(i + 2) == True:
                    twins = twins + 1
        i = i + 1
    print()
    print("Amongst these there are", twins, "twin primes.")
    
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

main()