# primes.py
# Prints out the first n prime numbers and the ammount of twin primes within those
#
# Tyler Robertson
# January 7, 2013

def main() :
    n = eval(input("How many primes do you want to print: "))
    print("The first",n,"primes are:")
    twinPrimes = 0
    printed = 1
    previous = 2
    current = 3
    if n > 0 :
        print(previous,end=' ')
    while printed < n :
        if isPrime(current) :
            print(current,end=' ')
            printed = printed + 1
            if current - previous == 2 :
                twinPrimes = twinPrimes + 1
            previous = current
        current = current + 2
    print("\nAmongst these there are",twinPrimes,"twin primes.")
    


def isPrime(x) :
    if x % 2 == 0 :
        return False
    for i in range(3,x//2,2):
        if x % i == 0 and x!=3:
            return False
    return True

main()
