import pickle
import numpy as np

def Load_Pickle(filename):

    with open(filename, 'rb') as f:
        struct = pickle.load(f)
        
    return(struct)
    
class READER:

    def __init__(self):
        pass
    def Load_Data(self, filename):
        return(Load_Pickle(filename))