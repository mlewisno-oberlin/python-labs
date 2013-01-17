# master.py
# January 13th 2013
#
# Mischa Lewis-Norelle
import random
    
def main():
    print("Hello, and welcome to the fantastic game of Mastermind!")
    print("I have a four letter code, made from 6 colors.")
    print("The colors are R, G, B, Y, P, or O.")
    code = generateCode()
    answered = False
    numTurns = 0
    # Prompt the user to enter a guess until either they have guessed correctly or they have
    # run out of turns
    while(numTurns < 10):
        
        if(answered):
            break
        guess = input("Please enter your guess: ")
        guess = guess.upper()
        guessCopy = guess
        codeCopy = code
        numWhite = 0
        numBlack = 0
        if(guess == "CHEAT"):
            print(code)
        
        # Calculate white pegs
        for i in range(0, 4):
            if(guessCopy[i] == codeCopy[i]):
                numWhite += 1
                codeCopy = codeCopy[0:i] + "x" + codeCopy[i+1:len(codeCopy)]
        
        # Calculate black pegs
        for j in range(0, 4):
            tempChar = guessCopy[j]
            for i in range(0, 4):
                if(codeCopy[i] == tempChar):
                    numBlack += 1
                    codeCopy = codeCopy[0:i] + "y" + codeCopy[i+1:len(codeCopy)]
        
        numTurns += 1
        if(numWhite == 4):
            answered = True
            print("Congratulations! You won!")
            break
        print("You have", numBlack, "black pegs,", numWhite, "white pegs, and", (10-numTurns), "turns left.")
    
    if(numWhite < 4):
        print("YOU FAILED!!! AHAHAHAHAHAHAHAHA, the code was", code, "!!!!!")
# Generate a 4 letter code for the Mastermind game. Returns the code as a string.
def generateCode() :
    code = ""
    for i in range(1, 5):
        randomNum = random.randrange(6)
        code = code + linkedChar(randomNum)
    
    return code

# Takes in an integer between 0 and 6 and returns the resultant character
def linkedChar(x):
    if(x == 0):
        return "R"
    if(x == 1):
        return "G"
    if(x == 2):
        return "B"
    if(x == 3):
        return "Y"
    if(x == 4):
        return "P"

    return "O"


main()
