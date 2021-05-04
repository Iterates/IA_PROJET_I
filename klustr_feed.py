from db_credential import PostgreSQLCredential
from klustr_dao import PostgreSQLKlustRDAO
from klustr_utils import *
from klustr_engine import *
from klustr_widget import *
import numpy as np

class KlustFeed():
    def __init__(self, dataset_name, training_image=True):
        credential = PostgreSQLCredential(host='jcd-prof-cvm-69b5.aivencloud.com', port=11702, database='data_kit', user='klustr_reader', password='h$2%1?')
        klustr_dao = PostgreSQLKlustRDAO(credential)
        self.dataset_images_name = np.array(klustr_dao.image_from_dataset(dataset_name, training_image), dtype=object)[:,1]
        self._raw_images = np.array(klustr_dao.image_from_dataset(dataset_name, training_image), dtype=object)[:, 6]
        self.labels = np.array(klustr_dao.available_datasets, dtype=object)[:,1]

        
#    def convert_to_qimage(self):
#        return [qimage_argb32_from_png_decoding(img) for img in self._self._raw_images]
#
#    def convert_to_array(self):
#        return [ndarray_from_qimage_argb32(img) for img in self.convert_to_qimage()] 

    def decode(self):
        return np.where(np.logical_not([ndarray_from_qimage_argb32(qimage_argb32_from_png_decoding(img)) for img in self._raw_images]), 1, 0) 
        f=np.vectorize(qimage_argb32_from_png_decoding)
        self._raw_images = f(self._raw_images)

if __name__ == "__main__":
    kf = KlustFeed("ABC")
    # self.dataset_image = np.array(self.klustr_dao.image_from_dataset(cbox_dataset_title, False), dtype=object)
    # self.dataset_image = np.array(self.klustr_dao.image_from_dataset('ABC', True), dtype=object)

    # print(kf.images_name)
    ke = KlustEngine(kf.decode()[0])
    a = ke.centroid_radius()
    b = ke.draw_circle_around_form()
    c = ke.centroid
    d = ke.nparray
    e = np.equal(b, d)
    f = ke.ext_form_area()
    g = ke.knn_axe2()
    h = ke.perimetre

    # print(kf.dataset_images_name)
    z=1