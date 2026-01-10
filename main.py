import matplotlib.pyplot as plt

cells_n: int
cell_size: int
WIDTH = 400
HEIGHT = 400


class Cell:
    S_wall: bool
    E_wall: bool
    N_wall: bool
    W_wall: bool
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x * cell_size
        self.y = y * cell_size
        self.S_wall = True
        self.E_wall = True
        self.N_wall = True
        self.W_wall = True


grid: list[list[Cell]]

def init_grid():
    global grid
    global cell_size
    cell_size = WIDTH / cells_n
    grid = [[Cell(j, i) for j in range(cells_n)] for i in range(cells_n)]

def visualize_grid():
    global grid
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


    plt.gca().set_aspect('equal', adjustable='box')#make the graph square
    plt.gca().axis('off')#remove axis
    plt.show()

if __name__ == "__main__":
    print("How many cells should one row of the maze have?")
    cells_n = int(input())

    init_grid()
    visualize_grid()

