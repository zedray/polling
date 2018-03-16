class Square:
    def __init__(self):
        party = 0
        x = 0
        y = 0


class Grid:
    size_x = 30
    size_y = 30
    no_of_parties = 2

    def __init__(self):
        self.total_size = self.size_x * self.size_y
        self.squares = [[0 for x in range(self.size_y)] for y in range(self.size_y)]
        for x in range(0, self.size_y):
            for y in range(0, self.size_y):
                square = Square()
                square.x = x
                square.y = y
                self.squares[x][y] = square

        # Print the status
        print 'Grid Size - x:' + repr(self.size_x) + ' y:' + repr(self.size_y) + '  Total:' + repr(self.total_size)
