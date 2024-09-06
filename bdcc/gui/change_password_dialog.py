import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QTextCursor
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QIcon
from PySide6.QtGui import QScreen
from PySide6.QtGui import QFont


from bdcc.gui.ui_change_password_dialog import Ui_Dialog
from bdcc.utils import to_json
from bdcc.utils import flush_input
from bdcc.utils import uformat

class ChangePasswordDialog(QDialog):

    def set_fonts(self):
        font = QFont()
        font_button = QFont()
    
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        dpi = QApplication.primaryScreen().logicalDotsPerInch()     

        # Set font family and scale factor.
        if sys.platform == "win32":     
            default_font = u"Segoe UI" 
            scale_factor = dpi / 120.0

        elif sys.platform == "darwin":
            default_font = u"San Francisco"
            scale_factor = dpi / 70.0


        font.setFamilies([default_font])
        font_button.setFamilies([default_font])

        # Set font size.
        font_size = int(12 * scale_factor)
        font.setPointSize(font_size)

        font_size = int(12 * scale_factor)
        font_button.setPointSize(font_size)


        self.ui.label_pw.setFont(font)
        self.ui.label_pw_2.setFont(font)
        self.ui.label_pw_3.setFont(font)
        
        self.ui.lineEdit_currentPw.setFont(font)
        self.ui.lineEdit_newPw.setFont(font)        
        self.ui.lineEdit_confirmPw.setFont(font)

        self.ui.buttonBox.setFont(font_button)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.set_fonts()

        self.ui.lineEdit_currentPw.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_newPw.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_confirmPw.setEchoMode(QLineEdit.Password)

        self.setWindowTitle("Change password")

    def clear(self):
        self.ui.lineEdit_currentPw.clear()
        self.ui.lineEdit_newPw.clear()
        self.ui.lineEdit_confirmPw.clear()
