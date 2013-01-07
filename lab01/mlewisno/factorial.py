# factorial.py
# Computes the sum of the first 4 positive integers
# 

def main():
    limit = eval(input("What factorial do you want me to compute? "))
    sum = 1
    for i in range(1,limit+1):
        sum = sum*i
    print(limit, "factorial is", sum)

main()