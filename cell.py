from cs1lib import *

class Cell:
    def __init__(self,x,y,cellwidth):
        self.x = x
        self.y = y
        self.cellwidth = cellwidth
        self.alive = False
        self.toset = False

    def draw(self):
        if (self.alive):
            set_fill_color(0,0,0)
        else:
            set_fill_color(1,1,1)

        draw_rectangle(self.x, self.y, self.cellwidth, self.cellwidth)

    def invert(self):
        if (self.alive):
            self.alive = False
        else:
            self.alive = True

    def setto(self,setstate):
        self.toset = setstate

    def pushtick(self):
        self.alive = self.toset