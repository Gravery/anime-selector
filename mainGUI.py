from re import A
import pygame
from funcs import *
from inputBox import InputBox
from button import Button

ANIMES_LIST = "Lists/animes.txt"
MOVIES_LIST = "Lists/movies.txt"
SERIES_LIST = "Lists/series.txt"

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))
buttons =  pygame.sprite.Group()
input_box = InputBox(200, 250, 140, 32)

def close():
    pygame.quit()
    exit()

def creating():
    bQuit = Button(screen, (560, 10), "Quit", 25, "yellow on red", command= lambda: close())

    bAnime = Button(screen, (10, 100), "Anime", 55, "white on green", command= lambda: chooser(ANIMES_LIST, 'anime'))
    bMovie = Button(screen, (240, 100), "Movie", 55, "white on green", command= lambda: chooser(MOVIES_LIST, 'movie'))
    bSerie = Button(screen, (460, 100), "Serie", 55, "white on green", command=lambda: chooser(SERIES_LIST, 'serie'))

    bAddAnime = Button(screen, (10, 170), "Add", 30, "white on Blue", command= lambda: handle_add(ANIMES_LIST))
    bAddMovie = Button(screen, (240, 170), "Add", 30, "white on Blue", command= lambda: handle_add(MOVIES_LIST))
    bAddSerie = Button(screen, (460, 170), "Add", 30, "white on Blue", command= lambda: handle_add(SERIES_LIST))


    buttons.add(bQuit)
    buttons.add(bAnime)
    buttons.add(bMovie)
    buttons.add(bSerie)
    buttons.add(bAddAnime)
    buttons.add(bAddMovie)
    buttons.add(bAddSerie)


def handle_buttons():
    buttons.update()
    buttons.draw(screen)

def handle_add(path):
    name = input_box.getText()
    add(path, name)
    input_box.resetText()
    input_box.render()        

def main():
    creating()


    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            input_box.handle_event(event)
            input_box.update()
            screen.fill((30, 30, 30))
            input_box.draw(screen)

        handle_buttons()

        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()


main()