# sum.py
# Asks the user how many cpnsecutive integers to add up and then computes and prints the sum
# 

def main():
    limit = eval(input("How many numbers do you wanna add up?"))
    sum = 0
    for i in range(1,limit+1):
        sum = sum + i
    print("The sum of the first", i, "positive integers is", sum)

main()