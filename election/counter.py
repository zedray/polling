import random


def count_squares(grid):
    results = [0] * grid.no_of_parties
    for x in range(0, len(grid.squares)):
        for y in range(0, len(grid.squares[x])):
            square = grid.squares[x][y]
            if hasattr(square, 'party'):
                results[square.party] += 1

    # Print the status
    print 'Raw election results for ' + repr(grid.total_size) + ' voters'
    for i in range(0, len(results)):
        print 'Party:' + repr(i) + '  Total Votes:' + repr(results[i])\
              + '  Vote Share:' + repr(100 * results[i] / grid.total_size) + '%'


def count_seats(grid):
    results = [0] * grid.no_of_parties
    for seat in grid.seats:
        seat_results = [0] * grid.no_of_parties
        for square in seat.squares:
            if hasattr(square, 'party'):
                seat_results[square.party] += 1

        winner = __get_winer(seat_results)
        seat.party = winner
        seat.majority = max(0, 2 * seat_results[winner] - len(seat.squares))
        results[winner] += 1

        print 'Seat: ' + repr(seat.id) + ', votes:' + repr(seat_results[0]) + ' vs ' + repr(seat_results[1])\
              + ' winner:' + repr(winner)

    # Print the status.
    print 'Seat election results for ' + repr(grid.no_of_seats) + ' seats'
    for i in range(0, len(results)):
        print 'Party:' + repr(i) + '  Total Seats:' + repr(results[i]) + '  Share:' + repr(
            100 * results[i] / grid.no_of_seats) + '%  Majority:' + repr(max(0, 2 * results[i] - grid.no_of_seats))


def __get_winer(results):
    largest_party = -1
    largest_result = 0
    for i in range(0, len(results)):
        if results[i] == largest_result:
            # Election is a tie, so flip a coin
            if bool(random.getrandbits(1)):
                largest_party = i
                largest_result = results[i]
        elif results[i] > largest_result:
            largest_party = i
            largest_result = results[i]
    return largest_party
