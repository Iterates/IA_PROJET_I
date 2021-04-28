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
        # self.comp_array = np.zeros(220*220).reshape((220, 220))
        # self.comp_array[34:-36, 34:-36] = self.nparray

        self.form_area = np.count_nonzero(self.nparray)
        # self.form_area = np.count_nonzero(self.comp_array)
        self.centroid = self.centroid_function(self.nparray)
        self.radius = self.centroid_radius()
        # self.centroid = self.centroid_function(self.comp_array)
        self.circle_around_form = self.draw_circle_around_form()



    def area_function(self, array):
        return np.count_nonzero(array)

    #On recherche la somme de tous les points non-nuls divise par le nombre de points
    def centroid_function(self, array):
        coordx, coordy = np.meshgrid(np.arange(len(array[0,:])), np.arange(len(array[:,0])))
        x = np.sum(coordx * array)
        y = np.sum(coordy * array)
        ele = np.count_nonzero(array == 1)
        return y/ele, x/ele

    #dessine un cerle autour de l'image
    def draw_circle_around_form(self):
        col_mesh, row_mesh = np.meshgrid(np.arange(self.nparray.shape[1]), np.arange(self.nparray.shape[0]))
        return np.where(np.sqrt((row_mesh - self.centroid[0])**2 + (col_mesh - self.centroid[1])**2) <= self.radius, np.ones(self.nparray.shape), np.zeros(self.nparray.shape))

    def ext_form_area(self):
        return np.count_nonzero(self.circle_around_form) - self.form_area

    #calcul la plus grande distance à partir du centroid
    def centroid_radius(self):
        col_mesh, row_mesh = np.meshgrid(np.arange(self.nparray.shape[1]), np.arange(self.nparray.shape[0]))
        # return np.max(np.where(self.nparray, np.sqrt(pow((col_mesh - self.centroid[0]), 2) + pow((row_mesh - self.centroid[1]), 2)), np.zeros(self.nparray.shape)))
        return np.where(self.nparray, np.sqrt(pow((row_mesh - self.centroid[0]), 2) + pow((col_mesh - self.centroid[1]), 2)), np.zeros(self.nparray.shape))

    def knn_axe1(self):
        # return aire/perimetre**2
        pass

    def knn_axe2(self):
        return self.ext_form_area() / self.form_area

    def knn_axe3(self):
        # return
        pass

if __name__ == '__main__':
    # array = np.array([220,220], dtype = np.uint8)
    array = np.ones(150*150).reshape((150,150))
    ke = KlustEngine(array)
    print(ke.centroid)

