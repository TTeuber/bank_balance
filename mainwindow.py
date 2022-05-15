# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QInputDialog
from login import Ui_MainWindow
from logged_in import Ui_Form
from PySide6.QtCore import Slot
import shelve
from os.path import exists


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.password_edit = self.ui.password_edit
        self.username_edit = self.ui.username_edit
        self.register_button = self.ui.register_button
        self.login_button = self.ui.login_button
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    @Slot()
    def register(self):
        shelf = shelve.open("logins")
        if self.username_edit.text() not in shelf.keys():
            shelf[self.username_edit.text()] = self.password_edit.text()
            user = shelve.open(f"./users/{self.username_edit.text()}")
            user["balance"] = 0
            self.login()
        else:
            self.username_edit.setText("username taken")
            self.password_edit.setText("")
        shelf.close()

    @Slot()
    def login(self):
        global log_in_window
        shelf = shelve.open('logins')
        if (self.username_edit.text(), self.password_edit.text()) in shelf.items():
            log_in_window = LogIn(self.username_edit.text())
            window.close()
            log_in_window.show()
            self.password_edit.setText("")
            self.username_edit.setText("")
        else:
            self.username_edit.setText("invalid username or password")
            self.password_edit.setText("")
        shelf.close()


class LogIn(QWidget):
    def __init__(self, username):
        super(LogIn, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = username
        self.password = self.get_password()
        self.create_db()
        self.balance = self.get_balance()
        self.logout_button = self.ui.logout_button
        self.balance_label = self.ui.balance_label
        self.balance_label.setText(f"${self.balance}")
        self.balance_edit = self.ui.balance_edit
        self.logout_button.clicked.connect(self.confirm_logout)
        self.deposit_button = self.ui.deposit_button
        self.deposit_button.clicked.connect(self.deposit_balance)
        self.withdraw_button = self.ui.withdraw_button
        self.withdraw_button.clicked.connect(self.withdraw_balance)
        self.username_label = self.ui.account_username_label
        self.username_label.setText(f"Username: {self.user}")
        self.password_label = self.ui.account_password_label
        self.password_label.setText(f"Password: {self.get_password()}")
        self.change_password_button = self.ui.change_password_button
        self.change_password_button.clicked.connect(self.change_password)

    def create_db(self):
        if not exists(f"./users/{self.user}.db"):
            shelf = shelve.open(f"./users/{self.user}")
            shelf["balance"] = 0
            shelf.close()
            shelf = shelve.open("logins")
            self.password_label.setText(f"Password: {shelf[self.user]}")
            shelf.close()

    def get_password(self):
        shelf = shelve.open("logins")
        password = shelf.get(self.user)
        shelf.close()
        return password

    @Slot()
    def change_password(self):
        text, ok = QInputDialog.getText(self, "input dialog", "enter text:")
        if ok:
            self.password_label.setText(f"Password: {text}")
            self.password = text
            shelf = shelve.open("logins")
            shelf[self.user] = text
            shelf.close()

    def get_balance(self):
        shelf = shelve.open(f"./users/{self.user}")
        balance = shelf.get("balance")
        shelf.close()
        return balance

    @Slot()
    def deposit_balance(self):
        shelf = shelve.open(f"./users/{self.user}")
        balance = shelf["balance"]
        shelf["balance"] = int(str(balance)) + int(self.balance_edit.text())
        self.balance_label.setText(f"${shelf['balance']}")
        shelf.close()

    @Slot()
    def withdraw_balance(self):
        shelf = shelve.open(f"./users/{self.user}")
        balance = shelf["balance"]
        shelf["balance"] = int(str(balance)) - int(self.balance_edit.text())
        self.balance_label.setText(f"${shelf['balance']}")
        shelf.close()

    @Slot()
    def confirm_logout(self):
        msg = QMessageBox()
        msg.setWindowTitle("confirm log out")
        msg.setText("Confirm log out?")
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        x = msg.exec()
        if x == msg.Yes:
            self.logout()

    @Slot()
    def logout(self):
        self.close()
        window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    log_in_window = ''


    def check_logins():
        shelf = shelve.open('logins')
        print(list(shelf.items()))
        shelf.close()


    check_logins()

    sys.exit(app.exec())
