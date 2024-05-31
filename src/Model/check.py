from src.Model.connect_db import ConnectDB


class Check:
    def __init__(self, ma=None, matkhau=None):
        self.ma = ma
        self.matkhau = matkhau

    @staticmethod
    def check(ma, matkhau):
        conn = ConnectDB()
        conn.connect()

        nhanvien = conn.execute_query("""SELECT * FROM nhanvien;""")

        for nv in nhanvien:
            if int(ma) == nv[0] and matkhau == nv[2]:
                if nv[3] == "Quan ly":
                    return "Quan ly"
                return True
        return False