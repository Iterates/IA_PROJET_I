import numpy as np

from db_credential import PostgreSQLCredential
from klustr_dao import PostgreSQLKlustRDAO
from klustr_utils import *

if __name__ == '__main__':
    credential = PostgreSQLCredential(host='jcd-prof-cvm-69b5.aivencloud.com', port=11702, database='data_kit', user='klustr_reader', password='h$2%1?')
    klustr_dao = PostgreSQLKlustRDAO(credential)

    print(klustr_dao.available_datasets)
    print()
    print(klustr_dao.image_from_dataset('ABC', True)[0][1])

    # image = qimage_argb32_from_png_decoding(klustr_dao.image_from_dataset('ABC', True)[0][6])
    # print(image)
    # ndimage = ndarray_from_qimage_argb32(image)
    # print(ndimage)