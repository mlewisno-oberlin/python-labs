# RecPic.py
# Creates fractal images recursively.
# 
# Connor Davies
# 1/23/13

from picture import Picture

def main():
    canvas = Picture((512,512))
    w = canvas.getWidth()
    h = canvas.getHeight()
    canvas.setPenColor(0,255,0)
    print("Welcome to the fractal image generator.")
    print()
    print("We have 4 fractals for you to choose from:")
    print("1. Bubble")
    print("2. Carpet")
    print("3. Gasket")
    print("4. Snowflake")
    print()
    k = eval(input("Please enter the number corresponding to the image you would like to see: "))
    n = eval(input("How many times would you like it to recurse? "))
    if k==1:
        bubble(0, 0, w, h, n, 0, canvas).display()
    if k==2:
        carpet(0, 0, w, h, n, canvas).display()
    if k==3:
        canvas.fillPoly((0,w//2,w-1),(h-1, 0, h-1))
        canvas.setPenColor(0,0,0)
        gasket(0, 0, w, h, n, canvas).display()
    if k==4:
        #make a canvas with width and height being a power of 3.
        canvas = Picture((468,468))
        canvas.setPenColor(0,255,0)
        w = canvas.getWidth()
        h = canvas.getHeight()
        canvas.setPosition(w//6,4*h//6)
        canvas = snowflake(n, 3*w//4, canvas)
        canvas.rotate(240)
        canvas = snowflake(n, 3*w//4, canvas)
        canvas.rotate(240)
        canvas = snowflake(n, 3*w//4, canvas)
        canvas.rotate(240)
        canvas.display()
        
    input("Press enter to end the program.")
    
##
#Creates a fractal of circles expanding outward
#@param x The x coordinate of the top left of the recursion's canvas
#@param y The y coordinate of the top left of the recursion's canvas
#@param w The width of the current recursion's canvas
#@param h The height of the current recursion's canvas
#@param n the number of recursions remaining
#@param c The position of the recursion relative to it's parent.
#@param canvas The picture being drawn.
def bubble(x, y, w, h, n, c, canvas):
    if n<1:
        return canvas
    else:
        canvas.drawCircleFill(x+(w//2), y+(h//2), w//2)
        if c!= 4: canvas = bubble(x, y, w//2, h//2, n-1, 1, canvas)
        if c!= 3: canvas = bubble(x+(w//2), y, w//2, h//2, n-1, 2, canvas)
        if c!= 2: canvas = bubble(x, y+(h//2), w//2, h//2, n-1, 3, canvas)
        if c!= 1: canvas = bubble(x+(w//2), y+(h//2), w//2, h//2, n-1, 4, canvas)
        return canvas
    
##
#Creates a fractal of circles expanding outward
#@param x The x coordinate of the top left of the recursion's canvas
#@param y The y coordinate of the top left of the recursion's canvas
#@param w The width of the current recursion's canvas
#@param h The height of the current recursion's canvas
#@param n the number of recursions remaining
#@param canvas The picture being drawn.
def carpet(x, y, w, h, n, canvas):
    if n<1:
        return canvas
    else:
        canvas.drawRectFill(x+w//3, y+h//3, w//3, h//3)
        canvas = carpet(x, y, w//3, h//3, n-1, canvas)
        canvas = carpet(x+(w//3), y, w//3, h//3, n-1, canvas)
        canvas = carpet(x+2*(w//3), y, w//3, h//3, n-1, canvas)
        canvas = carpet(x, y+(h//3), w//3, h//3, n-1, canvas)
        canvas = carpet(x+2*(w//3), y+(h//3), w//3, h//3, n-1, canvas)
        canvas = carpet(x, y+2*(h//3), w//3, h//3, n-1, canvas)
        canvas = carpet(x+(w//3), y+2*(h//3), w//3, h//3, n-1, canvas)
        canvas = carpet(x+2*(w//3), y+2*(h//3), w//3, h//3, n-1, canvas)
        return canvas
    
##
#Creates a fractal of circles expanding outward
#@param x The x coordinate of the top left of the recursion's canvas
#@param y The y coordinate of the top left of the recursion's canvas
#@param w The width of the current recursion's canvas
#@param h The height of the current recursion's canvas
#@param n the number of recursions remaining
#@param canvas The picture being drawn.
def gasket(x, y, w, h, n, canvas):
    if n<1:
        return canvas
    else:
        canvas.fillPoly((x+(w//4), x+3*(w//4), x+(w//2)),(y+(h//2), y+(h//2), y+h))
        canvas = gasket(x+(w//4), y, w//2, h//2, n-1, canvas)
        canvas = gasket(x, y+(h//2), w//2, h//2, n-1, canvas)
        canvas = gasket(x+(w//2), y+(h//2), w//2, h//2, n-1, canvas)
        return canvas
    
##
#Creates a fractal of circles expanding outward
#@param l the length of thie recursions piece of the snowflake
#@param n the number of recursions remaining
#@param canvas The picture being drawn.
def snowflake(n, l, canvas):
    if n<2:
        if l>1 : canvas.drawForward(l)
        else: canvas.drawForward(1)
        return canvas
    else:
        canvas = snowflake(n-1, l//3, canvas)
        canvas.rotate(60)
        canvas = snowflake(n-1, l//3, canvas)
        canvas.rotate(-120)
        canvas = snowflake(n-1, l//3, canvas)
        canvas.rotate(60)
        canvas = snowflake(n-1, l//3, canvas)
        return canvas
    
    
main()