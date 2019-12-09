# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import time
from myclock import Clock
from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
from record import Recorder
ADDR = ('127.0.0.1', 8000)

class Ui_Form(object):
    def __init__(self):
        super().__init__()


        self.rec = Recorder()
        # self.clo = Clock()

    def fill_single(self, d):
        tmp = d.split(' : ')
        self.first.setText(tmp[0])
        self.radioBtn_1_A.setText(tmp[1])
        self.radioBtn_1_B.setText(tmp[2])
        self.radioBtn_1_C.setText(tmp[3])
        self.radioBtn_1_D.setText(tmp[4])

    def fill_multy(self, d):
        tmp = d.split(' : ')
        self.second.setText(tmp[0])
        self.checkBox_1_A.setText(tmp[1])
        self.checkBox_1_B.setText(tmp[2])
        self.checkBox_1_C.setText(tmp[3])
        self.checkBox_1_D.setText(tmp[4])

    def fill_read(self,d):
        self.third.setText(d)

    def setupUi(self, Form):
        # self.button_clicked_signal = pyqtSignal()
        Form.setObjectName("Form")
        Form.resize(1272, 749)

        #交卷
        self.closeWinBtn = QtWidgets.QPushButton(Form)
        self.closeWinBtn.setGeometry(QtCore.QRect(1060, 680, 93, 28))
        self.closeWinBtn.setObjectName("closeWinBtn")
        self.closeWinBtn.clicked.connect(self.do_submit)
        #试题
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 731, 711))
        self.groupBox.setObjectName("groupBox")
        self.first = QtWidgets.QLabel(self.groupBox)
        self.first.setGeometry(QtCore.QRect(20, 30, 911, 20))
        self.first.setObjectName("first")
        self.second = QtWidgets.QLabel(self.groupBox)
        self.second.setGeometry(QtCore.QRect(20, 210, 911, 16))
        self.second.setObjectName("second")
        self.third = QtWidgets.QLabel(self.groupBox)
        self.third.setGeometry(QtCore.QRect(20, 430, 901, 16))
        self.third.setObjectName("third")
        #录音
        self.startButton = QtWidgets.QPushButton(self.groupBox)
        self.startButton.setGeometry(QtCore.QRect(100, 630, 93, 28))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.do_startRecord)
        self.stopButton = QtWidgets.QPushButton(self.groupBox)
        self.stopButton.setGeometry(QtCore.QRect(520, 630, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.do_stopRecord)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(71, 71, 531, 99))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioBtn_1_A = QtWidgets.QRadioButton(self.widget)
        self.radioBtn_1_A.setObjectName("radioBtn_1_A")
        self.verticalLayout.addWidget(self.radioBtn_1_A)
        self.radioBtn_1_B = QtWidgets.QRadioButton(self.widget)
        self.radioBtn_1_B.setObjectName("radioBtn_1_B")
        self.verticalLayout.addWidget(self.radioBtn_1_B)
        self.radioBtn_1_C = QtWidgets.QRadioButton(self.widget)
        self.radioBtn_1_C.setObjectName("radioBtn_1_C")
        self.verticalLayout.addWidget(self.radioBtn_1_C)
        self.radioBtn_1_D = QtWidgets.QRadioButton(self.widget)
        self.radioBtn_1_D.setObjectName("radioBtn_1_D")
        self.verticalLayout.addWidget(self.radioBtn_1_D)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(71, 251, 531, 99))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_1_A = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_1_A.setObjectName("checkBox_1_A")
        self.verticalLayout_2.addWidget(self.checkBox_1_A)
        self.checkBox_1_B = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_1_B.setObjectName("checkBox_1_B")
        self.verticalLayout_2.addWidget(self.checkBox_1_B)
        self.checkBox_1_C = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_1_C.setObjectName("checkBox_1_C")
        self.verticalLayout_2.addWidget(self.checkBox_1_C)
        self.checkBox_1_D = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_1_D.setObjectName("checkBox_1_D")
        self.verticalLayout_2.addWidget(self.checkBox_1_D)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(770, 20, 431, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rec = Recorder()
        self.begin = 0
        #登录
        self.loginButton = QtWidgets.QPushButton(self.groupBox_2)
        self.loginButton.setGeometry(QtCore.QRect(280, 190, 93, 28))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.do_login)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 72, 15))
        self.label_5.setObjectName("label_5")
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.nameEdit.setGeometry(QtCore.QRect(210, 50, 113, 21))
        self.nameEdit.setObjectName("nameEdit")
        self.passwdEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.passwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdEdit.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.passwdEdit.setObjectName("passwdEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(770, 340, 431, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber.setGeometry(QtCore.QRect(23, 52, 381, 91))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display("...")
        self.retranslateUi(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "英语测试"))
        self.closeWinBtn.setText(_translate("Form", "交卷"))
        self.groupBox.setTitle(_translate("Form", "答题"))
        self.first.setText(_translate("Form", "单选题(25分)"))
        self.second.setText(_translate("Form", "多选题(25分)"))
        self.third.setText(_translate("Form", "朗读题(50分)"))
        self.startButton.setText(_translate("Form", "开始录音"))
        self.stopButton.setText(_translate("Form", "停止录音"))
        self.radioBtn_1_A.setText(_translate("Form", "RadioButton"))
        self.radioBtn_1_B.setText(_translate("Form", "RadioButton"))
        self.radioBtn_1_C.setText(_translate("Form", "RadioButton"))
        self.radioBtn_1_D.setText(_translate("Form", "RadioButton"))
        self.checkBox_1_A.setText(_translate("Form", "CheckBox"))
        self.checkBox_1_B.setText(_translate("Form", "CheckBox"))
        self.checkBox_1_C.setText(_translate("Form", "CheckBox"))
        self.checkBox_1_D.setText(_translate("Form", "CheckBox"))
        self.groupBox_2.setTitle(_translate("Form", "登录"))
        self.loginButton.setText(_translate("Form", "登录"))
        self.label_4.setText(_translate("Form", "准考证号"))
        self.label_5.setText(_translate("Form", "密    码"))
        self.groupBox_3.setTitle(_translate("Form", "得分"))

    def do_login(self):
        name = self.nameEdit.text()
        passwd = self.passwdEdit.text()
        msg = "L %s %s" % (name, passwd)
        s = socket()
        s.connect(ADDR)
        s.send(msg.encode())  # 发送请求
        data =s.recv(128).decode()
        if data == 'OK':
            self.groupBox_2.setTitle('登陆成功')
            self.loginButton.setEnabled(False)
            data = s.recv(4096).decode()
            self.fill_single(data)
            data = s.recv(4096).decode()
            self.fill_multy(data)
            data = s.recv(4096).decode()
            self.fill_read(data)
            #s.send('E'.encode())
        else:
            print("登录失败")
        s.close()

    def do_submit(self):

        a= 0
        b=0
        if self.radioBtn_1_A.isChecked():
            a=1
        elif self.radioBtn_1_B.isChecked():
            a=2
        elif self.radioBtn_1_C.isChecked():
            a=3
        elif self.radioBtn_1_D.isChecked():
            a=4
        if self.checkBox_1_A.isChecked():
            b=b^1
        if self.checkBox_1_B.isChecked():
            b=b^2
        if self.checkBox_1_C.isChecked():
            b = b ^ 4
        if self.checkBox_1_D.isChecked():
            b = b ^ 8
        name = self.nameEdit.text()

        # msg = "L %s %s" % (name, passwd)
        msg = "C %s %d %d" % (name,a, b)
        print(msg)
        s = socket()
        s.connect(ADDR)
        s.send(msg.encode())  # 发送请求
        data = s.recv(128).decode()
        if data == 'OK':
            try:
                f = open('send\\'+self.nameEdit.text()+'.wav', 'rb')
            except Exception:
                print("该文件不存在")
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    s.send(b'##')
                    break
                s.send(data)
            f.close()
        data = s.recv(128).decode()
        if data.isdigit():
            self.lcdNumber.display(data)
        s.send(b'##')
        s.close()


    def do_startRecord(self):
        self.begin = time.time()
        print("Start recording")
        self.rec.start()
        self.startButton.setEnabled(False)


    def do_stopRecord(self):
        self.rec.stop()
        fina = time.time()
        t = fina - self.begin
        print('录音时间为%ds' % t)
        self.rec.save("send\\"+self.nameEdit.text()+".wav")
        self.stopButton.setEnabled(False)
        return False
