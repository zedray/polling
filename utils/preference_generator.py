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
    # TODO: This is a bit crap, rewrite it all.
    # TODO: Correctly divide the votes.
    remaining_votes = [grid.total_size / grid.no_of_parties] * grid.no_of_parties

    all_voted_squares = []
    all_squares = __get_all_squared(grid)

    # Vote for a bunch of square first.
    geo_bias_regions = 10
    for party in range(0, grid.no_of_parties):
        for votes in range(0, geo_bias_regions):
            remaining_votes[party] -= 1
            all_voted_squares.append(__vote_for_random_seat(all_squares, party))

    # Pick a voted on square.
    square = random.choice(all_voted_squares)
    nearby_squares = __get_adjacent_squares(grid, square)
    print nearby_squares

    nearby_square = random.choice(nearby_squares)
    nearby_square.party = 1
    all_squares.remove(nearby_square)
    print 'Square ' + repr(nearby_square.x) + ',' + repr(nearby_square.y) + ' is Voting for ' + repr(len(all_squares))


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
    print 'Square ' + repr(square.x) + ',' + repr(square.y) + ' is Voting for ' + repr(party)
    return square


def __get_adjacent_squares(grid, square):
    adjacent_squares = []
    if square.x > 0:
        __add_square_if_not_voted_yet(adjacent_squares, grid.squares[square.x - 1][square.y])
    if square.x < grid.size_x - 1:
        __add_square_if_not_voted_yet(adjacent_squares, grid.squares[square.x + 1][square.y])
    if square.y > 0:
        __add_square_if_not_voted_yet(adjacent_squares, grid.squares[square.x][square.y + 1])
    if square.y < grid.size_y - 1:
        __add_square_if_not_voted_yet(adjacent_squares, grid.squares[square.x][square.y - 1])
    return adjacent_squares


def __add_square_if_not_voted_yet(adjacent_squares, square):
    if not hasattr(square, 'party'):
        adjacent_squares.append(square)