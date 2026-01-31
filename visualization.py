import matplotlib.pyplot as plt
import matplotlib.patches as patches

visited_cells = [[]]
visited_n = 0

def visualize_grid(grid, cell_size):
    final = False
    global visited_n
    global visited_cells
    if visited_n == 0:#initialize visited cells first time
        visited_cells = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    plt.clf()
    for row in grid:
        for cell in row:
            #visualize active walls by lines
            if cell.N_wall:
                plt.plot([cell.x , cell.x + cell_size ], [cell.y + cell_size, cell.y + cell_size], color="black")
            if cell.S_wall:
                plt.plot([cell.x , cell.x + cell_size ], [cell.y , cell.y ], color="black")
            if cell.W_wall:
                plt.plot([cell.x , cell.x ], [cell.y , cell.y + cell_size], color="black")
            if cell.E_wall:
                plt.plot([cell.x + cell_size , cell.x + cell_size ], [cell.y , cell.y + cell_size], color="black")
            if cell.visited:#if cell has been visited mark it with diff color
                patch = patches.Rectangle((cell.x, cell.y), cell_size, cell_size, linewidth=1, color='lavender')
                if not visited_cells[cell.i][cell.j]:
                    visited_cells[cell.i][cell.j] = True
                    visited_n += 1
                plt.gca().add_patch(patch)
            if cell.start:
                patch = patches.Rectangle((cell.x, cell.y), cell_size, cell_size, linewidth=1, color='aquamarine')
                plt.gca().add_patch(patch)
            if cell.end:
                patch = patches.Rectangle((cell.x, cell.y), cell_size, cell_size, linewidth=1, color='violet')
                plt.gca().add_patch(patch)


    #check if all cells have been visited
    if visited_n == len(grid) * len(grid[0]):
        final = True

    plt.gca().set_aspect('equal', adjustable='box')#make the graph square
    plt.gca().axis('off')#remove axis

    #plt.draw()
    if not final:
        plt.pause(0.00001)
        plt.show(block=False)
    else:
        plt.show()