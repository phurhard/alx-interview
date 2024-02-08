# Island perimeter
## Problem statement
* Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

    * grid is a list of list of integers:
    * 0 represents water
    * 1 represents land
    * Each cell is square, with a side length of 1
    * Cells are connected horizontally/vertically (not diagonally).
    * grid is rectangular, with its width and height not exceeding 100
    * The grid is completely surrounded by water
    * There is only one island (or nothing).
    * The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
## How to solve
        Loop through the rows and coloumns,
        know that perimeter is the sum of all sides of the cell
        so for 1 cell the perimeter is 4 because it has four sides.
        so for each cell the perimeter will be increased by 4,
        but know that some of the cells are joined at one or two sides,
        so as such apart from the first row which does not have any cell above it
        the first coloumn which does not have cells before it.
        therefore,  for every other cells, if it has a cell before it, we'll minus 2 from the perimeter, 
        because the cells join at that point which reduces the perimeter by that value.
