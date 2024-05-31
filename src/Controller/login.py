import multiprocessing
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from src.Model.check import Check
from src.Controller.main import Main


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.result = None
        self.ui = uic.loadUi(r"src\View\login.ui", self)
        self.login_id = self.ui.login_id
        self.login_pw = self.ui.login_pw
        self.login_button = self.ui.login_button
        self.login_button.clicked.connect(lambda: self.on_login_button_clicked)

    def get_show_win(self):
        return self.result

    def on_login_button_clicked(self):
        login_id = self.login_id.text().strip()
        login_pw = self.login_pw.text().strip()

        nv = Check()
        self.result = nv.check(login_id, login_pw)
        if self.result is False:
            title = "Đăng nhập không thành công"
            log = "Vui lòng kiểm tra lại thông tin"
            self.show_log(title, log)
        else:
            # self.hide()
            self.close()

    @staticmethod
    def show_log(title, log):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(log)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.exec()

    # def closeEvent(self, event):
    #     msg_box = QMessageBox()
    #     msg_box.setWindowTitle("Thông báo")
    #     msg_box.setText("<font color = red >Bạn có muốn thoát ứng dụng? </font >")
    #     msg_box.setStandardButtons(
    #         QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
    #     msg_box.setStyleSheet("background-color: rgb(241, 241, 241);")
    #     ret = msg_box.exec()
    #     if ret == QtWidgets.QMessageBox.StandardButton.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
    result = window.get_show_win()
    apps = QtWidgets.QApplication(sys.argv)
    if result:
        window_main = Main()
        window_main.show()
        if result is True:
            window_main.tab.removeTab(4)
    apps.exec()
