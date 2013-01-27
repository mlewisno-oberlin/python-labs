# life.py
# displays a visual representation of the Game of Life
#
# Tyler Robertson
# 1/21/13

from picture import Picture

def main() :
    CELL_SIZE, ROUNDS = 6, 500
    try:
        cells, TILESX, TILESY  = fillCells(input("Open board from file: "))
    except FileNotFoundError :
        cells = []
        TILESX, TILESY = 50, 80
        for i in range(TILESY):
            cells.append([False]*TILESX)
        cells[39][40]=1
        cells[40][39]=1
        cells[40][40]=1
        cells[41][40]=1
        cells[39][41]=1
    cells2 = []
    for i in range(TILESY):
        cells2.append([False]*TILESX)
    board = Picture(((TILESX * (CELL_SIZE + 1))+1,1+(TILESY*(CELL_SIZE + 1))))
    # "plays" the game for ROUNDS times
    for i in range(ROUNDS):
        # for each cell...
        for x in range(TILESX):
            for y in range(TILESY):
                neighbors = numNeighbors(cells,y,x,TILESX,TILESY)
                if neighbors == 0:
                    cells2[y][x] = False
                if neighbors == 1:
                    cells2[y][x] = False
                if neighbors == 3:
                    cells2[y][x] = True
                if neighbors >= 4:
                    cells2[y][x] = False
        cells,cells2 = cells2,cells
        board = drawGrid(board,TILESX,TILESY,cells,CELL_SIZE)
        board.display()

# draws a new board
# @param board Graphical representation of the board
# @param tx Number of cells wide
# @param ty Number of cells tall
# @param cells The list of cells
# @param size Size of each cell
def drawGrid(board,tx,ty,cells,size) :
    board.setPenColor(0,255,0)
    # draw grid lines
    for a in range(0,board.getWidth(),size+1):
        board.drawLine(a,0,a,board.getHeight()-1)
    for a in range(0,board.getHeight(),size+1):
        board.drawLine(0,a,board.getWidth()-1,a)
    board.setPenColor(255,0,0)
    # fill in appropriate cells
    for x in range(tx):
        for y in range(ty):
            if cells[y][x] == True:
                board.drawRectFill((x*size)+(x+1),(y*size)+(y+1),size-1,size-1)
    return board

# returns the number of neighbors for the given cell
# @param cells The list of cells
# @param y Y-coordinate of given cell
# @param x X-coordinate of given cell
# @param tx Number of cells wide
# @param ty Number of cells tall
def numNeighbors(cells,y,x,tx,ty) :
    #y minus 1, y plus 1, etc...
    ym,yp,xm,xp = y-1,y+1,x-1,x+1
    #create the torrus
    if ym == -1 : ym = ty-1
    if yp == ty : yp = 0
    if xm == -1 : xm = tx-1
    if xp == tx : xp = 0
    #add em up
    total = 0
    if cells[ym][xm] == True : total += 1    #NW
    if cells[ym][x] == True : total += 1     #N
    if cells[ym][xp] == True : total += 1    #NE
    if cells[y][xm] == True : total += 1     #W
    if cells[y][xp] == True : total += 1     #E
    if cells[yp][xm] == True : total += 1    #SW
    if cells[yp][x] == True : total += 1     #S
    if cells[yp][xp] == True : total += 1    #SE
    return total

# opens a board from file
def fillCells(filename):
    thefile = open(filename,"r")
    cells = []
    y = 0
    x = 0
    for line in thefile:
        line = line[:-1]
        cells.append([])
        x = 0
        for char in line:
            if eval(char) == 0 :
                cells[y].append(False)
                x += 1
            if eval(char) == 1 :
                cells[y].append(True)
                x += 1
        y += 1
    return cells, x, y

main()
