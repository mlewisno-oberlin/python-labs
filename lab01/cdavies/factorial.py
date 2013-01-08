# factorial.py
# Computes the factorial of the first n positive integers
#
# Connor Davies
# 1/6/13

def main():
    n = eval(input("Enter a number: ")) #Get number from user.
    total = 1
    for i in range(1,n+1): #loop through the first n numbers
        total = total * i #sum the numbers
    print("The factorial of", n, "positive integers is", total) #print out the sum

main()