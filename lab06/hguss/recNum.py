# recNum.py
# Performs recursive number operations
#
# Henry Lionni Guss
# 1/25/13

def main():
    try:
        n, k = eval(input("Enter two non negative integers (seperated by commas): "))
    # User entered an empty string or an incorrect character
    except SyntaxError:
        print("You have entered either an incorrect character or an empty string.")
        return
    # User entered at least one non-evaluable object
    except NameError:
        print("You have entered at least one non-integer.")
        return
    # User did not enter two valuables
    except TypeError:
        print("You did not enter two values.")
        return
    # User did not enter a second value, or entered too many
    except ValueError:
        print("You did not enter a second value, or entered too many.")
        return
    print(power(n, k))
    print(sumSquares(n))
    print(choose(n, k))

#Returns x to the power of y
def power(x, y):
    try:
        if y == 0:
            return 1
    #Entered at least one string
    except TypeError:
        print("Do not enter values as strings.")
        return
    return x * power(x, y - 1)

#Returns the sum of n squares
def sumSquares(n):
    try:
        if n == 0:
            return 0
    #Entered at least one decimal
    except RuntimeError:
        print("This program does not accept decimals, floats, doubles.")
        return
    return n * n + sumSquares(n - 1)

#Returns n choose k
def choose(n, k):
    if k > n:
        return 0
    if k == n:
        return 1
    if k == 0:
        return 1
    return choose(n - 1, k) + choose(n - 1, k - 1)

main()