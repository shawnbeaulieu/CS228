import os
import time
import pickle
import constants
import numpy as np

from pygameWindow_Del03 import PYGAME_WINDOW

def Load_Pickle(filename):

    with open(filename, 'rb') as f:
        struct = pickle.load(f)
        
    return(struct)
    
class READER:

    def __init__(self):
    
        self.xMin = 10000.0
        self.xMax = -10000.0
        self.yMin = 10000.0
        self.yMax = -10000.0
        self.pygameWindow = PYGAME_WINDOW()
        
    def Load_Data(self, filename):
        path, dirs, files = next(os.walk(filename))
        self.numGestures = len(files)
        print(self.numGestures)
        for gesture in range(self.numGestures):
        
            self.pygameWindow.Prepare()
            print(gesture)
            gesture_data = Load_Pickle('{0}/gesture{1}.p'.format(filename, gesture))
            self.Draw_Gesture(gesture_data)
            self.pygameWindow.Reveal()
            time.sleep(1)
            
    def Adjust_Boundaries(self, coordinate, x=False, y=False, z=False):
    
        if x:
        
            if coordinate < self.xMin:
                self.xMin = coordinate
            if coordinate > self.xMax:
                self.xMax = coordinate
        elif y:
        
            if coordinate < self.yMin:
                self.yMin = coordinate
            if coordinate > self.yMax:
                self.yMax = coordinate
            
    def Draw_Gesture(self, gesture):
    
        for finger in range(5):
            self.Handle_Finger(gesture[finger, :, :])
    
    def Handle_Finger(self, finger):

        for bone_type in range(4):
            bone = self.Handle_Bone(finger, bone_type)

    def Handle_Bone(self, finger, bone_type):

        bone = finger[bone_type, :]
        base_x, base_y, base_z = bone[0], bone[1], bone[2]
        tip_x, tip_y, tip_z = bone[3], bone[4], bone[5]
       
        self.Adjust_Boundaries(base_x, x=True)
        base_x = self.Scale(base_x, self.xMax, self.xMin, 0, constants.windowWidth)
        self.Adjust_Boundaries(base_y, y=True)
        base_y = self.Scale(base_y, self.yMax, self.yMin, constants.windowWidth, 0)
        
        self.Adjust_Boundaries(tip_x, x=True)
        tip_x = self.Scale(tip_x, self.xMax, self.xMin, 0, constants.windowWidth)
        self.Adjust_Boundaries(tip_y, y=True)
        tip_y = self.Scale(tip_y, self.yMax, self.yMin, constants.windowWidth, 0)
    
        self.pygameWindow.Draw_Line(base_x, base_y, tip_x, tip_y, bone_type, color='green')
        
    def Scale(self, var_to_scale, r1, r2, r3, r4):
 
        if r1 == r2:
            scaled_value = int((r1+r2)/2)
        else:
            old_range = r2-r1
            new_range = r4-r3
        
            scaled_value = (((var_to_scale - r1)*new_range)/old_range)+r3
    
        return(int(scaled_value))
    