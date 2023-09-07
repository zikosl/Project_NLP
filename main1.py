# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 578)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:\"#fff\"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 691, 541))
        self.frame.setStyleSheet("background-color:\"#fff\"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 130, 651, 51))
        self.groupBox.setObjectName("groupBox")
        self.Dir = QtWidgets.QLabel(self.groupBox)
        self.Dir.setGeometry(QtCore.QRect(10, 20, 631, 20))
        self.Dir.setText("")
        self.Dir.setObjectName("Dir")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Files = QtWidgets.QGroupBox(self.frame)
        self.Files.setGeometry(QtCore.QRect(20, 200, 191, 301))
        self.Files.setObjectName("Files")
        self.listWidget = QtWidgets.QListWidget(self.Files)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 171, 271))
        self.listWidget.setStyleSheet("border:0")
        self.listWidget.setObjectName("listWidget")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(240, 210, 431, 291))
        self.scrollArea.setStyleSheet("border:0;\n"
"\n"
"background-color:\'#fff\'")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 431, 291))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 431, 291))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("border:1px solid #ccc")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.toolbar = QtWidgets.QFrame(self.frame)
        self.toolbar.setGeometry(QtCore.QRect(30, 10, 631, 31))
        self.toolbar.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(67, 67, 67, 255))")
        self.toolbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolbar.setObjectName("toolbar")
        self.pushButton = QtWidgets.QPushButton(self.toolbar)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background:\'#00000000\';\n"
"border:0;\n"
"justify-content:\"center\";\n"
"aligne-items:\"center\";\n"
"color:\"#fff\"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.toolbar)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 0, 31, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background:\'#00000000\';\n"
"border:0;\n"
"justify-content:\"center\";\n"
"aligne-items:\"center\";\n"
"color:\"#fff\"")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.toolbar)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(8)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background:\'#00000000\';\n"
"border:0;\n"
"justify-content:\"center\";\n"
"aligne-items:\"center\";\n"
"color:\"#fff\"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        self.menu_File.setFont(font)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Load = QtWidgets.QAction(MainWindow)
        self.action_Load.setObjectName("action_Load")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menu_File.addAction(self.action_Load)
        self.menu_File.addAction(self.actionNew)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionClose)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Location"))
        self.label_2.setText(_translate("MainWindow", "Grammer Analyser"))
        self.Files.setTitle(_translate("MainWindow", "Files"))
        self.pushButton.setText(_translate("MainWindow", "Start "))
        self.pushButton_3.setText(_translate("MainWindow", "Show grammer"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.action_Load.setText(_translate("MainWindow", "&Load"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionClose.setText(_translate("MainWindow", "Close"))