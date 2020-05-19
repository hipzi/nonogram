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
HIJAU = (149, 221, 218)

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
                level_menu()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                # options()

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

def level_menu():
    click = False
    running = True
    while running:
        # click = False
        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        # Image
        menu = pygame.image.load("Menu/Level.png")
        menu_back = pygame.image.load("Menu/Back.png")
        menu_1 = pygame.image.load("Menu/Level_1.png")
        menu_2 = pygame.image.load("Menu/Level_2.png")
        screen.blit(menu, (0, 0))

        back = screen.blit(menu_back, (36, 50, 20, 20))
        level_1 = screen.blit(menu_1, (36, 172, 10, 10))
        level_2 = screen.blit(menu_2, (150, 172, 10, 10))
        
        if back.collidepoint((mx, my)):
            if click:
                main_menu()
        if level_1.collidepoint((mx, my)):
            if click:
                level1()
        if level_2.collidepoint((mx, my)):
            if click:
                level2()

        # click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)
def displayDone():
    click = False
    running = True
    while running:
        screen.fill(HIJAU)

        mx, my = pygame.mouse.get_pos()

        menu_back = pygame.image.load("Menu/finish-back2.png")
        
        back = screen.blit(menu_back, (145, 400, 20, 20))

        fontDone = pygame.font.SysFont("Arial", 60)
        text = fontDone.render("Finished", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        
        if back.collidepoint((mx, my)):
            if click:
                level_menu()

        # click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(text, [text_x, text_y])

        pygame.display.update()
        clock.tick(60)

def level1():
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Array Kosongan
    arrayKosong = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Cek kemungkinan contraint terpenuhi atau tidak
    def gridChecker(grids, array):
        print('Grids:', grids)
        print('Array:', array)
        
        if grids != array:
            for i in range(10):
                if (grids[i] == 1 or grids[i] == 2) and array[i] == 0:
                    return 0
        
        return 1

    def checkOne (grid, clue):
        awal = arrayKosong.copy()
        
        startA = 0
        while (startA + clue[0] <= 10):
            temp1 = awal.copy()
            
            i = startA
            while (i < startA + clue[0]):
                temp1[i] = 1
                i = i + 1
            
            status = gridChecker(grid, temp1)
            print(status)
            if status == 1: break

            startA = startA + 1
            print('-----', startA)
        
        return status

    # Cek jika clue ada 2
    def checkTwo (grid, clue):
        awal = arrayKosong.copy()

        startA = 0
        while(startA + sum(clue) < 10):
            temp1 = awal.copy()
            
            i = startA
            while (i < startA + clue[0]):
                temp1[i] = 1
                i = i + 1
            
            x = 1
            while (x + startA + sum(clue) <= 10):
                startB = x + startA + clue[0]
                temp2 = temp1.copy()

                j = startB
                while (j < startB + clue[1]):
                    temp2[j] = 1
                    j = j + 1
                
                x = x + 1
                status = gridChecker(grid, temp2)
                print(status)
                if status == 1: break
        
            if status == 1: break
            startA = startA + 1
            print('-----', startA)
        
        return status

    # Cek jika clue ada 3
    def checkThree (grid, clue):
        
        awal = arrayKosong.copy()
        print(clue, '\n')
        
        startA = 0
        while(startA + sum(clue) + 1 < 10):
            temp1 = awal.copy()
            
            i = startA
            while (i < startA + clue[0]):
                temp1[i] = 1
                i = i + 1
            
            x = 1
            while (x + startA + sum(clue) + 1 <= 10):
                startB = x + startA + clue[0]
                temp2 = temp1.copy()
                
                j = startB
                while (j < startB + clue[1]):
                    temp2[j] = 1
                    j = j + 1
                
                y = 1
                while (y + startB + clue[1] + clue[2] <= 10):
                    startC = y + startB + clue[1]
                    
                    temp3 = temp2.copy()
                    
                    k = startC
                    while (k < startC + clue[2]):
                        temp3[k] = 1
                        k = k + 1
                    
                    y = y + 1
                    status = gridChecker(grid, temp3)
                    print(status)
                    if status == 1: break
                    
                x = x + 1
                if status == 1: break
            
            if status == 1: break
            startA = startA + 1
            print('-----', startA)
        
        return status

    def checkLen (grid, clue):
        if len(clue) == 1: hasil = checkOne(grid, clue)
        elif len(clue) == 2: hasil = checkTwo(grid, clue)
        elif len(clue) == 3: hasil = checkThree(grid, clue)

        return hasil

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 25
    HEIGHT = 25
    
    # This sets the margin between each cell
    MARGIN = 3

    # Level 1
    level1_Img = pygame.image.load("Level/Level-1.jpg").convert()
    level1 = [ [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ]

    level1_Baris = [ [2, 2], [6],
                    [10], [1, 2, 1],
                    [1, 2, 1], [1, 2, 1],
                    [10], [1, 2, 1],
                    [1, 2, 1], [10] ]

    level1_Kolom = [ [8], [1, 1, 1],
                    [3, 1, 1], [3, 1, 1],
                    [9], [9],
                    [3, 1, 1], [3, 1, 1],
                    [1, 1, 1], [8] ]

    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(10):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(10):
            grid[row].append(0)  # Append a cell

    gridCopy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
                    if grid[row][column] == 0: grid[row][column] = 1
                    elif grid[row][column] == 1 or grid[row][column] == 2: grid[row][column] = 0
                    print("Click ", pos, "Grid coordinates: ", row, column)

                    hasilBaris = checkLen(grid[row], level1_Baris[row])
                    
                    for i in range(10):
                        gridCopy[i] = grid[i][column]
                    print(gridCopy)

                    hasilKolom = checkLen(gridCopy, level1_Kolom[column])
                        
                    print('HASIL -->', hasilBaris, hasilKolom)
                    if hasilBaris == 0 or hasilKolom == 0:
                        if grid[row][column] == 0: grid[row][column] = 0
                        else: grid[row][column] = 2
                    elif hasilBaris == 1 and hasilKolom == 1:
                        for i in range(10):
                            if grid[row][i] == 2:
                                for j in range(10):
                                    gridCopy[j] = grid[j][i]
                                print(gridCopy)
                                hasilKolom1 = checkLen(gridCopy, level1_Kolom[i])
                                if hasilKolom1 == 1: grid[row][i] = 1
                            if grid[i][column] == 2:
                                hasilBaris1 = checkLen(grid[i], level1_Baris[i])
                                if hasilBaris1 == 1: grid[i][column] = 1


        # Set the screen background
        screen.fill(WHITE)
        screen.blit(level1_Img, (0, 0))

        pygame.draw.rect(screen, BLACK, [90, 210, 283, 283])

        # Draw the grid
        for row in range(10):
            for column in range(10):
                color = WHITE
                if grid[row][column] == 1: color = LETTUCE
                elif grid[row][column] == 2: color = RED
                pygame.draw.rect(screen, color, [90 + (MARGIN + WIDTH) * column + MARGIN,
                                210 + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT] )

        # Jika sudah(?)
        if level1 == grid:
            displayDone()
        
        # Limit to 60 frames per second
        clock.tick(60)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

def level2():
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Array Kosongan
    arrayKosong = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Cek kemungkinan contraint terpenuhi atau tidak
    def gridChecker(grids, array):
        print('Grids:', grids)
        print('Array:', array)
        
        if grids != array:
            for i in range(10):
                if (grids[i] == 1 or grids[i] == 2) and array[i] == 0:
                    return 0
        
        return 1

    def checkOne (grid, clue):
        awal = arrayKosong.copy()
        
        startA = 0
        while (startA + clue[0] <= 10):
            temp1 = awal.copy()
            
            i = startA
            while (i < startA + clue[0]):
                temp1[i] = 1
                i = i + 1
            
            status = gridChecker(grid, temp1)
            print(status)
            if status == 1: break

            startA = startA + 1
            print('-----', startA)
        
        return status

    # Cek jika clue ada 2
    def checkTwo (grid, clue):
        awal = arrayKosong.copy()

        startA = 0
        while(startA + sum(clue) < 10):
            temp1 = awal.copy()
            
            i = startA
            while (i < startA + clue[0]):
                temp1[i] = 1
                i = i + 1
            
            x = 1
            while (x + startA + sum(clue) <= 10):
                startB = x + startA + clue[0]
                temp2 = temp1.copy()

                j = startB
                while (j < startB + clue[1]):
                    temp2[j] = 1
                    j = j + 1
                
                x = x + 1
                status = gridChecker(grid, temp2)
                print(status)
                if status == 1: break
        
            if status == 1: break
            startA = startA + 1
            print('-----', startA)
        
        return status

    def checkLen (grid, clue):
        if len(clue) == 1: hasil = checkOne(grid, clue)
        elif len(clue) == 2: hasil = checkTwo(grid, clue)
        elif len(clue) == 3: hasil = checkThree(grid, clue)

        return hasil

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 25
    HEIGHT = 25
    
    # This sets the margin between each cell
    MARGIN = 3

    # Level 2
    level2_Img = pygame.image.load("Level/Level-2.png").convert()
    level2 = [ [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0] ]

    level2_Baris = [ [2, 1], [5],
                    [6], [8],
                    [10], [6],
                    [2, 2], [2, 2],
                    [2, 2], [6] ]

    level2_Kolom = [ [1], [2],
                    [8], [9],
                    [6, 1], [6, 1],
                    [9], [10],
                    [2], [1] ]

    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(10):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(10):
            grid[row].append(0)  # Append a cell

    gridCopy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
                    if grid[row][column] == 0: grid[row][column] = 1
                    elif grid[row][column] == 1 or grid[row][column] == 2: grid[row][column] = 0
                    print("Click ", pos, "Grid coordinates: ", row, column)

                    hasilBaris = checkLen(grid[row], level2_Baris[row])
                    
                    for i in range(10):
                        gridCopy[i] = grid[i][column]
                    print(gridCopy)

                    hasilKolom = checkLen(gridCopy, level2_Kolom[column])
                        
                    print('HASIL -->', hasilBaris, hasilKolom)
                    if hasilBaris == 0 or hasilKolom == 0:
                        if grid[row][column] == 0: grid[row][column] = 0
                        else: grid[row][column] = 2
                    elif hasilBaris == 1 and hasilKolom == 1:
                        for i in range(10):
                            if grid[row][i] == 2:
                                for j in range(10):
                                    gridCopy[j] = grid[j][i]
                                print(gridCopy)
                                hasilKolom1 = checkLen(gridCopy, level2_Kolom[i])
                                if hasilKolom1 == 1: grid[row][i] = 1
                            if grid[i][column] == 2:
                                hasilBaris1 = checkLen(grid[i], level2_Baris[i])
                                if hasilBaris1 == 1: grid[i][column] = 1


        # Set the screen background
        screen.fill(WHITE)
        screen.blit(level2_Img, (0, 0))

        pygame.draw.rect(screen, BLACK, [90, 210, 283, 283])

        # Draw the grid
        for row in range(10):
            for column in range(10):
                color = WHITE
                if grid[row][column] == 1: color = LETTUCE
                elif grid[row][column] == 2: color = RED
                pygame.draw.rect(screen, color, [90 + (MARGIN + WIDTH) * column + MARGIN,
                                210 + (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT] )

        # Jika sudah(?)
        if level2 == grid:
            displayDone()
        
        # Limit to 60 frames per second
        clock.tick(60)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

main_menu()