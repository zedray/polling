# Import a library of functions called 'pygame'
from election import counter
from utils import preference_generator, grid_draw, seat_generator
from gerrymander import rigger
from model import map

rig_for_party = 0
rig_for_majority = 2

grid_draw.render_help()
grid = map.Grid()
preference_generator.fair_random_party(grid)
seat_generator.stupid_seat_maker(grid)
grid_draw.render_grid(grid)
counter.count_squares(grid)
counter.count_seats(grid)
grid_draw.render_grid(grid)

while grid.majority(rig_for_party) < rig_for_majority:
    grid_draw.render_score(grid, 'ELECTION RIGGING IN PROGRESS')
    grid_draw.render_grid(grid)
    rigger.rig(grid, rig_for_party)
    counter.count_squares(grid)
    counter.count_seats(grid)
    grid_draw.render_grid(grid)

    rigger.add(grid.rig_seat, grid.rig_swap_square)
    grid.rig_seat = None
    grid.rig_swap_square = None
    counter.count_squares(grid)
    counter.count_seats(grid)
    grid_draw.render_grid(grid)

grid_draw.render_score(grid, 'VICTORY!!')
grid_draw.render_grid(grid)
