# sum.py
# Computes the sum of the first n positive integers
# 
# Connor Davies
# 1/6/13

def main():
    n = eval(input("Enter a number: ")) #Get number from user.
    sum = 0
    for i in range(1,n+1): #loop through the first n numbers
        sum = sum + i #sum the numbers
    print("The sum of the first", n, "positive integers is", sum) #print out the sum

main()