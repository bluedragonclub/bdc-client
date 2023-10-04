# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(429, 110)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(16777215, 110))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_pw = QLabel(Dialog)
        self.label_pw.setObjectName(u"label_pw")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_pw.sizePolicy().hasHeightForWidth())
        self.label_pw.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(10)
        self.label_pw.setFont(font)

        self.horizontalLayout.addWidget(self.label_pw)

        self.lineEdit_currentPw = QLineEdit(Dialog)
        self.lineEdit_currentPw.setObjectName(u"lineEdit_currentPw")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_currentPw.sizePolicy().hasHeightForWidth())
        self.lineEdit_currentPw.setSizePolicy(sizePolicy2)
        self.lineEdit_currentPw.setMaximumSize(QSize(16777215, 24))
        self.lineEdit_currentPw.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit_currentPw)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_pw_2 = QLabel(Dialog)
        self.label_pw_2.setObjectName(u"label_pw_2")
        sizePolicy1.setHeightForWidth(self.label_pw_2.sizePolicy().hasHeightForWidth())
        self.label_pw_2.setSizePolicy(sizePolicy1)
        self.label_pw_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_pw_2)

        self.lineEdit_newPw = QLineEdit(Dialog)
        self.lineEdit_newPw.setObjectName(u"lineEdit_newPw")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_newPw.sizePolicy().hasHeightForWidth())
        self.lineEdit_newPw.setSizePolicy(sizePolicy3)
        self.lineEdit_newPw.setMaximumSize(QSize(16777215, 24))
        self.lineEdit_newPw.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineEdit_newPw)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_pw_3 = QLabel(Dialog)
        self.label_pw_3.setObjectName(u"label_pw_3")
        sizePolicy1.setHeightForWidth(self.label_pw_3.sizePolicy().hasHeightForWidth())
        self.label_pw_3.setSizePolicy(sizePolicy1)
        self.label_pw_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_pw_3)

        self.lineEdit_confirmPw = QLineEdit(Dialog)
        self.lineEdit_confirmPw.setObjectName(u"lineEdit_confirmPw")
        sizePolicy3.setHeightForWidth(self.lineEdit_confirmPw.sizePolicy().hasHeightForWidth())
        self.lineEdit_confirmPw.setSizePolicy(sizePolicy3)
        self.lineEdit_confirmPw.setMaximumSize(QSize(16777215, 24))
        self.lineEdit_confirmPw.setFont(font)

        self.horizontalLayout_4.addWidget(self.lineEdit_confirmPw)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy4)
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_pw.setText(QCoreApplication.translate("Dialog", u"Current password:", None))
        self.label_pw_2.setText(QCoreApplication.translate("Dialog", u"New password:", None))
        self.label_pw_3.setText(QCoreApplication.translate("Dialog", u"Confirm password:", None))
    # retranslateUi

