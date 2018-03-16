import random


def random_party(grid):
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            s = grid.squares[x][y]
            s.party = random.randint(0, grid.no_of_parties - 1)


def fair_random_party(grid):
    all_squares = __get_all_squared(grid)
    for party in range(0, grid.no_of_parties):
        for votes in range(0, grid.total_size / grid.no_of_parties):
            __vote_for_random_seat(all_squares, party)
    while len(all_squares) > 0:
        __vote_for_random_seat(random.randint(0, grid.no_of_parties - 1))


def geo_party(grid):
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            s = grid.squares[x][y]
            s.party = random.randint(1, grid.no_of_parties)


def __get_all_squared(grid):
    all_squares = []
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            all_squares.append(grid.squares[x][y])
    return all_squares


def __vote_for_random_seat(all_squares, party):
    square = random.choice(all_squares)
    square.party = party
    all_squares.remove(square)
    print 'Square ' + repr(square.x) + ',' + repr(square.y) + ' is Voting for ' + repr(len(all_squares))
