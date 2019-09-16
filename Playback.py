"""

CS228: Human Computer Interaction

Deliverable 3: Drawing skeletons of hands with pyGame and LeapMotion

"""

import numpy as np
import pickle

from Reader import READER

DataReader = READER()
DataReader.Load_Data('userData')
