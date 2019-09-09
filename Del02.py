
"""

CS228: Human Computer Interaction

Deliverable 2: Drawing skeletons of hands with pyGame and LeapMotion

"""

import sys
sys.path.insert(0, '..')
import Leap
import pygame
import constants

controller = Leap.Controller()

from pygameWindow import PYGAME_WINDOW

global xMin, xMax, yMin, yMax
xMin = 10000.0
xMax = -10000.0
yMin = 10000.0
yMax = -10000.0

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
    for finger in fingers:
        Handle_Finger(finger)

def Handle_Finger(finger):

    for bone_type in range(4):
        bone = Handle_Bone(finger, bone_type)

def Handle_Bone(finger, bone_type):

    bone = finger.bone(bone_type)
    
    base = bone.prev_joint
    base_x, base_y = Handle_Vector_From_Leap(base)
    
    tip = bone.next_joint
    tip_x, tip_y = Handle_Vector_From_Leap(tip)
    
    pyWindow.Draw_Black_Line(base_x, base_y, tip_x, tip_y, bone_type)
    return(bone)

def Handle_Vector_From_Leap(vector):
    global xMin, xMax, yMin, yMax

    x = int(vector[0]*-1.0)
    y = int(vector[2])
    
    if x < xMin:
        xMin = x
    if x > xMax:
        xMax = x
    if y < yMin:
        yMin = y
    if y > yMax:
        yMax = y

    x = Scale(x, xMax, xMin, 0, constants.windowWidth)
    y = Scale(y, yMax, yMin, constants.windowWidth, 0)    
    
    return(x,y)

pyWindow = PYGAME_WINDOW()

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
        Handle_Frame(frame)

    pyWindow.Reveal()
    
pygame.quit()