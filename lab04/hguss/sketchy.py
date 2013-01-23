# sketchy.py
# Generates a drawing
#
# Henry Lionni Guss
# 1/13/12

from picture import Picture
import random

NUM_BUILDINGS = 100

def main():
    pic = Picture((800,800))
    pic.setPenColor(128,80,255)
    pic.drawRectFill(0,0,800,800)
    for i in range(0, NUM_BUILDINGS):
        drawBuilding(pic)
    for i in range(0, 24):
        drawSun(pic, i)
    pic.writeFile("guss.bmp")
    input()
    
def drawSun(pic, timeOfDay):
    pic.setPenColor(255, 255, 0)
    pic.drawCircleFill(timeOfDay * 40, (timeOfDay - 12) ** 2 + 100, 100)
    timeWaster(100)
    pic.display()
    pic.setPenColor(128, 80, 255)
    pic.drawCircleFill(timeOfDay * 40, (timeOfDay - 12) ** 2 + 100, 100)

def timeWaster(time):
    product = time
    for i in range(0, time):
        product = product * i

def drawBuilding(pic):
    rHeight = random.randint(20, 300)
    rWidth = random.randint(45, 200)
    randRed = random.randint(0, 256)
    randGreen = random.randint(0, 256)
    randBlue = random.randint(0, 256)
    pic.setPenColor(randRed, randGreen, randBlue)
    rStart = random.randint(0, 800)
    pic.drawRectFill(rStart, 800 - rHeight, rWidth, rHeight)
    pic.setPenColor(0, 0, 0)
    pic.drawRect(rStart, 800 - rHeight, rWidth, rHeight)
    drawWindows(pic, rHeight, rWidth, rStart)    

def drawWindows(pic, height, width, start):
    for y in range(0, height // 20):
        for x in range(0, width // 40):
            drawWindow(pic, start + width // (width // 40 + 2) + x * 40, 800 - height + 10 + y * 30, 10)
    
def drawWindow(pic, x, y, width):
    pic.setPenColor(255, 255, 255)
    pic.drawRectFill(x, y, width, width)
    pic.setPenColor(0, 0, 0)
    pic.drawRect(x, y, width, width)
    
main()