from picture import Picture

WIDTH = 0
HEIGHT = 0

def main():
    pic = Picture("crayons.bmp")
    WIDTH = pic.getWidth()
    HEIGHT = pic.getHeight()
    print(WIDTH, HEIGHT)
    pic2 = copyImage(pic)
    input()
    
def copyImage(pic):
    print (WIDTH, HEIGHT)
    pic2 = Picture((WIDTH, HEIGHT))
    pic2.display()
    input()
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            red = pic.getPixelRed(x, y)
            green = pic.getPixelGreen(x, y)
            blue = pic.getPixelBlue(x, y)
            pic2.setPixelRed(x, y, red)
            pic2.setPixelGreen(x, y, green)
            pic2.setPixelBlue(x, y, blue)
    return pic2

main()