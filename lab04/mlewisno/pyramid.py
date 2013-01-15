# pyramid.py
# January 12th 2013
#
# Mischa Lewis-Norelle
from picture import Picture

def main():
    # Get the width for the canvas
    width = int(eval(input("How wide do you want the canvas to be? (In pixels) ")))
    # Get the number of bricks tall the user wants the pyramid to be
    numBricks = int(eval(input("How many bricks tall do you want your pyramid to be? ")))
    # Create the canvas
    canvas = Picture((width, width))
    # Fill in the background
    canvas.drawRectFill(0, 0, width, width)
    # Calculate brick height and width
    brickHeight = int(width/numBricks)
    brickWidght = int(width/numBricks)
    # Loop through each row of the pyramid
    for i in range(0, numBricks):
        # Find the y coordinate for every brick in this row
        brickY = brickHeight*(i + 1)
        # Loop through each brick in each row
        for j in range(int(1/2*brickHeight), numBricks - i):
            # Find the x coordinate for each brick as you go along
            brickX = brickHeight(j)
            canvas.setPenColor(0, 0, 0)
            canvas.drawRect(brickX, brickY, brickWidth, brickHeight)
            
    canvas.display()

main()