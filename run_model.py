# Import a library of functions called 'pygame'
from election import counter
from utils import preference_generator, grid_draw, seat_generator
from gerrymander import rigger
from model import map

grid = map.Grid()
preference_generator.fair_random_party(grid)
seat_generator.stupid_seat_maker(grid)
counter.count_squares(grid)
counter.count_seats(grid)

for i in range(0, 10):
    rigger.rig(grid, 1)
    counter.count_squares(grid)
    counter.count_seats(grid)

grid_draw.render_grid(grid)
