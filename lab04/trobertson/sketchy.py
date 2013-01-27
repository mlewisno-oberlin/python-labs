# sketchy.py
# Draws a beautiful image of a lone wolf in the moonlight
#
# Tyler Robertson
# January 12, 2013

from picture import Picture
import random

def main() :
    W = 800
    H = 600
    art = Picture((W,H))
    art.setPenColor(20,0,20) #1
    art.drawRectFill(0,0,W,H) #2
    art = drawStars(art,W,H)
    art = drawMoon(art,60,60)
    art = drawLandscape(art)
    art = drawWolf(art,394,350)
    art.drawString(720,580,"-Tyler") #8
    art = pythonWT(art)
    art.writeFile("Wolf.bmp")
    art.display()
    
    
def drawStars(art,w,h) :
    numStars = 200
    art.setPenColor(255,255,255)
    for i in range(numStars):
        art.setPosition(random.randint(0,w),random.randint(0,h)) #3
        art.drawForward(1) #4
    return art

def drawMoon(art, x, y) :
    art.setPenColor(255,255,204)
    art.drawCircleFill(x,y,75) #5
    art.drawCircle(x,y,120) #6
    art.setPenColor(20,0,20)
    art.drawCircleFill(x+40,y,75)
    return art

def drawLandscape(art) :
    art.setPenColor(0,0,0)
    art.fillPoly((0,200,392,408,600,800,800,0),(400,450,350,350,450,400,600,600)) #7
    return art

def drawWolf(art,x,y) :
    art.setPenColor(119,119,119)
    art.fillPoly((x,x,x-2,x-2,x-3,x-2,x+3,x+3,x+8,x+12,x+12,x+4,x+2),(y,y-4,y-6,y-10,y-10,y-12,y-8,y-6,y,y-4,y,y,y-2))
    return art

def pythonWT(art) :
    art.setPenColor(255,0,0)
    art.setPenWidth(2)
    #P
    art.setPosition(450,100)
    art.setDirection(300)
    art.drawForward(75)
    art.setPosition(450,100)
    art.setDirection(0)
    art.drawForward(38)
    art.setDirection(225)
    art.drawForward(35)
    #Y
    art.setPosition(485,140)
    art.setDirection(315)
    art.drawForward(35)
    art.setPosition(510,135)
    art.setDirection(260)
    art.drawForward(70)
    #T
    art.setPosition(510,135)
    art.setDirection(30)
    art.drawForward(35)
    art.setPosition(515,110)
    art.setDirection(300)
    art.drawForward(70)
    #H
    art.setPosition(545,100)
    art.drawForward(70)
    art.setPosition(570,140)
    art.setDirection(60)
    art.drawForward(15)
    art.setDirection(300)
    art.drawForward(30)
    #O
    art.drawCircleFill(605,135,28)
    art.setPenColor(20,0,20)
    art.drawCircleFill(605,135,22)
    art.setPenColor(255,0,0)
    #N
    art.setPosition(625,110)
    art.drawForward(120)
    art.setPosition(630,120)
    art.setDirection(60)
    art.drawForward(15)
    art.setDirection(300)
    art.drawForward(30)
    #W
    art.setPosition(515,200)
    art.setDirection(315)
    art.drawForward(75)
    art.setDirection(90)
    art.drawForward(50)
    art.setDirection(315)
    art.drawForward(50)
    art.setDirection(90)
    art.drawForward(75)
    #T
    art.setDirection(30)
    art.drawForward(100)
    return art

main()
