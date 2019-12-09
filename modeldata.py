"""
数据处理模块
"""
import difflib
import pymysql
import hashlib
import speech_recognition as sr
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


    def save1and2(self,name,single,multy):
        sql = "UPDATE results SET single_result = {},multy_result={} where name = '{}';".format(single,multy,name)
        try:
            r = self.cur.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def save_wav(self,name):
        with open('recv\\'+name+'.wav','rb') as f:
            data = f.read()
        # try:
        #     sql = "update results set soundfile='{}' where name='{}';".format(data,name)
        #     print(sql)
        #     self.cur.execute(sql)
        #     db.commit()
        # except:
        #     db.rollback()

        try:
            sql = "update results set sound_file=%s where name=%s;"
            # sql = "update results set soundfile=%s where name=%s;"
            self.cur.execute(sql, [data,name])
            self.db.commit()
        except:
            self.db.rollback()


    # 根据随机数抽题

    def query(self,rand_num,table_name):
        if table_name == 'reader':
            sql = "select question from "+table_name+ " where id=%s;"
        else:
            sql = "select question,answer_1,answer_2,answer_3,answer_4 from "+table_name+ " where id=%s;"
        self.cur.execute(sql,[rand_num])
        r = self.cur.fetchone()
        if r:
            return r

    def insert_history(self,name,rint):

        #sql = "insert into results (name,rand_int) values (%s,%d);"
        sql = "insert into results (name,rand_int) values ('{}',{});".format(name,rint)
        print(sql)
        try:
            # self.cur.execute(sql,[name,rint])
            self.cur.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def wavtotext(self,wav_file):
        r = sr.Recognizer()
        harvard = sr.AudioFile(wav_file)
        with harvard as source:
            audio = r.record(source)
        try:
            return r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            return ("")
        except sr.RequestError as e:
            return ("")

    def get_equal_rate_1(self,str1,str2):
        return difflib.SequenceMatcher(None, str1,str2).quick_ratio()

    def gettrue(self,name):
        sql = "select rand_int from results where name='{}';".format(name)
        self.cur.execute(sql)
        true_id = self.cur.fetchone()[0]
        sql = "select correct from single where id={};".format(true_id)
        self.cur.execute(sql)
        true_single = self.cur.fetchone()[0]
        sql = "select correct from multy where id={};".format(true_id)
        self.cur.execute(sql)
        true_multy = self.cur.fetchone()[0]
        sql = "select question from reader where id={};".format(true_id)
        self.cur.execute(sql)
        true_reader = self.cur.fetchone()[0]
        result = true_single+"|"+true_multy+"|"+true_reader
        print(result)
        if result:
            return result
        else:
            return ""

if __name__ == '__main__':
    db = Database(database='bluedark')
    cu = db.create_cur()
    # db.insert_history('ni',3)
    db.gettrue('ta')
    s = db.gettrue(1)[0]
#    print(s)






