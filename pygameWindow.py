import pygame
#constants.width 

class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300,100))
        
    def Prepare(self):
        self.screen.fill((255,255,255))
        
    def Reveal(self):
        pygame.display.update()
    
    def Draw_Black_Circle(self, x,y):
        pygame.draw.circle(self.screen, (0,0,0), (x,y), 2)