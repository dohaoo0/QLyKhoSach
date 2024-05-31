from src.Model.phieu import Phieu


class Xuatkho(Phieu):
    def __init__(self, ma_phieu=None, ngay_nhap=None, nguoi_nhap_phieu=None, ma_sach=None, so_luong=None, gia=None):
        super(Xuatkho, self).__init__(ma_phieu, ngay_nhap, nguoi_nhap_phieu, ma_sach, so_luong, gia)

    def insert(self):
        insert_query = f"INSERT INTO xuatkho (ma_phieu_xuat, ngay_xuat, nguoi_nhap, ma_sach, so_luong, gia_xuat) VALUES\
                        ('{self.ma_phieu}', '{self.ngay_nhap}', '{self.nguoi_nhap_phieu}', \
                        '{self.ma_sach}', '{self.so_luong}', '{self.gia}');"
        return insert_query

    def update(self):
        update_query = f"UPDATE xuatkho SET\
                    ma_phieu_xuat='{self.ma_phieu}', ngay_xuat='{self.ngay_nhap}', nguoi_nhap='{self.nguoi_nhap_phieu}',\
                    ma_sach = '{self.ma_sach}', so_luong = '{self.so_luong}', gia_xuat = '{self.gia}';"
        return update_query

    def delete(self, id_delete):
        delete_query = f"DELETE FROM xuatkho WHERE ma_phieu_xuat = '{id_delete}';"
        return delete_query

    def search(self, id_search):
        search_query = f"  SELECT * FROM xuatkho WHERE ma_phieu_xuat = '{id_search}';"
        return search_query
