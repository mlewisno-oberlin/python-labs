# beer.py
# Displays the 99 bottles of beer on the wall song
#
# Henry Lionni Guss
# 1/5/12

def main():
    NUM_BOTTLES = 99
    for i in range(NUM_BOTTLES, 0, -1):
        print(i, "bottles of beer on the wall")
        print(i, "bottles of beer!")
        print("Take one down, pass it around")
        print(i - 1, "bottles of beer on the wall!")
main()