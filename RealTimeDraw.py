import pygame
from pygameWindow import PYGAME_WINDOW

pyWindow = PYGAME_WINDOW()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.event.get()
    pyWindow.Prepare()
    pyWindow.Draw_Black_Circle(150,50)#pass
    pyWindow.Reveal()
    
pygame.quit()