# sketchy.py
# Makes a picture
# 
# Connor Davies
# 1/12/13

from picture import Picture

def main():
    canvas = Picture((400, 400))
    sky(canvas)
    ground(canvas)
    pipe(canvas)
    blocks(canvas)
    questionMarks(canvas)
    mario(canvas)
    sun(canvas)
    clouds(canvas)
    horizontalLines(canvas)
    verticalLines(canvas)
    canvas.display()
    canvas.writeFile("cdavies.jpg")
    input("Press enter to end the prgram.")

def horizontalLines(canvas):
    canvas.setPenColor(50,50,50)
    for i in range(14,17):
        canvas.drawRect(0, 25*i, 400, 0)


def verticalLines(canvas):
    canvas.setPenColor(50,50,50)
    for i in range(0,17):
        canvas.drawRect(25*i, 350, 0, 400)

def sky(canvas):
    canvas.setPenColor(135,206,250)
    canvas.drawRectFill(0,0,400,400)


def ground(canvas):
    canvas.setPenColor(210,105,30)
    canvas.drawRectFill(0, 350, 400, 50)

def pipe(canvas):
    canvas.setPenColor(50,205,50)
    canvas.drawRectFill(250,300,50,25)
    canvas.drawRectFill(255,325,40,25)
    canvas.setPenColor(0,0,0)
    canvas.drawRect(250,300,50,25)
    canvas.drawRect(255,325,40,25)

def blocks(canvas):
    canvas.setPenColor(210,105,30)
    canvas.drawRectFill(50,250,125,25)
    canvas.setPenColor(255,215,0)
    canvas.drawRectFill(100,150,25,25)
    canvas.drawRectFill(75,250,25,25)
    canvas.drawRectFill(125,250,25,25)

    canvas.setPenColor(0,0,0)
    canvas.drawRect(50,250,125,25)
    canvas.drawRect(100,150,25,25)
    canvas.drawRect(75,250,25,25)
    canvas.drawRect(125,250,25,25)

def questionMarks(canvas):
    canvas.setPenColor(0,0,0)
    canvas.drawRectFill(85,270,5,4)
    canvas.drawRectFill(135,270,5,4)
    canvas.drawRectFill(110,170,5,4)
    canvas.drawRectFill(85,260,5,7)
    canvas.drawRectFill(135,260,5,7)
    canvas.drawRectFill(110,160,5,7)
    canvas.drawRectFill(90,253,5,10)
    canvas.drawRectFill(140,253,5,10)
    canvas.drawRectFill(115,153,5,10)
    canvas.drawRectFill(130,253,15,5)
    canvas.drawRectFill(80,253,15,5)
    canvas.drawRectFill(105,153,15,5)

def mario(canvas):
    canvas.setPenColor(160,82,45)
    canvas.drawRectFill(263,258,18,3)
    canvas.drawRectFill(260,261,21,3)
    canvas.drawRectFill(260,264,24,3)
    canvas.drawRectFill(260,267,30,3)
    canvas.drawRectFill(263,273,18,3)
    canvas.drawRectFill(260,276,30,3)
    canvas.drawRectFill(257,279,36,3)
    canvas.drawRectFill(263,282,3,3)
    canvas.drawRectFill(287,282,3,3)
    canvas.drawRectFill(260,294,9,3)
    canvas.drawRectFill(281,294,9,3)
    canvas.drawRectFill(257,297,12,3)
    canvas.drawRectFill(281,297,12,3)
    
    canvas.setPenColor(255,0,0)
    canvas.drawRectFill(266,252,15,3)
    canvas.drawRectFill(263,255,27,3)
    canvas.drawRectFill(269,273,3,3)
    canvas.drawRectFill(269,276,3,3)
    canvas.drawRectFill(278,276,3,3)
    canvas.drawRectFill(269,279,12,3)
    canvas.drawRectFill(266,282,3,3)
    canvas.drawRectFill(272,282,6,3)
    canvas.drawRectFill(281,282,3,3)
    canvas.drawRectFill(266,285,18,3)
    canvas.drawRectFill(263,288,24,3)
    canvas.drawRectFill(263,291,9,3)
    canvas.drawRectFill(278,291,9,3)

    canvas.setPenColor(255,222,173)
    canvas.drawRectFill(272,258,6,3)
    canvas.drawRectFill(281,258,3,3)
    canvas.drawRectFill(263,261,3,3)
    canvas.drawRectFill(269,261,9,3)
    canvas.drawRectFill(281,261,9,3)
    canvas.drawRectFill(263,264,3,3)
    canvas.drawRectFill(272,264,9,3)
    canvas.drawRectFill(284,264,9,3)
    canvas.drawRectFill(266,267,12,3)
    canvas.drawRectFill(266,270,21,3)
    canvas.drawRectFill(257,282,6,3)
    canvas.drawRectFill(269,282,3,3)
    canvas.drawRectFill(278,282,3,3)
    canvas.drawRectFill(287,282,6,3)
    canvas.drawRectFill(257,285,9,3)
    canvas.drawRectFill(284,285,9,3)
    canvas.drawRectFill(257,288,6,3)
    canvas.drawRectFill(287,288,6,3)

def clouds(canvas):
    canvas.setPenColor(255,255,255)
    canvas.drawRectFill(245,45,100,45)
    canvas.setPenColor(135,206,250)
    canvas.drawRectFill(245,45,18,9)
    canvas.drawRectFill(245,54,9,9)
    canvas.drawRectFill(245,72,9,9)
    canvas.drawRectFill(245,81,18,9)
    canvas.drawRectFill(245,45,18,9)
    canvas.drawRectFill(327,45,18,9)
    canvas.drawRectFill(336,54,9,9)
    canvas.drawRectFill(336,72,9,9)
    canvas.drawRectFill(327,81,18,9)

    canvas.setPenColor(255,255,255)
    canvas.drawRectFill(55,63,100,45)
    canvas.setPenColor(135,206,250)
    canvas.drawRectFill(55,63,18,9)
    canvas.drawRectFill(55,72,9,9)
    canvas.drawRectFill(55,90,9,9)
    canvas.drawRectFill(55,99,18,9)
    canvas.drawRectFill(55,63,18,9)
    canvas.drawRectFill(137,63,18,9)
    canvas.drawRectFill(146,72,9,9)
    canvas.drawRectFill(146,90,9,9)
    canvas.drawRectFill(137,99,18,9)

def sun(canvas):
    canvas.setPenColor(255,215,0)
    canvas.drawCircleFill(400,0,71)
    
main()
