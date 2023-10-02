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
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QTextCursor
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QIcon


from bdc_client.gui.ui_form import Ui_Dialog
import utils
from utils import flush_input
from utils import uformat


def colorize_log(log):
    log = re.sub('\[Problem (.+)\] (.+)\n', '<span style=\"color: #0048ff;\">[Problem \\1] \\2</span>\n', log)

    log = re.sub('All tests have been passed! \[(.+)pts]\n',
                 '<span style=\"color: #00BA00;\">All tests have been passed! [\\1pts]</span>\n',
                 log)

    log = log.replace("[ERROR]", "<span style=\"color: red;\">[ERROR]</span>")
    log = log.replace("[FAILED]", "<span style=\"color: red;\">[FAILED]</span>")
    log = log.replace("[MEMORY LEAK]", "<span style=\"color: red;\">[MEMORY LEAK]</span>")
    log = log.replace("100 / 100", "<span style=\"color: #00BA00;\">100 / 100</span>")
    return log

def show_error_msg(title, err_msg):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(err_msg)
    msg.exec()


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("BlueDragonClub")
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        # Initialize the buttons.
        self.ui.pushButton_openConfig.clicked.connect(self.open_config_clicked)
        self.ui.pushButton_exportConfig.clicked.connect(self.export_config_clicked)
        self.ui.pushButton_openFiles.clicked.connect(self.open_files_clicked)
        self.ui.pushButton_submitFiles.clicked.connect(self.submit_files_clicked)


        self.ui.pushButton_openConfig.setShortcut("Ctrl+O")
        self.ui.pushButton_exportConfig.setShortcut("Ctrl+E")
        self.ui.pushButton_submitFiles.setShortcut("Ctrl+S")
        self.ui.pushButton_openFiles.setShortcut("Ctrl+F")


        # Initialize the line edits.
        self.ui.lineEdit_id.setInputMask("00000000")
        #self.ui.lineEdit_id.setText("00000000")


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
            # self.ui.lineEdit_course
            # self.ui.lineEdit_id
            # self.ui.lineEdit_assignment


        except Exception as err:
            print(err)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Open a configuration file")
            msg.setText("Invalid file type or file contents:\n\n%s"%(traceback.format_exc()))
            msg.exec()
        # end of except

    def update_config(self, fpath):
        try:
            with open(fpath, "rt", encoding="utf-8") as fin:
                config = yaml.safe_load(fin)

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

                for i, problem in enumerate(list_problems):
                    self.ui.tableWidget_problems.setItem(i, 0, QTableWidgetItem(problem))

                for i, fpath in enumerate(list_files):
                    self.ui.tableWidget_files.setItem(i, 0, QTableWidgetItem(fpath))
            # end of with

        except yaml.scanner.ScannerError as err:
            print(err)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Open a configuration file")
            msg.setText("The configuration file contains some invalid characters.\n\n%s"%(traceback.format_exc()))
            msg.exec()

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

        # with open(fpath, "wt", encoding="utf-8") as fout:
        with open(fpath, "wt") as fout:
            yaml.dump(config, fout) #, encoding=('utf-8'))


    def open_files_clicked(self):
        try:
            dialog = QFileDialog(self)
            dialog.setWindowTitle("Open source codes")
            dialog.setAcceptMode(QFileDialog.AcceptOpen)
            dialog.setNameFilters(["Source codes (*.py *.cpp *.h *.cc *.hpp)"])
            dialog.setFileMode(QFileDialog.ExistingFile)

            fpaths, _ = dialog.getOpenFileNames(
                None,
                "Open source codes",
                filter="Source codes (*.py *.cpp *.h *.cc *.hpp)"
            )

            if not fpaths:
                return

        except Exception as err:
            print(err)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Open source codes")
            msg.setText("Invalid file type or file contents:\n\n%s"%(traceback.format_exc()))
            msg.exec()
        # end of except

        self.ui.tableWidget_files.clear()
        for i, fpath in enumerate(fpaths):
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
            if item:
                # fpath = item.text()
                fpath = str(Path(item.text()).absolute())
                config["FILES"].append(fpath)


        for i in range(self.ui.tableWidget_problems.rowCount()):
            item = self.ui.tableWidget_problems.item(i, 0)
            if item:
                problem_id = str(item.text())
                if problem_id:
                    config["PROBLEMS"].append(problem_id)


        return config


    def write_log(self, str_log, clear=True):
        if clear:
            self.ui.textBrowser_syslog.clear()

        str_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        str_log = colorize_log(str_log)
        # self.ui.textBrowser_syslog.insertPlainText(str_log)
        # self.ui.textBrowser_syslog.append(str_log)

        self.ui.textBrowser_syslog.insertPlainText("[Log time] %s\n"%(str_now))

        lines = str_log.split('\n')

        for line in lines:
            self.ui.textBrowser_syslog.insertHtml(line)
            self.ui.textBrowser_syslog.insertPlainText("\n")


    def submit(self, config):

        # Check student ID.
        err_msg = "You must insert Student ID!"
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
            print(fpath)

            if not osp.isfile(fpath):
                err_msg = "File not found:\n{}".format(fpath)
                show_error_msg("Submission", err_msg)
                return

            _, ext = osp.splitext(fname)
            if ext not in [".py", ".cpp", ".c", ".h"]:
                err_msg = "Invalid source file format:\n ▶ {}".format(fpath)
                show_error_msg("Submission", err_msg)
                return

            files.append(
                ('files', (fname, open(fpath, 'rb'), 'text/plain'))
            )
        # end of for

        # Submit the files with the meta-information.
        response = requests.post(uformat(config, b"c3VibWl0"), data=submission, files=files)
        res = utils.to_json(response)

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


def main():
    libpaths = QApplication.libraryPaths()
    libpaths.append(os.getcwd())
    QApplication.setLibraryPaths(libpaths)

    app = QApplication(sys.argv)
    widget = Dialog()

    icon = QIcon(osp.join(osp.dirname(__file__), "gui", "icon.png"))
    widget.setWindowIcon(icon)  # for Windows and Linux
    app.setWindowIcon(icon)

    widget.show()
    sys.exit(app.exec())
