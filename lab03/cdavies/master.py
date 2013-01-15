# master.py
# Simulates the game Mastermind against the Computer
# 
# Connor Davies
# 1/10/13

import random

def main():
    NUM_TURNS=10
    print("I have a 4 letter code, made from 6 colors.  The colors are R, G, B, Y, P, or O.")
    #for i in range(0,NUM_TURNS):
    code=generateCode()
    win = False
    for i in range(0,NUM_TURNS):
        guess = input("Enter Guess:")
        if clue(code, guess):
            win = True
            break
        print("Turns remaining:", NUM_TURNS-i-1)
    if win:
        print("You Win!")
    else: print("You have failed puny human.  Feel free to try again.")
    
    

def clue(code, guess):
    black=0
    white=0
    for i in range(0,4):
        if code[i]==guess[i]:
            black = black+1
            code = code[0:i] + "x" + code[i+1:int(len(code))]
            guess = guess[0:i] + "y" + guess[i+1:len(guess)]
    
    for i in range(0,4):
        for j in range(0,4):
            if code[j]==guess[i]:
                white=white+1
                break
    if black==4: return True
    print("Incorrect.  Black Pegs:", black, "White Pegs:", white)
    return False

#generate a random code for the player to guess
def generateCode():
    code=""
    for i in range(0,4):
        rInt = random.randint(0,5)
        if rInt==0: code=code+"R"
        if rInt==1: code=code+"B"
        if rInt==2: code=code+"G"
        if rInt==3: code=code+"Y"
        if rInt==4: code=code+"O"
        if rInt==5: code=code+"P"
    return code

main()