class Nhanvien:
    def __init__(self, ma=None, ten=None, matkhau=None, vitri=None):
        self.ma = ma
        self.ten = ten
        self.matkhau = matkhau
        self.vitri = vitri

    def insert(self):
        insert_query = f"INSERT INTO nhanvien (ma_nhan_vien, ten, mat_khau, vi_tri) VALUES\
                        '{self.ma}', '{self.ten}', '{self.matkhau}', '{self.vitri}';"
        return insert_query

    def update(self):
        update_query = f"UPDATE nhanvien SET\
                ma_nhan_vien='{self.ma_phieu}', ten='{self.ten}', mat_khau = '{self.matkhau}', vi_tri = '{self.vitri}';"
        return update_query

    @staticmethod
    def delete(id_delete):
        delete_query = f"DELETE FROM nhanvien WHERE ma_nhan_vien = '{id_delete}';"
        return delete_query

    @staticmethod
    def search(id_search):
        id_search = int(id_search)
        search_query = f"  SELECT * FROM nhanvien WHERE ma_nhan_vien = '{id_search}';"
        return search_query
