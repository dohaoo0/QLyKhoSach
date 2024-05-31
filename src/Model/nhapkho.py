from src.Model.phieu import Phieu


class Nhapkho(Phieu):
    def __init__(self, ma_phieu=None, ngay_nhap=None, nguoi_nhap_phieu=None, ma_sach=None, so_luong=None, gia=None):
        super(Nhapkho, self).__init__(ma_phieu, ngay_nhap, nguoi_nhap_phieu, ma_sach, so_luong, gia)

    def insert(self):
        insert_query = f"INSERT INTO nhapkho (ma_phieu_nhap, ngay_nhap, nguoi_nhap, ma_sach, so_luong, gia_nhap) VALUES\
                        ('{self.ma_phieu}', '{self.ngay_nhap}', '{self.nguoi_nhap_phieu}', \
                        '{self.ma_sach}', '{self.so_luong}', '{self.gia}');"
        return insert_query

    def update(self):
        update_query = f"UPDATE nhapkho SET\
                ma_phieu_nhap='{self.ma_phieu}', ngay_nhap='{self.ngay_nhap}', nguoi_nhap='{self.nguoi_nhap_phieu}',\
                ma_sach = '{self.ma_sach}', so_luong = '{self.so_luong}', gia_nhap = '{self.gia}';"
        return update_query

    def delete(self, id_delete):
        delete_query = f"DELETE FROM nhapkho WHERE ma_phieu_nhap = '{id_delete}';"
        return delete_query

    def search(self, id_search):
        search_query = f"SELECT * FROM nhapkho WHERE ma_phieu_nhap = '{id_search}';"
        return search_query
