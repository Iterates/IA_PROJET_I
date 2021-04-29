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

if __name__ == "__main__":
    #TODO Inverser colonnes et rangees 
     
    data = np.array([10, 3, 4, 5, 6])
    #Extraire
    impair = data%2
    res = data[impair == 1]
    #Meshgrid



    def create_image(size):
        return np.zeros(size, dtype=np.uint8)

    def draw_circle_the_numpy_way(image, center, radius): # the matrix way!
        col_mesh, row_mesh = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
        image[:] = np.logical_or(image[:], (np.sqrt((row_mesh - center[0])**2 + (col_mesh - center[1])**2) <= radius).astype(np.uint8))

    img = create_image((15, 15))

    draw_circle_the_numpy_way(img, (6, 6), 4)

    print(img)

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

    
    new_img = perimeter_function(img)
    x = extraire_coord(new_img)
    print(new_img * 1)
    print(np.sum(img))
    print(np.sum(new_img))
    print(0)