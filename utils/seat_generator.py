import math
from model import map

def stupid_seat_maker(grid):
    seat_size = int(grid.total_size / grid.no_of_seats)
    width = int(math.sqrt(seat_size))
    height = int(seat_size / width)
    print 'To produce about ' + repr(grid.no_of_seats) + ' seats, we need a size of ' + repr(seat_size)\
          + ' squares, or roughly ' + repr(width) + 'x' + repr(height)

    seat_x = 0
    seat_y = 0
    for seat_id in range(0, grid.no_of_seats):
        seat = map.Seat()
        seat.id = seat_id
        for x in range(seat_x, min(seat_x + width, grid.size_x)):
            for y in range(seat_y, min(seat_y + height, grid.size_y)):
                square = grid.squares[x][y]
                square.seat = seat
                seat.squares.append(square)
        seat_x += width
        if seat_x >= grid.size_x:
            seat_x = 0
            seat_y += height
        grid.seats.append(seat)

    for seat in grid.seats:
        print 'Seat id:' + repr(seat.id) + ' has ' + repr(len(seat.squares)) + ' squares'
