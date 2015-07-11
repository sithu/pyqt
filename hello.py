# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created: Sat Jul 11 08:49:45 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_home = QtGui.QWidget()
        self.tab_home.setObjectName(_fromUtf8("tab_home"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_home)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcdNumber = QtGui.QLCDNumber(self.tab_home)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.verticalLayout.addWidget(self.lcdNumber)
        self.lcdNumber_3 = QtGui.QLCDNumber(self.tab_home)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lcdNumber_3.setFont(font)
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.verticalLayout.addWidget(self.lcdNumber_3)
        self.dial_3 = QtGui.QDial(self.tab_home)
        self.dial_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dial_3.setMaximum(100)
        self.dial_3.setObjectName(_fromUtf8("dial_3"))
        self.verticalLayout.addWidget(self.dial_3)
        self.tabWidget.addTab(self.tab_home, _fromUtf8(""))
        self.tab_settings = QtGui.QWidget()
        self.tab_settings.setObjectName(_fromUtf8("tab_settings"))
        self.tabWidget.addTab(self.tab_settings, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.dial_3, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.lcdNumber_3.display)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), _translate("Dialog", "Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("Dialog", "Settings", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

