# RecNum.py
# Calculates various things recursively.
# 
# Connor Davies
# 1/22/13

def main():
    try:
        print("Welcome to the Recursive Calculator!") #Welcome the user to the program
        print()
        #Ask the user for 2 numbers
        n = eval(input("Please enter the base number (decimals will be rounded down):"))//1
        k = eval(input("Please enter the exponent number (decimals will be rounded down):"))//1
        print()
        print(n, "to the power of", k, "is", pow(n, k)) #print out n^k
        print("The sum of the first", n, "squares is", sps(n)) #print out the sum of the first n squares
        print(n, "choose", k, "is", choose(n,k)) #print out n choose k
    except NameError:
        print("Please enter a valid number")
    except SyntaxError:
        print("Please enter only a number")
    

##
#Calculate n^k recursively
#@param n The base number for the calculation
#@param k The exponent for the calculation
#@return n^k
def pow(n, k):
    if k==0: return 1
    return n*pow(n, k-1)

##
#Calculate the sum of the first n squares recursively
#@param n The number of squares to sum
#@return The sum of the first n squares
def sps(n):
    if n==0: return 0
    return n*n + sps(n-1)

##
#Calculate n choose k
#Calculate n choose k recursively
#@param n The first number for the calculation
#@param k The second number for the calculation
#@return n choose k
def choose(n, k):
    if k>n: return 0
    if k==n: return 1
    if k==0: return 1
    return choose(n-1, k) + choose(n-1, k-1)

main()