import cell
from cell import Cell
import random
from visualization import visualize_grid

wall_list = [] #list of walls

def add_walls(cell, cols, rows):
    global wall_list
    i, j = cell.i, cell.j

    if cell.S_wall and j > 0:
        wall_list.append((i ,j , "S"))
    if cell.E_wall and i < cols - 1:
        wall_list.append((i ,j , "E"))
    if cell.N_wall and j < rows - 1:
        wall_list.append((i ,j , "N"))
    if cell.W_wall and i > 0:
        wall_list.append((i ,j , "W"))

def get_neighbour_coords(i, j, direction, rows, cols):
    if direction == "S":
        return (i, j - 1) if j > 0 else None
    if direction == "E":
        return (i + 1, j) if i < cols - 1 else None
    if direction == "N":
        return (i, j + 1) if j < rows - 1 else None
    if direction == "W":
        return (i - 1, j) if i > 0 else None
    return None

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

def prim(grid, cell_size):
    global wall_list
    grid[0][0].start = True
    grid[-1][-1].end = True
    cols, rows = len(grid), len(grid[0])

    random_row = random.choice(grid)
    first_cell = random.choice(random_row)
    first_cell.visited = True
    add_walls(first_cell, cols, rows)

    while wall_list:
        wall_index = random.randint(0, len(wall_list) - 1)#pick a random wall index
        wall_i, wall_j, wall_dir = wall_list[wall_index]

        cell1 = grid[wall_i][wall_j]#find the corresponding cell
        neighbour_coords = get_neighbour_coords(wall_i, wall_j, wall_dir, rows, cols)#get coords of the cell behind the wall
        if neighbour_coords is None: continue
        cell2 = grid[neighbour_coords[0]][neighbour_coords[1]]

        if cell1.visited != cell2.visited:
            remove_wall(cell1, cell2)
            if not cell1.visited:
                cell1.visited = True
                add_walls(cell1, cols, rows)
            elif not cell2.visited:
                cell2.visited = True
                add_walls(cell2, cols, rows)

        wall_list.pop(wall_index)
        visualize_grid(grid, cell_size)

