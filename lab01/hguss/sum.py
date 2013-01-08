# helloworld.py
# Add n first positive integers
#
# Henry Lionni Guss
# 1/3/12

def main():
    n = eval(input("How many numbers would you like to add? "))
    nSum = 0
    for i in range(1, n + 1):
        nSum = nSum + i
    
    print("The sum of the first", n, "positive integers is", nSum)
    
main()
