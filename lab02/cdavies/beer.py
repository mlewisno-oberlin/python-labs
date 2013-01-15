# beer.py
# Recites a number of verses of beer on a wall.
# 
# Connor Davies
# 1/8/13

NUM_BOTTLES=99
def main():
    for i in range(0, NUM_BOTTLES): #loop through all verses
        print(NUM_BOTTLES-i, "bottles of beer on the wall")
        print(NUM_BOTTLES-i, "bottles of beer!")
        print("Take one down, pass it around")
        print(NUM_BOTTLES-i-1, "bottles of beer on the wall!")
        print()
    
main()
