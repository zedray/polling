# Import a library of functions called 'pygame'
from election import counter
from utils import preference_generator, grid_draw, seat_generator
from gerrymander import rigger
from model import map

grid = map.Grid()
preference_generator.fair_random_party(grid)
seat_generator.stupid_seat_maker(grid)
grid_draw.render_grid(grid)
counter.count_squares(grid)
counter.count_seats(grid)
grid_draw.render_grid(grid)
grid_draw.render_score(grid, 'ELECTION RIGGING IN PROGRESS')

for i in range(0, 1):
    rigger.rig(grid, 1)
    counter.count_squares(grid)
    counter.count_seats(grid)
    grid_draw.render_grid(grid)

    rigger.add(grid.rig_seat, grid.rig_swap_square)
    grid.rig_seat = None
    grid.rig_swap_square = None
    counter.count_squares(grid)
    counter.count_seats(grid)
    grid_draw.render_grid(grid)
    grid_draw.render_score(grid, 'NOT GOOD ENOUGH')

grid_draw.render_grid(grid)
