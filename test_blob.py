"""
存储二进制文件
"""

import  pymysql

#  链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='bluedark',
                     charset='utf8')

# 生成游标对象 (用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

# 存储文件
with open('./send/ni.wav','rb') as f:
    data = f.read()
try:
    sql = "update cls1 set img=%s where id=9;"
    cur.execute(sql,[data])
    db.commit()
except:
    db.rollback()

# 读取文件
# sql = "select img from cls1 where name='Tony';"
# cur.execute(sql)
# data = cur.fetchone()
# with open('Tony.gif','wb') as f:
#     f.write(data[0])

# 关闭游标和数据库链接
cur.close()
db.close()



