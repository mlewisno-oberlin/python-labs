# choose.py
# performs the choose function
#
# Henry Lionni Guss
# 1/3/12

def main():
    n, k = eval(input("Give me two numbers, seperated by commas. "))
    nFact = 1
    for i in range(1, n):
        nFact = nFact * i
    
    kFact = 1
    for i in range(1, k):
        kFact = kFact * i
        
    nk = n - k
    nkFact = 1
    for i in range(1, nk):
        nkFact = nkFact * i

    print(n, "choose", k, "equals", nFact / (kFact * nkFact))
    
main()