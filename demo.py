# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 911)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(520, 40, 291, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 2, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 0, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 0, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 3, 0, 1, 2)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 3, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 2, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1071, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 40, 512, 199))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listView = QtWidgets.QListView(self.layoutWidget1)
        self.listView.setObjectName("listView")
        self.horizontalLayout_2.addWidget(self.listView)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.layoutWidget1)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_2.addWidget(self.calendarWidget)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(820, 140, 141, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 240, 292, 69))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 0, 1, 1, 2)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 0, 3, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 1, 3, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 1, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(300, 240, 351, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_3.addWidget(self.pushButton_21, 0, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_3.addWidget(self.pushButton_20, 0, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_3.addWidget(self.pushButton_22, 0, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_3.addWidget(self.pushButton_23, 0, 3, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_3.addWidget(self.lineEdit_11, 1, 0, 1, 2)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_3.addWidget(self.lineEdit_12, 1, 2, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_3.addWidget(self.lineEdit_13, 1, 3, 1, 1)
        self.gridFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame_2.setGeometry(QtCore.QRect(660, 240, 381, 71))
        self.gridFrame_2.setObjectName("gridFrame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridFrame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_26 = QtWidgets.QPushButton(self.gridFrame_2)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_4.addWidget(self.pushButton_26, 0, 2, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridFrame_2)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_4.addWidget(self.pushButton_25, 0, 1, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridFrame_2)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_4.addWidget(self.pushButton_24, 0, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.gridFrame_2)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_4.addWidget(self.lineEdit_14, 1, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridFrame_2)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_4.addWidget(self.lineEdit_15, 1, 1, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.gridFrame_2)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_4.addWidget(self.lineEdit_16, 1, 2, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(820, 40, 141, 126))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(970, 50, 101, 61))
        self.pushButton_27.setObjectName("pushButton_27")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(970, 120, 89, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(970, 150, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 310, 256, 192))
        self.treeView.setObjectName("treeView")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(970, 170, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(970, 200, 121, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(280, 320, 241, 181))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_17)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_18)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_19)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(690, 320, 75, 23))
        self.pushButton_28.setObjectName("pushButton_28")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(690, 350, 71, 16))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(690, 380, 91, 16))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(690, 410, 91, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setGeometry(QtCore.QRect(780, 350, 113, 20))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(540, 320, 135, 126))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout.addWidget(self.lineEdit_20)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout.addWidget(self.lineEdit_21)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.verticalLayout.addWidget(self.lineEdit_22)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.verticalLayout.addWidget(self.lineEdit_23)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.verticalLayout.addWidget(self.lineEdit_24)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(10, 510, 1091, 200))
        self.webEngineView.setUrl(QtCore.QUrl("https://www.baidu.com/"))
        self.webEngineView.setObjectName("webEngineView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1128, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuData = QtWidgets.QMenu(self.menuBar)
        self.menuData.setObjectName("menuData")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuData.menuAction())
        self.label_10.setBuddy(self.lineEdit_17)
        self.label_11.setBuddy(self.lineEdit_18)
        self.label_12.setBuddy(self.lineEdit_19)

        self.retranslateUi(MainWindow)
        self.pushButton_28.clicked.connect(MainWindow.close)
        self.checkBox_2.toggled['bool'].connect(self.lineEdit_25.setVisible)
        self.checkBox_3.toggled['bool'].connect(self.textBrowser.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_17.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_18.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_21.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_20.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_22.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_23.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_26.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_25.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_24.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_27.setText(_translate("MainWindow", "PushButton"))
        self.radioButton_4.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label_10.setText(_translate("MainWindow", "姓名（&A）："))
        self.label_11.setText(_translate("MainWindow", "年龄（&B）："))
        self.label_12.setText(_translate("MainWindow", "职位（&C）："))
        self.pushButton_28.setText(_translate("MainWindow", "关闭窗口"))
        self.checkBox_2.setText(_translate("MainWindow", "显示/隐藏"))
        self.checkBox_3.setText(_translate("MainWindow", "可用/不可用"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "创建新文件"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
from PyQt5 import QtWebEngineWidgets
