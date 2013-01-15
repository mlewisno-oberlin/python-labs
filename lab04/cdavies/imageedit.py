# imageedit.py
# Edits a picture
# 
# Connor Davies
# 1/12/13

from picture import Picture

def main():
    try:
        print("Welcome to the Image Editor!  Here you can apply many transformations to you pictures!")
        file = input("Please enter the file name of the image you wish to change:")
        canvas = Picture(file)
        canvas.display()
        print("1. Flip Horizontally")
        print("2. Mirror Horizontally")
        print("3. Scroll Horizontally")
        print("4. Make Negative")
        print("5. Make Grayscale")
        print("6. Cycle Color Channels")
        print("7. Zoom")
        print("8. Posterize")
        print("9. Change Brightness")
        print("10. Increase Contrast")
        print("11. Blur")
        print("12. Rotate 180 Degrees")
        print("13. ???")
        print("14. ???")
        n = eval(input("Enter the number corresponding with the effect you want (or enter 0 to end the program):"))
        while n!=0:
            if n==1:
                canvas = flipHorizontally(canvas)
                canvas.display()
            elif n==2:
                canvas = mirrorHorizontally(canvas)
                canvas.display()
            elif n==3:
                canvas = scrollHorizontally(canvas)
                canvas.display()
            elif n==4:
                canvas = makeNegative(canvas)
                canvas.display()
            elif n==5:
                canvas = makeGrayscale(canvas)
                canvas.display()
            elif n==6:
                canvas = cycleColorChannels(canvas)
                canvas.display()
            elif n==7:
                canvas = zoom(canvas)
                canvas.display()
            elif n==8:
                canvas = posterize(canvas)
                canvas.display()
            elif n==9:
                canvas = changeBrightness(canvas)
                canvas.display()
            elif n==10:
                canvas = increaseContrast(canvas)
                canvas.display()
            elif n==11:
                canvas = blur(canvas)
                canvas.display()
            elif n==12:
                canvas = rotate180(canvas)
                canvas.display()
            elif n==13:
                canvas = negativeFlip(canvas)
                canvas.display()
            elif n==14:
                canvas = negativeMirror(canvas)
                canvas.display()
            elif n==0:
                break
            else:
                print("")
                print("Please enter one of the suggested numbers.")
                print("")
            print("")
            print("1. Flip Horizontally")
            print("2. Mirror Horizontally")
            print("3. Scroll Horizontally")
            print("4. Make Negative")
            print("5. Make Grayscale")
            print("6. Cycle Color Channels")
            print("7. Zoom")
            print("8. Posterize")
            print("9. Change Brightness")
            print("10. Increase Contrast")
            print("11. Blur")
            print("12. Rotate 180 Degrees")
            print("13. Mystery 1")
            print("14. Mystery 2")
            n = eval(input("Enter the number corresponding with the effect you want (or enter 0 to end the program):"))
            canvas.close()
    except FileNotFoundError:
        print("Please enter the location of the file correctly.")
    except NameError:
        print("Please enter a valid number next time.")
    except SyntaxError:
        print("Please enter a valid number next time.")
    except:
        print("Sorry, something unexpected has occured.  Please reload the program.")
    
def flipHorizontally(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    new_canvas = Picture((w,h))
    canvas.close()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(w-1-i,j)            
            g = canvas.getPixelGreen(w-1-i,j)
            b = canvas.getPixelBlue(w-1-i,j)
            new_canvas.setPixelColor(i,j,r,g,b)
    for i in range(0,w):
        for j in range(0,h):
            r = new_canvas.getPixelRed(i,j)            
            g = new_canvas.getPixelGreen(i,j)
            b = new_canvas.getPixelBlue(i,j)
            canvas.setPixelColor(i,j,r,g,b)
    return canvas

def mirrorHorizontally(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w//2):
        for j in range(0,h):
            r = canvas.getPixelRed(w-1-i,j)            
            g = canvas.getPixelGreen(w-1-i,j)
            b = canvas.getPixelBlue(w-1-i,j)
            canvas.setPixelColor(i,j,r,g,b)
    return canvas

def scrollHorizontally(canvas):
    n = eval(input("How many pixels would you like to scroll? "))
    w = canvas.getWidth()
    h = canvas.getHeight()
    new_canvas = Picture((w,h))
    canvas.close()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)            
            g = canvas.getPixelGreen(i,j)
            b = canvas.getPixelBlue(i,j)
            new_canvas.setPixelColor((i+n)%w,j,r,g,b)
    return new_canvas

def makeNegative(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)            
            g = canvas.getPixelGreen(i,j)
            b = canvas.getPixelBlue(i,j)
            canvas.setPixelColor(i,j,255-r,255-g,255-b)
    return canvas
    
def makeGrayscale(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)            
            g = canvas.getPixelGreen(i,j)
            b = canvas.getPixelBlue(i,j)
            avg = (r+g+b)//3
            canvas.setPixelColor(i,j,avg,avg,avg)
    return canvas

def cycleColorChannels(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)            
            g = canvas.getPixelGreen(i,j)
            b = canvas.getPixelBlue(i,j)
            canvas.setPixelColor(i,j,g,r,b)
    return canvas
    
def zoom(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    new_canvas = Picture((w,h))
    canvas.close()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(w//4+i//2,h//4+j//2)            
            g = canvas.getPixelGreen(w//4+i//2,h//4+j//2)
            b = canvas.getPixelBlue(w//4+i//2,h//4+j//2)
            new_canvas.setPixelColor(i,j,r,g,b)
    return new_canvas

def posterize(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)            
            g = canvas.getPixelGreen(i,j)
            b = canvas.getPixelBlue(i,j)
            canvas.setPixelColor(i,j,r//32*32,g//32*32,b//32*32)
    return canvas

def changeBrightness(canvas):
    n = eval(input("By how much would you like to change the brightness? "))
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)+n
            g = canvas.getPixelGreen(i,j)+n
            b = canvas.getPixelBlue(i,j)+n
            if r>255: r=255
            if r<0: r=0
            if g>255: g=255
            if g<0: g=0
            if b>255: b=255
            if b<0: b=0
            canvas.setPixelColor(i,j,r,g,b)
    return canvas

def increaseContrast(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)
            g = canvas.getPixelGreen(i,j)
            b = canvas.getPixelBlue(i,j)
            canvas.setPixelColor(i,j,(r-128)*2+r,(g-128)*2+g,(b-128)*2+b)
    return canvas

def blur(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    new_canvas = Picture((w,h))
    canvas.close()
    #dealing with the corners
    r = (canvas.getPixelRed(0,0)+canvas.getPixelRed(1,0)+canvas.getPixelRed(0,1)+canvas.getPixelRed(1,1))//4
    g = (canvas.getPixelGreen(0,0)+canvas.getPixelGreen(1,0)+canvas.getPixelGreen(0,1)+canvas.getPixelGreen(1,1))//4
    b = (canvas.getPixelBlue(0,0)+canvas.getPixelBlue(1,0)+canvas.getPixelBlue(0,1)+canvas.getPixelBlue(1,1))//4
    new_canvas.setPixelColor(0,0,r,g,b)
    
    r = (canvas.getPixelRed(w-1,0)+canvas.getPixelRed(w-2,0)+canvas.getPixelRed(w-1,1)+canvas.getPixelRed(w-2,1))//4
    g = (canvas.getPixelGreen(w-1,0)+canvas.getPixelGreen(w-2,0)+canvas.getPixelGreen(w-1,1)+canvas.getPixelGreen(w-2,1))//4
    b = (canvas.getPixelBlue(w-1,0)+canvas.getPixelBlue(w-2,0)+canvas.getPixelBlue(w-1,1)+canvas.getPixelBlue(w-2,1))//4
    new_canvas.setPixelColor(w-1,0,r,g,b)
    
    r = (canvas.getPixelRed(w-1,h-1)+canvas.getPixelRed(w-2,h-1)+canvas.getPixelRed(w-1,h-2)+canvas.getPixelRed(w-2,h-2))//4
    g = (canvas.getPixelGreen(w-1,h-1)+canvas.getPixelGreen(w-2,h-1)+canvas.getPixelGreen(w-1,h-2)+canvas.getPixelGreen(w-2,h-2))//4
    b = (canvas.getPixelBlue(w-1,h-1)+canvas.getPixelBlue(w-2,h-1)+canvas.getPixelBlue(w-1,h-2)+canvas.getPixelBlue(w-2,h-2))//4
    new_canvas.setPixelColor(w-1,h-1,r,g,b)
    
    r = (canvas.getPixelRed(0,h-1)+canvas.getPixelRed(1,h-1)+canvas.getPixelRed(0,h-2)+canvas.getPixelRed(1,h-2))//4
    g = (canvas.getPixelGreen(0,h-1)+canvas.getPixelGreen(1,h-1)+canvas.getPixelGreen(0,h-2)+canvas.getPixelGreen(1,h-2))//4
    b = (canvas.getPixelBlue(0,h-1)+canvas.getPixelBlue(1,h-1)+canvas.getPixelBlue(0,h-2)+canvas.getPixelBlue(1,h-2))//4
    new_canvas.setPixelColor(0,h-1,r,g,b)
    #top row
    for i in range(1,w-1):
        r = (canvas.getPixelRed(i,0)+canvas.getPixelRed(i-1,0)+canvas.getPixelRed(i+1,0)+canvas.getPixelRed(i,1)+canvas.getPixelRed(i-1,1)+canvas.getPixelRed(i+1,1))//6
        g = (canvas.getPixelGreen(i,0)+canvas.getPixelGreen(i-1,0)+canvas.getPixelGreen(i+1,0)+canvas.getPixelGreen(i,1)+canvas.getPixelGreen(i-1,1)+canvas.getPixelGreen(i+1,1))//6
        b = (canvas.getPixelBlue(i,0)+canvas.getPixelBlue(i-1,0)+canvas.getPixelBlue(i+1,0)+canvas.getPixelBlue(i,1)+canvas.getPixelBlue(i-1,1)+canvas.getPixelBlue(i+1,1))//6
        new_canvas.setPixelColor(i,0,r,g,b)
    #bottom row
    for i in range(1,w-1):
        r = (canvas.getPixelRed(i,h-1)+canvas.getPixelRed(i-1,h-1)+canvas.getPixelRed(i+1,h-1)+canvas.getPixelRed(i,h-2)+canvas.getPixelRed(i-1,h-2)+canvas.getPixelRed(i+1,h-2))//6
        g = (canvas.getPixelGreen(i,h-1)+canvas.getPixelGreen(i-1,h-1)+canvas.getPixelGreen(i+1,h-1)+canvas.getPixelGreen(i,h-2)+canvas.getPixelGreen(i-1,h-2)+canvas.getPixelGreen(i+1,h-2))//6
        b = (canvas.getPixelBlue(i,h-1)+canvas.getPixelBlue(i-1,h-1)+canvas.getPixelBlue(i+1,h-1)+canvas.getPixelBlue(i,h-2)+canvas.getPixelBlue(i-1,h-2)+canvas.getPixelBlue(i+1,h-2))//6
        new_canvas.setPixelColor(i,h-1,r,g,b)
    #left most column
    for i in range(1,h-1):
        r = (canvas.getPixelRed(0,i)+canvas.getPixelRed(0,i-1)+canvas.getPixelRed(0,i+1)+canvas.getPixelRed(1,i)+canvas.getPixelRed(1,i-1)+canvas.getPixelRed(1,i+1))//6
        g = (canvas.getPixelGreen(0,i)+canvas.getPixelGreen(0,i-1)+canvas.getPixelGreen(0,i+1)+canvas.getPixelGreen(1,i)+canvas.getPixelGreen(1,i-1)+canvas.getPixelGreen(1,i+1))//6
        b = (canvas.getPixelBlue(0,i)+canvas.getPixelBlue(0,i-1)+canvas.getPixelBlue(0,i+1)+canvas.getPixelBlue(1,i)+canvas.getPixelBlue(1,i-1)+canvas.getPixelBlue(1,i+1))//6
        new_canvas.setPixelColor(0,i,r,g,b)
    #right most column
    for i in range(1,h-1):
        r = (canvas.getPixelRed(w-1,i)+canvas.getPixelRed(w-1,i-1)+canvas.getPixelRed(w-1,i+1)+canvas.getPixelRed(w-2,i)+canvas.getPixelRed(w-2,i-1)+canvas.getPixelRed(w-2,i+1))//6
        g = (canvas.getPixelGreen(w-1,i)+canvas.getPixelGreen(w-1,i-1)+canvas.getPixelGreen(w-1,i+1)+canvas.getPixelGreen(w-2,i)+canvas.getPixelGreen(w-2,i-1)+canvas.getPixelGreen(w-2,i+1))//6
        b = (canvas.getPixelBlue(w-1,i)+canvas.getPixelBlue(w-1,i-1)+canvas.getPixelBlue(w-1,i+1)+canvas.getPixelBlue(w-2,i)+canvas.getPixelBlue(w-2,i-1)+canvas.getPixelBlue(w-2,i+1))//6
        new_canvas.setPixelColor(w-1,i,r,g,b)
    #The middle (finally)
    for i in range(1,w-1):
        for j in range(1,h-1):
            r = (canvas.getPixelRed(i-1,j-1)+canvas.getPixelRed(i-1,j)+canvas.getPixelRed(i-1,j+1)+canvas.getPixelRed(i,j-1)+canvas.getPixelRed(i,j)+canvas.getPixelRed(i,j+1)+canvas.getPixelRed(i+1,j-1)+canvas.getPixelRed(i+1,j)+canvas.getPixelRed(i+1,j+1))//9
            g = (canvas.getPixelGreen(i-1,j-1)+canvas.getPixelGreen(i-1,j)+canvas.getPixelGreen(i-1,j+1)+canvas.getPixelGreen(i,j-1)+canvas.getPixelGreen(i,j)+canvas.getPixelGreen(i,j+1)+canvas.getPixelGreen(i+1,j-1)+canvas.getPixelGreen(i+1,j)+canvas.getPixelGreen(i+1,j+1))//9
            b = (canvas.getPixelBlue(i-1,j-1)+canvas.getPixelBlue(i-1,j)+canvas.getPixelBlue(i-1,j+1)+canvas.getPixelBlue(i,j-1)+canvas.getPixelBlue(i,j)+canvas.getPixelBlue(i,j+1)+canvas.getPixelBlue(i+1,j-1)+canvas.getPixelBlue(i+1,j)+canvas.getPixelBlue(i+1,j+1))//9
            new_canvas.setPixelColor(i,j,r,g,b)
    return new_canvas

def rotate180(canvas):
    w = canvas.getWidth()
    h = canvas.getHeight()
    new_canvas = Picture((w,h))
    canvas.close()
    for i in range(0,w):
        for j in range(0,h):
            r = canvas.getPixelRed(w-1-i,h-1-j)            
            g = canvas.getPixelGreen(w-1-i,h-1-j)
            b = canvas.getPixelBlue(w-1-i,h-1-j)
            new_canvas.setPixelColor(i,j,r,g,b)
    return new_canvas

def negativeFlip(canvas):
    canvas = flipHorizontally(canvas)
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w//2):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)            
            g = canvas.getPixelGreen(i,j)
            b = canvas.getPixelBlue(i,j)
            canvas.setPixelColor(i,j,255-r,255-g,255-b)
    return canvas

def negativeMirror(canvas):
    canvas = mirrorHorizontally(canvas)
    w = canvas.getWidth()
    h = canvas.getHeight()
    for i in range(0,w//2):
        for j in range(0,h):
            r = canvas.getPixelRed(i,j)            
            g = canvas.getPixelGreen(i,j)
            b = canvas.getPixelBlue(i,j)
            canvas.setPixelColor(i,j,255-r,255-g,255-b)
    return canvas    
    

main()