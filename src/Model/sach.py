class Sach:
    def __init__(self, ma=None, ten=None, tacgia=None, namsx=None, giabia=None):
        self.ma = ma
        self.ten = ten
        self.tacgia = tacgia
        self.namsx = namsx
        self.giabia = giabia

    def insert(self):
        insert_query = f"INSERT INTO sach (ma_sach, ten, tac_gia, nam_phat_hanh, gia_bia) VALUES\
                       ('{self.ma}', '{self.ten}', '{self.tacgia}', '{self.namsx}', '{self.giabia}');"
        return insert_query

    @staticmethod
    def delete(ma_sach):
        delete_query = f"DELETE FROM sach WHERE ma_sach = '{ma_sach}';"
        return delete_query

    def update_data(self):
        update_query = f"UPDATE sach SET\
                            ma_sach = '{self.ma}', ten = '{self.ten}', tacgia = '{self.tacgia}',\
                            nam_phat_hanh = '{self.namsx}', gia_bia = '{self.giabia}';"
        return update_query

    @staticmethod
    def search(search_id):
        search_query = f"SELECT * FROM Sach where ma_sach = '{search_id}';"
        return search_query
