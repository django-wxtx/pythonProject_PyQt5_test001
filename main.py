import sys
import demo

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)#创建应用程序
    mainWindow = QMainWindow()#创建窗口
    ui = demo.Ui_MainWindow()
    #向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


