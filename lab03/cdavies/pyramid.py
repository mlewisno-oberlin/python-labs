# pyramid.py
# Makes a pyramid
# 
# Connor Davies
# 1/10/13

from picture import Picture

def main():
    width = eval(input("Please enter the desired width for the canvas: "))
    n = eval(input("Please enter the desired number of blocks for bottom row of the pyramid: "))
    size=width/n
    canvas = Picture((width, width))
    canvas.setPenColor(255,0,0)
    for i in range(0,n): #loop through the rows of the pyramid
        for j in range(i,n): #loop through the bricks
            canvas.drawRectFill(i*size/2+(j-i)*size,width-size*(i+1),size-2,size-1) #draw each rectangle, stopping a pixil short to leave visible lines between each block
    canvas.display() #display the pyramid
    input("Press enter to end the program.") #leave an input so the program doesnt end before we can see the picture
    
main()