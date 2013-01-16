# pyramid.py
# Draws a pyramid with a given canvas size and number of bricks (with exceptions)
#
# Henry Lionni Guss
# 1/11/13

from picture import Picture

def main():
    try:
        width = eval(input("Enter a width/height of the canvas (pixels): "))
    except NameError:
        print("Please enter a numeric value.")
        return
    try:
        numBricks = eval(input("Enter a number of bricks for the height of the pyramid: "))
    except NameError:
        print("Please enter a numeric value.")
        return
    canvas = Picture((width, width))
    canvas.setPenColor(0, 255, 255)
    canvas.drawRectFill(0, 0, width, width)
    try:
        sideLength = width // numBricks
    except ZeroDivisionError:
        print("Please select a non-zero height for the pyramid.")
        return
    for i in range(0, numBricks):
        drawRow(canvas, i * (sideLength / 2), width - 1 - sideLength * (i+1), numBricks - i, sideLength)
    canvas.display()

def drawRow(canvas, x, y, n, s):
    for i in range(0, n):
        drawBrick(canvas, x + i * s, y, s)

def drawBrick(canvas, x, y, w):
    canvas.setPenColor(255, 255, 0)
    canvas.drawRectFill(x, y, w, w)
    canvas.setPenColor(0, 0, 0)
    canvas.drawRect(x, y, w, w)

main()
