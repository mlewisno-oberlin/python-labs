# imageedit.py
# January 18th 2013
#
# Mischa Lewis-Norelle

from picture import Picture
# The main method will ask the user to enter a file name as well as handle the menu.
def main():
    picName = input("Hello User, please enter the name of the bitmap you would like edited: ")
    try:
        canvas = Picture(picName)
        done = False
        while not done:
            printMenu()
            choice = eval(input("Which effect would you like applied first? "))
            if(choice == 1):
                remRed()
            elif(choice == 2):
                remRed()
            elif(choice == 3):
                remRed()
            elif(choice == 4):
                remRed()
            elif(choice == 5):
                remRed()
            elif(choice == 6):
                remRed()
            elif(choice == 7):
                remRed()
            elif(choice == 8):
                remRed()
            elif(choice == 9):
                remRed()
            elif(choice == 10):
                remRed()
            elif(choice == 19):
                exit
            
    except:
        print("That was an invalid file name!")
        exit
    

def printMenu():
    print("1. Remove Red")
    print("2. Color Shift Left")
    print("3. Color Shift Right")
    print("4. Negate")
    print("5. Scroll Horizntally")
    print("6. Scroll Vertically")
    print("7. Scroll Both")
    print("8. Make Blurry")
    print("9. Make Grayscale")
    print("10. Incrase Contrast")
    print("11. Posterize")
    print("12. Mirror Horizontally")
    print("13. Mirror Verically")
    print("14. Mirror Both")
    print("15. Comic Book Basic")
    print("16. Comic Book Negative")
    print("17. Crop")
    print("18. Rotate")
    print("19. Exit")
