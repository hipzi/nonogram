import pygame, sys
from pygame.locals import *

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

font = pygame.font.SysFont(None, 20)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Image
menu = pygame.image.load("Menu/Menu-1.png")

# Display Image
def displayImage(x, y):
    screen.blit(menu, (x, y))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# def blit_alpha(target, source, location, opacity):
#         x = location[0]
#         y = location[1]
#         temp = pygame.Surface((source.get_width(), source.get_height())).convert()
#         temp.blit(target, (-x, -y))
#         temp.blit(source, (0, 0))
#         temp.set_alpha(opacity)        
#         target.blit(temp, location)

# --- class ---
# click = False

# class GameState(object):

#     def __init__(self):
#         self.state = 'main_menu'

#     def main_menu(self):
#         screen.fill((0,0,0))
#         displayImage(0, 0)

#         mx, my = pygame.mouse.get_pos()

#         # Image
#         image_1 = pygame.image.load("Menu/Start.png")
#         image_2 = pygame.image.load("Menu/Quit.png")

#         button_1 = screen.blit(image_1, (25, 377, 20, 20))
#         button_2 = screen.blit(image_2, (25, 447, 20, 20))

#         if button_1.collidepoint((mx, my)):
#             if click:
#                 # game()
#                 # main()
#                 # pygame.quit()
#                 self.state = 'menu_level'
#         if button_2.collidepoint((mx, my)):
#             if click:
#                 pygame.quit()
#                 # main()

#         click = False
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#             if event.type == MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     click = True

#         pygame.display.update()
#         # clock.tick(60)
#     def level_menu(self):
#         screen.fill((0,0,0))

#         mx, my = pygame.mouse.get_pos()

#         # Image
#         menu = pygame.image.load("Menu/Level.png")
#         menu_back = pygame.image.load("Menu/Back.png")
#         menu_1 = pygame.image.load("Menu/Level_1.png")
#         screen.blit(menu, (0, 0))

#         level_1 = screen.blit(menu_1, (0, 0, 10, 10))
#         # back = screen.blit(menu_back, (25, 377, 20, 20))
        
#         if level_1.collidepoint((mx, my)):
#             if click:
#                 main()
#         # if back.collidepoint((ax, ay)):
#         #     if click:
#         #         pygame.quit()

#         click = False
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#             # if event.type == MOUSEBUTTONDOWN:
#             #     # if event.button == 1:
#             #         # click = True
#             #         self.state = 'main_menu'

#         pygame.display.update()

#     def state_manager(self):
#         if self.state == 'main_menu':
#             self.main_menu()
#         if self.state == 'level_menu':
#             self.level_menu()
def main_menu():
    click = False
    while True:

        screen.fill((0,0,0))
        displayImage(0, 0)

        mx, my = pygame.mouse.get_pos()

        # Image
        image_1 = pygame.image.load("Menu/Start.png")
        image_2 = pygame.image.load("Menu/Quit.png")

        button_1 = screen.blit(image_1, (25, 377, 20, 20))
        button_2 = screen.blit(image_2, (25, 447, 20, 20))

        if button_1.collidepoint((mx, my)):
            if click:
                # game()
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                # pygame.quit()
                main()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

# def game():
#     click = False
#     running = True
#     while True:
        # # click = False
        # screen.fill((0,0,0))

        # mx, my = pygame.mouse.get_pos()

        # # Image
        # menu = pygame.image.load("Menu/Level.png")
        # menu_back = pygame.image.load("Menu/Back.png")
        # menu_1 = pygame.image.load("Menu/Level_1.png")
        # screen.blit(menu, (0, 0))

        # level_1 = screen.blit(menu_1, (0, 0, 10, 10))
        # # back = screen.blit(menu_back, (25, 377, 20, 20))
        
        # if level_1.collidepoint((mx, my)):
        #     if click:
        #         main()
        # # if back.collidepoint((ax, ay)):
        # #     if click:
        # #         pygame.quit()

        # click = False
        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == KEYDOWN:
        #         if event.key == K_ESCAPE:
        #             # pygame.quit()
        #             # sys.exit()
        #             running = False
        #     if event.type == MOUSEBUTTONDOWN:
        #         if event.button == 1:
        #             click = True

        # pygame.display.update()
        # clock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

def main():
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
