import sys
sys.path.insert(0, '..')
import Leap
import pygame
import constants

controller = Leap.Controller()

from pygameWindow import PYGAME_WINDOW

global xMin, xMax, yMin, yMax
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

def Scale(var_to_scale, r1, r2, r3, r4):
 
    print(r1, r2)
    if r1 == r2:
        scaled_value = int((r1+r2)/2)
    else:
        old_range = r2-r1
        new_range = r4-r3
        
        scaled_value = (((var_to_scale - r1)*new_range)/old_range)+r3
    
    return(int(scaled_value))
    
def Handle_Frame(frame):
    global xMin, xMax, yMin, yMax

    hand = frame.hands[0]
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
    tip_coordinates = distalPhalanx.next_joint
    x = int(tip_coordinates[0])
    y = int(tip_coordinates[1])

    if x < xMin:
        xMin = x
    if x > xMax:
        xMax = x
    if y < yMin:
        yMin = y
    if y > yMax:
        yMax = y
        
    return(int(x), int(y))

pyWindow = PYGAME_WINDOW()

size = 15
x = 500
y = 250

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.event.get()
    pyWindow.Prepare()
    frame = controller.frame()
    handlist = frame.hands
    if (len(handlist) > 0):
        x,y = Handle_Frame(frame)
        x = Scale(x, xMax, xMin, 0, constants.windowWidth)
        y = Scale(y, yMax, yMin, constants.windowDepth, 0)
        print(x,y)
        pyWindow.Draw_Black_Circle(x,y, size)#pass
    #x,y = pyWindow.Perturb_Circle_Position(x,y)
    pyWindow.Reveal()
    
pygame.quit()