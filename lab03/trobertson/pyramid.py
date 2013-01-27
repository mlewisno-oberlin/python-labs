# pyramid.py
# Draws a pyramid of bricks on a canvas of a user provided size
#
# Tyler Robertson
# January 11, 2013

from picture import Picture

def main() :
    # Gather user input
    width = eval(input("Please enter a width: "))
    n = eval(input("How many bricks tall will your pyramid be: "))
    # Set up the canvas
    canvas = Picture((width, width))
    canvas.setPenColor(0,255,255)
    canvas.drawRectFill(0,0,width,width)
    s = width//n
    # Place each brick in its proper location
    for i in range(0,n):
        x = (s//2)*i
        y = width - (i+1)*s
        for j in range(0,n-i):
            canvas = drawBrick(canvas,s,x,y)
            x += s
    # Display the canvas
    canvas.display()

# Draws an individual brick in the given location
def drawBrick(canvas,s,x,y) :
    canvas.setPenColor(0,0,0)
    canvas.drawRect(x,y,s,s)
    canvas.setPenColor(255,255,0)
    canvas.drawRectFill(x+1,y+1,s-2,s-2)
    return canvas

main()
