# recNum.py
# gives various mathmatical responses based on the user's input
#
# Tyler Robertson
# 1/25/13

def main() :
    x = eval(input("Please enter a natural number x: "))
    k = eval(input("Pleave enter a natural number k: "))
    print(x,"raised to the power of",k,"is",power(x,k))
    print("The sum of the first",x,"squares is",sumSq(x))
    print(x,"choose",k,"is",choose(x,k))

# recursively finds x^k
def power(x,k) :
    if k == 0 :
        return 1
    else :
        return x*power(x,k-1)
    
# recursively finds the sum of the first x squares
def sumSq(x) :
    if x == 0 :
        return 0
    else :
        return power(x,2) + sumSq(x-1)
    
# recursively finds x choose k
def choose(x,k):
    if k > x :
        return 0
    if k == x :
        return 1
    if k == 0 :
        return 1
    else:
        return choose(x-1,k) + choose(x-1,k-1)
    
main()
