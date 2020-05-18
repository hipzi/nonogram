import pygame

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LETTUCE = (147, 206, 103)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [400, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("NONOGRAM")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Image
level1 = pygame.image.load("Level/Level-1.jpg").convert()

# Display Image
def displayImage(x, y):
    screen.blit(level1, (x, y))

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 25
HEIGHT = 25

# This sets the margin between each cell
MARGIN = 3

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:   # If user clicked close
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if 90 < pos[0] and pos[0] < 373 and 210 < pos[1] and pos[1] < 493:
                # Change the x/y screen coordinates to grid coordinates
                column = (pos[0] - 90) // (WIDTH + MARGIN)
                row = (pos[1] - 210) // (HEIGHT + MARGIN)
                # Set that location to one
                if grid[row][column] == 0:
                    grid[row][column] = 1
                elif grid[row][column] == 1:
                    grid[row][column] = 0
                print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(WHITE)
    screen.blit(level1, (0, 0))

    pygame.draw.rect(screen, BLACK, [90, 210, 283, 283])

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = LETTUCE
            pygame.draw.rect(screen, color, [90 + (MARGIN + WIDTH) * column + MARGIN,
                             210 + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT] )


    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()