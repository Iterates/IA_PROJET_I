from klustr_engine import *
import numpy as np

class Knn():
    def __init__(self, array, labels, classify_pt):
        self.distances = self.calcul_distance(array, classify_pt)
        self.labels = labels
        print(1)

    # calculer la distance entre tous les points et celui choisi
    def calcul_distance(self, array, classify_pt):
        # a = np.array([[6, 5, 2, 99, 100], [7, 5, 2, 88, 100], [8, 5, 2, 77, 100]])
        # pt2 = np.array([[0],[0],[0]])
        classify_pt = np.reshape(classify_pt, (array.shape[0],1))
        return np.sqrt((np.sum((array - classify_pt)**2, axis=0)))

        
    def knn_classifiy(self, k, distance):
        if k < 1:
            self.k = 1
        elif k > self.distances.shape[0]:
            self.k = self.distances.shape[0]
        else:
            self.k = k

        # self.dict_etiquettes = dict(enumerate(labels, 0))
        self.distances_classees = np.argsort(self.distances)
        self.etiquettes_classees = np.take(self.labels, self.distances_classees)
        self.k_voisins = self.etiquettes_classees[:self.k]
        self.label_gagnant, self.frequency = np.unique(self.k_voisins, return_inverse = True)
        counts = np.bincount(self.frequency)
        maxpos = counts.argmax()
        

        print(self.label_gagnant[maxpos])
        return self.label_gagnant[maxpos]

