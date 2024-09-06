# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(790, 463)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_files = QGroupBox(Dialog)
        self.groupBox_files.setObjectName(u"groupBox_files")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_files.sizePolicy().hasHeightForWidth())
        self.groupBox_files.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(14)
        self.groupBox_files.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_files)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget_files = QTableWidget(self.groupBox_files)
        self.tableWidget_files.setObjectName(u"tableWidget_files")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget_files.sizePolicy().hasHeightForWidth())
        self.tableWidget_files.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.tableWidget_files)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_openFiles = QPushButton(self.groupBox_files)
        self.pushButton_openFiles.setObjectName(u"pushButton_openFiles")
        self.pushButton_openFiles.setMinimumSize(QSize(0, 24))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        self.pushButton_openFiles.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton_openFiles, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.pushButton_submitFiles = QPushButton(self.groupBox_files)
        self.pushButton_submitFiles.setObjectName(u"pushButton_submitFiles")
        self.pushButton_submitFiles.setMinimumSize(QSize(0, 24))
        self.pushButton_submitFiles.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton_submitFiles, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.groupBox_files, 3, 0, 1, 1)

        self.groupBox_systemlog = QGroupBox(Dialog)
        self.groupBox_systemlog.setObjectName(u"groupBox_systemlog")
        sizePolicy.setHeightForWidth(self.groupBox_systemlog.sizePolicy().hasHeightForWidth())
        self.groupBox_systemlog.setSizePolicy(sizePolicy)
        self.groupBox_systemlog.setFont(font)
        self.groupBox_systemlog.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_systemlog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser_syslog = QTextBrowser(self.groupBox_systemlog)
        self.textBrowser_syslog.setObjectName(u"textBrowser_syslog")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser_syslog.sizePolicy().hasHeightForWidth())
        self.textBrowser_syslog.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Courier New"])
        font2.setPointSize(14)
        self.textBrowser_syslog.setFont(font2)

        self.verticalLayout_3.addWidget(self.textBrowser_syslog)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_showResults = QPushButton(self.groupBox_systemlog)
        self.pushButton_showResults.setObjectName(u"pushButton_showResults")
        self.pushButton_showResults.setMinimumSize(QSize(90, 24))
        self.pushButton_showResults.setMaximumSize(QSize(16777215, 90))
        self.pushButton_showResults.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton_showResults, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.gridLayout.addWidget(self.groupBox_systemlog, 0, 1, 4, 1)

        self.groupBox_problems = QGroupBox(Dialog)
        self.groupBox_problems.setObjectName(u"groupBox_problems")
        sizePolicy.setHeightForWidth(self.groupBox_problems.sizePolicy().hasHeightForWidth())
        self.groupBox_problems.setSizePolicy(sizePolicy)
        self.groupBox_problems.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_problems)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget_problems = QTableWidget(self.groupBox_problems)
        self.tableWidget_problems.setObjectName(u"tableWidget_problems")
        sizePolicy.setHeightForWidth(self.tableWidget_problems.sizePolicy().hasHeightForWidth())
        self.tableWidget_problems.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.tableWidget_problems)


        self.gridLayout.addWidget(self.groupBox_problems, 2, 0, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lineEdit_config = QLineEdit(self.groupBox)
        self.lineEdit_config.setObjectName(u"lineEdit_config")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_config.sizePolicy().hasHeightForWidth())
        self.lineEdit_config.setSizePolicy(sizePolicy4)
        self.lineEdit_config.setFont(font)

        self.horizontalLayout_4.addWidget(self.lineEdit_config)

        self.pushButton_openConfig = QPushButton(self.groupBox)
        self.pushButton_openConfig.setObjectName(u"pushButton_openConfig")
        self.pushButton_openConfig.setMinimumSize(QSize(0, 24))
        self.pushButton_openConfig.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_openConfig)

        self.pushButton_exportConfig = QPushButton(self.groupBox)
        self.pushButton_exportConfig.setObjectName(u"pushButton_exportConfig")
        self.pushButton_exportConfig.setMinimumSize(QSize(0, 24))
        self.pushButton_exportConfig.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_exportConfig)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_id = QLabel(self.groupBox)
        self.label_id.setObjectName(u"label_id")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_id.sizePolicy().hasHeightForWidth())
        self.label_id.setSizePolicy(sizePolicy5)
        self.label_id.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_id)

        self.lineEdit_id = QLineEdit(self.groupBox)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        sizePolicy4.setHeightForWidth(self.lineEdit_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_id.setSizePolicy(sizePolicy4)
        self.lineEdit_id.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_id)

        self.label_pw = QLabel(self.groupBox)
        self.label_pw.setObjectName(u"label_pw")
        sizePolicy5.setHeightForWidth(self.label_pw.sizePolicy().hasHeightForWidth())
        self.label_pw.setSizePolicy(sizePolicy5)
        self.label_pw.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_pw)

        self.lineEdit_pw = QLineEdit(self.groupBox)
        self.lineEdit_pw.setObjectName(u"lineEdit_pw")
        sizePolicy4.setHeightForWidth(self.lineEdit_pw.sizePolicy().hasHeightForWidth())
        self.lineEdit_pw.setSizePolicy(sizePolicy4)
        self.lineEdit_pw.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_pw)

        self.pushButton_changePassword = QPushButton(self.groupBox)
        self.pushButton_changePassword.setObjectName(u"pushButton_changePassword")
        self.pushButton_changePassword.setMinimumSize(QSize(0, 24))
        self.pushButton_changePassword.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_changePassword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font)

        self.horizontalLayout_1.addWidget(self.label_4)

        self.lineEdit_course = QLineEdit(self.groupBox)
        self.lineEdit_course.setObjectName(u"lineEdit_course")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_course.sizePolicy().hasHeightForWidth())
        self.lineEdit_course.setSizePolicy(sizePolicy6)
        self.lineEdit_course.setFont(font)

        self.horizontalLayout_1.addWidget(self.lineEdit_course)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_assignment = QLineEdit(self.groupBox)
        self.lineEdit_assignment.setObjectName(u"lineEdit_assignment")
        sizePolicy6.setHeightForWidth(self.lineEdit_assignment.sizePolicy().hasHeightForWidth())
        self.lineEdit_assignment.setSizePolicy(sizePolicy6)
        self.lineEdit_assignment.setMinimumSize(QSize(0, 24))
        self.lineEdit_assignment.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineEdit_assignment)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_files.setTitle(QCoreApplication.translate("Dialog", u"Source codes", None))
        self.pushButton_openFiles.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.pushButton_submitFiles.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.groupBox_systemlog.setTitle(QCoreApplication.translate("Dialog", u"System log", None))
        self.pushButton_showResults.setText(QCoreApplication.translate("Dialog", u"Show Results", None))
        self.groupBox_problems.setTitle(QCoreApplication.translate("Dialog", u"Problems", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Configuration", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"File:", None))
        self.pushButton_openConfig.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.pushButton_exportConfig.setText(QCoreApplication.translate("Dialog", u"Export", None))
        self.label_id.setText(QCoreApplication.translate("Dialog", u"ID:", None))
        self.label_pw.setText(QCoreApplication.translate("Dialog", u"PW:", None))
        self.pushButton_changePassword.setText(QCoreApplication.translate("Dialog", u"Change", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Course", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Assignment:", None))
    # retranslateUi

