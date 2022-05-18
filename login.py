# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(464, 600)
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QWidget\n"
"{\n"
"	Background: #303030;\n"
"	color: \"white\";\n"
"}\n"
"QPushButton\n"
"{\n"
"	Background: #444444;\n"
"	border: \"black\";\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"	Background: #555555;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.password_edit = QLineEdit(self.centralwidget)
        self.password_edit.setObjectName(u"password_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_edit.sizePolicy().hasHeightForWidth())
        self.password_edit.setSizePolicy(sizePolicy)
        self.password_edit.setMinimumSize(QSize(40, 30))
        font1 = QFont()
        font1.setPointSize(18)
        self.password_edit.setFont(font1)
        self.password_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.password_edit, 4, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 8, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 2)

        self.username_edit = QLineEdit(self.centralwidget)
        self.username_edit.setObjectName(u"username_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username_edit.sizePolicy().hasHeightForWidth())
        self.username_edit.setSizePolicy(sizePolicy1)
        self.username_edit.setMinimumSize(QSize(0, 30))
        self.username_edit.setFont(font1)
        self.username_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.username_edit, 2, 1, 1, 2)

        self.register_button = QPushButton(self.centralwidget)
        self.register_button.setObjectName(u"register_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.register_button.sizePolicy().hasHeightForWidth())
        self.register_button.setSizePolicy(sizePolicy2)
        self.register_button.setMinimumSize(QSize(0, 30))
        self.register_button.setFont(font1)

        self.gridLayout.addWidget(self.register_button, 7, 1, 1, 1)

        self.login_button = QPushButton(self.centralwidget)
        self.login_button.setObjectName(u"login_button")
        sizePolicy2.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy2)
        self.login_button.setMinimumSize(QSize(0, 30))
        self.login_button.setFont(font1)

        self.gridLayout.addWidget(self.login_button, 7, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 7, 3, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(32)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 4)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(64)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 464, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"register", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

