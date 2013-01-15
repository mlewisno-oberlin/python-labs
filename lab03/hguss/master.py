# master.py
# Simulates a game of mastermind
#
# Henry Lionni Guss
# 1/11/13

import random

NUM_TURNS = 10

def main():
    code = generateCode()
    print(code)
    print("I have a 4 letter code, made from 6 colours.")
    print("The colours are R, G, B, Y, P, or O.")
    for i in range(0, NUM_TURNS):
        guess = input("    Your Guess: ")
        if clue(code, guess) == True:
            print("You win! Aren't you smart.")
            return
        blacks, whites = clue(code, guess)
        print("Not quite.  You get", blacks, "black pegs, and", whites, "white pegs.")
    print("Sorry!  Better luck next time...")
    
def generateCode():
    newCode = ""
    for i in range(0, 4):
        newInt = random.randint(0, 6)
        if newInt == 0:
            newCode = newCode + "R"
        elif newInt == 1:
            newCode = newCode + "B"
        elif newInt == 2:
            newCode = newCode + "G"
        elif newInt == 3:
            newCode = newCode + "Y"
        elif newInt == 4:
            newCode = newCode + "O"
        else:
            newCode = newCode + "P"
    return newCode

def clue(code, guess):
    blacks = 0
    whites = 0
    for i in range(0,4):
        if code[i] == guess[i]:
            code = code[0:i] + "X" + code[i + 1: len(code)]
            guess = guess[0:i] + "Z" + guess[i + 1: len(code)]
            blacks = blacks + 1
    if blacks == 4:
        return True
    for c in range(0, 4):
        for i in range(0, 4):
            if code[c] == guess[i]:
                code = code[0:c] + "X" + code[c + 1: len(code)]
                guess = guess[0:i] + "Z" + guess[i + 1: len(code)]
                whites = whites + 1
    return blacks, whites

main()