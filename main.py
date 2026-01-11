from cell import Cell
from recurcive_backtracker import  backtrack_recursively

cells_n: int = None
cell_size: int
WIDTH = 500
HEIGHT = 500

grid: list[list[Cell]]

def init_grid():
    global grid
    global cell_size
    global cells_n
    print("How many cells should one row of the maze have?")
    while cells_n is None or cells_n <= 1:
        try:
            cells_n = int(input())
        except ValueError:
            print("Invalid input. Enter a number > 1.")
    cell_size = WIDTH / cells_n
    grid = [[Cell(i, j, cell_size) for j in range(cells_n)] for i in range(cells_n)]


if __name__ == "__main__":

    init_grid()

    print("\nChoose an algorithm for maze generation:"
          "\n1. Recursive Backtracker"
          )

    algorithm_choice = None
    while algorithm_choice is None:
       try:
            algorithm_choice = int(input())
       except ValueError:
            print("Invalid input. Enter a number.")

    if algorithm_choice == 1:
        backtrack_recursively(grid, cell_size)
    else:
        print("Invalid algorithm choice.")

