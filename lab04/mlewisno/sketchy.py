# sketchy.py
# January 15th 2013
#
# Mischa Lewis-Norelle

## Methods to use:
# setPenWidth
# setPenColor
# setPosition
# setDirection
# drawCircle
# drawCircleFill
# drawRect
# drawRectFill
# drawForward

# This program will make modern and post-modern art and save both of them

import random
from picture import Picture
WIDTH = 800
HEIGHT = 600

def main():
    # Create the canvas and fill in the background
    canvas = Picture((WIDTH, HEIGHT))
    chooseColor(canvas)
    canvas.drawRectFill(0, 0, WIDTH, HEIGHT)
    # Create 13 objects on the canvas
    for i in range(0, 13):
        chooseColor(canvas)
        chooseShape(canvas)
        
    canvas.display()
    canvas.writeFile("mlewisno.bmp")

# Chooses which of the shapes or shape combinations to draw
def chooseShape(canvas):
    x = random.randrange(7)
    if(x == 0):
        drawLine(canvas)
    if(x == 1):
        drawCircleOutline(canvas)
    if(x == 2):
        drawCircleFill(canvas)
    if(x == 3):
        drawCircle(canvas)
    if(x == 4):
        drawRectOutline(canvas)
    if(x == 5):
        drawRectFill(canvas)
    if(x == 6):
        drawRect(canvas)

# These methods draw each of the 7 possible shapes necessary

# Draws a line using a random set of starting and stopping coordinates   
def drawLine(canvas):
    chooseThickness(canvas)
    startX = randCoord(WIDTH)
    startY = randCoord(HEIGHT)
    endX = randCoord(WIDTH)
    endY = randCoord(HEIGHT)
    canvas.drawLine(startX, startY, endX, endY)
    
# Draws the outline of a circle with a random radius and coordinates
def drawCircleFill(canvas):
    chooseThickness(canvas)
    centerX = randCoord(WIDTH)
    centerY = randCoord(HEIGHT)
    radius = randRadius()
    canvas.drawCircle(centerX, centerY, radius)

# Draws a circle with a random radius and coordinates
def drawCircleOutline(canvas):
    chooseThickness(canvas)
    centerX = randCoord(WIDTH)
    centerY = randCoord(HEIGHT)
    radius = randRadius()
    canvas.drawCircleFill(centerX, centerY, radius)
    
# Draws the outline of a circle with a random radius and coordinates and fills it
def drawCircle(canvas):
    chooseThickness(canvas)
    centerX = randCoord(WIDTH)
    centerY = randCoord(HEIGHT)
    radius = randRadius()
    canvas.drawCircle(centerX, centerY, radius)
    chooseColor(canvas)
    chooseThickness(canvas)
    canvas.drawCircleFill(centerX, centerY, radius)
    
# Draws a rectangle
def drawRectFill(canvas):
    chooseThickness(canvas)
    startX = randCoord(WIDTH)
    startY = randCoord(HEIGHT)
    width = randCoord(WIDTH - startX)
    height = randCoord(HEIGHT - startY)
    canvas.drawRectFill
    
# Draws a rectangle's outline without filling it in
def drawRectOutline(canvas):
    chooseThickness(canvas)
    startX = randCoord(WIDTH)
    startY = randCoord(HEIGHT)
    width = randCoord(WIDTH - startX)
    height = randCoord(HEIGHT - startY)
    canvas.drawRect
    
# Draws a rectangle with an outline and then fills it in with another color
def drawRect(canvas):
    chooseThickness(canvas)
    startX = randCoord(WIDTH)
    startY = randCoord(HEIGHT)
    width = randCoord(WIDTH - startX)
    height = randCoord(HEIGHT - startY)
    canvas.drawRectFill
    chooseThickness(canvas)
    chooseColor(canvas)
    canvas.drawRectFill

# These are all helper methods, usually to get random colors and coordinates and the like

# Chooses a random red, green and blue value and sets the pen's colors to those values
def chooseColor(canvas):
    randRed = random.randrange(256)
    randGreen = random.randrange(256)
    randBlue = random.randrange(256)
    canvas.setPenColor(randRed, randGreen, randBlue)
   
# Picks and sets the pen to a random pen width    
def chooseThickness(canvas):
    randThick = random.randrange(15, 45)
    canvas.setPenWidth(randThick)
    
# Pick a random coordinate in the range    
def randCoord(x):
    return random.randrange(x)

# Pick a random radius
def randRadius():
    return random.randrange(int(HEIGHT/3))

    


main()