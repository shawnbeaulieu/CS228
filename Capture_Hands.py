import sys
sys.path.insert(0, '..')

import Leap
import pygame
import constants

from pygameWindow_Del03 import PYGAME_WINDOW

class Capture_Hands:
    def __init__(self):
    
        self.controller = Leap.Controller()
        self.pyWindow = PYGAME_WINDOW()
        
        self.xMin = 10000.0
        self.xMax = -10000.0
        self.yMin = 10000.0
        self.yMax = -10000.0
                
        self.numberOfHands = 0
                
    def Scale(self, var_to_scale, r1, r2, r3, r4):
 
        if r1 == r2:
            scaled_value = int((r1+r2)/2)
        else:
            old_range = r2-r1
            new_range = r4-r3
        
            scaled_value = (((var_to_scale - r1)*new_range)/old_range)+r3
    
        return(int(scaled_value))
    
    def Handle_Frame(self, frame):

        hand = frame.hands[0]
        fingers = hand.fingers
        for finger in fingers:
            self.Handle_Finger(finger)

    def Handle_Finger(self, finger):

        for bone_type in range(4):
            bone = self.Handle_Bone(finger, bone_type)

    def Handle_Bone(self, finger, bone_type):

        bone = finger.bone(bone_type)
    
        base = bone.prev_joint
        base_x, base_y = self.Handle_Vector_From_Leap(base)
    
        tip = bone.next_joint
        tip_x, tip_y = self.Handle_Vector_From_Leap(tip)
    
        self.pyWindow.Draw_Black_Line(base_x, base_y, tip_x, tip_y, bone_type)
        
        return(bone)

    def Handle_Vector_From_Leap(self, vector):

        self.x = int(vector[0]*-1.0) 
        self.y = int(vector[2])
    
        if self.x < self.xMin:
            self.xMin = self.x
        if self.x > self.xMax:
            self.xMax = self.x
        if self.y < self.yMin:
            self.yMin = self.y
        if self.y > self.yMax:
            self.yMax = self.y

        self.x = self.Scale(self.x, self.xMax, self.xMin, 0, constants.windowWidth)
        self.y = self.Scale(self.y, self.yMax, self.yMin, constants.windowWidth, 0)    
    
        return(self.x,self.y)

    def Run_Forever(self):
    
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.event.get()
            self.pyWindow.Prepare()
            frame = self.controller.frame()
            handlist = frame.hands
            if (len(handlist) > 0):
                self.numberOfHands = len(handlist)
                self.Handle_Frame(frame)

            self.pyWindow.Reveal()
    
        pygame.quit()