# beer.py
# gives a designated fibonacci place
#
# Henry Lionni Guss
# 1/5/12

def main():
    place = eval(input("Enter an integer 2 or greater: "))
    numOne = 1
    numTwo = 1
    for i in range(place -1, 1, -1):
        temp = numOne
        numOne = numTwo
        numTwo = temp + numTwo
    print("The",place,"number in the fibonacci sequence is",numTwo)
main()