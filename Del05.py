import sys
sys.path.insert(0, '..')

import Leap
import pickle
import pygame
import constants

import numpy as np

from pygameWindow_Del03 import PYGAME_WINDOW

def Pickler(data, filename):
    p = pickle.Pickler(open("{0}.p".format(filename), 'wb'))
    p.fast = True
    p.dump(data)

class Capture_Hands:
    def __init__(self):
    
        self.numberOfGestures = 1000
        self.gestureIndex = 0
    
        self.controller = Leap.Controller()
        self.pyWindow = PYGAME_WINDOW()
        
        self.xMin = 10000.0
        self.xMax = -10000.0
        self.yMin = 10000.0
        self.yMax = -10000.0
                
        self.previousNumberOfHands = 0
        self.currentNumberOfHands = 0
        self.Recording = False
        self.waiting2record = False
        
        self.record_counter = 0
        
        self.gestureData = np.zeros((5,4,6, self.numberOfGestures), dtype='float32')
                
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
        
        self.Recording_Is_Ending()
        
        for f in range(len(fingers)):
            self.Handle_Finger(fingers[f], f)
        
        if self.currentNumberOfHands == 2:#self.waiting2record == False and self.Recording == True:
        
            #self.Save_Gesture()
            
            self.gestureIndex += 1
            if self.gestureIndex == self.numberOfGestures:
                self.Save_Gesture()
                #print(self.gestureIndex)
                #print(self.gestureData[:,:,:,0])
                print(self.gestureData[:,:,:,99])
                exit(0)
        
    def Handle_Finger(self, finger, f_index):

        for bone_type in range(4):
            bone = self.Handle_Bone(finger, bone_type, f_index)

    def Handle_Bone(self, finger, bone_type, f_index):

        bone = finger.bone(bone_type)
    
        base = bone.prev_joint
        base_x, base_y, base_z, b_x, b_y, b_z = self.Handle_Vector_From_Leap(base)
    
        tip = bone.next_joint
        tip_x, tip_y, tip_z, t_x, t_y, t_z = self.Handle_Vector_From_Leap(tip)
        
        if self.currentNumberOfHands == 2: #self.waiting2record == False and self.Recording == True:
            self.gestureData[f_index, bone_type, :, self.gestureIndex] = [b_x, b_y, b_z, t_x, t_y, t_z]
            
        if self.currentNumberOfHands == 1:
            color = 'green'
        elif self.currentNumberOfHands == 2:
            color = 'red'
    
        self.pyWindow.Draw_Line(base_x, base_y, tip_x, tip_y, bone_type, color)
        
        return(bone)

    def Handle_Vector_From_Leap(self, vector):

        self.x = int(vector[0]*-1.0) 
        self.y = int(vector[2])
        self.z = int(vector[1])
    
        if self.x < self.xMin:
            self.xMin = self.x
        if self.x > self.xMax:
            self.xMax = self.x
        if self.y < self.yMin:
            self.yMin = self.y
        if self.y > self.yMax:
            self.yMax = self.y

        unscaled_x = self.x
        unscaled_y = self.y
        unscaled_z = self.z
        
        self.x = self.Scale(self.x, self.xMax, self.xMin, 0, constants.windowWidth)
        self.y = self.Scale(self.y, self.yMax, self.yMin, constants.windowWidth, 0)    
    
        return(self.x, self.y, self.z, unscaled_x, unscaled_y, unscaled_z)

    def Recording_Is_Ending(self):
    
        if self.currentNumberOfHands == 1 and self.previousNumberOfHands == 2:
            self.waiting2record = False
            self.Recording = True
        else:
            self.waiting2record = True
            self.Recording = False
    
    def Save_Gesture(self):
        Pickler(self.gestureData, "userData/gesture")    #{0}".format(self.record_counter))
        self.record_counter += 1
 
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
                self.previousNumberOfHands = self.currentNumberOfHands
                self.currentNumberOfHands = len(handlist)
                self.Handle_Frame(frame)
                
            else:
                self.previousNumberOfHands = self.currentNumberOfHands
                self.currentNumberOfHands = 0
                
            self.pyWindow.Reveal()
    
        pygame.quit()