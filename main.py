import time

from cell import Cell
from recurcive_backtracker import  backtrack_recursively
from prim_algorithm import prim

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
            if cells_n <= 1:
                print("Invalid input. Enter a number > 1.")
                cells_n = None
        except ValueError:
            print("Invalid input. Enter a number > 1.")
    cell_size = WIDTH / cells_n
    grid = [[Cell(i, j, cell_size) for j in range(cells_n)] for i in range(cells_n)]


if __name__ == "__main__":

    init_grid()

    print("\nChoose an algorithm for maze generation:"
          "\n1. Recursive Backtracker"
          "\n2. Randomized Prim's Algorithm"
          )

    algorithm_choice = None
    while algorithm_choice is None:
       try:
            algorithm_choice = int(input())
       except ValueError:
            print("Invalid input. Enter a number.")

    start_time = time.time()

    if algorithm_choice == 1:
        backtrack_recursively(grid, cell_size)
    elif algorithm_choice == 2:
        prim(grid, cell_size)
    else:
        print("Invalid algorithm choice.")

    end_time = time.time()

    print(f"\nTime elapsed: {end_time - start_time:.2f} seconds")
