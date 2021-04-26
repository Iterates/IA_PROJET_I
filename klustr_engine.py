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

def area_function(array):
    return np.count_nonzero(array)

#On recherche la somme de tous les points non-nuls divise par le nombre de points 
def centroid_function(array):
    coordx, coordy = np.meshgrid(np.arange(len(array[0,:])), np.arange(len(array[:,0])))
    x = np.sum(coordx * array)
    y = np.sum(coordy * array)
    ele = np.count_nonzero(array == 1)
    return x/ele, y/ele








