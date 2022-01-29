import sqlite3
from datetime import  datetime, timedelta
class DBUser:
    def __init__(self, db_name):
        self.conn=sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory=sqlite3.Row

    # DB bilan aloqani amalga oshiradi
    def db_exequite(self, sql, commit=False, fetchone=False, fechall=False):
        self.conn=sqlite3.connect('Data_base.db', check_same_thread=False)
        connection =self.conn
        cursor = connection.cursor()
        data=None
        cursor.execute(sql)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fechall:
            data = cursor.fetchall()

        connection.close()

        return data

     # Foydalanuvchi ma'lumotlar bazasida bor yoki yo'qligini tekshiradigan funksiya
    def check_user(self, id):
        sql = f"SELECT id FROM Users WHERE id={id}"
        res=self.db_exequite(sql,fechall=True)
        if len(res)==0: return True
        else : return False

    # Faydalanuvchilarni qo'shuvchi funksiya
    def add_user(self, id, phone, name):
        sql = f""" INSERT INTO Users VALUES( {id}, '{name}', {phone},"empty" )"""
        self.db_exequite(sql,commit=True)

    # Foydalanuvchilarni bazadan o'chiradi
    def delete_user(self, id):
        sql= f""" DELETE FROM Users WHERE id={id} """
        self.db_exequite(sql,True)

    def get_user(self):
        sql=""" SELECT id FROM Users WHERE position="empty" """
        if self.db_exequite(sql,fetchone=True)==None:
            return 0
        else:
            return self.db_exequite(sql,fetchone=True)[0]

    def set_position(self, id, position):
        sql = f""" UPDATE Users
                    SET position="{position}"
                    WHERE id={id} """
        self.db_exequite(sql,commit=True)

    def get_position(self,id):
        sql = f""" SELECT position FROM Users WHERE id={id}"""
        return self.db_exequite(sql, fetchone=True)[0]

    def get_user_name(self, id):
        sql = f""" SELECT name FROM Users WHERE id={id}"""
        return self.db_exequite(sql, fetchone=True)[0]

    def get_user_number(self, id):
        sql = f""" SELECT number FROM Users WHERE id={id}"""
        return self.db_exequite(sql, fetchone=True)[0]

    # Hamma foydalanuvchilarni id sini olib beraqdi
    def get_all_users(self):
        sql = """ SELECT id FROM Users """
        return self.db_exequite(sql, fechall=True)

    # qancha foydalanuvchi borligini qaytaradi
    def get_count_users(self):
        sql = " SELECT COUNT(id) FROM Users "
        return self.db_exequite(sql, fetchone=True)[0]
    
        # ===========================Money part=============================
    def add_money(self, id, name, comment, way):
        time=str(datetime.now()+timedelta(hours=5))[:-7]
        sql= f""" INSERT INTO Money VALUES("{name}", 0, "{comment}","{time}", "{self.get_position(id)}") """
        self.set_position(id,time)
        self.db_exequite(sql,True)
    # summaning miqdorini o'zgarrtirish uchun
    def set_value(self, time, value):
        sql = f""" UPDATE Money
                    SET value={value}
                    WHERE time="{time}" """
        self.db_exequite(sql,commit=True)
    
    def get_dayly(self):
        time=str(datetime.now()+timedelta(hours=5))[:10]
        sql = f""" SELECT * FROM Money WHERE time like "{time}%" """
        return self.db_exequite(sql,fechall=True)
    
    def get_monthly(self):
        time=str(datetime.now()+timedelta(hours=5))[:7]
        sql = f""" SELECT * FROM Money WHERE time like "{time}%" """
        return self.db_exequite(sql,fechall=True)
    
    def get_income(self):
        sql = """ SELECT SUM(value) FROM Money WHERE way="come";"""
        return self.db_exequite(sql,fetchone=True)[0]
    
    def get_expense(self):
        sql = """ SELECT SUM(value) FROM Money WHERE way="gone";"""
        return self.db_exequite(sql,fetchone=True)[0]

    def get_dayly_income(self):
        time=str(datetime.now()+timedelta(hours=5))[:10]
        sql = f""" SELECT SUM(value) FROM Money WHERE way="come" AND time like "{time}%" """
        return self.db_exequite(sql,fetchone=True)[0]

    def get_monthly_income(self):
        time=str(datetime.now()+timedelta(hours=5))[:7]
        sql = f""" SELECT SUM(value) FROM Money WHERE way="come" AND time like "{time}%" """
        return self.db_exequite(sql,fetchone=True)[0]

    def get_dayly_expense(self):
        time=str(datetime.now()+timedelta(hours=5))[:10]
        sql = f""" SELECT SUM(value) FROM Money WHERE way="gone" AND time like "{time}%" """
        return self.db_exequite(sql,fetchone=True)[0]

    def get_monthly_expense(self):
        time=str(datetime.now()+timedelta(hours=5))[:7]
        sql = f""" SELECT SUM(value) FROM Money WHERE way="gone" AND time like "{time}%" """
        return self.db_exequite(sql,fetchone=True)[0]
    
    def clear_db(self):
        sql = "DELETE FROM Money"
        self.db_exequite(sql, True)
