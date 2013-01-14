# primes.py
# January 13th 2013
#
# Mischa Lewis-Norelle
import math

def main():
    print("Welcome to the magical and wonderful primes calculator! ")
    numPrimes = eval(input("How many primes would you like calculated? "))
    current = 2
    primeCounter = 0
    numTwinPrimes = 0
    
    print("The first", numPrimes, "primes are:")
    while(primeCounter < numPrimes):
        # Here we check to see if the current number is prime
        if(isPrime(current)):
            primeCounter += 1
            # Now we check and see if this prime has a twin, if it is, the counter increases
            if(isPrime(current + 2)):
                if(primeCounter < numPrimes):
                    numTwinPrimes += 1
            print(current, " ", end='', sep='')
        if(current > 2):
            current += 1
        current += 1
    
    print("")
    print("Amongst these there are", numTwinPrimes, "twin primes.")
    
def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0):
            return False
    
    return True

main()