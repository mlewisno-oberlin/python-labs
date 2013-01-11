# Allison Gross
# beer.py
# Prints 99 bottles of beer on the wall
# 01-08-13

def main():
    NUM_BOTTLES = 99
    for i in range(NUM_BOTTLES,0,-1):
        print(i, "bottles of beer on the wall")
        print(i, "bottles of beer! \nTake one down, pass it around")
        print(i-1, "bottles of beer on the wall!")
        print()

main()