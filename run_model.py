# Import a library of functions called 'pygame'
import utils
from utils import preference_generator, grid_draw
from model import map

grid = map.Grid()
utils.preference_generator.random_party(grid, 2)
utils.grid_draw.render_grid(grid)
