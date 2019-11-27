import random

from dictdata import Database
# db = Database(database='bluedark')
        # db.create_cur()
        # name = self.nameEdit.text()
        # passwd = self.passwdEdit.text()
        # if db.do_login(name,passwd):
        #     self.groupBox_2.setTitle('登陆成功')
"""
逻辑处理模块
"""

from socket import *
from multiprocessing import Process
from signal import *
import sys


# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

# 链接数据库
db = Database(user='root',password='123456',database='bluedark')

# 处理注册
# def do_register(c,name,passwd):
#     if db.register(name,passwd):
#         c.send(b'OK')  # 告诉客户端一下结果
#     else:
#         c.send(b'Fail')

#　处理登录
def do_login(c,name,passwd):
    if db.do_login(name,passwd):
        c.send(b'OK')  # 告诉客户端一下结果
        #发送试题

    else:
        c.send(b'Fail')

# 单词查询
def do_sendQuestion(c):
    a_qtn = random.randint(1,5)
    question = db.query(a_qtn,'single')
    if not question:
        c.send('抽题失败'.encode())
    else:
        msg = "%s : %s : %s : %s : %s"%(question)
        c.send(msg.encode())

    question = db.query(a_qtn, 'multy')
    if not question:
        c.send('抽题失败'.encode())
    else:
        msg = "%s : %s : %s : %s : %s"%(question)
        c.send(msg.encode())
    question = db.query(a_qtn, 'reader')
    if not question:
        c.send('抽题失败'.encode())
    else:
        msg = "%s"%(question)
        c.send(msg.encode())

# 具体处理客户端请求
def handle(c):
    db.create_cur() # 每个子进程单独生成自己的游标对象
    # 循环接收来自客户端的请求，然后调用相应的函数进行处理
    the_name=''
    while True:
        data = c.recv(1024).decode()
        # print(c.getpeername(),':',data)
        tmp = data.split(' ') # 解析请求
        if not data or tmp[0] == 'E':
            return
     #登录，随即发试题给客户端
        elif tmp[0] == 'L':
            # L name passwd
            the_name=tmp[1]
            do_login(c,tmp[1],tmp[2])
            do_sendQuestion(c)
        elif tmp[0] == 'C':#交卷
            #tmp[1]\tmp[2]存入数据库,传入the_name
            do_saveResult(the_name,tmp[1],tmp[2],c)


def do_saveResult(one_name,single,multy,con):
    #先将单选题和多选题的答题写入数据库
    # db.saveResult(single,multy)
    f = open(one_name+'.wav', 'wb')
    while True:
        # 边收取内容,边写入文件
        data = con.recv(1024)
        if data == b'##':
            break  # 文件发送完毕
        f.write(data)
    f.close()

# 启动函数
def main():
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    # signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 循环等待客户端链接
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            db.close() # 关闭了数据库
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        #  有客户链接
        p = Process(target=handle,args=(c,))
        p.daemon = True
        p.start()
        #p.join()


if __name__ == '__main__':
    main()


