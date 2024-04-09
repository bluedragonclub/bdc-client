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


from bdcc.gui.ui_change_password_dialog import Ui_Dialog
from bdcc.utils import to_json
from bdcc.utils import flush_input
from bdcc.utils import uformat

class ChangePasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.lineEdit_currentPw.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_newPw.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_confirmPw.setEchoMode(QLineEdit.Password)

        self.setWindowTitle("Change password")

    def clear(self):
        self.ui.lineEdit_currentPw.clear()
        self.ui.lineEdit_newPw.clear()
        self.ui.lineEdit_confirmPw.clear()
