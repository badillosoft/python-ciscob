# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import urllib
import urllib2
import json

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 403)
        self.txt_messages = QtWidgets.QPlainTextEdit(Form)
        self.txt_messages.setGeometry(QtCore.QRect(230, 10, 291, 281))
        self.txt_messages.setReadOnly(True)
        self.txt_messages.setObjectName("txt_messages")
        self.txt_user = QtWidgets.QLineEdit(Form)
        self.txt_user.setGeometry(QtCore.QRect(20, 100, 191, 22))
        self.txt_user.setObjectName("txt_user")
        self.txt_password = QtWidgets.QLineEdit(Form)
        self.txt_password.setGeometry(QtCore.QRect(20, 150, 191, 22))
        self.txt_password.setObjectName("txt_password")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 180, 110, 32))
        self.pushButton.setObjectName("pushButton")
        self.btn_load = QtWidgets.QPushButton(Form)
        self.btn_load.setGeometry(QtCore.QRect(420, 300, 110, 32))
        self.btn_load.setObjectName("btn_load")
        self.txt_host = QtWidgets.QLineEdit(Form)
        self.txt_host.setGeometry(QtCore.QRect(20, 30, 191, 22))
        self.txt_host.setObjectName("txt_host")
        self.txt_message = QtWidgets.QLineEdit(Form)
        self.txt_message.setGeometry(QtCore.QRect(20, 370, 401, 22))
        self.txt_message.setObjectName("txt_message")
        self.btn_send = QtWidgets.QPushButton(Form)
        self.btn_send.setGeometry(QtCore.QRect(420, 370, 110, 32))
        self.btn_send.setObjectName("btn_send")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 56, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 56, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 56, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 171, 101))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")

        self.pushButton.clicked.connect(self.login)
        self.btn_load.clicked.connect(self.load_messages)
        self.btn_send.clicked.connect(self.send_message)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def login(self):
        host = self.txt_host.text()
        BASE_URL = "http://%s" % host

        print BASE_URL

        username = self.txt_user.text()
        password = self.txt_password.text()

        response = urllib2.urlopen("%s/login?user=%s&password=%s" % (BASE_URL, username, password))
        content = response.read()
        result = json.loads(content)

        if result["error"]:
            print result["message"]
            return

        print result["message"]
        self.username = username
        self.token = result["token"]

    def send_message(self):
        host = self.txt_host.text()
        BASE_URL = "http://%s" % host

        message = self.txt_message.text()
        message = urllib.pathname2url(message)

        url = "%s/%s/send?m=%s&token=%s" % (BASE_URL, self.username, message, self.token)

        response = urllib2.urlopen(url)
        content = response.read()

        result = json.loads(content)

        print result["message"]

    def load_messages(self):
        host = self.txt_host.text()
        BASE_URL = "http://%s" % host

        url = "%s/%s/messages?token=%s" % (BASE_URL, self.username, self.token)

        response = urllib2.urlopen(url)
        content = response.read()

        messages = json.loads(content)

        for message in messages:
            s = "From: %s at %s (%d)" % (message["user"], message["datetime"], message["hearts"])
            s += "\n%s\n" % message["content"]
            s += ", ".join(message["seen"])
            s += "\n" + "-" * 80
            self.txt_messages.appendPlainText(s)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "login"))
        self.btn_load.setText(_translate("Form", "load"))
        self.txt_host.setText(_translate("Form", "localhost:5000"))
        self.btn_send.setText(_translate("Form", "send"))
        self.label.setText(_translate("Form", "Host:port"))
        self.label_2.setText(_translate("Form", "User"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "> "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

