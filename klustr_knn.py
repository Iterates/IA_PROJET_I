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
        
        self.distances = self.calcul_distance(array, classify_pt)
        self.dict_etiquettes = dict(enumerate(labels, 0))
        self.distances_classees = np.argsort(self.distances)
        self.etiquettes_classees = np.take(np.array(self.dict_etiquettes), self.distances_classees)
        print(1)

    # calculer la distance entre tous les points et celui choisi
    def calcul_distance(self, array, classify_pt):
        # dist = np.array([])
        col_mesh, row_mesh = np.meshgrid(np.arange(array.shape[1]), np.arange(array.shape[0]))
        # for pt in array[0]:
        #     print(pt)
        #     np.append(dist, (np.sqrt(pt[0] - classify_pt[0]))**2 + (np.sqrt(pt[1] - classify_pt[1]))**2 + (np.sqrt(pt[1] - classify_pt[1]))**2)
        dist = np.sqrt(array[0] - classify_pt[0])**2 + (np.sqrt(array[1] - classify_pt[1]))**2 + (np.sqrt(array[1] - classify_pt[1]))**2
        return dist


        
    def knn_classifiy(self):
        pass

