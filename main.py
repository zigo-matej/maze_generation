from tkinter import IntVar

from cell import Cell
from visualization import visualize_grid
from recurcive_backtracker import  backtrack_recursively

cells_n: int
cell_size: int
WIDTH = 400
HEIGHT = 400

grid: list[list[Cell]]

def init_grid():
    global grid
    global cell_size
    cell_size = WIDTH / cells_n
    grid = [[Cell(j, i, cell_size) for j in range(cells_n)] for i in range(cells_n)]


if __name__ == "__main__":
    print("How many cells should one row of the maze have?")
    cells_n = int(input())

    init_grid()

    print()
    print("Choose an algorithm for maze generation:"
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
    visualize_grid(grid, cell_size)

