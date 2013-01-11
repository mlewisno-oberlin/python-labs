# Allison Gross
# sum.py
# Computes the sum of the first 4 positive integers
# 01-07-13

   
def main():
    sum = 0
    n = eval(input( "Please give me a number: "))
    for i in range(1, n+1):
        sum = sum + i
        
    print("The sum of the first", i, "positive integers is", sum)

main()
   