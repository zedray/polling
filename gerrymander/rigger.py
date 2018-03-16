# Rig the election in favour of the given party.
def rig(grid, party):

    # Score seats by vote majority.
    seats_we_want = []
    print 'All seats'
    for seat in grid.seats:
        print 'Seat: ' + repr(seat.party) + ', majority:' + repr(seat.majority)
        if party != seat.party:
            seats_we_want.append(seat)

    print 'seats_we_want'
    seats_we_want.sort(key=lambda seat: seat.majority, reverse=True)
    for seat in seats_we_want:
        print 'Seat: ' + repr(seat.id) + ', majority:' + repr(seat.majority)



    # Find our closest loosing election.

    # ADDITIVE (vs REDUCTIVE) strategies.
    # Score squares with boundaries connecting to other seats.
    # Score square/connecting seats for loosing majorities.
    # Move square to this seat.


    # What we want:
    #  - Seats we don't like should win by a greater majority (push up).
    #  - Seats we want show be losing by a smaller margin.

    # Swap squares between two different seats.

    pass


