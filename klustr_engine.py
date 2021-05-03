# -------------------------------------------------------------
# Auteur  : Henri-Paul Bolduc
#           Ari Hotz-Garber
#           Gael Lane Lepine
# Cours   : 420-C52-IN - AI 1
# TP 1    : Analyse KNN des images
# Fichier : klustr_engine.py
# -------------------------------------------------------------

# Importation des modules
# -------------------------------------------------------------
import numpy as np
from klustr_utils import *
from db_credential import PostgreSQLCredential
from klustr_dao import PostgreSQLKlustRDAO
# -------------------------------------------------------------

# KlustEngine
# -------------------------------------------------------------
class KlustEngine():
    def __init__(self, nparrays):
        self.nparrays = np.where(np.logical_not([ndarray_from_qimage_argb32(qimage_argb32_from_png_decoding(img)) for img in nparrays]), 1, 0)

    def extraire_coord(self):
        x = []
        y = []
        z = []

        for i in self.nparrays:
            centroid = self.centroid_function(i)
            radius = self.centroid_radius(i, centroid)
            aire = self.area_function(i)
            perimetre = np.count_nonzero(self.perimeter_image(i) * 1)
            cercle = self.draw_circle_around_form(i, centroid, radius)
            aire_cerlce = self.area_function(cercle)
            
            x.append(self.knn_axe1(aire, perimetre))
            y.append(self.knn_axe2(aire, aire_cerlce))
            z.append(self.knn_axe3(self.perimeter_image(i) * 1, centroid))

        return x, y, z

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
    def draw_circle_around_form(self, image, centroid, radius):
        col_mesh, row_mesh = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
        return np.where(np.sqrt((row_mesh - centroid[0])**2 + (col_mesh - centroid[1])**2) <= radius, np.ones(image.shape), np.zeros(image.shape))

    #calcul la plus grande distance à partir du centroid
    def centroid_radius(self, image, centroid):
        col_mesh, row_mesh = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
        return np.max(np.where(image, np.sqrt(pow((row_mesh - centroid[0]), 2) + pow((col_mesh - centroid[1]), 2)), np.zeros(image.shape)))

    def radius_min(self, perimeter, centroid):
        col_mesh, row_mesh = np.meshgrid(np.arange(perimeter.shape[1]), np.arange(perimeter.shape[0]))
        return np.min(np.where(perimeter, np.sqrt(pow((row_mesh - centroid[0]), 2) + pow((col_mesh - centroid[1]), 2)), np.zeros(perimeter.shape)))

    def dist_moyenne_centre(self, perimeter, centroid):
        m_coord_x, m_coord_y = np.meshgrid(np.arange(perimeter.shape[1]), np.arange(perimeter.shape[0])) 
        return np.mean(np.sqrt((m_coord_x - centroid[0])**2 + (m_coord_y - centroid[1])**2))

    # calcul du perimetre
    def perimeter_image(self, image):
        m_left = image[1:-1, 0:-2]
        m_center = image[1:-1, 1:-1]
        m_top = image[0:-2, 1:-1]
        m_right = image[1:-1, 2:]
        m_bottom = image[2:, 1:-1]
        temp_bottom = np.logical_and(m_center, np.logical_xor(m_bottom, m_center))
        temp_right = np.logical_and(m_center, np.logical_xor(m_right, m_center))
        temp_top = np.logical_and(m_center, np.logical_xor(m_top, m_center))
        temp_left = np.logical_and(m_center, np.logical_xor(m_left, m_center))
        return np.logical_or(temp_right, np.logical_or(temp_bottom, np.logical_or(temp_top, temp_left)))


    def knn_axe1(self, area, perimeter):
        return (4 * np.pi * area) / perimeter**2

    def knn_axe2(self, area, area_circle):
        return area / area_circle

    def knn_axe3(self, image, centroid):
        return self.dist_moyenne_centre(image, centroid) / self.centroid_radius(image, centroid)
# -------------------------------------------------------------

