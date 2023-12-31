# cgolpython

## This is an implementation of Conway's Game of Life that I created for my CS1 class.
jamesunderwood.net/cgolpython

This is a Python implementation of Conway's Game of Life (CGOL). CGOL
consists of a grid of cells that are either "alive" or "dead." In each
iteration of the game, called a generation, specific rules govern
whether a cell will be alive or dead based on its neighbors (the eight
cells horizontally, vertically, or diagonally adjacent):
* Live cells with two or three live neighbors survive
* Dead cells with three live neighbors become alive
* All other cells are dead, even if they were previously alive
  
The course of the game is entirely predetermined by the starting
conditions.
  
My implementation uses a class called Cell to simulate CGOL. The class
contains methods to draw itself as either dead (white) or alive
(black), to invert its alive state, to set its alive state for the
future generation, and to "push" that alive state to its actual state.
Cells are stored in a list; each generation, main.py iterates through
the list, counts the number of alive neighbors for each cell,
determines whether the cell should change its alive/dead status in the
next generation, and finally pushes these changes.
  
Window dimensions, cell size, and frame rate can be easily customized.
The program will only simulate the cells that are on-screen, so
"border activity" will not be rendered properly.
  
Controls: in the start phase, click on cells to activate/deactivate
them. Press space to begin "gameplay." Press R to reset the board and
return to the start phase.
  
=====
  
More about Conway's Game of Life: https://en.wikipedia.org/wiki/
Conway's_Game_of_Life
