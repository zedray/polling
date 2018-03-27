import pygame


def render_grid(grid):
    # Setup the space.
    sizeInPixels = 20
    spacingInPixels = 8
    xOffsetPixels = 50
    yOffsetPixels = 50

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
    size = [800, 800]
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
                done = True  # Flag that we are done so we exit this loop

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
                local_x = xOffsetPixels + (sizeInPixels + spacingInPixels) * x
                local_y = yOffsetPixels + (sizeInPixels + spacingInPixels) * y
                pygame.draw.rect(screen, color, [
                    local_x,
                    local_y,
                    sizeInPixels,
                    sizeInPixels
                ])

                # Draw 4 lines around the square.
                hs = spacingInPixels / 2

                dark_color = DARK_GREEN
                if square.seat.party == 0:
                    dark_color = DARK_RED
                if square.seat.party == 1:
                    dark_color = DARK_BLUE

                # Left
                if x == 0 or square.seat != grid.squares[x - 1][y].seat:
                    pygame.draw.line(screen, dark_color,
                                     [local_x - hs, local_y - hs],
                                     [local_x - hs, local_y + sizeInPixels + hs],
                                     4)
                # Right
                if x == grid.size_x - 1 or square.seat != grid.squares[x + 1][y].seat:
                    pygame.draw.line(screen, dark_color,
                                     [local_x + sizeInPixels - hs, local_y - hs],
                                     [local_x + sizeInPixels - hs, local_y + sizeInPixels + hs],
                                     4)
                # Up
                if y == 0 or square.seat != grid.squares[x][y - 1].seat:
                    pygame.draw.line(screen, dark_color,
                                     [local_x - hs, local_y - hs],
                                     [local_x + sizeInPixels + hs, local_y - hs],
                                     4)
                # Down
                if y == grid.size_y - 1 or square.seat != grid.squares[x][y + 1].seat:
                    pygame.draw.line(screen, dark_color,
                                     [local_x - hs, local_y + sizeInPixels + hs],
                                     [local_x + sizeInPixels + hs, local_y + sizeInPixels + hs],
                                     4)


                # HORZ
                #pygame.draw.line(screen, BLACK, [local_x - hs, local_y - hs], [local_x + sizeInPixels + hs, local_y - hs], 4)
                #pygame.draw.line(screen, BLACK, [local_x - hs, local_y + sizeInPixels + hs], [local_x + sizeInPixels + hs, local_y + sizeInPixels + hs], 4)

                # VERT
                #pygame.draw.line(screen, BLACK, [local_x - hs, local_y - hs], [local_x - hs, local_y + sizeInPixels + hs], 4)
                #pygame.draw.line(screen, BLACK, [local_x + sizeInPixels - hs, local_y - hs], [local_x + sizeInPixels - hs, local_y + sizeInPixels + hs], 4)


        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()