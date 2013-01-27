# recPic.py
#
#
# Tyler Robertson
# 1/25/13

from picture import Picture

def main() :
    print("1. Bubbles\n2. Carpet\n3. Gasket\n4. Snowflake\n\n")
    choice = eval(input("Input the number of the pattern you would like:"))
    size = eval(input("Please enter a size: "))
    depth = eval(input("Please enter a depth: "))
    if choice == 1 : #Draw Bubbles
        canvas = Picture((size*4,size*4))
        canvas.setPenColor(255,102,0)
        canvas.drawRectFill(0,0,size*4,size*4)
        canvas.setPenColor(0,0,255)
        canvas = bubbles(canvas,0,0,size*4,depth)
        canvas.display()
    if choice == 2 : #Draw Carpet
        canvas = Picture((size*3,size*3))
        canvas.setPenColor(0,255,0)
        canvas.drawRectFill(0,0,size*3,size*3)
        canvas.setPenColor(255,0,0)
        canvas = carpet(canvas,0,0,size*3,depth)
        canvas.display()
    if choice == 3 : #Draw Gasket
        canvas = Picture((size,size))
        canvas.setPenColor(0,255,255)
        canvas.drawRectFill(0,0,size,size)
        canvas.setPenColor(0,0,255)
        canvas.fillPoly([0,size//2,size],[size,0,size])
        canvas.setPenColor(0,255,255)
        canvas = gasket(canvas,0,0,size,depth)
        canvas.display()
    if choice == 4 : #Draw Snowflake
        canvas = Picture((size + (size//2),size + (size//2)))
        canvas.setPenColor(80,0,80)
        canvas.drawRectFill(0,0,size + (size//2),size + (size//2))
        canvas.setPenColor(0,255,0)
        canvas.setPosition(size + (size//4),size)
        canvas.rotate(240)
        canvas = snowflake(canvas,size,depth)
        canvas.rotate(240)
        canvas = snowflake(canvas,size,depth)
        canvas.rotate(240)
        canvas = snowflake(canvas,size,depth)
        canvas.display()
    
    
# draws fractal circles everywhere!!!1!!one!!
def bubbles(canvas,x,y,r,depth) :
    if depth == 0 :
        return canvas
    else:
        canvas.drawCircleFill(x + (r//2),y+(r//2),r//2)
        canvas = bubbles(canvas,x,y,r//2,depth-1) #NW
        canvas = bubbles(canvas,x+(r//2),y,r//2,depth-1) #NE
        canvas = bubbles(canvas,x,y+(r//2),r//2,depth-1) #SW
        canvas = bubbles(canvas,x+(r//2),y+(r//2),r//2,depth-1) #SE
        return canvas
    
# draws squares liek all over the place :O    
def carpet(canvas,x,y,r,depth) :
    if depth == 0:
        return canvas
    else:
        canvas.drawRectFill(x+r//3,y+r//3,r//3,r//3)
        canvas = carpet(canvas,x,y,r//3,depth-1) #NW
        canvas = carpet(canvas,x+(r//3),y,r//3,depth-1) #N
        canvas = carpet(canvas,x+2*(r//3),y,r//3,depth-1) #NE
        canvas = carpet(canvas,x,y+(r//3),r//3,depth-1) #W
        canvas = carpet(canvas,x+2*(r//3),y+(r//3),r//3,depth-1) #E
        canvas = carpet(canvas,x,y+2*(r//3),r//3,depth-1) #SW
        canvas = carpet(canvas,x+(r//3),y+2*(r//3),r//3,depth-1) #S
        canvas = carpet(canvas,x+2*(r//3),y+2*(r//3),r//3,depth-1) #SE
        return canvas
    
# draws Triangles recursively placed within each other
def gasket(canvas,x,y,r,depth) :
    if depth == 1:
        return canvas
    else:
        canvas.fillPoly([x+(r//4),x + (r//2 + r//4),x+(r//2)],[y + (r//2),y + (r//2),y+r])
        canvas = gasket(canvas,x + (r//4),y,r//2,depth-1) #N
        canvas = gasket(canvas,x,y + (r//2),r//2,depth-1) #SW
        canvas = gasket(canvas,x + (r//2),y + (r//2),r//2,depth-1) #SE
        return canvas

# draws a pretty snowflake, show your girlfriend!
def snowflake(canvas,r,depth) :
    if depth == 1 :
        canvas.drawForward(r)
        return canvas
    else:
        canvas = snowflake(canvas,r//3,depth-1)
        canvas.rotate(60)
        canvas = snowflake(canvas,r//3,depth-1)
        canvas.rotate(-120)
        canvas = snowflake(canvas,r//3,depth-1)
        canvas.rotate(60)
        canvas = snowflake(canvas,r//3,depth-1)
        return canvas

main()
