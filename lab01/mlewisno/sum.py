# sum.py
# Computes the sum of the first 4 positive integers
# 

def main():
    limit = eval(input("How many numbers do you wanna add up?"))
    sum = 0
    for i in range(1,limit+1):
        sum = sum + i
    print("The sum of the first", i, "positive integers is", sum)

main()