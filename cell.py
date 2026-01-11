class Cell:
    S_wall: bool
    E_wall: bool
    N_wall: bool
    W_wall: bool
    x: int
    y: int
    visited: bool

    def __init__(self, x, y, cell_size):
        self.i = x
        self.j = y
        self.start = False
        self.end = False
        self.x = x * cell_size
        self.y = y * cell_size
        self.S_wall = True
        self.E_wall = True
        self.N_wall = True
        self.W_wall = True
        self.visited = False