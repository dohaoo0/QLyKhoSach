from abc import abstractmethod


class Phieu:
    def __init__(self, ma_phieu=None, ngay_nhap=None, nguoi_nhap_phieu=None, ma_sach=None, so_luong=None, gia=None):
        self.ma_phieu = ma_phieu
        self.ngay_nhap = ngay_nhap
        self.nguoi_nhap_phieu = nguoi_nhap_phieu
        self.ma_sach = ma_sach
        self.so_luong = so_luong
        self.gia = gia

    @abstractmethod
    def insert(self):
        raise NotImplementedError("Define abstractmethod 'insert_data'")

    @abstractmethod
    def update(self):
        raise NotImplementedError("Define abstractmethod 'update_data'")

    @abstractmethod
    def delete(self, id_delete):
        raise NotImplementedError("Define abstractmethod 'delete'")

    @abstractmethod
    def search(self, id_search):
        raise NotImplementedError("Define abstractmethod 'search'")
