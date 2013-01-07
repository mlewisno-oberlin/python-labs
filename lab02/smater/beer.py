#Samantha Mater
#beer.py
#prints all 99 verses of 100 bottles of beer.

def main():
    NUM_BOTTLES = 99
    for i in range(NUM_BOTTLES,0,-1):
        print(i, "bottles of beer on the wall")
        print(i, "bottles of beer!")
        print("Take one down, pass it around")
        print(i-1, "bottles of beer on the wall!")
        print()
        
main()