import random


def random_party(grid):
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            s = grid.squares[x][y]
            s.party = random.randint(0, grid.no_of_parties - 1)


def fair_random_party(grid):
    all_squares = []
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            all_squares.append(grid.squares[x][y])
    print 'Party ' + repr(len(all_squares))
    for party in range(0, grid.no_of_parties):
        for votes in range(0, grid.total_size / grid.no_of_parties):
            vote_for_random_seat(all_squares, party)
    while len(all_squares) > 0:
        vote_for_random_seat(random.randint(0, grid.no_of_parties - 1))


def vote_for_random_seat(all_squares, party):
    square = random.choice(all_squares)
    square.party = party
    all_squares.remove(square)
    print 'Voting for ' + repr(len(all_squares))


def geo_party(grid, no_of_parties):
    grid.no_of_parties = no_of_parties
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            s = grid.squares[x][y]
            s.party = random.randint(1, no_of_parties)