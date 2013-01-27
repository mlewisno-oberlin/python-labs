# master.py
# Interactive Mind Mastery game
#
# Tyler Robertson
# January 7, 2013

import random

def main() :
    print("I have a 4 letter code, made from 6 colours.\nThe colours are R, G, B, Y, P, or O.")
    code = generateCode()
    NUM_TURNS = 10
    for i in range(NUM_TURNS) :
        guess = input("Your guess: ")
        if clue(guess,code) :
            break

def generateCode() :
    toReturn = ""
    for i in range(4) :
        rand = random.randrange(6)
        if rand == 0 :
            toReturn = toReturn + 'R'
        if rand == 1 :
            toReturn = toReturn + 'G'
        if rand == 2 :
            toReturn = toReturn + 'B'
        if rand == 3 :
            toReturn = toReturn + 'Y'
        if rand == 4 :
            toReturn = toReturn + 'P'
        if rand == 5 :
            toReturn = toReturn + 'O'
    return toReturn

def clue(guess,code) :
    if guess == code :
        print("You win! Aren't you smart!")
        return True
    black = 0
    white = 0
    for i in range(4):      #black
        if guess[i] == code[i] :
            black += 1
            guess = guess[0:i] + "x" + guess[i+1:len(guess)]
            code = code[0:i] + "z" + code[i+1:len(code)]
    for g in range(4):      #white
        for c in range(4):
            if c!=g and code[c] == guess[g] :
                white += 1
                guess = guess[0:g] + "x" + guess[g+1:len(guess)]
                code = code[0:c] + "y" + code[c+1:len(code)]
    print("Not quite. You get",black,"black pegs,",white,"white pegs.\n")
    return False

main()
