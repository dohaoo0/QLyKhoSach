class Kho:
    @staticmethod
    def search(search_id):
        search_query = f"SELECT k.ma_sach, k.ten, SUM(nk.so_luong) - SUM(xk.so_luong) \
                            FROM kho k left join nhapkho nk on k.ma_sach = nk.ma_sach \
                                        left JOIN xuatkho xk ON nk.ma_sach = xk.ma_sach WHERE k.ma_sach = '{search_id}'\
                            GROUP BY k.ma_sach, k.ten;"
        return search_query
