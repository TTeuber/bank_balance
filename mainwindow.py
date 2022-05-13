# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from login import Ui_MainWindow
from logged_in import Ui_Form
from PySide6.QtCore import Slot
import shelve


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
        self.balance = self.get_balance()

    def get_password(self):
        shelf = shelve.open("logins")
        password = shelf.get(self.user)
        shelf.close()
        return password

    def get_balance(self):
        shelf = shelve.open(f"./users/{self.user}")
        balance = shelf.get("balance")
        shelf.close()
        return balance



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    password_edit = window.ui.password_edit
    username_edit = window.ui.username_edit
    register_button = window.ui.register_button
    login_button = window.ui.login_button

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


    log_in_window = LogIn("sup")
    logout_button = log_in_window.ui.logout_button

    @Slot()
    def login():
        shelf = shelve.open('logins')
        if (username_edit.text(), password_edit.text()) in shelf.items():
            window.close()
            log_in_window.show()
        else:
            username_edit.setText("invalid username or password")
            password_edit.setText("")
        shelf.close()


    @Slot()
    def confirm_logout():
        msg = QMessageBox()
        msg.setWindowTitle("confirm log out")
        msg.setText("Confirm log out?")
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        x = msg.exec()
        if x == msg.Yes:
            logout()


    @Slot()
    def logout():
        log_in_window.close()
        password_edit.setText("")
        username_edit.setText("")
        window.show()

    login_button.clicked.connect(login)
    register_button.clicked.connect(register)
    logout_button.clicked.connect(confirm_logout)

    def check_logins():
        shelf = shelve.open('logins')
        print(list(shelf.items()))
        shelf.close()


    check_logins()

    sys.exit(app.exec())
