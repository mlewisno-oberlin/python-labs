# sum.py
# Computes the sum of the first 4 positive integers
#
# Tyler Robertson
# January 4, 2013
   
def main():
    n = eval(input("Find sum of how many integers?: "))
    sum = 0
    for i in range(1,n+1):
       sum = sum + i
    print("The sum of the first", i, "positive integers is", sum)

main()
