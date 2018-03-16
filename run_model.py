# Import a library of functions called 'pygame'
import utils
from election import counter
from utils import preference_generator, grid_draw, seat_generator
from gerrymander import rigger
from model import map

grid = map.Grid()
preference_generator.fair_random_party(grid)
#preference_generator.random_party(grid)
#preference_generator.geo_party(grid)
seat_generator.stupid_seat_maker(grid)
counter.count_squares(grid)
counter.count_seats(grid)
rigger.rig(grid, 1)

grid_draw.render_grid(grid)
