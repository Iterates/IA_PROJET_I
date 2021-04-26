# Importation des modules
import sys
from db_credential import PostgreSQLCredential
from klustr_dao import PostgreSQLKlustRDAO
from klustr_widget import KlustRDataSourceViewWidget
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from __feature__ import snake_case, true_property


if __name__ == "__main__":
    app = QApplication(sys.argv)

    credential = PostgreSQLCredential(host='jcd-prof-cvm-69b5.aivencloud.com', port=11702, database='data_kit', user='klustr_reader', password='h$2%1?')
    klustr_dao = PostgreSQLKlustRDAO(credential)
    source_data_widget = KlustRDataSourceViewWidget(klustr_dao)
    source_data_widget.show()

    sys.exit(app.exec_())