# life.py
# Displays the Game of Life
# 
# Connor Davies
# 1/16/13

from picture import Picture
import time

def main():
    try:
        #Set variables
        WIDTH = 50
        HEIGHT = 80
        CELL_SIZE = 6
        ROUNDS = 500
        #create picture
        canvas = Picture((WIDTH*CELL_SIZE+1,HEIGHT*CELL_SIZE+1))
        #create lists that represent the board
        board = []
        boardCopy = []
        for i in range(0,WIDTH):
            h = []
            hCopy = []
            for j in range(0,HEIGHT):
                h.append(0)
                hCopy.append(0)
            board.append(h)
            boardCopy.append(hCopy)
        #draw out the grid
        canvas.setPenColor(0,0,0)
        canvas.drawRectFill(0,0,WIDTH*CELL_SIZE,HEIGHT*CELL_SIZE)
        canvas.setPenColor(0,255,0)
        canvas.drawLine(0,HEIGHT*CELL_SIZE,WIDTH*CELL_SIZE,HEIGHT*CELL_SIZE)
        canvas.drawLine(WIDTH*CELL_SIZE,0,HEIGHT*CELL_SIZE,WIDTH*CELL_SIZE)
        for i in range(0,HEIGHT):
            canvas.drawLine(0,CELL_SIZE*i,WIDTH*CELL_SIZE,i*CELL_SIZE)
        for i in range(0,WIDTH):
            canvas.drawLine(CELL_SIZE*i,0,i*CELL_SIZE,HEIGHT*CELL_SIZE)
        n=0
        while n<1 or n>3:
            n = eval(input("Please enter a number 1-3: "))
            if n==1:
                board[39][40]=1
                board[40][39]=1
                board[40][40]=1
                board[41][40]=1
                board[39][41]=1
            elif n==2:
                board[39][39]=1
                board[39][40]=1
                board[39][41]=0
                board[40][39]=0
                board[40][40]=1
                board[40][41]=0
                board[41][39]=0
                board[41][40]=1
                board[41][41]=0
                board[39][42]=0
                board[39][43]=1
                board[39][44]=0
                board[40][42]=0
                board[40][43]=1
                board[40][44]=0
                board[41][42]=1
                board[41][43]=1
                board[41][44]=0
            elif n==3:
                board[39][39]=1
                board[39][40]=0
                board[39][41]=1
                board[40][39]=1
                board[40][40]=1
                board[40][41]=0
                board[41][39]=1
                board[41][40]=0
                board[41][41]=1
            else:
                print("Please try again")
        #Draw any squares the start alive red.
        for i in range(0,WIDTH):
                for j in range(0,HEIGHT):
                    if board[i][j]==1:
                        canvas.setPenColor(255,0,0)
                        canvas.drawRectFill(i*CELL_SIZE+1,j*CELL_SIZE+1,CELL_SIZE-2,CELL_SIZE-2)
                    if board[i][j]==0:
                        canvas.setPenColor(0,0,0)
                        canvas.drawRectFill(i*CELL_SIZE+1,j*CELL_SIZE+1,CELL_SIZE-2,CELL_SIZE-2)
        canvas.display()
        #begin the game of life
        for count in range(0,ROUNDS):
            for i in range(0,WIDTH):
                for j in range(0,HEIGHT):
                    boardCopy[i][j]=lifeCheck(board,i,j,WIDTH,HEIGHT)
                    if boardCopy[i][j]==1:
                        canvas.setPenColor(255,0,0)
                        canvas.drawRectFill(i*CELL_SIZE+1,j*CELL_SIZE+1,CELL_SIZE-2,CELL_SIZE-2)
                    else:
                        canvas.setPenColor(0,0,0)
                        canvas.drawRectFill(i*CELL_SIZE+1,j*CELL_SIZE+1,CELL_SIZE-2,CELL_SIZE-2)
            canvas.display()
            for i in range(0,WIDTH):
                for j in range(0,HEIGHT):
                    board[i][j]=boardCopy[i][j]
    except NameError:
        print("Please enter a valid number next time.")
    except SyntaxError:
        print("Please enter a valid number next time.")
    except:
        print("Sorry, something unexpected has occured.  Please reload the program.")
    
    #takes in the coordinates of a square on the board and calculates if it will be alive next round.
def lifeCheck(board, x, y, WIDTH, HEIGHT):
    count = 0
    if board[(x+1)%(WIDTH)][(y+1)%(HEIGHT)]==1 : count=count+1
    if board[(x+1)%(WIDTH)][y]==1 : count=count+1
    if board[(x+1)%(WIDTH)][(y-1)%(HEIGHT)]==1 : count=count+1
    if board[x][(y+1)%(HEIGHT)]==1 : count=count+1
    if board[x][(y-1)%(HEIGHT)]==1 : count=count+1
    if board[(x-1)%(WIDTH)][(y+1)%(HEIGHT)]==1 : count=count+1
    if board[(x-1)%(WIDTH)][y]==1 : count=count+1
    if board[(x-1)%(WIDTH)][(y-1)%(HEIGHT)]==1 : count=count+1
    if count<2 : return 0
    if count==2 : return board[x][y]
    if count==3 : return 1
    return 0
    
main()