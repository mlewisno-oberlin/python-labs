# Samantha Mater
# 8 January 2013
#
# pyramid.py

from picture import Picture

def drawPyramid(canvas, n, RowX, RowY, width, height):
    for r in range(1, n+1):
        for c in range(1, n-r+2):
            canvas.setPenColor(255, 255, 00);
            canvas.drawRectFill(RowX, RowY, width/n, height/n)
            canvas.setPenColor(0,0,0)
            canvas.drawRect(RowX, RowY, width/n, height/n)
            RowX = RowX + (width/n)
        RowX = ((width/n)*(.5*r))
        RowY = height - ((height/n)*(r+1))
    

def main():
    width = eval(input("Enter a width for your canvas:  "))
    height = eval(input("Enter a height for your canvas:  "))
    n = eval(input("How many bricks tall would you like to make this pyramid?  "))
    
    canvas = Picture((width, height))
    x = 0
    y = height - (height/n)
    canvas.setPenColor(0,225,225)
    canvas.drawRectFill(0,0,width,height)

    drawPyramid(canvas, n, x, y, width, height)
    
    canvas.display()
   
main()
