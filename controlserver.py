import random
from socket import *
from multiprocessing import Process
import sys
from time import sleep
from multiprocessing import Pool
from modeldata import Database

"""
逻辑处理模块
"""

# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

# 链接数据库
db = Database(user='root',password='123456',database='bluedark')

#　处理登录
def do_login(c,name,passwd):
    if db.do_login(name,passwd):
        c.send(b'OK')  # 告诉客户端一下结果
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
    return a_qtn
# 具体处理客户端请求
def handle(c):
    db.create_cur() # 每个子进程单独生成自己的游标对象
    # 循环接收来自客户端的请求，然后调用相应的函数进行处理
    the_name=''
    the_ran_int = 0
    while True:
        data = c.recv(1024).decode()
        # print(c.getpeername(),':',data)
        tmp = data.split(' ') # 解析请求
        if not data or tmp[0] == 'E':
            return

        elif tmp[0] == 'L':
            # L name passwd
            the_name=tmp[1]
            print(the_name+'登录成功！')
            do_login(c,tmp[1],tmp[2])
            the_ran_int=do_sendQuestion(c) #登录，随即发试题给客户端
            db.insert_history(the_name,the_ran_int)
            print('给%s发送第%d套试题。'%(the_name,the_ran_int))
            # sleep(0.1)

            # c.close()
            return
        elif tmp[0] == 'C':#交卷
            #tmp[1]\tmp[2]\temp[3]存入数据库,传入the_name
            if db.save1and2(tmp[1], tmp[2],tmp[3]):
                c.send(b'OK')  # 告诉客户端一下结果
            else:
                c.send(b'Fail')
                return
            do_saveResult(c,tmp[1],tmp[2],tmp[3],the_ran_int)

            return

def do_saveResult(con,one_name,single,multy,the_rint):
    #先将单选题和多选题的答题写入数据库
    # db.saveResult(single,multy)
    filename='recv\\'+one_name+'.wav'
    f = open(filename, 'wb')
    score=0

    while True:
        # 边收取内容,边写入文件
        data = con.recv(1024)
        if data == b'##':
            break  # 文件发送完毕
        f.write(data)
    f.close()
    b = db.gettrue(one_name)
    c=b.split("|")
    if c[0]==single:
        score+=25
    if c[1]==multy:
        score+=25
    # print(c[2])
    # print(type(b))
    a = db.wavtotext(filename)
    print("识别结果%s" % (a))
    #
    third_score = db.get_equal_rate_1(a,c[2])
    print(third_score)
    score+=third_score*50
    db.save_wav(one_name)
    msg = "%d" % (score)
    con.send(msg.encode())
    print("%d得分%d" %(one_name,score))
    return score



# 启动函数
def main():
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)
    print('服务器已启动')
    pool = Pool(4)
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
        #p = Process(target=handle,args=(c,))
        p = pool.apply_async(func=handle, args=(c,))
        #p.daemon = True
        #p.start()
        #p.join()
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()


