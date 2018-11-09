class Square:

    def __init__(self):
        self.party = 0
        self.x = 0
        self.y = 0
        self.seat = None

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
    size_x = 18
    size_y = 9
    no_of_parties = 2
    no_of_seats = 18
    rig_seat = 0
    rig_swap_square = 0
    results = None
    votes = [0] * no_of_parties
    voters = size_x * size_y

    def __init__(self):
        self.total_size = self.size_x * self.size_y
        self.squares = [[0] * self.size_y for i in range(self.size_x)]
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                square = Square()
                square.x = x
                square.y = y
                self.squares[x][y] = square
        self.seats = []

        # Print the status
        print 'Grid of size {0}x{1}'.format(repr(self.size_x), repr(self.size_y))
        print 'Voting population:{0}'.format(repr(self.total_size))

    def majority(self, party):
        return 2 * self.results[party] - self.no_of_seats