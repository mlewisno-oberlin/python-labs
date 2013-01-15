# Samantha Mater
# master.py
# This plays the game of mastermind with the user
# 7 January 2013

import random

def generateCode(): #this creates the code the user needs to guess
    code = ""
    for i in range(1, 5):
        x = random.randint(0, 5)
        if x == 0:
            code = code + "R"
        if x == 1:
            code = code + "B"
        if x == 2:
            code = code + "G"
        if x == 3:
            code = code + "Y"
        if x == 4:
            code = code + "O"
        if x == 5:
            code = code + "P"
    #print(code)
    print()
    return code

def clue(code, guess):
    if code == guess:
        print()
        print("Congratulations!  You've guessed the code!  It is indeed", code)
        print("    Thank you for playing!")
        return True
    whitepegs = 0
    blackpegs = 0
    for i in range(0, 4):
        if code[i] == guess[i]:
            blackpegs = blackpegs + 1
            code = code[0:i] + "x" + code[i+1:len(code)]
            guess = guess[0:i] + "z" + guess[i+1:len(guess)]
    for n in range(0,4):
        for m in range(0,4):
            if guess[n] == code[m]:
                whitepegs = whitepegs + 1
                code = code[0:m] + "x" + code[m+1:len(code)]
                guess = guess[0:n] + "z" + guess[n+1:len(guess)]
    print("There are", blackpegs, "black pegs, and", whitepegs, "white pegs.")
    print()
    return False
    
    

def main():
    NUM_TURNS = 10
    print("Welcome to the game of Mastermind!")
    print()
    print("You have 10 turns to guess a four letter code made up of the letters")
    print("R, O, Y, G, B, P.  A black peg means you have a correct letter in the")
    print("correct spot.  A white peg means you have a correct letter in the wrong")
    print("spot.  Good luck!")
    print()
    print("If you are a grader, press 1 and hit enter.")
    print("If you are a student or want to play, press 2 and hit enter.")
    grader = eval(input("  "))
    if grader == 2:
        code = generateCode()
    if grader == 1:
        print()
        code = input("Please enter a code for grading purposes:   ")
        print()
    
    done = False
    
    for i in range(1, NUM_TURNS+1):
        if done == False:
            guess = input("Please, enter your guess: ")
            done = clue(code, guess)
    if done == False:
        print("Sorry, you've run out of turns.  The code was", code)
        print("     GAME OVER")

main()