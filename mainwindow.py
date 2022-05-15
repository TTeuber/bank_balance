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
    password_edit = window.ui.password_edit
    username_edit = window.ui.username_edit
    register_button = window.ui.register_button
    login_button = window.ui.login_button
    log_in_window = ''

    @Slot()
    def register():
        shelf = shelve.open("logins")
        if username_edit.text() not in shelf.keys():
            shelf[username_edit.text()] = password_edit.text()
            user = shelve.open(f"./users/{username_edit.text()}")
            user["balance"] = 0
            login()
        else:
            username_edit.setText("username taken")
            password_edit.setText("")
        shelf.close()


    @Slot()
    def login():
        global log_in_window
        shelf = shelve.open('logins')
        if (username_edit.text(), password_edit.text()) in shelf.items():
            log_in_window = LogIn(username_edit.text())
            window.close()
            log_in_window.show()
            password_edit.setText("")
            username_edit.setText("")
        else:
            username_edit.setText("invalid username or password")
            password_edit.setText("")
        shelf.close()


    login_button.clicked.connect(login)
    register_button.clicked.connect(register)

    def check_logins():
        shelf = shelve.open('logins')
        print(list(shelf.items()))
        shelf.close()


    check_logins()

    sys.exit(app.exec())
