import numpy as np
# from klustr_feed import *
from klustr_utils import *
from db_credential import PostgreSQLCredential
from klustr_dao import PostgreSQLKlustRDAO

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
    def __init__(self, nparrays):
        # self.nparray = nparray
        # self.comp_array = np.zeros(220*220).reshape((220, 220))
        # self.comp_array[34:-36, 34:-36] = self.nparray
        self.nparrays = np.where(np.logical_not([ndarray_from_qimage_argb32(qimage_argb32_from_png_decoding(img)) for img in nparrays]), 1, 0)
        # f=np.vectorize(qimage_argb32_from_png_decoding)
        # self.nparrays = f(nparrays)
        # convert=np.vectorize(ndarray_from_qimage_argb32)
        # self.nparrays = convert(self.nparrays[1])
        print(self.nparrays)
        self.extraire_coord()

        # self.form_area = np.count_nonzero(self.nparray)
        # # self.form_area = np.count_nonzero(self.comp_array)
        # self.centroid = self.centroid_function(self.nparray)
        # self.radius = self.centroid_radius()
        # self.circle_around_form = self.draw_circle_around_form()
        # self.area_circle_around_form = np.count_nonzero(self.circle_around_form)
        # self.perimetre = np.count_nonzero(self.perimeter_image(nparray) * 1)


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
            z.append(self.knn_axe3(i, centroid, radius, perimetre))
            # print(self.dist_moyenne_centre(i))
        return x, y, z
        # print(x, y, z)


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

    # def calculate_area_circle_around_form(self):



    # def ext_form_area(self):
    #     return np.count_nonzero(self.circle_around_form) - self.form_area

    #calcul la plus grande distance à partir du centroid
    def centroid_radius(self, image, centroid):
        col_mesh, row_mesh = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
        return np.max(np.where(image, np.sqrt(pow((row_mesh - centroid[0]), 2) + pow((col_mesh - centroid[1]), 2)), np.zeros(image.shape)))
        # return np.where(image, np.sqrt(pow((row_mesh - centroid[0]), 2) + pow((col_mesh - centroid[1]), 2)), np.zeros(image.shape))

    def dist_moyenne_centre(self, image):
        m_coord_x, m_coord_y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0])) 
        centroid_x, centroid_y = self.centroid_function(image)[1], self.centroid_function(image)[0]
        return np.mean(np.sqrt((m_coord_x - centroid_x)**2 + (m_coord_y - centroid_y)**2))

    # calcul du périmètre
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
        # return self.form_area * 4 * np.pi

    def knn_axe2(self, area, area_circle):
        return area / area_circle

    def knn_axe3(self, image, centroid, radius, perimeter):
        return np.count_nonzero(np.logical_and(image[1:-1, 1:-1], self.perimeter_image(self.draw_circle_around_form(image, centroid, radius))) * 1) / perimeter

if __name__ == '__main__':
    # array = np.array([220,220], dtype = np.uint8)
    credential = PostgreSQLCredential(host='jcd-prof-cvm-69b5.aivencloud.com', port=11702, database='data_kit', user='klustr_reader', password='h$2%1?')
    klustr_dao = PostgreSQLKlustRDAO(credential)
    raw_images = np.array(klustr_dao.image_from_dataset('ABC', True), dtype=object)[:, 6]
    ke = KlustEngine(raw_images)
    print(klustr_dao.image_from_dataset('ABC', True))

