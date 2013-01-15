# primes.py
# Makes a list of primes and finds any twin primes among them.
# 
# Connor Davies
# 1/10/13

def main():
    n = eval(input("Please enter a number greater than 1:"))
    prev=2 #the first prime
    total=0 #total number of twins
    print("The first", n, "primes are: ", end="")
    print(2, end="")
    for i in range(3,n+1): #loop through all numbers up to n
        if isPrime(i): #check if they're prime
            print(",", i, end="") #print out the primes
            if i-prev==2: #check for twins
                total=total+1 #add to the twin total
            prev=i #set the previous prime to the current one for future twin checks
    print()
    print("Amongst these there are", total, "twin primes.")


def isPrime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

main()