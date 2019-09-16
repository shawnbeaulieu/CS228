"""

CS228: Human Computer Interaction

Deliverable 3: Drawing skeletons of hands with pyGame and LeapMotion

"""

import os

from Capture_Hands import Capture_Hands

def make_directory(pathway):
    try:
        os.makedirs(pathway)
    except OSError:
        if not os.path.isdir(pathway):
            raise


make_directory("userData")

Hand_Captue_Class = Capture_Hands()
print("Initializing Hand Capture: Please engage the LeapMotion Device")
Hand_Captue_Class.Run_Forever()
print("Hand capture session has ended")