# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import os
import os.path as osp
import re
import sys
import traceback
import requests
import socket
from datetime import datetime
from pathlib import Path, PurePath

import yaml

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QScreen
from PySide6.QtGui import QTextCursor
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QIcon
from PySide6.QtGui import QFont


from bdcc.gui.ui_main_dialog import Ui_Dialog
from bdcc.gui.change_password_dialog import ChangePasswordDialog
from bdcc.utils import to_json
from bdcc.utils import flush_input
from bdcc.utils import uformat
from bdcc.utils import read_config


yaml.reader.Reader.NON_PRINTABLE = re.compile('[^\t\n\r -�-\U0010ffff]')


def colorize_log(log):
    log = re.sub('\[Problem (.+)\] (.+)\n', '<span style=\"color: #0048ff;\">[Problem \\1] \\2</span>\n', log)

    log = re.sub('All tests have been passed! \[(.+)pts]\n',
                 '<span style=\"color: #009600;\">All tests have been passed! [\\1pts]</span>\n',
                 log)

    log = log.replace("[ERROR]", '<span style=\"color: red;\">[ERROR]</span>')
    log = log.replace("[FAILED]", '<span style=\"color: red;\">[FAILED]</span>')
    log = log.replace("[MEMORY LEAK]", '<span style=\"color: red;\">[MEMORY LEAK]</span>')
    # log = log.replace("100 / 100", '<span style=\"color: #009600;\">100 / 100</span>')
    return log

def show_error_msg(title, err_msg):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(err_msg)
    msg.exec()


class Dialog(QDialog):
    def set_fonts(self):

        font = QFont()
        font_button = QFont()
        font_syslog = QFont()
    
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        dpi = QApplication.primaryScreen().logicalDotsPerInch()     

        # Set font family and scale factor.
        if sys.platform == "win32":     
            default_font = u"Segoe UI"    
            font_syslog.setFamilies([u"Consolas"])
            
            scale_factor = dpi / 120.0

        elif sys.platform == "darwin":
            default_font = u"San Francisco"
            font_syslog.setFamilies([u"Courier New"])

            scale_factor = dpi / 70.0


        font.setFamilies([default_font])
        font_button.setFamilies([default_font])


        # Set font size.
        font.setPointSize(int(12 * scale_factor))
        font_button.setPointSize(int(12 * scale_factor))
        font_syslog.setPointSize(int(12 * scale_factor) + 1)

        # Set the font of syslog
        self.ui.textBrowser_syslog.setFont(font_syslog)

        # Set the fonts of goupBoxes.
        self.ui.groupBox_files.setFont(font)
        self.ui.groupBox_systemlog.setFont(font)        
        self.ui.groupBox_problems.setFont(font)
        self.ui.groupBox.setFont(font)

        # Set the fonts of labels.
        self.ui.label_id.setFont(font)
        self.ui.label_pw.setFont(font)
        self.ui.label_3.setFont(font)
        self.ui.label_4.setFont(font)
        self.ui.label_6.setFont(font)

        # Set the fonts of lineEdits.
        self.ui.lineEdit_config.setFont(font)                
        self.ui.lineEdit_id.setFont(font)        
        self.ui.lineEdit_pw.setFont(font)        
        self.ui.lineEdit_course.setFont(font)
        self.ui.lineEdit_assignment.setFont(font)
        
        # Set the fonts of buttons.
        self.ui.pushButton_openFiles.setFont(font_button)
        self.ui.pushButton_submitFiles.setFont(font_button)
        self.ui.pushButton_showResults.setFont(font_button)
        self.ui.pushButton_openConfig.setFont(font_button)
        self.ui.pushButton_exportConfig.setFont(font_button)
        self.ui.pushButton_changePassword.setFont(font_button)



    def __init__(self, parent=None):        
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.set_fonts()

        self.setWindowTitle("BlueDragonClub")
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        # Initialize the buttons.
        self.ui.pushButton_openConfig.clicked.connect(self.open_config_clicked)
        self.ui.pushButton_exportConfig.clicked.connect(self.export_config_clicked)

        self.ui.pushButton_changePassword.clicked.connect(self.change_password_clicked)

        self.ui.pushButton_openFiles.clicked.connect(self.open_files_clicked)
        self.ui.pushButton_submitFiles.clicked.connect(self.submit_files_clicked)

        self.ui.pushButton_showResults.clicked.connect(self.show_results_clicked)

        self.ui.pushButton_openConfig.setShortcut("Ctrl+O")
        self.ui.pushButton_exportConfig.setShortcut("Ctrl+E")
        self.ui.pushButton_changePassword.setShortcut("Ctrl+C")
        self.ui.pushButton_openFiles.setShortcut("Ctrl+F")
        self.ui.pushButton_submitFiles.setShortcut("Ctrl+S")
        self.ui.pushButton_showResults.setShortcut("Ctrl+R")


        # Initialize the line edits.
        self.ui.lineEdit_id.setInputMask("00000000")
        self.ui.lineEdit_pw.setEchoMode(QLineEdit.Password)

        # Initialize the TableWidget for Problems
        self.ui.tableWidget_problems.setRowCount(20)
        self.ui.tableWidget_problems.setColumnCount(1)
        self.ui.tableWidget_problems.horizontalHeader().hide()

        header = self.ui.tableWidget_problems.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

        # Initialize the TableWidget for Files
        self.ui.tableWidget_files.setRowCount(2)
        self.ui.tableWidget_files.setColumnCount(1)
        self.ui.tableWidget_files.horizontalHeader().hide()

        header = self.ui.tableWidget_files.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

        # Create the change password dialog.
        self.change_password_dialog = ChangePasswordDialog()



    def open_config_clicked(self):
        try:
            dialog = QFileDialog(self)
            dialog.setWindowTitle("Open a configuration file")
            dialog.setAcceptMode(QFileDialog.AcceptOpen)
            dialog.setNameFilters(["Configuration file (*.yml *.yaml)"])
            dialog.setFileMode(QFileDialog.ExistingFile)

            fpath, _ = dialog.getOpenFileName(
                None,
                "Open a configuration file",
                "",
                "Configuration file (*.yml *.yaml)"
            )

            if not fpath:
                return

            self.ui.lineEdit_config.clear()

            # Update the widgets.
            self.ui.lineEdit_config.setText(fpath)
            self.update_config(fpath)

        except Exception as err:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Open a configuration file")
            msg.setText("%s"%(err))
            msg.exec()
        # end of except

    def update_config(self, fpath):
        
        try:
            config = read_config(fpath)
        except yaml.scanner.ScannerError as err:
            print(err)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Open a configuration file")
            msg.setText("The configuration file contains some invalid characters.\n\n%s"%(traceback.format_exc()))
            msg.exec()
        
        
        str_id = config.get("ID", "")
        str_pw = config.get("PW", "")

        str_course = config.get("COURSE", "")
        str_assignment = config.get("ASSIGNMENT", "")

        list_problems = config.get("PROBLEMS", [])
        list_files = config.get("FILES", [])

        self.ui.lineEdit_id.setText(str_id)
        self.ui.lineEdit_pw.setText(str_pw)
        self.ui.lineEdit_course.setText(str_course)
        self.ui.lineEdit_assignment.setText(str_assignment)

        self.ui.tableWidget_problems.clear()
        for i, problem in enumerate(list_problems):
            self.ui.tableWidget_problems.setItem(i, 0, QTableWidgetItem(problem))

        self.ui.tableWidget_files.clear()
        for i, fpath in enumerate(list_files):
            self.ui.tableWidget_files.setItem(i, 0, QTableWidgetItem(fpath))




    def export_config_clicked(self):
        try:
            dialog = QFileDialog(self)
            dialog.setWindowTitle("Export configuration file")
            dialog.setAcceptMode(QFileDialog.AcceptSave)
            dialog.setNameFilters(["Configuration file (*.yml *.yaml)"])
            dialog.setFileMode(QFileDialog.AnyFile)

            fpath, _ = dialog.getSaveFileName(
                None,
                "Export configuration",
                filter="Configuration file (*.yml *.yaml)"
            )

            if not fpath:
                return

        except Exception as err:
            print(err)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Open a configuration file")
            msg.setText("Invalid file type or file contents:\n\n%s"%(traceback.format_exc()))
            msg.exec()
        # end of except


        config = self.get_config_from_gui()

        if "PW" in config:
            config.pop("PW")

        with open(fpath, "wt", encoding="utf-8") as fout:
            yaml.dump(config, fout, allow_unicode=True)

    def change_password_clicked(self):
        self.change_password_dialog.clear()
        ans = self.change_password_dialog.exec()

        if ans == QDialog.Accepted:
            pw_new = self.change_password_dialog.ui.lineEdit_newPw.text()
            pw_confirm = self.change_password_dialog.ui.lineEdit_confirmPw.text()

            if len(pw_new) < 4:
                err_msg = "The length of new password should be greater than 3."
                show_error_msg("Error in changing password", err_msg)
                return

            if pw_new != pw_confirm:
                err_msg = "The new password and confirmation do not match!"
                show_error_msg("Error in changing password", err_msg)
                return

            # Process update the password.
            student_id = self.ui.lineEdit_id.text()
            pw_old = self.change_password_dialog.ui.lineEdit_currentPw.text()

            student = {
                "id": student_id,
                "pw": pw_old,
                "pw_new": pw_new,
                "name": "",
                "group": 0
            }

            try:
                config = self.get_config_from_gui()

                course_id = config["COURSE"]
                if not course_id:
                    err_msg = "Course ID must be defined!"
                    show_error_msg("Error in changing password", err_msg)
                    return    

                config["PW"] = pw_old

                response = requests.post(uformat(config, b"dXBkYXRl"), json=student)
                res = to_json(response)

                if "error" in res:
                    show_error_msg("Error in changing password", res["error"])
                elif "result" in res:
                    # res["result"] == student_id
                    self.write_log('\n<span style=\"color: blue;\">Password updated successfully!</span>')
                    
                    config["PW"] = pw_new
                    self.ui.lineEdit_pw.setText(pw_new)
                    
                    
            except Exception as err:
                print(err)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error in changing password")
                msg.setText("%s"%(traceback.format_exc()))
                msg.exec()
            # end of except

    def open_files_clicked(self):
        try:
            dialog = QFileDialog(self)
            dialog.setWindowTitle("Open source codes")
            dialog.setAcceptMode(QFileDialog.AcceptOpen)
            dialog.setNameFilters(["Source codes (*.py *.cpp *.h *.cc *.hpp *.csv)"])
            dialog.setFileMode(QFileDialog.ExistingFile)

            fpaths, _ = dialog.getOpenFileNames(
                None,
                "Open source codes",
                filter="Source codes (*.py *.cpp *.h *.cc *.hpp *.csv)"
            )

            if not fpaths:
                return

        except Exception as err:
            print(err)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Open source codes")
            msg.setText("Invalid file type or file contents:\n\n%s"%(err))
            msg.exec()
        # end of except

        self.ui.tableWidget_files.clear()
        for i, fpath in enumerate(fpaths):
            fpath = fpath.strip()
            fpath = fpath.strip('"')
            fpath = fpath.strip("'")
            self.ui.tableWidget_files.setItem(i, 0, QTableWidgetItem(fpath))

    def get_config_from_gui(self):
        config = {}

        config["ID"] = str(self.ui.lineEdit_id.text())
        config["PW"] = str(self.ui.lineEdit_pw.text())

        config["COURSE"] = str(self.ui.lineEdit_course.text())
        config["ASSIGNMENT"] = str(self.ui.lineEdit_assignment.text())

        config["FILES"] = []
        config["PROBLEMS"] = []

        for i in range(self.ui.tableWidget_files.rowCount()):
            item = self.ui.tableWidget_files.item(i, 0)
            item_text = item.text() if item else None
            if item and item_text:
                fpath = item.text()
                fpath = fpath.strip(' \'"')                
                config["FILES"].append(fpath)


        for i in range(self.ui.tableWidget_problems.rowCount()):
            item = self.ui.tableWidget_problems.item(i, 0)
            item_text = item.text() if item else None
            if item and item_text:
                problem_id = str(item.text())
                if problem_id:
                    config["PROBLEMS"].append(problem_id)


        return config


    def write_log(self, log, clear=True):
        if clear:
            self.ui.textBrowser_syslog.clear()

        self.ui.textBrowser_syslog.insertHtml('<span style=\"color: black;\"></span>')
        str_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        str_logging_time = "[Log time] %s\n"%(str_now)
        self.ui.textBrowser_syslog.insertPlainText(str_logging_time)

        if isinstance(log, str):
            str_log = colorize_log(log)
            lines = str_log.split('\n')
        elif isinstance(log, list):
            lines = []
            for line in log:
                lines.append(colorize_log(line))

        for line in lines:
            self.ui.textBrowser_syslog.insertHtml(line)
            self.ui.textBrowser_syslog.insertPlainText("\n")


    def submit(self, config):

        # Check student ID.
        err_msg = "You must insert ID!"
        if "ID" in config:
            ID = config["ID"]
            if not ID or not isinstance(ID, str):
                show_error_msg("Submission", err_msg)
                return
        else:
            show_error_msg("Submission", err_msg)
            return

        # Check student password.
        err_msg = "You must insert Password!"
        if "PW" in config:
            PW = config["PW"]
            if not PW or not isinstance(PW, str):
                show_error_msg("Submission", err_msg)
                return
        else:
            show_error_msg("Submission", err_msg)
            return


        # Check course ID.
        err_msg = "You must define Course ID!"
        if "COURSE" in config:
            COURSE = config["COURSE"]
            if not COURSE or not isinstance(COURSE, str):
                show_error_msg("Submission", err_msg)
                return
        else:
            show_error_msg("Submission", err_msg)
            return

        # Check assignment ID.
        err_msg = "You must define Assignment ID!"
        if "ASSIGNMENT" in config:
            ASSIGNMENT = config["ASSIGNMENT"]
            if not ASSIGNMENT or not isinstance(ASSIGNMENT, str):
                show_error_msg("Submission", err_msg)
                return
        else:
            show_error_msg("Submission", err_msg)
            return

        # Check problem ID.
        err_msg = "You must define at least one Problem ID!"
        if "PROBLEMS" in config:
            PROBLEMS = config["PROBLEMS"]
            if not PROBLEMS or not isinstance(PROBLEMS, list) or len(PROBLEMS) < 1:
                show_error_msg("Submission", err_msg)
                return
        else:
            show_error_msg("Submission", err_msg)
            return

        try:
            ip_address = socket.gethostbyname(socket.gethostname())
        except Exception as err:
            ip_address = ""

        try:
            hostname = socket.gethostname()
        except Exception as err:
            hostname = ""

        submission = {
            "student_id": config["ID"],
            "password": config["PW"],
            "course_id": config["COURSE"],
            "assignment_id": config["ASSIGNMENT"],
            "problems": config["PROBLEMS"],
            "ip_address": ip_address,
            "hostname": hostname
        }

        # Check and collect files.
        err_msg = "You must define file paths!"
        if "FILES" in config:
            FILES = config["FILES"]
            if not FILES  or len(FILES) < 1:
                show_error_msg("Submission", err_msg)
                return
        else:
            show_error_msg("Submission", err_msg)
            return

        files = []
        for fpath in FILES:
            fname = osp.basename(fpath)
            if not osp.isfile(fpath):
                err_msg = "File not found:\n{}".format(fpath)
                show_error_msg("Submission", err_msg)
                return

            _, ext = osp.splitext(fname)
            if ext not in [".py", ".cpp", ".cc", ".c", ".h", ".hpp", ".csv"]:
                err_msg = "Invalid source file format:\n ▶ {}".format(fpath)
                show_error_msg("Submission", err_msg)
                return

            files.append(
                ('files', (fname, open(fpath, 'rb'), 'text/plain'))
            )
        # end of for

        # Submit the files with the meta-information.
        response = requests.post(uformat(config, b"c3VibWl0"), data=submission, files=files)
        res = to_json(response)

        if "error" in res:
            self.write_log("\n[ERROR] {}".format(res["error"]))
        elif "result" in res:
            result = res["result"]
            log = result["log"]
            self.write_log("\n{}".format(log))
        else:
            err_msg = "[SYSTEM ERROR] %s"%(response)
            show_error_msg("Submission", err_msg)



    def submit_files_clicked(self):
        config = self.get_config_from_gui()
        self.submit(config)

        self.ui.textBrowser_syslog.moveCursor(QTextCursor.End)


    def show_results_clicked(self):
        config = self.get_config_from_gui()

        # Check student ID.
        err_msg = "You must insert ID!"
        if "ID" in config:
            ID = config["ID"]
            if not ID or not isinstance(ID, str):
                show_error_msg("Submission", err_msg)
                return
        else:
            show_error_msg("Submission", err_msg)
            return
        
        # Check student password.
        err_msg = "You must insert Password!"
        if "PW" in config:
            PW = config["PW"]
            if not PW or not isinstance(PW, str):
                show_error_msg("Show results", err_msg)
                return
        else:
            show_error_msg("Show results", err_msg)
            return


        student_id = str(config["ID"])

        # Process show the results.
        student = {
            "student_id": student_id,
        }
        response = requests.get(uformat(config, b"cmVzdWx0cw=="), params=student)
        res = to_json(response)

        if "error" in res and "result" not in res:
            self.write_log("\n[ERROR] {}".format(res["error"]))
            return

        logs = []
        logs.append('Current Results')

        fstr = '- [<span style=\"color: blue;\">{}</span>] Total Score: {} / 100'
        for assignment_id, total_score in res["result"].items():
            logs.append(fstr.format(assignment_id, total_score))

        self.write_log(logs)

def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    libpaths = QApplication.libraryPaths()
    libpaths.append(os.getcwd())
    QApplication.setLibraryPaths(libpaths)

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    #app.setStyle("Fusion")
    if sys.platform == "darwin":
        app.setStyle("Fusion")
    elif sys.platform == "win32":
        app.setStyle("Fusion")
    
    
    widget = Dialog()

    # icon = QIcon(osp.join(osp.dirname(__file__), "icon.png"))
    dpath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    fpath_icon = os.path.abspath(os.path.join(dpath, 'icon.png'))
    icon = QIcon(fpath_icon)
    widget.setWindowIcon(icon)  # for Windows and Linux
    app.setWindowIcon(icon)

    widget.show()
    sys.exit(app.exec())
