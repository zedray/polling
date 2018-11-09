import pygame, sys, os
from pygame.locals import *


def print_text(text_array):
    for i in range(0, len(text_array)):
        print text_array[i]


def print_array(start_x, start_y, game_font, screen, text_array):
    font_line_spacing = 20
    for i in range(0, len(text_array)):
        text_surface = game_font.render(text_array[i], True, (0, 0, 0))
        screen.blit(text_surface, (start_x, start_y + (font_line_spacing * i)))


def render_grid(grid):
    # Setup the space.
    size_in_pixels = 20
    spacing_in_pixels = 4
    x_offset_pixels = 33
    y_offset_pixels = 20
    line_thickness = 3

    # Draw the map
    # Initialize the game engine
    pygame.init()

    # Define the colors we will use in RGB format
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    UP = 120
    GREEN = (UP, 255, UP)
    BLUE = (UP, UP, 255)
    RED = (255, UP, UP)

    DARK_GREEN = (0, 255, 0)
    DARK_BLUE = (0, 0, 255)
    DARK_RED = (255, 0, 0)

    # Set the height and width of the screen
    size = [506, 253]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Model results")
    pygame.font.init()
    game_font = pygame.font.Font(os.path.join("fonts", 'Roboto-Black.ttf'), 15)

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                pygame.quit()
                return
            if event.type == KEYDOWN:
                done = True

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        for x in range(0, grid.size_x):
            for y in range(0, grid.size_y):
                square = grid.squares[x][y]
                color = GREEN
                if hasattr(square, 'party') and square.party == 0:
                      color = RED
                if hasattr(square, 'party') and square.party == 1:
                    color = BLUE
                local_x = x_offset_pixels + (size_in_pixels + spacing_in_pixels) * x
                local_y = y_offset_pixels + (size_in_pixels + spacing_in_pixels) * y
                pygame.draw.rect(screen, color, [
                    local_x,
                    local_y,
                    size_in_pixels,
                    size_in_pixels
                ])

                dark_color = BLACK
                if square.seat.party == 0:
                    dark_color = DARK_RED
                if square.seat.party == 1:
                    dark_color = DARK_BLUE
                if square.seat.party == 2:
                    dark_color = DARK_GREEN

                force_draw = False
                if square.seat == grid.rig_seat:
                    dark_color = DARK_GREEN
                if square == grid.rig_swap_square:
                    dark_color = DARK_GREEN
                    force_draw = True

                top_left = 1
                bottom_right = 3

                # Left
                if x == 0 or square.seat != grid.squares[x - 1][y].seat or force_draw:
                    pygame.draw.line(screen, dark_color,
                                     [local_x - line_thickness + top_left, local_y - line_thickness],
                                     [local_x - line_thickness + top_left, local_y + size_in_pixels + line_thickness - top_left],
                                     line_thickness)
                # Right
                if x == grid.size_x - 1 or square.seat != grid.squares[x + 1][y].seat or force_draw:
                    pygame.draw.line(screen, dark_color,
                                     [local_x + size_in_pixels + line_thickness - bottom_right, local_y - line_thickness],
                                     [local_x + size_in_pixels + line_thickness - bottom_right, local_y + size_in_pixels + line_thickness - top_left],
                                     line_thickness)
                # Up
                if y == 0 or square.seat != grid.squares[x][y - 1].seat or force_draw:
                    pygame.draw.line(screen, dark_color,
                                     [local_x - line_thickness, local_y - line_thickness + top_left],
                                     [local_x + size_in_pixels + line_thickness - top_left, local_y - line_thickness + top_left],
                                     line_thickness)
                # Down
                if y == grid.size_y - 1 or square.seat != grid.squares[x][y + 1].seat or force_draw  :
                    pygame.draw.line(screen, dark_color,
                                     [local_x - line_thickness, local_y + size_in_pixels + line_thickness - bottom_right],
                                     [local_x + size_in_pixels + line_thickness - top_left, local_y + size_in_pixels + line_thickness - bottom_right],
                                     line_thickness)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    #pygame.quit()
