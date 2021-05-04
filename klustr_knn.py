from klustr_engine import *
import numpy as np

class Knn():
    def __init__(self, array, labels, k, distance, classify_pt):
        if k < 1:
            self.k = 1
        elif k > array.shape[0]:
            self.k = array.shape[0]
        else:
            self.k = k
        
    def knn_classifiy(self):
        pass

