# imageedit.py
# Edits a user uploaded image
#
# Tyler Robertson
# January 13,2013

from picture import Picture

def main():
    ifile = input("Open a file: ")
    canvas = Picture(ifile)
    canvas.display()
    print("This program performs the following operations:\n\n",
            "1. Flip Horizontally\n",
            "2. Mirror Horizontally\n",
            "3. Scroll Horizontally\n",
            "4. Make Negative\n",
            "5. Make Grayscale\n",
            "6. Cycle Color Channels\n",
            "7. Zoom\n",
            "8. Posterize\n",
            "9. Change Brightness\n",
            "10. Increase Contrast\n",
            "11. Blur\n",
            "12. Rotate 180 Degrees\n",
            "13. Tiled\n",
            "14. Deuteranopia (Red-Green Colorblindess)\n")
    whatdo = eval(input("Enter the number of the operation you'd like to perform: "))
    if whatdo == 1: canvas = flipHoriz(canvas)
    if whatdo == 2: canvas = mirrorHoriz(canvas)
    if whatdo == 3: canvas = scrollHoriz(canvas)
    if whatdo == 4: canvas = neg(canvas)
    if whatdo == 5: canvas = grayscale(canvas)
    if whatdo == 6: canvas = cycleColorChannels(canvas)
    if whatdo == 7: canvas = zoom(canvas)
    if whatdo == 8: canvas = posterize(canvas)
    if whatdo == 9: canvas = changeBright(canvas)
    if whatdo == 10: canvas = changeContrast(canvas)
    if whatdo == 11: canvas = blur(canvas)
    if whatdo == 12: canvas = rotate180(canvas)
    if whatdo == 13: canvas = tiled(canvas)
    if whatdo == 14: canvas = deuteranopia(canvas)
    #try:
    #    n = eval(input("Enter 1 to save: "))
    #    if n == 1 : save(canvas)

    
def flipHoriz(canvas):
    n = Picture((canvas.getWidth(),canvas.getHeight()))
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            n.setPixelColor(canvas.getWidth()-x-1,y,r,g,b)
    canvas.close()
    n.display()
    return n
    
def mirrorHoriz(canvas):
    for x in range(canvas.getWidth()//2):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            canvas.setPixelColor(canvas.getWidth()-x-1,y,r,g,b)
    canvas.display()
    return canvas
   
def scrollHoriz(canvas) :
    m = eval(input("Scroll by how many pixels: "))
    n = Picture((canvas.getWidth(),canvas.getHeight()))
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            n.setPixelColor((x+m)%canvas.getWidth(),y,r,g,b)
    canvas.close()
    n.display()
    return n
    
def neg(canvas) :
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            r, g, b = 255 - r, 255 - g, 255 - b
            canvas.setPixelColor(x,y,r,g,b)
    canvas.display()
    return canvas
    
def grayscale(canvas) :
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            avg = (r+b+g)//3
            canvas.setPixelColor(x,y,avg,avg,avg)
    canvas.display()
    return canvas
    
def cycleColorChannels(canvas) :
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            canvas.setPixelColor(x,y,b,r,g)
    canvas.display()
    return canvas
    
def zoom(canvas) :
    w, h = canvas.getWidth(), canvas.getHeight()
    n = Picture((w,h))
    for x in range(w//4,w-(w//4)):
        for y in range(h//4,h-(h//4)):
            r, g, b = canvas.getPixelColor(x,y)
            c,d = x-(w//4),y-(h//4)
            n.setPixelColor(c*2,d*2,r,g,b)
            n.setPixelColor((c*2)+1,d*2,r,g,b)
            n.setPixelColor(c*2,(d*2)+1,r,g,b)
            n.setPixelColor((c*2)+1,(d*2)+1,r,g,b)
    canvas.close()
    n.display()
    return n
    
def posterize(canvas) :
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            r, g, b = round(r/32)*32, round(g/32)*32, round(b/32)*32
            canvas.setPixelColor(x,y,r,g,b)
    canvas.display()
    return canvas
    
def changeBright(canvas) :
    dBright = eval(input("Enter an integer change to brightness: "))
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            r, g, b = r+dBright, g+dBright, b+dBright
            if r < 0 :
                r = 0
            if g < 0 :
                g = 0
            if b < 0 :
                b = 0
            if r > 255 :
                r = 255
            if g > 255 :
                g = 255
            if b > 255 :
                b = 255
            canvas.setPixelColor(x,y,r,g,b)
    canvas.display()
    return canvas
    
def changeContrast(canvas) :
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            r, g, b = 128 + (2*(r-128)), 128 + (2*(g-128)), 128 + (2*(b-128))
            if r < 0 :
                r = 0
            if g < 0 :
                g = 0
            if b < 0 :
                b = 0
            if r > 255 :
                r = 255
            if g > 255 :
                g = 255
            if b > 255 :
                b = 255
            canvas.setPixelColor(x,y,r,g,b)
    canvas.display()
    return canvas
    
def blur(canvas) :
    w, h = canvas.getWidth(), canvas.getHeight()
    n = Picture((w,h))
    for x in range(w):
        for y in range(h):
            r, g, b = getAdjAvg(canvas,x,y)
            n.setPixelColor(x,y,r,g,b)
    canvas.close()
    n.display()
    return canvas
    
def getAdjAvg(canvas,x,y) :
    w, h = canvas.getWidth(), canvas.getHeight()
    #left side
    if x == 0 and y != 0 and y != h-1:
        r, g, b = 0,0,0
        for i in range(2):
            for j in range(y-1,y+2):
                r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
        r, g, b = r//6,g//6,b//6
        return(r,g,b)
    #right side
    if x == w-1 and y != 0 and y != h-1:
        r, g, b = 0,0,0
        for i in range(w-2,w):
            for j in range(y-1,y+2):
                r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
        r, g, b = r//6,g//6,b//6
        return(r,g,b)
    #top
    if y==0 and x!=0 and x!=w-1:
        r, g, b = 0,0,0
        for i in range(x-1,x+2):
            for j in range(2):
                r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
        r, g, b = r//6,g//6,b//6
        return(r,g,b)
    #bottom
    if y==h-1 and x!=0 and x!=w-1:
        r, g, b = 0,0,0
        for i in range(x-1,x+2):
            for j in range(h-2,h):
                r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
        r, g, b = r//6,g//6,b//6
        return(r,g,b)
    #topleft
    if x==0 and y==0 :
        r, g, b = 0,0,0
        for i in range(2):
            for j in range(2):
                r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
        r, g, b = r//4,g//4,b//4
        return(r,g,b)
    #bottomright
    if x==w-1 and y==h-1 :
        r, g, b = 0,0,0
        for i in range(w-2,w):
            for j in range(h-2,h):
                r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
        r, g, b = r//4,g//4,b//4
        return(r,g,b)
    #topright
    if x==0 and y==h-1 :
        r, g, b = 0,0,0
        for i in range(2):
            for j in range(h-2,h):
                r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
        r, g, b = r//4,g//4,b//4
        return(r,g,b)
    #bottomleft
    if x==w-1 and y==0 :
        r, g, b = 0,0,0
        for i in range(w-2,w):
            for j in range(2):
                r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
        r, g, b = r//4,g//4,b//4
        return(r,g,b)
    #else
    r, g, b = 0,0,0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            r, g, b = r + canvas.getPixelRed(i,j),g + canvas.getPixelGreen(i,j),b + canvas.getPixelBlue(i,j)
    r, g, b = r//9,g//9,b//9
    return(r,g,b)
    
def rotate180(canvas) :
    w, h = canvas.getWidth(), canvas.getHeight()
    n = Picture((w,h))
    for x in range(w):
        for y in range(h):
            r, g, b = canvas.getPixelColor(x,y)
            n.setPixelColor(w-x-1,h-y-1,r,g,b)
    canvas.close()
    n.display()
    return n

def tiled(canvas) :
    w, h = canvas.getWidth(), canvas.getHeight()
    n = Picture((w,h))
    for x in range(0,w,3):
        for y in range(0,h,3):
            r, g, b = canvas.getPixelColor(x,y)
            #first row
            n.setPixelColor(x//3,y//3,r,g,b)
            n.setPixelColor(x//3 + w//3,y//3,r,g,b)
            n.setPixelColor(x//3 + 2*(w//3),y//3,r,g,b)
            #second
            n.setPixelColor(x//3,y//3 + h//3,r,g,b)
            n.setPixelColor(x//3 + w//3,y//3 + h//3,r,g,b)
            n.setPixelColor(x//3 + 2*(w//3),y//3 + h//3,r,g,b)
            #third row
            n.setPixelColor(x//3,y//3 + 2*(h//3),r,g,b)
            n.setPixelColor(x//3 + w//3,y//3 + 2*(h//3),r,g,b)
            n.setPixelColor(x//3 + 2*(w//3),y//3 + 2*(h//3),r,g,b)
    canvas.close()
    n.display()
    return n

def deuteranopia(canvas) :
    for x in range(canvas.getWidth()):
        for y in range(canvas.getHeight()):
            r, g, b = canvas.getPixelColor(x,y)
            cb = (r + g)//2
            canvas.setPixelColor(x,y,cb,cb,b)
    canvas.display()
    return canvas
    
def save(canvas):
    name = input("Save as: ")
    canvas.writeFile(name)

main()
    
