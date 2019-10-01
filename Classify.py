import pickle
import numpy as np


with open("userData/gesture.p", 'r') as dataFile:
    data = pickle.load(dataFile)
    
print(data.shape)