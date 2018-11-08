class Square:

    def __init__(self):
        self.party = 0
        self.x = 0
        self.y = 0
        self.seat = -1

    def get_adjacent_squares(self, grid):
        adjacent_squares = []
        if self.x > 0:
            adjacent_squares.append(grid.squares[self.x - 1][self.y])
        if self.x < grid.size_x - 1:
            adjacent_squares.append(grid.squares[self.x + 1][self.y])
        if self.y > 0:
            adjacent_squares.append(grid.squares[self.x][self.y - 1])
        if self.y < grid.size_y - 1:
            adjacent_squares.append(grid.squares[self.x][self.y + 1])
        return adjacent_squares


class SwapSquare:
    def __init__(self):
        self.square = -1
        self.swap_square = -1

    def majority(self):
        return self.swap_square.seat.majority


class Seat:
    def __init__(self):
        self.squares = []
        self.id = -1
        self.party = -1
        self.majority = 0


class Grid:
    size_x = 30
    size_y = 30
    no_of_parties = 2
    no_of_seats = 30
    result_left = []
    result_right = []
    rig_seat = 0
    rig_swap_square = 0

    def __init__(self):
        self.total_size = self.size_x * self.size_y
        self.squares = [[0 for x in range(self.size_y)] for y in range(self.size_y)]
        for x in range(0, self.size_y):
            for y in range(0, self.size_y):
                square = Square()
                square.x = x
                square.y = y
                self.squares[x][y] = square
        self.seats = []

        # Print the status
        self.result_left.append('Grid of size {0}x{1} votes:{2}'\
            .format(repr(self.size_x), repr(self.size_y), repr(self.total_size)))
