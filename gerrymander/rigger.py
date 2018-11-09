from model import map
from election import counter


# Rig the election in favour of the given party.
def rig(grid, party):

    print '##### Lets try and rig the election... #####'
    # Score seats by vote majority.
    seats_we_want = []
    for seat in grid.seats:
        if party != seat.party:
            seats_we_want.append(seat)

    seats_we_want.sort(key=lambda seat: seat.majority, reverse=False)
    print 'Seats of the other party that we want...'
    for i in range(len(seats_we_want)):
        print '  ID {0} Party {1} Majority {2}'.format(seats_we_want[i].id, seats_we_want[i].party, seats_we_want[i].majority)

    # Find our closest loosing election.
    closest_loosing_seat = seats_we_want[0]
    print 'Closest loosing seat: ID {0} Party {1} Majority {2}'.format(seats_we_want[i].id, seats_we_want[i].party,
                                                   seats_we_want[i].majority)

    # Use an ADDITIVE, as opposed to a REDUCTIVE strategy.
    # Score squares with boundaries connecting to other seats.
    swap_squares = []
    for square in closest_loosing_seat.squares:
        adjacent_squares = map.Square.get_adjacent_squares(square, grid)
        for adjacent_square in adjacent_squares:
            if adjacent_square.party == party and adjacent_square.seat != square.seat:
                swap_square = map.SwapSquare()
                swap_square.square = square
                swap_square.swap_square = adjacent_square
                swap_squares.append(swap_square)

    swap_squares.sort(key=lambda swap_square: swap_square.majority(), reverse=False)
    for swap_square in swap_squares:
        print repr(swap_square.square.x) + 'x' + repr(swap_square.square.y) + ' next to '\
              + repr(swap_square.swap_square.x) + 'x' + repr(swap_square.swap_square.y)\
              + ' party' + repr(swap_square.swap_square.party)\
              + ' majority s' + repr(swap_square.square.seat.majority)\
              + ' majority o' + repr(swap_square.swap_square.seat.majority)

    # SwapSquare
    print 'pick_square'
    pick_square = swap_squares[0]
    print repr(pick_square.square.x) + 'x' + repr(pick_square.square.y) + ' next to '\
          + repr(pick_square.swap_square.x) + 'x' + repr(pick_square.swap_square.y)
    print 'from majority:' + repr(pick_square.square.seat.majority) \
          + ' to majority:' + repr(pick_square.swap_square.seat.majority)

    # Move square to this seat.
    grid.rig_seat = pick_square.square.seat
    grid.rig_swap_square = pick_square.swap_square

    # What we want:
    #  - Seats we don't like should win by a greater majority (push up).
    #  - Seats we want show be losing by a smaller margin.

    # Swap squares between two different seats.


def add(seat, square):
    if not isinstance(seat, map.Seat):
        print ('Not Seat')
    if not isinstance(square, map.Square):
        print ('Not Square')
    seat.squares.append(square)
    square.seat = seat
