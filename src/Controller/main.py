import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import pyqtSlot
from PyQt6 import uic

from src.Model.connect_db import ConnectDB
from src.Model.nhapkho import Nhapkho
from src.Model.xuatkho import Xuatkho
from src.Model.nhanvien import Nhanvien
from src.Model.sach import Sach
from src.Model.tablemodel import TableModel
from src.Model.kho import Kho


class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(r"src/View/new_win.ui", self)
        self.conn = ConnectDB()
        self.conn.connect()
        self.model = None

        # Tồn kho
        self.pro_input_id = self.ui.pro_input_id
        self.pro_input_name = self.ui.pro_input_name
        self.pro_input_author = self.ui.pro_input_author
        self.pro_input_price = self.ui.pro_input_price
        self.pro_input_year = self.ui.pro_input_year
        self.pro_input_search = self.ui.pro_input_search

        self.pro_button_add = self.ui.pro_button_add
        self.pro_button_add.clicked.connect(lambda: self.on_pro_button_add_clicked)
        self.pro_button_update = self.ui.pro_button_update
        self.pro_button_update.clicked.connect(lambda: self.on_pro_button_update_clicked)
        self.pro_button_search = self.ui.pro_button_search
        self.pro_button_search.clicked.connect(lambda: self.on_pro_button_search_clicked)
        self.pro_button_delete = self.ui.pro_button_delete
        self.pro_button_delete.clicked.connect(lambda: self.on_pro_button_delete_clicked)

        self.pro_table_view = self.ui.pro_table_view
        self.pro_show_data()

        # Nhập kho
        self.import_input_id = self.ui.import_input_id
        self.import_input_date = self.ui.import_input_date
        self.import_input_user = self.ui.import_input_user
        self.import_input_search = self.ui.import_input_search

        self.import_pro_id = self.ui.import_pro_id
        self.import_pro_quantity = self.ui.import_pro_quantity
        self.import_pro_price = self.ui.import_pro_price

        self.import_button_add = self.ui.import_button_add
        self.import_button_add.clicked.connect(lambda: self.on_import_button_add_clicked)
        self.import_button_update = self.ui.import_button_update
        self.import_button_update.clicked.connect(lambda: self.on_import_button_update_clicked)
        self.import_button_search = self.ui.import_button_search
        self.import_button_search.clicked.connect(lambda: self.on_import_button_search_clicked)
        self.import_button_delete = self.ui.import_button_delete
        self.import_button_delete.clicked.connect(lambda: self.on_import_button_delete_clicked)

        self.import_table_view = self.ui.import_table_view
        self.import_show_data()

        # Xuất kho
        self.export_input_id = self.ui.export_input_id
        self.export_input_date = self.ui.export_input_date
        self.export_input_user = self.ui.export_input_user
        self.export_pro_id = self.ui.export_pro_id
        self.export_pro_quantity = self.ui.export_pro_quantity
        self.export_pro_price = self.ui.export_pro_price
        self.export_input_search = self.ui.export_input_search

        self.export_button_add = self.ui.export_button_add
        self.export_button_add.clicked.connect(lambda: self.on_export_button_add_clicked)
        self.export_button_update = self.ui.export_button_update
        self.export_button_update.clicked.connect(lambda: self.on_export_button_update_clicked)
        self.export_button_delete = self.ui.export_button_delete
        self.export_button_delete.clicked.connect(lambda: self.on_export_button_delete_clicked)
        self.export_button_search = self.ui.export_button_search
        self.export_button_search.clicked.connect(lambda: self.on_export_button_search_clicked)

        self.export_table_view = self.ui.export_table_view
        self.export_show_data()

        # Người dùng
        self.user_input_id = self.ui.user_input_id
        self.user_input_name = self.ui.user_input_name
        self.user_input_role = self.ui.user_input_role
        self.user_input_pw = self.ui.user_input_pw
        self.user_input_search = self.ui.user_input_search

        self.user_button_add = self.ui.user_button_add
        self.user_button_add.clicked.connect(lambda: self.on_user_button_add_clicked)
        self.user_button_update = self.ui.user_button_update
        self.user_button_update.clicked.connect(lambda: self.on_user_button_update_clicked)
        self.user_button_delete = self.ui.user_button_delete
        self.user_button_delete.clicked.connect(lambda: self.on_user_button_delete_clicked)
        self.user_button_search = self.ui.user_button_search
        self.user_button_search.clicked.connect(lambda: self.on_user_button_search_clicked)

        self.user_table_view = self.ui.user_table_view
        self.user_show_data()

        # Kho
        self.storehouse_input_search = self.ui.storehouse_input_search
        self.storehouse_button_search = self.ui.storehouse_button_search
        self.storehouse_button_search.clicked.connect(lambda: self.on_storehouse_button_search_clicked)
        self.storehouse_table_view = self.ui.storehouse_table_view
        self.storehouse_show_data()

        # tab
        self.tab = self.ui.tabWidget

    def storehouse_show_data(self):
        show_query = "SELECT k.ma_sach, k.ten, SUM(nk.so_luong) - SUM(xk.so_luong) \
                        FROM kho k left join nhapkho nk on k.ma_sach = nk.ma_sach \
                        left JOIN xuatkho xk ON nk.ma_sach = xk.ma_sach \
                        GROUP BY  k.ma_sach, k.ten;"
        table_data = self.conn.execute_query(show_query)
        if len(table_data) > 0:
            table_data_new = []
            for data in table_data:
                data_new = list(data)
                if data_new[2] is None:
                    data_new[2] = 0
                else:
                    data_new[2] = int(data_new[2])
                table_data_new.append(data_new)
            self.model = None
            header = ["Mã sách", "Tên sách", "Tồn kho"]
            self.model = TableModel(table_data_new, header)
            self.storehouse_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.storehouse_table_view.horizontalHeader().setStretchLastSection(True)
            self.storehouse_table_view.setModel(self.model)

    @pyqtSlot()
    def on_storehouse_button_search_clicked(self):
        storehouse = Kho()
        storehouse_id = self.storehouse_input_search.text().strip()
        storehouse_search = storehouse.search(storehouse_id)
        table_data = self.conn.execute_query(storehouse_search)
        if len(table_data) > 0:
            table_data_new = []
            for data in table_data:
                data_new = list(data)
                if data_new[2] is None:
                    data_new[2] = 0
                else:
                    data_new[2] = int(data_new[2])
                table_data_new.append(data_new)
            self.model = None
            header = ["Mã sách", "Tên sách", "Tồn kho"]
            self.model = TableModel(table_data_new, header)
            self.storehouse_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.storehouse_table_view.horizontalHeader().setStretchLastSection(True)
            self.storehouse_table_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    def get_data_pro(self):
        pro_input_id = self.pro_input_id.text().strip()
        pro_input_name = self.pro_input_name.text().strip()
        pro_input_author = self.pro_input_author.text().strip()
        pro_input_price = self.pro_input_price.text().strip()
        pro_input_year = self.pro_input_year.text().strip()

        book = Sach(pro_input_id, pro_input_name, pro_input_author, pro_input_year, pro_input_price)
        return book

    def pro_show_data(self):
        show_query = "select * from sach;"
        table_data = self.conn.execute_query(show_query)
        if len(table_data) > 0:
            self.model = None
            header = ["Mã sách", "Tên sách", "Tác giả", "Năm phát hành", "Giá bìa"]
            self.model = TableModel(table_data, header)
            self.pro_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.pro_table_view.horizontalHeader().setStretchLastSection(True)
            self.pro_table_view.setModel(self.model)

    @pyqtSlot()
    def on_pro_button_add_clicked(self):
        book = self.get_data_pro()

        add_book = book.insert()
        self.conn.execute_query(add_book, fetch=False)

        title = "Thông báo"
        log = "Đã thêm thông tin sách thành công"
        self.show_log(title, log)

    @pyqtSlot()
    def on_pro_button_update_clicked(self):
        book = self.get_data_pro()

        update_book = book.update_data()
        self.conn.execute_query(update_book, fetch=False)
        title = "Thông báo"
        log = "Đã sửa thông tin thành công"
        self.show_log(title, log)

    @pyqtSlot()
    def on_pro_button_search_clicked(self):
        book = self.get_data_pro()
        search_id = self.pro_input_search.text().strip()

        search_book = book.search(search_id)
        table_data = self.conn.execute_query(search_book)
        if len(table_data) > 0:
            self.model = None
            header = ["Mã sáchh", "Tên sách", "Tác giả", "Năm phát hành", "Giá bìa"]
            self.model = TableModel(table_data, header)
            self.pro_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.pro_table_view.horizontalHeader().setStretchLastSection(True)
            self.pro_table_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    @pyqtSlot()
    def on_pro_button_delete_clicked(self):
        book = self.get_data_pro()
        book_id = self.pro_input_search.text().strip()
        book_delete = book.delete(book_id)
        self.conn.execute_query(book_delete, fetch=False)

        title = "Thông báo"
        log = "Đã xóa thông tin sách"
        self.show_log(title, log)

    def get_data_user(self):
        user_input_id = self.user_input_id.text().strip()
        user_input_name = self.user_input_name.text().strip()
        user_input_role = self.user_input_role.text().strip()
        user_input_pw = self.user_input_pw.text().strip()

        user = Nhanvien(user_input_id, user_input_name, user_input_pw, user_input_role)
        return user

    def user_show_data(self):
        show_query = "select * from nhanvien;"
        table_data = self.conn.execute_query(show_query)
        if len(table_data) > 0:
            self.model = None
            header = ["Mã nhân viên", "Tên nhân viên", "Mật khẩu", "Vị trí"]
            self.model = TableModel(table_data, header)

            self.user_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.user_table_view.horizontalHeader().setStretchLastSection(True)
            self.user_table_view.setModel(self.model)

    @pyqtSlot()
    def on_user_button_add_clicked(self):
        user = self.get_data_user()

        user_add = user.insert()
        self.conn.execute_query(user_add, fetch=False)

        title = "Thông báo"
        log = "Đã thêm thông tin thành công"
        self.show_log(title, log)

    @pyqtSlot()
    def on_user_button_update_clicked(self):
        user = self.get_data_user()

        user_update = user.update()
        self.conn.execute_query(user_update, fetch=False)

        title = "Thông báo"
        log = "Đã sửa thông tin"
        self.show_log(title, log)

    @pyqtSlot()
    def on_user_button_delete_clicked(self):
        user = self.get_data_user()
        user_id = self.user_input_search.text().strip()
        user_delete = user.delete(user_id)
        self.conn.execute_query(user_delete, fetch=False)

        title = "Thông báo"
        log = "Đã xóa thông tin"
        self.show_log(title, log)

    @pyqtSlot()
    def on_user_button_search_clicked(self):
        user = Nhanvien()
        user_id = self.user_input_search.text().strip()
        user_search = user.search(user_id)
        table_data = self.conn.execute_query(user_search)
        if len(table_data) > 0:
            self.model = None
            header = ["Mã nhân viên", "Tên nhân viên", "Mật khẩu", "Vị trí"]
            self.model = TableModel(table_data, header)

            self.user_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.user_table_view.horizontalHeader().setStretchLastSection(True)
            self.user_table_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    def import_show_data(self):
        show_query = "  SELECT * FROM nhapkho order by ma_phieu_nhap asc;"
        table_data = self.conn.execute_query(show_query)
        if len(table_data) > 0:
            self.model = None
            header = ["Mã phiếu nhập", "Ngày nhập", "Người nhập", "Mã sách", "Số lượng", "Giá nhập"]
            self.model = TableModel(table_data, header)
            self.import_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.import_table_view.horizontalHeader().setStretchLastSection(True)
            self.import_table_view.setModel(self.model)

    def import_get_data(self):
        import_input_id = self.import_input_id.text().strip()
        import_input_date = self.import_input_date.text().strip()
        import_input_user = self.import_input_user.text().strip()
        import_pro_id = self.import_pro_id.text().strip()
        import_pro_quantity = self.import_pro_quantity.text().strip()
        import_pro_price = self.import_pro_price.text().strip()
        import_data = Nhapkho(import_input_id, import_input_date, import_input_user,
                              import_pro_id, import_pro_quantity, import_pro_price)
        return import_data

    @pyqtSlot()
    def on_import_button_add_clicked(self):
        import_data = self.import_get_data()
        import_add = import_data.insert()
        self.conn.execute_query(import_add, fetch=False)
        title = "Thông báo"
        log = "Đã thêm thông tin thành công"
        self.show_log(title, log)

    @pyqtSlot()
    def on_import_button_update_clicked(self):
        import_data = self.import_get_data()
        import_update = import_data.update()
        self.conn.execute_query(import_update, fetch=False)
        title = "Thông báo"
        log = "Đã sửa thông tin"
        self.show_log(title, log)

    @pyqtSlot()
    def on_import_button_search_clicked(self):
        import_data = Nhapkho()
        import_id = self.import_input_search.text().strip()
        import_search = import_data.search(import_id)
        table_data = self.conn.execute_query(import_search)
        if len(table_data) > 0:
            self.model = None
            header = ["Mã phiếu nhập", "Ngày nhập", "Người nhập", "Mã sách", "Số lượng", "Giá nhập"]
            self.model = TableModel(table_data, header)
            self.import_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.import_table_view.horizontalHeader().setStretchLastSection(True)
            self.import_table_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    @pyqtSlot()
    def on_import_button_delete_clicked(self):
        import_data = Nhapkho()
        import_id = self.import_input_search.text().strip()
        import_delete = import_data.search(import_id)
        self.conn.execute_query(import_delete, fetch=False)
        title = "Thông báo"
        log = "Đã xóa thông tin"
        self.show_log(title, log)

    def export_show_data(self):
        show_query = "  SELECT * FROM xuatkho order by ma_phieu_xuat asc;"
        table_data = self.conn.execute_query(show_query)
        if len(table_data) > 0:
            self.model = None
            header = ["Mã phiếu xuất", "Ngày xuất", "Người xuất", "Mã sách", "Số lượng", "Giá xuất"]
            self.model = TableModel(table_data, header)
            self.export_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.export_table_view.horizontalHeader().setStretchLastSection(True)
            self.export_table_view.setModel(self.model)

    def get_data_export(self):
        export_input_id = self.export_input_id.text().strip()
        export_input_date = self.export_input_date.text().strip()
        export_input_user = self.export_input_user.text().strip()

        export_pro_id = self.export_pro_id.text().strip()
        export_pro_quantity = self.export_pro_quantity.text().strip()
        export_pro_price = self.export_pro_price.text().strip()

        export = Xuatkho(export_input_id, export_input_date, export_input_user,
                         export_pro_id, export_pro_quantity, export_pro_price)
        return export

    @pyqtSlot()
    def on_export_button_add_clicked(self):
        export = self.get_data_export()
        export_add = export.insert()
        self.conn.execute_query(export_add, fetch=False)

        title = "Thông báo"
        log = "Đã thêm thông tin"
        self.show_log(title, log)

    @pyqtSlot()
    def on_export_button_update_clicked(self):
        export = self.get_data_export()
        export_update = export.update()
        self.conn.execute_query(export_update, fetch=False)

        title = "Thông báo!"
        log = "Đã sửa thông tin thành công."
        self.show_log(title, log)

    def on_export_button_delete_clicked(self):
        export = Xuatkho()
        delete_id = self.export_input_search.text().strip()
        delete = export.delete(delete_id)
        self.conn.execute_query(delete, fetch=False)

        title = "Thông báo!"
        log = "Đã xóa thành công."
        self.show_log(title, log)

    @pyqtSlot()
    def on_export_button_search_clicked(self):
        export = Xuatkho()
        search_id = self.export_input_search.text().strip()
        search = export.search(search_id)
        table_data = self.conn.execute_query(search)
        if len(table_data) > 0:
            self.model = None
            header = ["Mã phiếu xuất", "Ngày xuất", "Người xuất", "Mã sách", "Số lượng", "Giá xuất"]
            self.model = TableModel(table_data, header)
            self.export_table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.export_table_view.horizontalHeader().setStretchLastSection(True)
            self.export_table_view.setModel(self.model)
        else:
            title = "Thông báo"
            log = "Không tìm thấy"
            self.show_log(title, log)

    @staticmethod
    def show_log(title, log):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setInformativeText(log)
        msg.setIcon(QMessageBox.Icon.Information)

        # Hiển thị hộp thông báo
        msg.exec()

    def closeEvent(self, event):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText("<font color = red >Bạn có muốn thoát ứng dụng? </font >")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg_box.setStyleSheet("background-color: rgb(241, 241, 241);")
        ret = msg_box.exec()
        if ret == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
