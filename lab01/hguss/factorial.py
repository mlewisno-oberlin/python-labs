# factorial.py
# Computes factorials
#
# Henry Lionni Guss
# 1/3/12

def main():
    n = eval(input("Give me a positive number! "))
    product = 1
    for i in range(1, n + 1):
        product = product * i
    print(n, "factorial is", product)
    
main()