# imageedit.py
# modifies an image 14 different ways
#
# Henry Lionni Guss
# 1/14/12

from picture import Picture
import random

# Receives input picture file and begins the editing process.
def main():
    name = input("Enter the filename of an image you would like to edit: ")
    pic = Picture(name)
    pic.display()
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    instructions()
    while True:
        options()
        userInput = input("Enter the number corresponding to the change you want to perform: ")
        if userInput == "exit":
            return
        else:
            userInput = eval(userInput)
            pic = doEdit(userInput, pic)
            pic.display()

# This function prints the instructions for the program.
def instructions():
    print("This program can be used to edit an image that is in the same directory.",
        "Before each change, you will be prompted to enter a number.",
        "This number corresponds to a certain change that can be executed.",
        "The changes made to the picture will be cumulitive.  Let's begin.", end = '\n\n')

# This function prints the editing options for the program.
def options():
    print("1. Flip", "2. Mirror", "3. Scroll", "4. Negative", "5. Grayscale",
        "6. Cycle Colors", "7. Zoom", "8. Posterize", "9. Brightness",
        "10. Contrast", "11. Blur", "12. Rotate", "13. Squish", "14. Experiment",
        "You can exit by typing \"exit\"", sep = '\n')
    
# This function takes user input and calls upon the appropriate function.
def doEdit(number, pic):
    if number == 1:
        pic2 = flip(pic)
    elif number == 2:
        pic2 = mirror(pic)
    elif number == 3:
        pic2 = scroll(pic)
    elif number == 4:
        pic2 = negative(pic)
    elif number == 5:
        pic2 = grayscale(pic)
    elif number == 6:
        pic2 = cycleColors(pic)
    elif number == 7:
        pic2 = zoom(pic)
    elif number == 8:
        pic2 = posterize(pic)
    elif number == 9:
        pic2 = brightness(pic)
    elif number == 10:
        pic2 = contrast(pic)
    elif number == 11:
        pic2 = blur(pic)
    elif number == 12:
        pic2 = rotate(pic)
    elif number == 13:
        pic2 = shuffle(pic)
    elif number == 14:
        pic2 = someOtherThing(pic)
    return pic2
    
# This function flips the image horizontally.
def flip(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    pic2 = copyImage(pic)
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic2.getPixelRed(WIDTH - 1 - x, y)
            green = pic2.getPixelGreen(WIDTH - 1 - x, y)
            blue = pic2.getPixelBlue(WIDTH - 1 - x, y)
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function mirrors the left side of the image onto the right side.
def mirror(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    pic2 = copyImage(pic)
    for y in range(0, HEIGHT):
        for x in range(WIDTH // 2, WIDTH):
            red = pic2.getPixelRed(WIDTH - x - 1, y)
            green = pic2.getPixelGreen(WIDTH - x - 1, y)
            blue = pic2.getPixelBlue(WIDTH - x - 1, y)
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function scrolls all pixels to the right.
def scroll(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    pixels = eval(input("Enter a number of pixels by which you picture should be shifted to the right: "))
    if pixels > 0:
        pixels = WIDTH - pixels
    pic2 = copyImage(pic)
    for y in range(0, HEIGHT):
        for x in range(0, pixels):
            red = pic2.getPixelRed(x + WIDTH - pixels, y)
            green = pic2.getPixelGreen(x + WIDTH - pixels, y)
            blue = pic2.getPixelBlue(x + WIDTH - pixels, y)
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    for y in range(0, HEIGHT):
        for x in range(pixels, WIDTH):
            red = pic2.getPixelRed(x - pixels, y)
            green = pic2.getPixelGreen(x - pixels, y)
            blue = pic2.getPixelBlue(x - pixels, y)
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function creates a negative of the image by subtracting color values from 255.
def negative(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = 255 - pic.getPixelRed(x, y)
            green = 255 - pic.getPixelGreen(x, y)
            blue = 255 - pic.getPixelBlue(x, y)
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function averages color channels to create a grayscale image.
def grayscale(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic.getPixelRed(x, y)
            green = pic.getPixelGreen(x, y)
            blue = pic.getPixelBlue(x, y)
            new = (red + green + blue) // 3
            pic.setPixelRed(x, y, new)
            pic.setPixelGreen(x, y, new)
            pic.setPixelBlue(x, y, new)
    return pic
    
# This function switches the red, green and blue values.  Doing it 3 times restores original.
def cycleColors(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic.getPixelRed(x, y)
            green = pic.getPixelGreen(x, y)
            blue = pic.getPixelBlue(x, y)
            pic.setPixelRed(x, y, blue)
            pic.setPixelGreen(x, y, red)
            pic.setPixelBlue(x, y, green)
    return pic
    
# This function zooms into the middle portion of size width / 2 by height / 2.
def zoom(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    pic2 = copyImage(pic)
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic2.getPixelRed((x + WIDTH // 2) // 2, (y + HEIGHT // 2) // 2)
            green = pic2.getPixelGreen((x + WIDTH // 2) // 2, (y + HEIGHT // 2) // 2)
            blue = pic2.getPixelBlue((x + WIDTH // 2) // 2, (y + HEIGHT // 2) // 2)
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function reduces the possible color values in the image.
def posterize(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic.getPixelRed(x, y) // 32 * 32
            green = pic.getPixelGreen(x, y) // 32 * 32
            blue = pic.getPixelBlue(x, y) // 32 * 32
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function increases brightness by a user specified value (negative decreases).
def brightness(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    change = eval(input("Enter a value to increase the brightness by (negative == decrease): "))
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic.getPixelRed(x, y) + change
            if red > 255:
                red = 255
            elif red < 0:
                red = 0
            green = pic.getPixelGreen(x, y) + change
            if green > 255:
                green = 255
            elif green < 0:
                green = 0
            blue = pic.getPixelBlue(x, y) + change
            if blue > 255:
                blue = 255
            elif blue < 0:
                blue = 0
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic

# This function increases contrast by a user specified value.
def contrast(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    change = eval(input("Enter a value to increase the contrast by: "))
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic.getPixelRed(x, y) * 2 - 128
            green = pic.getPixelGreen(x, y) * 2 - 128
            blue = pic.getPixelBlue(x, y) * 2 - 128
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function averages picture colors with those of nearby pixels.
def blur(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    pic2 = copyImage(pic)
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            total = 1
            red = pic2.getPixelRed(x, y)
            green = pic2.getPixelRed(x,y)
            blue = pic2.getPixelBlue(x, y)
            if x >= 1 and y >= 1:
                red = red + pic2.getPixelRed(x - 1, y - 1)
                green = green + pic2.getPixelGreen(x - 1, y - 1)
                blue = blue + pic2.getPixelBlue(x - 1, y - 1)
                total = total + 1
            if x >= 1:
                red = red + pic2.getPixelRed(x - 1, y)
                green = green + pic2.getPixelGreen(x - 1, y)
                blue = blue + pic2.getPixelBlue(x - 1, y)
                total = total + 1
            if y >= 1:
                red = red + pic2.getPixelRed(x, y - 1)
                green = green + pic2.getPixelGreen(x, y - 1)
                blue = blue + pic2.getPixelBlue(x, y - 1)
                total = total + 1
            if x <= WIDTH - 2 and y <= HEIGHT - 2:
                red = red + pic2.getPixelRed(x + 1, y + 1)
                green = green + pic2.getPixelGreen(x + 1, y + 1)
                blue = blue + pic2.getPixelBlue(x + 1, y + 1)
                total = total + 1
            if x <= WIDTH - 2:
                red = red + pic2.getPixelRed(x + 1, y)
                green = green + pic2.getPixelGreen(x + 1, y)
                blue = blue + pic2.getPixelBlue(x + 1, y)
                total = total + 1
            if y <= HEIGHT - 2:
                red = red + pic2.getPixelRed(x, y + 1)
                green = green + pic2.getPixelGreen(x, y + 1)
                blue = blue + pic2.getPixelBlue(x, y + 1)
                total = total + 1
            if x >= 1 and y <= HEIGHT - 2:
                red = red + pic2.getPixelRed(x - 1, y + 1)
                green = green + pic2.getPixelGreen(x - 1, y + 1)
                blue = blue + pic2.getPixelBlue(x - 1, y + 1)
                total = total + 1
            if x <= WIDTH - 2 and y >= 1:
                red = red + pic2.getPixelRed(x + 1, y - 1)
                green = green + pic2.getPixelGreen(x + 1, y - 1)
                blue = blue + pic2.getPixelBlue(x + 1, y - 1)
                total = total + 1
            red = red // total
            green = green // total
            blue = blue // total
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function rotates the image by 180 degrees.
def rotate(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    pic2 = copyImage(pic)
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic2.getPixelRed(WIDTH - 1 - x, HEIGHT - 1 - y)
            green = pic2.getPixelGreen(WIDTH - 1 - x, HEIGHT - 1 - y)
            blue = pic2.getPixelBlue(WIDTH - 1 - x, HEIGHT - 1 - y)
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic
    
# This function shuffles boxes of user specified size.
def shuffle(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    printFactors(WIDTH, pic)
    width = eval(input("Enter one of the above numbers as the box width: "))
    pic2 = copyImage(pic)
    y2 = 0
    x2 = 0
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic2.getPixelRed(x2, y2)
            green = pic2.getPixelGreen(x2, y2)
            blue = pic2.getPixelBlue(x2, y2)
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
            if x > 0:
                if WIDTH % x == width:
                    y2 = y2 + 1
                    if y2 == HEIGHT:
                        y2 = 0
            x2 = x2 + 1
            if x2 == WIDTH:
                x2 = 0
        x2 = 0
    return pic

# This function does something
def someOtherThing(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    pic2 = copyImage(pic)
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic2.getPixelRed(random.randrange(WIDTH), y)
            green = pic2.getPixelGreen(x, y)
            blue = pic2.getPixelBlue(x, random.randrange(HEIGHT))
            pic.setPixelRed(x, y, red)
            pic.setPixelGreen(x, y, green)
            pic.setPixelBlue(x, y, blue)
    return pic

def copyImage(pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    pic2 = Picture((WIDTH, HEIGHT))
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic.getPixelRed(x, y)
            green = pic.getPixelGreen(x, y)
            blue = pic.getPixelBlue(x, y)
            pic2.setPixelRed(x, y, red)
            pic2.setPixelGreen(x, y, green)
            pic2.setPixelBlue(x, y, blue)
    return pic2

def printFactors(int, pic):
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    for i in range(1, WIDTH + 1):
        if WIDTH % i == 0:
            print(i)

main()