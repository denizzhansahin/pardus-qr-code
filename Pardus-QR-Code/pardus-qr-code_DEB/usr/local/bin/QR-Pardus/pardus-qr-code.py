# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqrcode
import png
from pyqrcode import QRCode
import time


class Ui_qrCode_Pardus(object):
    def setupUi(self, qrCode_Pardus):
        qrCode_Pardus.setObjectName("qrCode_Pardus")
        qrCode_Pardus.resize(757, 695)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/local/bin/qr_logo/pardus_qr_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        qrCode_Pardus.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(qrCode_Pardus)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 641, 27))
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 50, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 110, 561, 531))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 641, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 80, 521, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 650, 301, 20))
        self.label_4.setObjectName("label_4")
        qrCode_Pardus.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(qrCode_Pardus)
        self.statusbar.setObjectName("statusbar")
        qrCode_Pardus.setStatusBar(self.statusbar)

        self.retranslateUi(qrCode_Pardus)
        QtCore.QMetaObject.connectSlotsByName(qrCode_Pardus)

    def retranslateUi(self, qrCode_Pardus):
        _translate = QtCore.QCoreApplication.translate
        qrCode_Pardus.setWindowTitle(_translate("Qr Kod Olusturucu", "Qr Kod Olusturucu"))
        self.pushButton.setText(_translate("qrCode_Pardus", "QR Oluştur"))
        self.label_2.setText(_translate("qrCode_Pardus", "Metin ifadesini yazınız. (Türkçe karakter yazmayınız)"))
        self.label_3.setText(_translate("qrCode_Pardus", " "))
        self.label_4.setText(_translate("qrCode_Pardus", "<html><head/><body><p>Denizhan ŞAHİN - <a href=\"www.denizhansahin.com\"><span style=\" text-decoration: underline; color:#0000ff;\">www.denizhansahin.com</span></a></p></body></html>"))
        self.pushButton.clicked.connect(self.Qr_fonksiyon)

    def Qr_fonksiyon(self):
        deger = self.lineEdit.text()
        url = pyqrcode.create(deger)
        
        zaman = time.asctime()

        url.png(zaman+'.png', scale = 10)
        self.label.setPixmap(QtGui.QPixmap(zaman+".png"))

        self.label_3.setText("Dosya bilgisayarınıza kayıt edildi. Ev dizini/"+zaman+".png")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qrCode_Pardus = QtWidgets.QMainWindow()
    ui = Ui_qrCode_Pardus()
    ui.setupUi(qrCode_Pardus)
    qrCode_Pardus.show()
    sys.exit(app.exec_())
