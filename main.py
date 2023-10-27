#CGOL main file
#Oct. 2023
#James Underwood

from cell import Cell
from cs1lib import *

FRAMER = 5

WIN_WIDTH = 1000
WIN_HEIGHT = 800

CELL_WIDTH = 15

rowsize = WIN_WIDTH // CELL_WIDTH
columnsize = WIN_HEIGHT // CELL_WIDTH

start = False

cells = []
i = 0
while (i<rowsize):
    j = 0
    temp = []
    while (j<columnsize):
         cell = Cell(i*CELL_WIDTH,j*CELL_WIDTH,CELL_WIDTH)
         temp.append(cell)
         j+=1
    cells.append(temp)
    i+=1

def tick(i,j):

            neighborsalive = 0

            try:
                if (cells[i-1][j-1].alive):
                    neighborsalive += 1
            except:
                pass
            try:
                if (cells[i-1][j].alive):
                    neighborsalive += 1
            except:
                pass
            try:
                if (cells[i-1][j+1].alive):
                    neighborsalive += 1
            except:
                pass

            try:
                if (cells[i][j-1].alive):
                    neighborsalive += 1
            except:
                pass

            try:
                if (cells[i][j+1].alive):
                    neighborsalive += 1
            except:
                pass

            try:
                if (cells[i+1][j-1].alive):
                    neighborsalive += 1
            except:
                pass
            try:
                if (cells[i+1][j].alive):
                    neighborsalive += 1
            except:
                pass
            try:
                if (cells[i+1][j+1].alive):
                    neighborsalive += 1
            except:
                pass

            cells[i][j].setto(cells[i][j].alive)

            if ((neighborsalive < 2) or (neighborsalive > 3) and cells[i][j].alive == True):
                cells[i][j].setto(False)


            if ((neighborsalive == 3) and cells[i][j].alive == False):
                cells[i][j].setto(True)

def draw():
    i = 0
    while (i < rowsize):
        j = 0
        while (j < columnsize):

            cells[i][j].draw()
            if (start):
                tick(i, j)
            j += 1
        i += 1

    for column in cells:
        for cell in column:
            if (start):
                cell.pushtick()
            cell.draw()

def clicked(x,y):
    global mousex, mousey
    if(start == False):
        cells[x//CELL_WIDTH][y//CELL_WIDTH].invert()

def key(key):
    global start
    if (key == " "):
        start = True
    elif (key == "r"):
        start = False
        for column in cells:
            for cell in column:
                cell.alive = False

start_graphics(draw,width=WIN_WIDTH,height=WIN_HEIGHT,mouse_press=clicked,framerate=FRAMER,key_press=key)