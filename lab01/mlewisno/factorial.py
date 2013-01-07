# factorial.py
# Prompts the user to say what factorial they'd like computed and then computes and prints it.
# 

def main():
    limit = eval(input("What factorial do you want me to compute? "))
    product = 1
    for i in range(1,limit+1):
        product = product*i
    print(limit, "factorial is", product)

main()