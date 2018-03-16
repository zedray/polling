from model import map
from election import counter


# Rig the election in favour of the given party.
def rig(grid, party):

    # Score seats by vote majority.
    seats_we_want = []
    #print 'All seats'
    for seat in grid.seats:
        #print 'Seat: ' + repr(seat.party) + ', majority:' + repr(seat.majority)
        if party != seat.party:
            seats_we_want.append(seat)

    #print 'seats_we_want'
    seats_we_want.sort(key=lambda seat: seat.majority, reverse=False)
    #for seat in seats_we_want:
        #print 'Seat: ' + repr(seat.id) + ', majority:' + repr(seat.majority)

    # Find our closest loosing election.
    closest_loosing_seat = seats_we_want[0]

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

    #print 'swap_square we can use'
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
    print repr(pick_square.square.x) + 'x' + repr(pick_square.square.y) + ' next to ' \
          + repr(pick_square.swap_square.x) + 'x' + repr(pick_square.swap_square.y)
    print 'from majority:' + repr(pick_square.square.seat.majority) \
          + ' to majority:' + repr(pick_square.swap_square.seat.majority)

    # Move square to this seat.
    __add(pick_square.square.seat, pick_square.swap_square)

    # What we want:
    #  - Seats we don't like should win by a greater majority (push up).
    #  - Seats we want show be losing by a smaller margin.

    # Swap squares between two different seats.

def __add(seat, square):
    seat.squares.append(seat)
    square.seat = seat
