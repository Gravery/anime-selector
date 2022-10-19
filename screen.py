import pygame
from funcs import *
ANIMES_LIST = "Lists/animes.txt"
MOVIES_LIST = "Lists/movies.txt"
SERIES_LIST = "Lists/series.txt"

pygame.init()
screen = pygame.display.set_mode((600, 400))

#Creation of buttons
def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, bg, (x, y, w , h))
    print(screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y)) 
 
#Menu with all interactions
def menu():

    bQuit = button(screen, (550, 10), "Quit", 30, "black on red")
    b0 = button(screen, (130, 10), "Watch Selector", 60, "white on red")
    b1 = button(screen, (20, 150), "Anime", 50, "white on green")
    b2 = button(screen, (240, 150), "Movie", 50, "white on green")
    b3 = button(screen, (460, 150), "Series", 50, "white on green")

    bAdd1 = button(screen, (50, 210), "Add", 30, "white on blue")
    bAdd2 = button(screen, (270, 210), "Add", 30, "white on blue")
    bAdd3 = button(screen, (490, 210), "Add", 30, "white on blue")

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #Check when you click if the coordinates of the pointer are in the rectangle of the buttons
                if bQuit.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit()
                elif b1.collidepoint(pygame.mouse.get_pos()):
                    chooser(ANIMES_LIST, 'anime')
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    chooser(MOVIES_LIST, 'movie')
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    chooser(SERIES_LIST, 'serie')

                elif bAdd1.collidepoint(pygame.mouse.get_pos()):
                    add(ANIMES_LIST)
                elif bAdd2.collidepoint(pygame.mouse.get_pos()):
                    add(MOVIES_LIST)
                elif bAdd3.collidepoint(pygame.mouse.get_pos()):
                    add(SERIES_LIST)
        pygame.display.update()
 
menu()