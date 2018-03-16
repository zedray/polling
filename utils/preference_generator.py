import random
from model import map


def random_party(grid, no_of_parties):
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            s = grid.squares[x][y]
            s.party = random.randint(1, no_of_parties)


def geo_party(grid, parties):
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            s = grid.squares[x][y]
            s.party = random.randint(1, parties)