# choose.py
# Computes n choose k
#
# Tyler Robertson
# January 4, 2013

def main() :
    n = eval(input("Enter an \'n\' value: "))
    k = eval(input("Enter a \'k\' value: "))
    productN = 1 #implying I don't know how to methods
    for i in range(1,n+1):
       productN = productN * i
    productK = 1
    for i in range(1,k+1):
       productK = productK * i
    productNK = 1
    for i in range(1,(n-k)+1):
         productNK = productNK * i
    print("The value of n choose k for:",n,"choose",k,"is:",(productN/(productK*productNK)))
    
main()
