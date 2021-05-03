import numpy as np
import time
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

    def perimeter_function(image):
        m_left = image[1:-1, 0:-2]
        m_center = image[1:-1, 1:-1]
        m_top = image[0:-2, 1:-1]
        m_right = image[1:-1, 2:]
        m_bottom = image[2:, 1:-1]
        temp_bottom = np.logical_and(m_center, np.logical_xor(m_bottom, m_center, dtype=np.uint8))
        temp_right = np.logical_and(m_center, np.logical_xor(m_right, m_center, dtype=np.uint8))
        temp_top = np.logical_and(m_center, np.logical_xor(m_top, m_center, dtype=np.uint8))
        temp_left = np.logical_and(m_center, np.logical_xor(m_left, m_center, dtype=np.uint8))
        return np.logical_or(temp_right, np.logical_or(temp_bottom, np.logical_or(temp_top, temp_left, dtype=np.uint8)))
    
    def extraire_coord(image):
        m_coord_x, m_coord_y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0])) 
        m_coord_x = m_coord_x[image == 1] + 1
        m_coord_y = m_coord_y[image == 1] + 1
        coord = np.empty((m_coord_x.shape[0], 2), dtype=np.uint16)    
        coord[:, 0] = m_coord_x
        coord[:, 1] = m_coord_y
        return coord

    def create_image(size):
        return np.zeros(size, dtype=np.uint8)

    def draw_circle_the_numpy_way(image, center, radius): # the matrix way!
        col_mesh, row_mesh = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
        image[:] = np.logical_or(image[:], (np.sqrt((row_mesh - center[0])**2 + (col_mesh - center[1])**2) <= radius).astype(np.uint8))

    def dist_moyenne_centre(image):
        m_coord_x, m_coord_y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0])) 
        centroid_x, centroid_y = centroid_function(image)[1], centroid_function(image)[0]
        return np.mean(np.sqrt((m_coord_x - centroid_x)**2 + (m_coord_y - centroid_y)**2))

    def centroid_function(array):
        coordx, coordy = np.meshgrid(np.arange(len(array[0,:])), np.arange(len(array[:,0])))
        x = np.sum(coordx * array)
        y = np.sum(coordy * array)
        ele = np.count_nonzero(array == 1)
        return y/ele, x/ele

    img = create_image((15, 15))

    draw_circle_the_numpy_way(img, (6, 6), 4)

    print(img)

    new_img = perimeter_function(img)
    x = extraire_coord(new_img)
    print(new_img * 1)
    print(np.sum(img))
    print(np.sum(new_img))
    x = dist_moyenne_centre(new_img)
    array_of_arrays = np.array([np.arange(16).reshape(4,4), np.arange(16).reshape(4,4), np.arange(16).reshape(4,4)])
    s = lambda arr : np.sum(arr)
    vect_s = np.vectorize(s, signature="(m,n)->()")
    sum_array = vect_s(array_of_arrays)
    print(array_of_arrays)
    print(sum_array)

    def d_print(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            function(*args, **kwargs)
        return wrapper


    def f_chrono(function):
        def wrapper(*args, **kwargs):
            start = time.time_ns()
            function(*args, **kwargs)
            end = time.time_ns()
            return print(end - start)
        return wrapper

    @f_chrono 
    @d_print
    def fonction(hh):
        print(hh)

    @f_chrono
    def sum_of_array(array):
        return np.sum(array)

    fonction("pp")
    sum_of_array(new_img)