import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualize_grid(grid, cell_size):
    for row in grid:
        for cell in row:
            #visualize active walls by lines
            if cell.N_wall:
                plt.plot([cell.x , cell.x + cell_size ], [cell.y + cell_size, cell.y + cell_size], color="black")
            if cell.S_wall:
                plt.plot([cell.x , cell.x + cell_size ], [cell.y , cell.y ], color="black")
            if cell.E_wall:
                plt.plot([cell.x , cell.x ], [cell.y , cell.y + cell_size], color="black")
            if cell.W_wall:
                plt.plot([cell.x + cell_size , cell.x + cell_size ], [cell.y , cell.y + cell_size], color="black")
            if cell.visited:#if cell has been visited mark it with diff color
                patch = patches.Rectangle((cell.x, cell.y), cell_size, cell_size, linewidth=1, color='lavender')
                plt.gca().add_patch(patch)


    plt.gca().set_aspect('equal', adjustable='box')#make the graph square
    plt.gca().axis('off')#remove axis

    plt.show()