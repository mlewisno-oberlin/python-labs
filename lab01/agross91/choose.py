# Allison Gross
# choose.py
# computes n choose k
# 01-07-13

def main():
    n = eval(input("Enter the total number of objects: "))
    k = eval(input("Enter how many you want to choose: "))
    factN = 1
    for i in range(1,n+1):
        factN = factN*i
        
    factK=1
    for i in range(1, k+1):
        factK = factK*i
        
    factNminusK =1
    for i in range(1, n-k+1):
        factNminusK= factNminusK*i
    
    choose = factN/(factK*factNminusK)
    print(n, "choose", k, "equals", choose)

main()
    