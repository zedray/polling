import pygame, sys, os
from pygame.locals import *


def render_grid(grid):
    # Setup the space.
    size_in_pixels = 20
    spacing_in_pixels = 8
    x_offset_pixels = 5
    y_offset_pixels = 5
    line_thickness = 4

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

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
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


def print_text(x, y, game_font, screen, text):
    text_surface = game_font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (x, y))


def draw_bar(line_thickness, offset_x, offset_y, screen, score_a, score_b):
    BLACK = (0, 0, 0)
    DARK_BLUE = (0, 0, 255)
    DARK_RED = (255, 0, 0)
    bar_width = 475
    bar_height = 36
    pygame.draw.rect(screen, BLACK, (offset_x, offset_y, bar_width, bar_height), 0)
    total = score_a + score_b
    middle = (score_a * bar_width) / total
    pygame.draw.rect(screen, DARK_RED, (
    offset_x + line_thickness, offset_y + line_thickness, middle - line_thickness, bar_height - line_thickness * 2), 0)
    pygame.draw.rect(screen, DARK_BLUE, (
    offset_x + line_thickness + middle, offset_y + line_thickness, bar_width - middle - line_thickness * 2,
    bar_height - line_thickness * 2), 0)


def render_help():
    # Draw the map
    # Initialize the game engine
    pygame.init()

    # Define the colors we will use in RGB format
    WHITE = (255, 255, 255)

    # Set the height and width of the screen
    size = [506, 253]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Model results")
    pygame.font.init()

    help_image = pygame.image.load("images/help.png")
    help_image_rect = help_image.get_rect()

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()
                return
            if event.type == KEYDOWN:
                done = True

        # Clear the screen and set the screen background
        screen.fill(WHITE)
        screen.blit(help_image, help_image_rect)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

def render_score(grid, status_text):
    # Setup the space.
    line_thickness = 2

    # Draw the map
    # Initialize the game engine
    pygame.init()

    # Define the colors we will use in RGB format
    WHITE = (255, 255, 255)

    # Set the height and width of the screen
    size = [506, 253]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Model results")
    pygame.font.init()
    game_font = pygame.font.Font(os.path.join("fonts", 'Roboto-Black.ttf'), 30)

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()
                return
            if event.type == KEYDOWN:
                done = True

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        print_text(16, 23, game_font, screen, status_text)
        first_row = 85
        print_text(10, first_row, game_font, screen, repr(grid.results[0]))
        print_text(214, first_row, game_font, screen, 'Seats')
        print_text(445, first_row, game_font, screen, repr(grid.results[1]))
        second_row = 164
        print_text(10, second_row, game_font, screen, repr(100 * grid.votes[0] / grid.voters) + '%')
        print_text(210, second_row, game_font, screen, 'Votes')
        print_text(435, second_row, game_font, screen, repr(100 * grid.votes[1] / grid.voters) + '%')

        draw_bar(line_thickness, 12, 120, screen, grid.results[0], grid.results[1])
        draw_bar(line_thickness, 12, 196, screen, 100 * grid.votes[0] / grid.voters, 100 * grid.votes[1] / grid.voters)
        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
