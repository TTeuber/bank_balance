# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logged_in.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(494, 618)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.logout_button = QPushButton(Form)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.logout_button, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.tab_widget = QTabWidget(Form)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_2 = QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.balance_label = QLabel(self.tab_1)
        self.balance_label.setObjectName(u"balance_label")
        font = QFont()
        font.setPointSize(48)
        self.balance_label.setFont(font)
        self.balance_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.balance_label, 1, 0, 1, 2)

        self.balance_edit = QLineEdit(self.tab_1)
        self.balance_edit.setObjectName(u"balance_edit")

        self.gridLayout_2.addWidget(self.balance_edit, 2, 0, 1, 2)

        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)

        self.withdraw_button = QPushButton(self.tab_1)
        self.withdraw_button.setObjectName(u"withdraw_button")

        self.gridLayout_2.addWidget(self.withdraw_button, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.deposit_button = QPushButton(self.tab_1)
        self.deposit_button.setObjectName(u"deposit_button")

        self.gridLayout_2.addWidget(self.deposit_button, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.tab_widget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.change_password_button = QPushButton(self.tab_2)
        self.change_password_button.setObjectName(u"change_password_button")

        self.gridLayout_3.addWidget(self.change_password_button, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 3)

        self.account_username_label = QLabel(self.tab_2)
        self.account_username_label.setObjectName(u"account_username_edit")
        font1 = QFont()
        font1.setPointSize(36)
        self.account_username_label.setFont(font1)

        self.gridLayout_3.addWidget(self.account_username_label, 1, 0, 1, 3)

        self.account_password_label = QLabel(self.tab_2)
        self.account_password_label.setObjectName(u"account_password_edit")
        self.account_password_label.setFont(font1)

        self.gridLayout_3.addWidget(self.account_password_label, 2, 0, 1, 3)

        self.tab_widget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tab_widget, 1, 0, 1, 3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(64)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)


        self.retranslateUi(Form)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logout_button.setText(QCoreApplication.translate("Form", u"Log Out", None))
        self.balance_label.setText(QCoreApplication.translate("Form", u"$0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Balance", None))
        self.withdraw_button.setText(QCoreApplication.translate("Form", u"Withdraw", None))
        self.deposit_button.setText(QCoreApplication.translate("Form", u"Deposit", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"Balance", None))
        self.change_password_button.setText(QCoreApplication.translate("Form", u"Change Password", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Account Info", None))
        self.account_username_label.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.account_password_label.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Account", None))
        self.label.setText(QCoreApplication.translate("Form", u"Logged In", None))
    # retranslateUi

