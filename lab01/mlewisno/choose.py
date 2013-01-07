# choose.py
# Prompts the user to pick an n and k and then computes and prints n take k
# 

def main():
    print("Hello user, this will calculate n take k for probability and the like")
    nlimit = eval(input("What n would you like? "))
    klimit = eval(input("What k would you like? "))
    
    # Calculates n factorial
    nsum = 1
    for i in range(1,nlimit+1):
        nsum = nsum*i
    
    
    # Calculates k factorial
    ksum = 1
    for i in range(1,klimit+1):
        ksum = ksum*i
    
    # Calculates k factorial
    nksum = 1
    for i in range(1,(nlimit - klimit + 1)):
        nksum = nksum*i
    
    print(nlimit, "take", klimit, "is", (nsum/(ksum*nksum) ))

main()