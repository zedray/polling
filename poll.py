# Import a library of functions called 'pygame'
import pygame

# Setup the space.
sizeX = 10
sizeY = 10
sizeInPixels = 50
spacingInPixels = 10
xOffsetPixels = 50
yOffsetPixels = 50
totalSize = sizeX * sizeY

# Print the status
print 'Grid Size - x:' + repr(sizeX) + ' y:' + repr(sizeY) + '  Total:' + repr(totalSize)

# Draw the map
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [800, 800]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

class Square:
    def __init__(self):
        self.party = 0
        self.x = 0
        self.y = 0


squares = [[0 for x in range(sizeX)] for y in range(sizeY)]
for x in range(0, sizeX):
    for y in range(0, sizeY):
        square = Square()
        square.x = x
        square.y = y
        squares[x][y]= square

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draw on the screen a GREEN line from (0,0) to (50.75)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)

    # Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)

    for x in range(0, sizeX):
        for y in range(0, sizeY):
            s = squares[x][y]
            print 'Square - x:' + repr(s.x) + ' y:' + repr(s.y) + '  Party:' + repr(s.party)

            pygame.draw.rect(screen, GREEN, [
                xOffsetPixels + (sizeInPixels + spacingInPixels) * x,
                yOffsetPixels + (sizeInPixels + spacingInPixels) * y,
                sizeInPixels,
                sizeInPixels
            ])

    # Draw a solid rectangle
    pygame.draw.rect(screen, GREEN, [150, 10, 50, 20])

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()