from cell import Cell
from typing import List
import random
from visualization import visualize_grid

def neighbors(grid, cell:Cell):
    #return existing neighbors
    neighbors = []
    i = cell.i
    j = cell.j
    if i > 0: neighbors.append(grid[i-1][j])
    if j > 0: neighbors.append(grid[i][j-1])
    if i < len(grid)-1: neighbors.append(grid[i+1][j])
    if j < len(grid[0])-1: neighbors.append(grid[i][j+1])
    return neighbors

def remove_wall(cell1:Cell, cell2:Cell):
    #removes a wall between two cells
    i1 = cell1.x
    j1 = cell1.y
    i2 = cell2.x
    j2 = cell2.y
    if j1 < j2: #cell1 is below cell2
        cell1.N_wall = False
        cell2.S_wall = False
        return
    if j1 > j2: #cell1 is above cell2
        cell1.S_wall = False
        cell2.N_wall = False
        return
    if i1 < i2: # cell1 is left of cell2
        cell1.E_wall = False
        cell2.W_wall = False
        return
    if i1 > i2: # cell1 is right of cell2
        cell1.W_wall = False
        cell2.E_wall = False
        return


def backtrack_recursively(grid, cell_size):
    cells_stack: List[Cell] = []
    cells_stack.append(grid[0][0])
    grid[0][0].visited = True
    grid[0][0].start = True
    grid[-1][-1].end = True

    while cells_stack:
        current_cell = cells_stack.pop()#select cell from the top of the stack
        neighbors_list = neighbors(grid, current_cell)
        unvisited_neighbors_list = [neighbor for neighbor in neighbors_list if neighbor.visited == False]
        if unvisited_neighbors_list:#if the cell has unvisited neighbors
            cells_stack.append(current_cell)#push the current cell back to the stack

            next_cell = random.choice(unvisited_neighbors_list)#choose a random unvisited neighbor cell
            remove_wall(current_cell, next_cell)#remove wall between the two cells
            next_cell.visited = True

            cells_stack.append(next_cell)#add the chosen cell to the stack
            visualize_grid(grid, cell_size)



