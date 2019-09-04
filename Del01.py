import pygame
from pygameWindow import PYGAME_WINDOW

pyWindow = PYGAME_WINDOW()

size = 25
x = 500
y = 250

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.event.get()
    pyWindow.Prepare()
    pyWindow.Draw_Black_Circle(x,y, size)#pass
    x,y = pyWindow.Perturb_Circle_Position(x,y)
    pyWindow.Reveal()
    
pygame.quit()