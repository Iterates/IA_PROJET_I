import numpy as np
from klustr_feed import *

#Metriques
#Centroide
#Perimetre
#Tracer cercle
#Aire
#Padder les matrices
#Encapsuler K(s'assurer que minimum = 1)
#Notion de distance minimale
#Dimensions nombre d'images

class KlustEngine():
    def __init__(self, nparray):
        self.nparray = nparray
        self.comp_array = np.ones(220*220).reshape((220, 220))
        self.form_area = np.count_nonzero(self.nparray)
        self.centroid = self.centroid_function(self.nparray)




    def area_function(self, array):
        return np.count_nonzero(array)

    #On recherche la somme de tous les points non-nuls divise par le nombre de points 
    def centroid_function(self, array):
        coordx, coordy = np.meshgrid(np.arange(len(array[0,:])), np.arange(len(array[:,0])))
        x = np.sum(coordx * array)
        y = np.sum(coordy * array)
        ele = np.count_nonzero(array == 1)
        return x/ele, y/ele

    #dessine un cerle autour de l'image
    def draw_circle_around_form(self, array):
        pass

    #calcul la plus grande distance à partir du centroid
    def centroid_radius(self):
        pass






if __name__ == '__main__':
    # array = np.array([220,220], dtype = np.uint8)
    array = np.ones(150*150).reshape((150,150))
    ke = KlustEngine(array)
    print(ke.centroid)

