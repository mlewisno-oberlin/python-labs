# beer.py
# Prints out 99 verses of the song "Ninety-Nine Bottles of Beer on the Wall"
#
# Tyler Robertson
# January 6, 2013

def main() :
    NUM_BOTTLES = 99
    for i in range(NUM_BOTTLES,0,-1):
        print(i,"bottles of beer on the wall\n",i,"bottles of beer!\nTake one down, pass it around\n",i-1,"bottles of beer on the wall!")

main()
