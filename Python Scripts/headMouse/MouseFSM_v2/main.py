from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import acd_file_io_lib
import ui


class MainClass(QDialog, ui.Ui_Dialog):
	def __init__(self, parent=None):
		super(MainClass, self).__init__(parent)
		self.setupUi(self)




app = QApplication(sys.argv)
form = MainClass()
form.show()
app.exec_()