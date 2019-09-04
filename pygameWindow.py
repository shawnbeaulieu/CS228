import pygame
import random
#constants.width 

class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,500))
        
    def Prepare(self):
        self.screen.fill((255,255,255))
        
    def Reveal(self):
        pygame.display.update()
    
    def Draw_Black_Circle(self, x, y, size):
        pygame.draw.circle(self.screen, (0,0,0), (x,y), size)
        
    def Perturb_Circle_Position(self, x, y):
        fourSidedDieRoll = random.randint(1,4)
        if fourSidedDieRoll == 1:
            x -= 1
        elif fourSidedDieRoll == 2:
            x += 1
        elif fourSidedDieRoll == 3:
            y -= 1
        elif fourSidedDieRoll == 4:
            y += 1
            
        return(x,y)