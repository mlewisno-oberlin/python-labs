# pyramid.py
# January 12th 2013
#
# Mischa Lewis-Norelle
from picture import Picture

def main():
    # Get the width for the canvas
    width = int(eval(input("How wide do you want the canvas to be? (In pixels) ")))
    height = width
    # Get the number of bricks tall the user wants the pyramid to be
    try:
        numBricks = int(eval(input("How many bricks tall do you want your pyramid to be? ")))
    except:
        print("That was a non-numeric value. You are the worst ever. Exciting.")
    # Create the canvas
    canvas = Picture((width, width))
    # Fill in the background
    canvas.setPenColor(255, 255, 255)
    canvas.drawRectFill(0, 0, width, width)
    # Calculate brick height and width
    try:
        brickHeight = int(width/numBricks)
        brickWidth = int(width/numBricks)
    except:
        print("You put in 0 bricks, so you will only get a background. AHAHAHAHAHAAHAHAHAHAHAHAHA. AHAHA. AHA. HA.")
    # Loop through each row of the pyramid
    
    rowX = 0
    rowY = 0
    
    for i in range(0, numBricks):
        # Find the y coordinate for every brick in this row
        brickY = brickHeight*(i + 1)
        # Loop through each brick in each row
        for j in range(0, numBricks - i):
            # Find the x coordinate for each brick as you go along
            canvas.setPenColor(0, 255, 255)
            canvas.drawRectFill(rowX + j*brickWidth, height - brickHeight - rowY, brickWidth, brickHeight)
            canvas.setPenColor(0, 0, 0)
            canvas.drawRect(rowX + j*brickWidth, height - brickHeight - rowY, brickWidth, brickHeight)
            
        rowX += int(brickWidth/2)
        rowY += brickHeight
    canvas.writeFile("pyramid.bmp")
    canvas.display()

main()