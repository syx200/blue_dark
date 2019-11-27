"""
数据处理模块
"""
import pymysql
import hashlib

#　密码转换函数
def change_passwd(passwd):
    salt = '*#06#'
    hash = hashlib.md5(salt.encode())  # 生成加密对象
    hash.update(passwd.encode())  # 算法加密处理
    passwd = hash.hexdigest()  # 获取加密后的字串
    return passwd

class Database:
    def __init__(self,host='localhost',port=3306,user=None,password=None,database=None,charset='utf8'):
        self.db = pymysql.connect(host=host,
                     port=port,
                     user=user,
                     password=password,
                     database=database,
                     charset=charset)
        self.cur = None

    def create_cur(self):
        self.cur = self.db.cursor()

    def close(self):
        if self.cur:
            self.cur.close()
        self.db.close()

    def register(self,name,passwd):
        # 判断该用户名是否存在
        sql = "select name from user where name='%s';"%name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return False
        # 插入用户
        passwd = change_passwd(passwd)
        try:
            sql="insert into user (name,passwd) values (%s,%s)"
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def do_login(self,name,passwd):
        passwd = change_passwd(passwd) #　转换密码

        # 和数据库信息进行比对
        sql = "select name,passwd from users where name=%s and passwd=%s;"
        self.cur.execute(sql,[name,passwd])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    # 查单词
    def query(self,rand_num,table_name):
        if table_name == 'reader':
            sql = "select question from "+table_name+ " where id=%s;"
        else:
            sql = "select question,answer_1,answer_2,answer_3,answer_4 from "+table_name+ " where id=%s;"
        self.cur.execute(sql,[rand_num])
        r = self.cur.fetchone()
        if r:
            return r

    def insert_history(self,name,word):
        sql = "insert into hist1 (name,word) values (%s,%s);"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except:
            self.db.rollback()

if __name__ == '__main__':
    db = Database(database='bluedark')
    cu = db.create_cur()
    s = db.query(1,'reader')
    print(s)






