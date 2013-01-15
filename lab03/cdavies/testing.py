from picture import Picture

def main():
    canvas = Picture((500, 500))
    canvas.display()
    canvas.setPenColor(200,0,0)
    canvas.drawRectFill(250,250,200,200)
    canvas.display()
    input()
    
    
    
main()