# beer.py
# This program will print out all 99 verses of the 99 bottles of beer on the wall song
#
# Mischa Lewis-Norelle
# January 6, 2012


def main():
    NUM_BOTTLES = 99
    for i in range(1, NUM_BOTTLES + 1):
        print(i, "bottles of beer on the wall", i, "bottles of beer.\nTake one down, pass it around,", i, "bottles of beer on the wall")
    
    
main()