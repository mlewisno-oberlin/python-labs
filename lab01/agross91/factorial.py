# Allison Gross
# factorial.py
# computes factorial
# 01-07-13

def main():
    fact = 1
    n = eval(input( "What number should we compute the factorial of? "))
    for i in range(1, n+1):
        fact = fact*i
    print(n, "factorial is", fact)   

main()